# Pipeline Analytics Views That Feed Forecast Accuracy

On-demand reference for the revops-forecasting skill.

Four diagnostic views that turn pipeline data into forecast intelligence. Build these as saved views or dashboards alongside the forecast process.

## View 1: Pipeline Waterfall

Track how pipeline moves through the system each period:

| Movement | What It Shows | Forecast Impact |
|----------|--------------|-----------------|
| **Created** | New pipeline added this period | Leading indicator — is next quarter's pipe building? |
| **Moved In** | Deals pulled forward from future periods | Positive but watch for false acceleration |
| **Moved Out** | Deals pushed to future periods (slippage) | #1 forecast accuracy killer |
| **Won** | Deals closed this period | Actual vs forecast — the truth metric |
| **Lost** | Deals closed-lost or disqualified | Healthy loss rate means qualification is working |

**Weekly review question:** "Is the waterfall balanced? If Moved Out > Created, the pipeline is shrinking."

## View 2: Forecast vs Actuals Tracking

Compare forecast at each checkpoint against actual close:

| Week of Quarter | Commit Forecast | Actual Close | Variance | Diagnosis |
|----------------|----------------|-------------|----------|-----------|
| Week 1 | €X | | | Starting position |
| Week 4 | €Y | | | If Y < X: deals slipping early |
| Week 8 | €Z | | | If Z < Y: pattern problem |
| Week 13 | €Final | €Actual | ±% | Accuracy score |

**Diagnosis patterns:**
- Forecast shrinks steadily → over-commitment at start of quarter (tighten Commit criteria)
- Forecast grows late → sandbagging or late-quarter inbound (capture earlier)
- Wild swings → stage definitions don't mean anything (standardize)

## View 3: At-Risk Opportunity Identification

Six risk signals with threshold triggers:

| Risk Signal | Threshold | Action When Triggered |
|------------|-----------|----------------------|
| No activity in 14+ days | 14 days since last logged activity | Flag deal owner — deal is likely dead |
| Close date unchanged 3+ weeks | Same close date for 21+ days | Challenge close date in next forecast call |
| Single-threaded | Only 1 contact on deal | Coach multi-threading immediately |
| No next step scheduled | Next activity date is empty | Create task: "Set concrete next step within 48 hours" |
| SPICED score ≤7 at Proposal+ stage | Score below threshold for stage | Send back to discovery — not qualified |
| Deal health score ≤9 | Composite health below threshold | Manager intervention required |

**Automation:** Build a "Deals at Risk" saved view combining these signals. Review at every forecast call.

## View 4: Pipeline Health Snapshot

Weekly diagnostic combining all analytics:

| Metric | This Week | Last Week | Trend | Action |
|--------|----------|----------|-------|--------|
| Total active pipeline | | | | |
| Coverage ratio (vs target) | | | | If <3x: activate contingency |
| Deals created this week | | | | |
| Deals moved out (slipped) | | | | If >15% of pipe: process review |
| Average deal age (open) | | | | If rising: velocity problem |
| At-risk deals (count) | | | | Each needs a documented plan |
| Forecast confidence range | | | | Commit ± Best Case spread |

**Purpose:** One view, five minutes, complete pipeline diagnostic. Use at the start of every forecast call.

## Canon References for Pipeline Analytics

Cross-references: full pipeline analytics views with implementation specs, and signal-trigger-action patterns for at-risk identification.
