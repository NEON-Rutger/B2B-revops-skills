# Pipeline Visibility and Reporting: Dashboard Architecture

On-demand reference for the revops-forecasting skill.

Pipeline visibility is the ability to see what's in your pipeline, trust that it's accurate, and act on it before it's too late. Most revenue teams have dashboards. Few have visibility. The difference: dashboards show numbers; visibility drives decisions.

## The Visibility Stack (4 Layers)

- **Layer 1: Pipeline Structure.** Stage design with verifiable exit criteria (buyer actions, not seller activities). 5-8 stages max. Probabilities increase monotonically.
- **Layer 2: Pipeline Reporting.** Reports and dashboards that show pipeline state. What most teams stop at.
- **Layer 3: Pipeline Hygiene.** Automated systems that keep pipeline data clean, current, and trustworthy.
- **Layer 4: Pipeline Intelligence.** Alerts and signals that surface what needs attention NOW, before humans notice.

## Dashboard Architecture

One dashboard per audience. Leading indicators first. Exceptions over summaries. Consistent time frames.

**Executive Dashboard** (CRO/VP Sales/CEO, weekly): "Are we going to hit the number?"
| Widget | Metric | Format |
|--------|--------|--------|
| 1 | Pipeline by Forecast Category (current period) | Stacked bar |
| 2 | Pipeline Coverage Ratio (open pipeline ÷ remaining target) | Single number with RAG |
| 3 | Win Rate Trend (rolling 3 months) | Line chart |
| 4 | Average Deal Size Trend | Line chart |
| 5 | Forecast vs Actual (current + prior 2 periods) | Bar chart |
| 6 | Top 10 Deals (value, stage, next step, days in stage) | Table |

RAG thresholds: Green ≥3.5x, Amber 2.5-3.4x, Red <2.5x. *Based on Clari 3.2x benchmark; Ebsta 2025 suggests up to 5.3x may be needed given declining win rates. Calibrate: quota ÷ win rate.*

**Sales Manager Dashboard** (daily): "Which deals need my attention today?"
Stage movement, stale deals (by threshold), activity per rep, speed-to-lead SLA, forecast accuracy by rep, pipeline created versus target.

**Individual Rep Dashboard** (daily): "What should I work on right now?"
Pipeline by stage, deals closing this month/quarter, activities versus target, overdue tasks, quota attainment.

**RevOps Operational Dashboard** (weekly): "Is the system healthy?"
Data quality score, stage conversion rates (funnel), pipeline velocity (days per stage), loss reason distribution, pipeline created vs. target, enrichment coverage.

## Pipeline Hygiene Automation

**Stale Deal Thresholds** (recommended by stage):
| Stage | Stale After | Action |
|-------|------------|--------|
| Discovery | 7 days | Alert rep |
| Qualification | 10 days | Alert rep + manager |
| Solution Design | 14 days | Alert rep + manager |
| Proposal | 7 days | Alert manager (high urgency) |
| Negotiation | 5 days | Alert manager + VP |

**Overdue Close Date Handling:** Daily job auto-pushes past close dates to end of current month, creates a task, and tracks `Close_Date_Push_Count`. Target: <5% of pipeline with overdue close dates.

## Pipeline Quality Score

Six dimensions based on Gong and Ebsta research (300+ signals, 655K+ analyzed opportunities):

| Dimension | What to Measure | Research Backing |
|-----------|----------------|-----------------|
| **Engagement / Activity Velocity** | Frequency and recency of buyer interactions | Gong core signal; Ebsta: interaction frequency, recency, type |
| **Multi-Threading** | Contacts engaged per deal from different functions | Ebsta 2023: single-threaded ~8% win rate; 3+ contacts = 2.4x higher close rate |
| **Decision-Maker Access** | Direct engagement with economic buyer | Ebsta 2025: early DM involvement = +55% win rate |
| **Time in Stage / Deal Age** | Days in stage versus historical average | Gong 2024-25: win rate drops 50% when deal pushed from 1 week to 1 month |
| **Next Steps / Progression** | Clarity of agreed next action with date | Gong: clarity of next steps as core progression signal |
| **Trend Direction** | Positive vs. negative engagement trajectory | Ebsta: engagement trend as forward indicator |

*Operational template: adapt weights to your GTM process. Track trend over time, not just absolute score. Deals declining on 2+ dimensions: flag for immediate deal review.*

**Big Deal Alerts:** Trigger when deal value exceeds threshold (e.g., >$50K mid-market; >$200K enterprise), advances to Qualification+, or close date moves into current quarter. Recipients: VP Sales, CRO, RevOps.

## Pipeline Intelligence Signals

| Signal | What It Indicates | Action |
|--------|-------------------|--------|
| No activity >7 days at Proposal+ | Deal at risk | Manager intervention |
| Close date pushed 3+ times | Timeline not real | Honest conversation about buyer readiness |
| Single-threaded (1 contact) | Fragile deal | Multi-threading campaign |
| Amount decreased | Scope shrink or competitive pressure | Win strategy review |
| New competitor mentioned in notes | Competitive threat | Competitive positioning resources |
| Stage regression | Qualification lost | Re-qualify or close |
| Champion went dark | Org change or lost interest | Executive sponsor outreach |
| Activity spike from buyer | Evaluation intensifying | Accelerate access to resources |

## Pipeline Movement Waterfall

Track weekly changes to understand momentum:
```
Starting Pipeline: $4.2M
  + Created:  +$800K
  + Advanced: $1.1M moved forward
  - Pushed:   -$300K pushed to next quarter
  - Lost:     -$450K closed lost
  - Won:      -$600K closed won
= Ending Pipeline: $4.45M
```

This waterfall, reviewed weekly, is the single most powerful pipeline visibility tool.

## Essential Reports Checklist

| Report | Purpose |
|--------|---------|
| Pipeline by Stage | Pipeline health |
| Pipeline by Close Date | Timing distribution |
| Win Rate (Won ÷ Won + Lost) | Conversion performance |
| Sales Cycle (avg days created to close) | Velocity |
| Conversion Funnel (count by stage, cohort) | Drop-off analysis |
| Stale Deals (no activity > threshold) | Hygiene |
| Loss Analysis (by reason, last 90 days) | Pattern detection |
| Pipeline Coverage (open ÷ remaining target) | Forecast risk |
| Rep Scorecard (Rep × metrics matrix) | Individual performance |
| Pipeline Created (by week) | Leading indicator |

*References: Clari (3.2x pipeline coverage benchmark, 2024-25); Ebsta 2025 GTM Benchmarks (655K opportunities, $43B pipeline); Gong (close date push impact: win rate drops ~50% at 1 month versus 1 week); Salesforce research: active pipeline health management = 18% higher win rates, 28% more accurate forecasts.*
