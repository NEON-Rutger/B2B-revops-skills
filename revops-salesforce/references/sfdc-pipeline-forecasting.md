# Salesforce Pipeline & Forecasting Reference

## Opportunity Stage Architecture

### Stage Design Principles

1. Each stage must have a **verifiable exit criterion** — not "rep feels confident"
2. Stages represent **buyer milestones**, not seller activities
3. Keep to **5-8 stages**
4. Close probability should **increase monotonically**
5. **Consistent across teams** unless truly different motions (use Record Types)

### Recommended B2B SaaS Stage Model

> *Common SaaS defaults. Replace with your historical stage-to-close conversion rates within 90 days of implementation.*

| Stage | Probability | Forecast Category | Exit Criteria |
|-------|------------|-------------------|---------------|
| **Discovery** | 10% | Pipeline | Meeting completed; pain confirmed; ≥1 stakeholder identified |
| **Qualification** | 20% | Pipeline | Budget confirmed; decision process mapped; timeline established; champion identified |
| **Solution Design** | 40% | Pipeline | Technical requirements documented; demo/POC delivered; success criteria agreed |
| **Proposal** | 60% | Best Case | Proposal delivered; pricing discussed; no unresolved objections |
| **Negotiation** | 75% | Commit | Verbal agreement; contract in legal review; procurement engaged |
| **Closed Won** | 100% | Closed | Signed contract; PO received |
| **Closed Lost** | 0% | Omitted | Documented loss reason (required) |

### Stage Variations by Motion

- **PLG/Self-Serve**: Trial → Activated → Converted → Closed Won
- **Enterprise**: Add "Security Review" and "Procurement" between Negotiation and Closed Won
- **Channel/Partner**: Add "Partner Qualified" after Discovery
- **Renewal**: Renewal Upcoming → Renewal Sent → Negotiation → Renewed/Churned
- **Expansion**: Expansion Identified → Qualification → Proposal → Negotiation → Closed Won/Lost

### Validation Rules

| Rule | Logic | Purpose |
|------|-------|---------|
| No stage skipping | Only advance by 1 step (or Closed Lost from any) | Prevents jumping to Closed Won |
| Amount at Proposal | Stage ≥ Proposal → Amount ≠ null | Pipeline value accuracy |
| Close Date sanity | Stage < Negotiation → Close Date > TODAY + 14 | Realistic forecasting |
| Contact Role required | Stage ≥ Qualification → ≥1 OpportunityContactRole | Multi-threading documentation |
| Loss reason required | Closed Lost → Loss_Reason__c ≠ null | Win/loss analysis |
| Next Step required | Open stages → Next_Step__c ≠ null | Action orientation |

## Forecast Categories

| Category | Definition | Minimum Criteria |
|----------|-----------|-----------------|
| **Pipeline** | Early-stage, not forecast-ready | Active opportunity, not yet qualified |
| **Best Case** | Could close this period but uncertain | Qualified, close plan exists, timeline fits |
| **Commit** | Will close this period | Verbal yes from economic buyer, contract in legal, no competing evaluations |
| **Closed** | Done | Signed contract |
| **Omitted** | Excluded from forecast | Closed Lost, pushed, or disqualified |

**The Commit rule**: If a deal has been in Commit for >30 days without advancing, it is not a Commit. Downgrade to Best Case.

## Collaborative Forecasting

### Configuration

| Setting | Options |
|---------|---------|
| **Forecast type** | Opportunity Amount, Opportunity Product, Opportunity Split, Product Family |
| **Hierarchy** | Maps to role hierarchy (Rep → Manager → Director → VP → CRO) |
| **Period** | Monthly or Quarterly (match business cadence) |
| **Adjustments** | Manager override up/down; tracked and auditable |
| **Split forecasting** | Each person sees their split amount, not full opportunity value |

### When to Use Each Forecast Type

| Type | Best For |
|------|---------|
| **Opportunity Amount** | Standard; single product/price per deal |
| **Opportunity Product** | Multiple products per deal; product-level forecast needed |
| **Opportunity Split** | Team selling; multiple reps share credit |
| **Product Family** | Forecasting by product category |

## Opportunity Splits

Enable team selling attribution without double-counting.

**Split types**:
- **Revenue Split**: Must total 100% across team members; feeds individual quota attainment
- **Overlay Split**: Can exceed 100%; tracks influence without affecting primary quota

**Common configurations**:
- AE 70% + SE 30% (co-sell)
- AE 80% + SDR 20% (sourcing credit)
- AE 100% + Product Specialist 20% overlay

## Pipeline Inspection Tool

Salesforce's built-in enhanced pipeline view:

**Features**:
- Opportunity list with Einstein Score, Activity count, Close Date changes
- Week-over-week pipeline value changes
- AI-driven insights (Einstein enabled)
- Inline editing for quick updates during reviews

**Einstein Opportunity Score** (paid add-on):
- 1-99 score predicting close likelihood
- High (67-99), Medium (34-66), Low (1-33)
- Based on: historical win patterns, activity, progression speed, engagement
- Updates weekly

**Meeting usage**:
- Filter by Commit + Best Case for forecast calls
- Sort by Einstein Score descending (focus on risk)
- Use change column to spot slipped deals
- Inline edit Close Date and Next Step live

## CRM Analytics (Einstein Analytics / Tableau CRM)

### When Native Reports Aren't Enough

| Need | Native Reports | CRM Analytics |
|------|---------------|---------------|
| Simple pipeline views | ✅ | Overkill |
| Cross-object joins (3+) | ❌ Limited | ✅ Full SAQL |
| Cohort analysis | ❌ Manual | ✅ Built-in |
| Trend with snapshots | ❌ | ✅ Snapshot datasets |
| AI predictions | ❌ | ✅ Einstein Discovery |

### Key CRM Analytics Dashboards

1. **Pipeline Trending**: Weekly snapshot; visualise growth, conversion, leakage
2. **Cohort Performance**: Group deals by creation month; track conversion per cohort
3. **Rep Performance Matrix**: Activity volume vs win rate scatter plot
4. **Forecast Accuracy History**: Actual vs forecast by period; identify bias patterns

## Forecast Accuracy

### Measurement

Forecast Accuracy = 1 - |Actual - Forecast| / Target

| Accuracy | Rating | Action |
|----------|--------|--------|
| ≥95% | Excellent | Maintain |
| 85-94% | Good | Minor calibration |
| 70-84% | Acceptable | Review commit criteria |
| 50-69% | Poor | Process issue |
| <50% | Broken | Fix data quality first |

**Benchmark**: Only 25% of B2B companies forecast within 5% accuracy.

### Snapshot Tracking

Custom object `Forecast_Snapshot__c`:
- Period__c, Snapshot_Date__c, Rep__c (User lookup)
- Commit_Value__c, Best_Case_Value__c, Pipeline_Value__c
- Actual_Closed__c (populated after period ends)
- Accuracy__c (formula)

Populate via Scheduled Flow at each forecast cadence.

## Pipeline Hygiene Automation

### Monthly Scrub Flow (Scheduled, first Monday)

```
Query open Opportunities:

Flag 1: Close Date in past AND not Closed
  → Push Close Date to end of current month
  → Task: "Update close date"

Flag 2: No activity >30 days AND Stage ≥ Qualification
  → Set Pipeline_Health = "At Risk"
  → Notify owner + manager

Flag 3: Same stage >2x average days
  → Set Pipeline_Health = "Stalled"
  → Task: "Review or close"

Flag 4: Amount = 0 AND Stage ≥ Proposal
  → Notify: "Missing amount"
```

### Pipeline Quality Score

Formula field `Pipeline_Quality_Score__c` (max 100):
- +20: Amount > 0
- +20: Close Date in future
- +15: ≥1 Contact Role
- +15: Next Step populated, date in future
- +10: Activity in last 14 days
- +10: Loss Reason (if Closed Lost)
- +10: All stage-required fields populated

Dashboard: Average score by team/rep. Below 60 = data quality problem.
n> For a research-backed Pipeline Quality Score based on Gong and Ebsta deal health dimensions, see the `pipeline-visibility` skill.
