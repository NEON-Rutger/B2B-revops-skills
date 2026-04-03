---
name: pipeline-visibility
description: >
  Pipeline visibility, reporting architecture, dashboard design, pipeline
  hygiene, and forecast reporting for B2B revenue teams. CRM-agnostic
  patterns for any platform. Use when the user mentions pipeline visibility,
  pipeline reporting, sales dashboards, pipeline hygiene, stale deals,
  pipeline coverage, pipeline health, deal inspection, pipeline review,
  win rate reporting, conversion funnels, pipeline cleanup, pipeline scrub,
  forecast reporting, forecast accuracy tracking, big deal alerts, or
  pipeline quality score. Also trigger on 'we can't see our pipeline,'
  'deals go stale,' 'pipeline reports are wrong,' 'we need better
  dashboards,' or 'how do we track pipeline health.' BOUNDARY: Covers
  pipeline VISIBILITY and REPORTING (CRM-agnostic). For CRM-specific
  implementation, see revops-hubspot or revops-salesforce. For forecast
  methodology, see revops-forecasting. For metrics, see revops-metrics.
---

# Pipeline Visibility for B2B Revenue Operations

Pipeline visibility is the ability to see what's in your pipeline, trust that it's accurate, and act on it before it's too late. Most revenue teams have dashboards. Few have visibility.

The difference: dashboards show numbers; visibility drives decisions.

---

## The Visibility Stack

Pipeline visibility has four layers. Most teams only build the first two and wonder why their forecast is wrong.

### Layer 1: Pipeline Structure (Foundation)
What stages exist, what they mean, and what data is required at each.

**Stage design principles**:
1. Each stage has a **verifiable exit criterion** (not "rep feels good about it")
2. Stages represent **buyer actions**, not seller activities
3. 5-8 stages maximum (more creates friction and reduces compliance)
4. Probability increases monotonically (if it doesn't, stages are wrong)

**Recommended B2B SaaS stages**:

| Stage | Probability | What It Means |
|-------|------------|---------------|
> *Common SaaS defaults. Replace with your historical stage-to-close conversion rates within 90 days of implementation.*

| Discovery | 10% | Initial meeting done; pain confirmed |
| Qualification | 20% | Budget, timeline, decision process, champion identified |
| Solution Design | 40% | Requirements documented; demo/POC delivered |
| Proposal | 60% | Proposal delivered; pricing discussed |
| Negotiation | 75% | Verbal yes; contract in legal |
| Closed Won | 100% | Signed |
| Closed Lost | 0% | Documented loss reason |

### Layer 2: Pipeline Reporting (What most teams stop at)
Reports and dashboards that show pipeline state.

### Layer 3: Pipeline Hygiene (Where accuracy comes from)
Automated systems that keep pipeline data clean, current, and trustworthy.

### Layer 4: Pipeline Intelligence (Where decisions come from)
Alerts, signals, and analysis that surface what needs attention NOW — before humans notice it.

---

## Dashboard Architecture

### Design Principles

1. **One dashboard per audience** — executives, managers, and reps need different views
2. **Leading indicators first** — pipeline created and activities before closed revenue
3. **Exceptions over summaries** — surface what's wrong, not what's fine
4. **Minimal click depth** — the answer should be visible without drilling down
5. **Consistent time frames** — pick a standard (rolling 90 days, current quarter, etc.)

### Executive Dashboard

**Audience**: CRO, VP Sales, CEO
**Cadence**: Weekly review
**Purpose**: "Are we going to hit the number?"

| Widget | Metric | Format |
|--------|--------|--------|
| 1 | Pipeline by Forecast Category (current period) | Stacked bar |
| 2 | Pipeline Coverage Ratio (open pipeline ÷ remaining target) | Single number with RAG status |
| 3 | Win Rate Trend (rolling 3 months) | Line chart |
| 4 | Average Deal Size Trend | Line chart |
| 5 | Forecast vs Actual (current + prior 2 periods) | Bar chart comparison |
| 6 | Top 10 Deals (value, stage, next step, days in stage) | Table |

**RAG thresholds for Pipeline Coverage**:
- Green: ≥3.5x
- Amber: 2.5-3.4x
- Red: <2.5x
n> *Based on Clari's vetted pipeline benchmark of 3.2× (2024-2025) and the 3-5× industry range. Note: Ebsta's 2025 GTM Benchmarks (655K opportunities) suggest effective coverage may need to be as high as 5.3× given declining win rates. Calibrate to your historical win rate: required coverage = quota ÷ win rate.*

### Sales Manager Dashboard

**Audience**: Front-line sales managers
**Cadence**: Daily
**Purpose**: "Which deals need my attention today?"

| Widget | Metric | Format |
|--------|--------|--------|
| 1 | Team Pipeline by Rep and Stage | Matrix/heatmap |
| 2 | Deals Advancing vs Stalling This Week | Comparison bar |
| 3 | Activities per Rep (calls, meetings, emails) | Bar chart |
| 4 | Stale Deals (no activity > threshold) | Table with days-stale column |
| 5 | Speed-to-Lead SLA Compliance | Gauge/percentage |
| 6 | Forecast Accuracy by Rep (historical) | Table with trend arrows |
| 7 | Pipeline Created This Week/Month vs Target | Progress bar |

### Individual Rep Dashboard

**Audience**: AEs, SDRs
**Cadence**: Daily
**Purpose**: "What should I work on right now?"

| Widget | Metric | Format |
|--------|--------|--------|
| 1 | My Pipeline by Stage | Funnel or bar |
| 2 | Deals Closing This Month/Quarter | Table sorted by close date |
| 3 | My Activities This Week vs Target | Progress bar |
| 4 | My Overdue Tasks | Task list |
| 5 | My Quota Attainment (actual + forecasted) | Gauge |

### RevOps Operational Dashboard

**Audience**: RevOps team
**Cadence**: Weekly
**Purpose**: "Is the system healthy?"

| Widget | Metric | Format |
|--------|--------|--------|
| 1 | Data Quality Score (avg pipeline quality across open deals) | Number + trend |
| 2 | Stage Conversion Rates (funnel) | Funnel chart |
| 3 | Pipeline Velocity (days per stage, avg) | Table |
| 4 | Loss Reason Distribution | Pie/bar chart |
| 5 | Pipeline Created vs Target | Progress bar |
| 6 | Enrichment Coverage (% records with key fields) | Bar chart |

---

## Pipeline Hygiene Automation

### The Hygiene Problem

Pipeline rots silently. Deals go stale, close dates pass without update, amounts stay at placeholder values. Without automated hygiene, your "€5M pipeline" might be worth €2M in reality.

### Stale Deal Detection

**Definition**: An opportunity with no logged activity for a configurable threshold.

**Recommended thresholds by stage**:

| Stage | Stale After | Action |
|-------|------------|--------|
| Discovery | 7 days | Alert rep |
| Qualification | 10 days | Alert rep + manager |
| Solution Design | 14 days | Alert rep + manager |
| Proposal | 7 days | Alert manager (high urgency) |
| Negotiation | 5 days | Alert manager + VP |

**Automation**:
- Daily scheduled job queries open deals past threshold
- Marks deal with stale flag for dashboard visibility
- Sends notification to owner + manager
- Creates task: "Review stale deal — no activity in X days"
- If still stale after 2x threshold: escalate to VP + RevOps

### Overdue Close Date Handling

Deals with close dates in the past are the single biggest source of forecast error.

**Automation**:
- Daily job: Query open deals where Close Date < TODAY
- Auto-push Close Date to end of current month
- Create task: "Close date was overdue — confirm new timeline"
- Flag deal for next pipeline review
- Track: # of times close date has been pushed (Close_Date_Push_Count)

**Dashboard metric**: % of pipeline with overdue close dates (target: <5%)

### Pipeline Quality Score

A composite deal health metric informed by Gong and Ebsta's published deal health research. Gong analyses 300+ signals (split ~50/50 between conversation intelligence and CRM/activity data). Ebsta's Deal Score (1-99) is based on 655K+ analysed opportunities.

**Six core dimensions** (based on Gong and Ebsta research):

| Dimension | What to Measure | Research Backing |
|----------|----------------|-----------------|
| **Engagement / Activity Velocity** | Frequency and recency of buyer interactions; pace of deal advancement | Gong: core signal category. Ebsta: interaction frequency, recency, type, direction (inbound/outbound). |
| **Multi-Threading / Stakeholder Dynamics** | Number of contacts engaged per deal from different functions | Gong: new contacts joining, champion engagement frequency. Ebsta 2023: single-threaded ~8% win rate; 3+ contacts = 2.4× higher close rate. |
| **Decision-Maker Access** | Direct engagement with economic buyer or decision authority | Ebsta 2025: early decision-maker involvement boosts win rates by 55%. |
| **Time in Stage / Deal Age** | Days in current stage vs historical average for that stage | Gong: actual vs expected time in stage. Ebsta: flags when too long. Gong 2024-2025: win rate drops 50% when deal pushed from 1 week to 1 month. |
| **Next Steps / Progression** | Clarity and specificity of agreed next action with date | Gong: clarity of next steps as core progression signal. |
| **Trend Direction** | Positive vs negative trajectory of engagement over time | Ebsta: positive vs negative engagement trends. |

> *Operational template — adapt scoring weights and thresholds to your GTM process. Gong and Ebsta use proprietary weighting that changes dynamically per deal; these dimensions represent their published signal categories, not their exact algorithms.*

**Usage**:
- Dashboard: Average Pipeline Quality Score by team/rep
- Track trend over time, not just absolute score
- Deals declining on 2+ dimensions simultaneously: flag for immediate deal review
### Big Deal Alerts

Automatically surface high-value deals that need executive attention:

**Trigger conditions**:
- Deal value exceeds configurable threshold (e.g., >€50K for mid-market; >€200K for enterprise)
- Deal advances to Qualification or beyond
- Deal value increases by >25%
- Deal close date moves into current quarter
n> *Template thresholds — configure based on your ACV distribution and deal-size tiers.*

**Alert content**: Deal name, value, stage, owner, next step, days in stage, close date
**Recipients**: VP Sales, CRO, RevOps lead
**Channel**: Slack + email (redundancy for critical signals)

---

## Pipeline Intelligence

### Signals That Predict Outcomes

Move beyond descriptive reporting to predictive signals:

| Signal | What It Indicates | Action |
|--------|-------------------|--------|
| **No activity in >7 days at Proposal+ stage** | Deal at risk | Manager intervention; check with champion |
| **Close date pushed 3+ times** | Timeline not real | Honest conversation about buyer readiness |
| **Single-threaded (1 contact)** | Fragile deal | Multi-threading campaign |
| **Amount decreased** | Scope shrink or competitive pressure | Win strategy review |
| **New competitor mentioned in notes** | Competitive threat | Competitive positioning resources |
| **Stage regression** | Qualification lost | Re-qualify or close |
| **Champion went dark** | Organisational change or lost interest | Executive sponsor outreach |
| **Activity spike from buyer** | Evaluation intensifying | Accelerate; ensure access to resources |

### Pipeline Movement Analysis

Track weekly changes to pipeline to understand momentum:

| Movement Type | Definition | What to Watch |
|--------------|-----------|---------------|
| **Created** | New pipeline added this week | Pace vs target |
| **Advanced** | Deals that moved to a later stage | Velocity signal |
| **Stalled** | Deals that didn't advance and had no activity | Hygiene issue |
| **Pushed** | Close date moved to a later period | Forecast risk |
| **Pulled In** | Close date moved to an earlier period | Potential upside (verify it's real) |
| **Lost** | Moved to Closed Lost | Loss reason analysis |
| **Won** | Moved to Closed Won | Celebrate; capture learnings |

**Weekly pipeline waterfall**:
```
Starting Pipeline: €4.2M
  + Created:  +€800K
  + Advanced: €1.1M moved forward
  - Pushed:   -€300K pushed to next quarter
  - Lost:     -€450K closed lost
  - Won:      -€600K closed won
= Ending Pipeline: €4.45M
```

This waterfall, reviewed weekly, is the single most powerful pipeline visibility tool.

---

## Forecast Accuracy Reporting

### Tracking Setup

Capture forecast snapshots at regular intervals:

| Field | Purpose |
|-------|---------|
| Period | Quarter/Month being forecast |
| Snapshot Date | When this forecast was captured |
| Rep | Individual forecaster |
| Commit Value | Amount in Commit category |
| Best Case Value | Amount in Best Case |
| Pipeline Value | Amount in Pipeline |
| Actual Closed | Populated after period ends |
| Accuracy | Formula: 1 - ABS(Actual - Commit) / Target |

**Cadence**: Snapshot weekly (or at each forecast call). Enables trend analysis: "How does our forecast accuracy change as we get closer to period end?"

### Accuracy Patterns to Spot

| Pattern | What It Means | Fix |
|---------|--------------|-----|
| Consistently over-forecasts | Reps/managers optimistic; Commit criteria too loose | Tighten Commit definition; require independent verification |
| Consistently under-forecasts | Sandbagging; conservative culture | Review incentive structure; celebrate accurate forecasting |
| Accurate early, wrong late | Late-quarter deals spike or collapse | Better pipeline coverage earlier; less reliance on last-week heroics |
| Individual rep outlier | One rep consistently off | Coaching opportunity; investigate deal progression habits |

---

## Essential Reports Checklist

The minimum reporting set every B2B revenue team needs:

| Report | Grouping | Filters | Purpose |
|--------|----------|---------|---------|
| Pipeline by Stage | Summary by Stage | Open, current FY | Pipeline health |
| Pipeline by Close Date | Summary by Month | Open, next 2 quarters | Timing distribution |
| Win Rate | Won ÷ (Won + Lost) | Closed this quarter | Conversion performance |
| Sales Cycle | Avg days from creation to close | Closed Won, current quarter | Velocity |
| Conversion Funnel | Count by stage | Created in cohort period | Drop-off analysis |
| Stale Deals | Tabular | Open, no activity > threshold | Hygiene |
| Loss Analysis | Summary by Reason | Closed Lost, last 90 days | Pattern detection |
| Pipeline Coverage | Formula | Open ÷ remaining target | Forecast risk |
| Rep Scorecard | Matrix (Rep × metrics) | Current quarter | Individual performance |
| Pipeline Created | Summary by week | Created date | Leading indicator |

---

## Cross-References

- For CRM-specific dashboard implementation → see **revops-hubspot** or **revops-salesforce**
- For forecast methodology and categories → see **revops-forecasting**
- For pipeline metrics and benchmarks → see **revops-metrics**
- For meeting architecture to review pipeline → see **revenue-operating-cadence**
- For enrichment that feeds pipeline data quality → see **data-enrichment**


---

## References

- **Pipeline coverage**: Clari, "Sales Pipeline Coverage Ratio" (2024-2025). 3.2× for vetted opportunities. Industry range: 3-5×.
- **Deal slippage**: Ebsta 2025 GTM Benchmarks. 36% slippage rate (down from 44% in 2024). 655K opportunities, $43B pipeline analysed.
- **Forecast accuracy tiers**: Fullcast, "Forecast Accuracy Benchmarks" (2024-2025). 80-85% acceptable; 85-95% good; 95%+ world-class.
- **Forecast variance**: InsightSquared, "2021 State of Sales Forecasting." Only 9% of organisations achieve ≤5% forecast variance.
- **Close date push impact**: Gong (2024-2025). Win rate drops ~50% when deal pushed from 1 week to 1 month.
- **Deal health scoring approach**: Gong Deal Likelihood Score (300+ signals, dynamic weighting); Ebsta Deal Score (1-99, 7 published attributes across 655K+ opportunities).
- **Ebsta 2025 GTM Benchmarks**: Early decision-maker involvement: +55% win rates. Delayed deals: -113% win rates. Top performers close 11× faster. A-players manage 164% more pipeline.
- **Pipeline health management**: Salesforce research: teams actively managing pipeline health metrics achieve 18% higher win rates and 28% more accurate forecasts.

> Built by [Neon Triforce](https://neontriforce.com)
