# Plan Versioning and Governance

Three versions of the annual revenue plan must coexist and be preserved. This governs the file structure, naming conventions, access controls, and approval gates.

---

## Three-Version System

### Version 1: Bottoms-Up Original (BO)

**What it is:** Revenue team's independent assessment of capacity and production capability.

**When created:** Weeks 3-5, completed by VP Sales and RevOps

**Contents:**
- Segment-by-segment breakdown (New Business, Expansion, Renewal, Services)
- Capacity model (FTE, ramp curves, quota)
- Named pipeline overlay (booked deals with probabilities)
- Bottoms-up total and confidence assessment per segment

**File naming:** `annual-plan-2026-bottoms-up-original.md`

**Approval:** VP Sales and RevOps sign-off; shared with Finance for pre-review

**Status after reconciliation:** LOCKED. Never overwritten. Preserved for reforecast comparison.

**Access:** Revenue, Finance, executive team (read-only)

### Version 2: Finance Stretch Iteration (FS)

**What it is:** Finance's top-down target and the assumptions that drive it.

**When created:** Week 6, Finance completes based on board guidance and company strategy

**Contents:**
- Top-down revenue target (e.g. EUR 8.5M)
- High-level drivers (20% YoY growth, 5% market expansion, 3% win-rate improvement)
- Sensitivity analysis (what if growth is 15%? 25%?)
- Headcount implications and cost modelling
- Cash flow impact and working-capital assumptions

**File naming:** `annual-plan-2026-finance-stretch.md`

**Approval:** CFO and Finance leadership sign-off

**Status after reconciliation:** LOCKED. Never overwritten. Serves as comparison baseline for mid-year reforecasts.

**Access:** Finance, executive team (read-only); shared with Revenue for reconciliation

### Version 3: Plan of Record (POR)

**What it is:** The single agreed plan. All teams execute against this number.

**When created:** Week 8, after reconciliation and scenario assignment

**Contents:**
- Locked revenue target (e.g. EUR 8.5M, reconciled from BO + FS)
- Segment-by-segment breakdown with confidence levels
- Named stretch scenarios with owners and dependencies
- Executive summary for board narrative
- Risk register (what could make us miss)

**File naming:** `annual-plan-2026-plan-of-record.md`

**Approval:** CEO, CFO, VP Sales, VP RevOps signature block

**Status:** LIVE. This is the source of truth from approval (Week 10) through end of year.

**Access:** All revenue, finance, and executive teams (read-only for most, edit by planning committee only)

**Updates mid-year:** Only via formal reforecast process (see below). Plan of Record is intentionally difficult to change.

---

## Reforecasting and Version Control Mid-Year

### Monthly Check-In Files

**File naming:** `annual-plan-2026-check-in-M3.md` (Month 3), `annual-plan-2026-check-in-M6.md` (Month 6), etc.

**Contents:**
- Current forecast vs Plan of Record
- Variance explanation (if >plus or minus 10%)
- No formal approval needed; RevOps and Finance review together
- Status: Informational; does not update Plan of Record

**Access:** Revenue and Finance teams

**Retention:** Keep all check-ins for audit trail. Archive to `/reforecasting-history/` after annual close.

### Quarterly/Trigger-Based Reforecasts

**When:** Q1, Q2, Q3 formal reforecasts plus any ad-hoc trigger reforecasts (coverage drops below 2.5x, etc.)

**File naming:** `annual-plan-2026-reforecast-Q2.md` or `annual-plan-2026-reforecast-trigger-coverage-M6.md`

**Contents:**
- Comparison table: Plan of Record vs Bottoms-Up Original vs Current Forecast
- Trigger analysis (which trigger fired, if any)
- Segment-by-segment updated forecast
- Updated assumptions (if changed since original plan)
- Variance explanation and mitigation plan
- Recommendation: confirm POR or update it

**Approval gate:** Revenue + Finance joint sign-off. If POR needs update, CEO approval.

**Status after approval:** Reforecast is published. POR is updated if variance exceeds threshold (e.g. >15% miss expected). Reforecast file is then LOCKED for permanent record.

**Access:** Revenue, Finance, executive team; board if material variance

**Retention:** PERMANENT. These are your audit trail. Stack them chronologically in `/annual-plans/2026/reforecasts/`

---

## File Structure and Storage

### Directory Layout

```
annual-plans/
  2026/
    annual-plan-2026-bottoms-up-original.md          [LOCKED after reconciliation]
    annual-plan-2026-finance-stretch.md              [LOCKED after reconciliation]
    annual-plan-2026-plan-of-record.md               [LIVE; updated only via formal reforecast]
    reforecasts/
      annual-plan-2026-check-in-M3.md                [Informational]
      annual-plan-2026-check-in-M6.md                [Informational]
      annual-plan-2026-reforecast-Q2.md              [LOCKED after approval]
      annual-plan-2026-reforecast-Q3.md              [LOCKED after approval]
      annual-plan-2026-reforecast-trigger-coverage-M8.md   [LOCKED if triggered]
    assumptions/
      annual-plan-2026-assumptions-locked.md         [Single source of truth for all planning assumptions]
    scenarios/
      scenario-A-additional-hiring.md                [Named scenarios from reconciliation]
      scenario-B-expansion-acceleration.md           [One file per scenario]
      scenario-C-pipeline-generation.md
```

### Access Control Framework

| File | Owner | Edit Access | Read Access | Lock Policy |
|---|---|---|---|---|
| Bottoms-Up Original | VP Sales/RevOps | Revenue only (during Weeks 3-5) | Finance, Exec team | LOCK after reconciliation (Week 8) |
| Finance Stretch | CFO | Finance only (Week 6) | Revenue, Exec team | LOCK after reconciliation (Week 8) |
| Plan of Record | CFO + VP Sales | Planning committee only | All teams | LOCK after board approval; only reforecast process can update |
| Monthly Check-Ins | RevOps | RevOps + Finance | All teams | No lock; informational |
| Quarterly Reforecasts | RevOps + FP&A | Joint review and approval | All teams | LOCK after approval |
| Assumptions Sheet | Revenue + Finance | Shared edit (with change tracking) | All teams | LOCK Week 5; update only via documented trigger |

---

## Versioning Discipline: When to Create a New File vs Update

**Create a new version file (do not overwrite) when:**
- Reforecasting has fired and forecast changes >10% from Plan of Record
- Plan of Record is being formally updated (e.g. Q2 reforecast shows 12% miss; Q2 reforecast becomes the new baseline for Q3)

**Overwrite existing file only when:**
- Correcting a typo or administrative error (not a material forecast change)
- Formatting or link update (no data change)
- In both cases, document the change in a "Change Log" section at the top of the file

**Example change log:**
```
## Change Log

**2026-07-15, 10:30 UTC:** Link corrected in Scenario A (benchmarks-sourced.md URL). No forecast impact.
**2026-06-30, 16:00 UTC:** Bottoms-Up Original revised from EUR 7.8M to EUR 7.95M following new AE hire approval. Scenario owners updated.
```

---

## Quarterly Close and Archive

**At fiscal year-end (December 31 for calendar-year businesses):**

1. All reforecast files locked and moved to `/annual-plans/2026/archive/`
2. Plan of Record marked as "final approved" with actual results appended
3. Variance analysis completed: "Forecasted EUR 8.5M, closed EUR 8.2M (3.5% miss). Root cause analysis: [detail]"
4. Learning documented for next year's planning cycle
5. Metrics recorded: forecast accuracy by month, reforecast frequency, biggest assumption misses

**Retention period:** All planning files retained for 3 years minimum (audit and learning).

---

## Governance Gates

### Approval Authority

| Decision | Authority | Escalation If Blocked |
|---|---|---|
| Lock Bottoms-Up Original (Week 8) | VP Sales + RevOps | CFO if concerns about capacity realism |
| Lock Finance Stretch (Week 8) | CFO | CEO if stretch is >15% above bottoms-up without scenarios |
| Approve Plan of Record (Week 10) | CEO + CFO + VP Sales | Board if variance from prior guidance >20% |
| Approve Quarterly Reforecast | RevOps + FP&A joint | CEO if reforecast changes POR by >15% |
| Update Plan of Record mid-year | CEO | Board notification if miss >10% |

### Escalation Triggers

**Escalate to CEO immediately if:**
- Reforecast identifies miss >15% vs Plan of Record
- Scenario owners cannot deliver committed uplift (hiring delayed, CS expansion not materialising)
- Material market or competitive change requiring plan pivot

**Escalate to Board if:**
- Annual variance >20% vs announced guidance
- Reforecasting happens more than quarterly (signals broken planning process)

---

**Last updated:** 2026-07-15
