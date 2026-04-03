---
name: revops-salesforce
description: >
  Salesforce implementation patterns for revenue operations teams. Use when
  the user mentions Salesforce, SFDC, Salesforce setup, Salesforce object
  model, Salesforce Flows, record-triggered flows, Salesforce automation,
  Salesforce properties, Salesforce reporting, Salesforce dashboards,
  opportunity stages in Salesforce, Salesforce pipeline, collaborative
  forecasting, Einstein, CRM Analytics, Pipeline Inspection, Salesforce
  data model, Salesforce migration, Process Builder replacement, Salesforce
  field governance, Salesforce territory management, or Salesforce
  integrations. Also trigger on 'our Salesforce is a mess,' 'how should we
  set up Salesforce,' 'migrate from Process Builder to Flow,' or any CRM
  architecture question where the team uses Salesforce. BOUNDARY: Covers
  Salesforce-specific implementation. For CRM-agnostic strategy, see
  revops-strategy. For HubSpot, see revops-hubspot. For generic enrichment,
  see data-enrichment. For generic routing, see lead-routing.
---

# Salesforce Implementation for B2B Revenue Operations

The Salesforce equivalent of revops-hubspot. Covers object model architecture, Flow automation, opportunity pipeline configuration, forecasting setup, reporting patterns, and integration architecture — all specific to Salesforce.

**For deeper dives**, read the reference files:
- `references/sfdc-object-model.md` — Object relationships, custom objects, record types, field governance
- `references/sfdc-automation-flows.md` — Flow types, migration from Process Builder, architecture patterns
- `references/sfdc-pipeline-forecasting.md` — Opportunity stages, forecast categories, collaborative forecasting, Pipeline Inspection

---

## Salesforce vs HubSpot: Architectural Differences

When advising clients on Salesforce (especially those familiar with HubSpot), ground the conversation in these structural differences:

| Aspect | Salesforce | HubSpot |
|--------|-----------|---------|
| **Data model** | Account-centric (Account → Contact → Opportunity) | Person-centric (Contact-first, company association) |
| **Leads** | Separate object; conversion creates Account + Contact + Opportunity | Contact lifecycle stages (no separate Lead object required) |
| **Custom objects** | Full RDBMS-style (lookups, master-detail, junction objects, roll-ups) | Simpler custom objects; fewer relational capabilities |
| **Automation** | Salesforce Flow (record-triggered, scheduled, platform events, screen) | Workflows (simpler, fewer branching options) |
| **Forecasting** | Collaborative forecasting with multi-level rollup, manager overrides, splits | Basic forecasting in Sales Hub Enterprise |
| **Reporting** | Report builder + dashboards + CRM Analytics (Tableau CRM) | Reports + dashboards; less depth for complex analysis |
| **Territory mgmt** | Enterprise Territory Management with hierarchies, multi-assignment | Basic assignment rules only |
| **Enrichment** | No native enrichment; requires third-party (ZoomInfo, Apollo, Clearbit) | Native enrichment + Clearbit (HubSpot-owned) |
| **Scoring** | Einstein AI (paid) or custom Flow-based | Property-based scoring + predictive (paid) |
| **Splits** | Native opportunity splits for team selling | Not native; workaround with custom objects |
| **Pricing** | Per-user licensing; feature tiers (Essentials → Enterprise → Unlimited) | Tiered hubs; more included at each level |

### When Salesforce Is the Right Choice
- Complex selling motions (team selling, splits, multi-pipeline)
- Enterprise accounts with deep hierarchies
- Advanced territory management needs
- Heavy customisation requirements
- Existing Salesforce investment/ecosystem

### When HubSpot Is the Right Choice
- Marketing-heavy orgs wanting CRM + marketing automation in one platform
- Simpler sales motions; smaller teams
- Speed-to-value priority (faster setup)
- Budget-conscious orgs wanting all-in-one

---

## Core Implementation Checklist

When setting up or auditing Salesforce for RevOps, work through these areas in order:

### 1. Object Model Design
**Read**: `references/sfdc-object-model.md`

Key decisions:
- Lead-first vs Contact/Account-first workflow (most consequential choice)
- Record Type strategy (New Business vs Renewal vs Expansion opportunities)
- Custom objects needed (Subscription, Handoff Record, Health Score)
- Relationship types (lookup vs master-detail, when to use junction objects)
- Field governance (naming conventions, required fields, field limits)

### 2. Automation Architecture
**Read**: `references/sfdc-automation-flows.md`

Key decisions:
- Flow consolidation strategy (max 3 flows per object: before-save, after-save, before-delete)
- Flow naming convention: `[Object]_[Trigger]_[Purpose]_v[Version]`
- Feature flags via Custom Metadata Types (enable/disable logic without redeployment)
- Flow vs Apex boundary (Flow-first; Apex for >10K records, complex error handling, sub-second integrations)
- Migration plan from deprecated Process Builders and Workflow Rules

### 3. Opportunity Pipeline
**Read**: `references/sfdc-pipeline-forecasting.md`

Key decisions:
- Stage model (5-8 stages with verifiable exit criteria)
- Forecast category mapping (Pipeline, Best Case, Commit, Closed, Omitted)
- Validation rules (no stage skipping, amount required at Proposal, loss reason required)
- Multi-pipeline via Record Types (if different motions exist)
- Opportunity Splits configuration (if team selling)

### 4. Forecasting Setup
**Read**: `references/sfdc-pipeline-forecasting.md`

Key decisions:
- Forecast type (Opportunity Amount, Product, Split, Product Family)
- Forecast hierarchy aligned to role hierarchy
- Manager override permissions
- Period (monthly vs quarterly)
- Forecast snapshot tracking for accuracy measurement

### 5. Reporting & Dashboards

Essential dashboard framework by audience:

**Executive** (CRO/VP — weekly):
- Pipeline by forecast category
- Pipeline coverage ratio (pipeline ÷ remaining target)
- Win rate trend (rolling 3 months)
- Forecast vs actual (current + prior 2 periods)
- Top 10 deals with stage and next step

**Manager** (front-line — daily):
- Team pipeline by rep and stage
- Deals advancing vs stalling this week
- Stale deals (no activity in configurable threshold)
- Speed-to-lead SLA compliance
- Forecast accuracy by rep

**RevOps Operational** (RevOps team — weekly):
- Data quality scores (field completion %)
- Stage conversion rates (funnel)
- Pipeline velocity (days per stage)
- Loss reason distribution
- Pipeline created vs target

### 6. Integrations

Common integration patterns:

| Integration | Direction | System of Record |
|------------|-----------|-----------------|
| HubSpot ↔ Salesforce | Bi-directional (lifecycle and campaign data) | Salesforce for revenue; HubSpot for marketing |
| Enrichment (ZoomInfo, Apollo) | Inbound to Salesforce | Enrichment provider |
| Slack | Outbound from Salesforce | Salesforce (notifications only) |
| CPQ | Bi-directional | Salesforce (pricing/quoting) |
| CS Platform (Gainsight, Vitally) | Bi-directional | Depends on CS maturity |

---

## Common Salesforce Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Too many custom fields | >500 fields on Account/Opportunity | Audit and deprecate unused fields quarterly |
| No field naming convention | Fields named inconsistently (MQL_Date vs Date_MQL vs mql_dt) | Adopt `[Category]_[Name]__c` standard |
| Mixed automation | Flows AND Apex triggers on same object | Pick one entry point per object |
| No validation rules | Reps skip stages, leave Amount blank | Layer validation (field-level → record-level → Flow) |
| Stale Process Builders | Legacy automation still firing (deprecated Dec 2025) | Migrate to Flow; deactivate old PBs |
| Manual territory assignment | Reps assigned accounts by spreadsheet | Implement ETM or Flow-based territory logic |
| No forecast snapshots | Can't measure forecast accuracy | Build Forecast_Snapshot__c custom object |
| Over-customised page layouts | 50+ fields on one layout | Role-based layouts with progressive disclosure |

---

## Cross-References

- For CRM-agnostic revenue strategy → see **revops-strategy**
- For HubSpot implementation → see **revops-hubspot**
- For CRM-agnostic data governance → see **revops-data-governance**
- For generic enrichment patterns → see **data-enrichment**
- For generic routing patterns → see **lead-routing**
- For pipeline metrics and benchmarks → see **revops-metrics**
- For handoff design → see **revops-handoffs**


---

## References

- Clari (2024-2025). Pipeline coverage benchmark: 3.2× for vetted opportunities.
- Ebsta 2025 GTM Benchmarks (655K opportunities). Deal slippage: 36%. Top performers: 11× faster close.
- Fullcast (2024-2025). Forecast accuracy benchmarks.
- Salesforce. Teams managing pipeline health metrics: +18% win rates, +28% forecast accuracy.

> Built by [Neon Triforce](https://neontriforce.com)
