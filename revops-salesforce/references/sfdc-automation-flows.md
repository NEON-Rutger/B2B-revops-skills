# Salesforce Automation & Flow Reference

**As of January 2026**: Process Builder and Workflow Rules are deprecated. All automation must use Salesforce Flow.

## Flow Types

| Flow Type | Trigger | Use For |
|-----------|---------|---------|
| **Record-Triggered (Before Save)** | Before database commit | Field updates on same record; validation; defaults |
| **Record-Triggered (After Save)** | After database commit | Creating/updating other records; notifications; external calls |
| **Scheduled Flow** | Cron schedule or one-time datetime | Batch jobs; nightly recalculations; SLA escalations |
| **Platform Event-Triggered** | Platform event published | Async processing; integration patterns; decoupled architecture |
| **Screen Flow** | User clicks button/link | Guided processes; multi-step forms; wizard data entry |
| **Autolaunched Flow** | Called from other flows, Apex, or REST API | Reusable logic modules; sub-flows; integration endpoints |

## Before-Save vs After-Save Decision

```
Need to update the SAME record that triggered the flow?
  → Before-Save (faster, no extra DML)

Need to create/update OTHER records?
  → After-Save

Need to call external services or send notifications?
  → After-Save with Async Path (non-blocking)

Performance-critical with high volume?
  → Before-Save wherever possible
```

## Flow Architecture Best Practices

### Consolidation Strategy

Maximum 3 record-triggered flows per object:
1. **Before-Save** (field defaults, validations, same-record updates)
2. **After-Save** (cross-object updates, notifications, integrations)
3. **Before-Delete** (validation, cleanup, archival)

Within each flow, use Decision elements to branch logic.

### Naming Convention

`[Object]_[Trigger]_[Purpose]_v[Version]`

Examples:
- `Lead_AfterSave_Assignment_v3`
- `Opportunity_BeforeSave_StageValidation_v1`
- `Account_Scheduled_EnrichmentRefresh_v2`

### Version Management

- Keep last working version inactive (not deleted) for rollback
- Date-stamp description: `v12 (2026-03-15): Added territory-based routing`
- Never delete a flow version that was active in production

### Feature Flags

Store configuration in Custom Metadata Types or Custom Settings to enable/disable flow logic without redeployment.

```
Decision Element: "Is Feature Enabled?"
  → Get Records: Custom_Setting__c WHERE Feature_Name = "New_Routing"
  → If Enabled__c = true → Execute new logic
  → If Enabled__c = false → Execute legacy logic
```

## Flow vs Apex Decision

```
Start with Flow (default for 80% of use cases)
  ↓
Batch processing >10K records? → Apex Batch
  ↓
Logic too complex (>50 flow elements)? → Apex Invocable Action (callable from Flow)
  ↓
Advanced error handling / retry? → Apex with try-catch-finally
  ↓
Real-time integration, sub-second response? → Apex callout
  ↓
Otherwise → Stay with Flow
```

**Hybrid pattern**: Complex logic in Apex as Invocable Actions, called from Flow. Flow handles orchestration, Apex handles heavy lifting.

## Common Anti-Patterns

### 1. Mixing Automation Entry Points
Running both Apex triggers AND flows on same object creates unpredictable execution order. Pick one.

### 2. DML in Loops
The single greatest cause of governor limit failures. Always bulkify — process collections, not individual records.

### 3. Recursive Flows
After-Save flow updates a record, triggering another After-Save flow. Solutions:
- Use `$Flow.CurrentRecord` checks
- Recursion guard via static variable (Apex) or Custom Setting flag
- Before-Save for same-record updates (avoids recursion entirely)

### 4. No Error Handling
Flows that fail silently. Always add Fault paths with admin notification.

### 5. Hardcoded IDs
Referencing record IDs, user IDs, or queue IDs directly. Use Custom Metadata Types or Custom Labels.

## Process Builder → Flow Migration Guide

### Migration Steps

1. **Audit**: Document every Process Builder, Workflow Rule, and Apex trigger per object
2. **Map execution order**: Understand current firing sequence
3. **Consolidate**: Multiple PBs on same object → one After-Save Flow with Decision branches
4. **Test in sandbox**: Flow execution order differs from PB — validate all rules
5. **Migrate in phases**: One object at a time, lowest-risk first
6. **Deactivate, don't delete**: Keep old PBs inactive until new Flows validated

### Migration Pitfalls

- **Execution order changes**: Flows run differently than PBs. Test all scenarios.
- **Recursive triggers**: PBs had built-in recursion prevention; Flows don't. Add guards.
- **Field update timing**: Before-Save Flows run earlier than PB "immediate actions."

## Common Flow Patterns for RevOps

### Lead Scoring Recalculation
```
Before-Save on Lead (any update)
  → Calculate Fit_Score__c (firmographic criteria)
  → Calculate Engagement_Score__c (activity-based)
  → Set Total_Score__c = Fit + Engagement
  → Set Score_Tier__c based on thresholds
```

### Opportunity Stage Gate
```
Before-Save on Opportunity (Stage changed)
  → Decision: Is new stage > old stage + 1?
    → Yes: Show error "Cannot skip stages"
  → Decision: Is Stage ≥ Proposal AND Amount = null?
    → Yes: Show error "Amount required at Proposal stage"
  → Decision: Is Stage = Closed Lost AND Loss_Reason = null?
    → Yes: Show error "Loss reason required"
```

### Stale Deal Alert
```
Scheduled Flow (daily at 08:00)
  → Query Opportunities WHERE IsClosed = false
    AND Last_Activity_Date < TODAY - threshold
    AND Stale_Alert_Sent__c = false
  → For each:
    → Set Stale_Flag__c = true
    → Send notification to Owner + Manager
    → Create Task: "Review stale opportunity"
```

### Enrichment Integration
```
After-Save on Lead (create only, Async Path)
  → Invocable Apex: Call enrichment API
  → Map response → Lead fields
  → Trigger scoring recalculation
```
