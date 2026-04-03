---
name: revops-forecasting
description: >
  Revenue forecasting methodology, forecast categories, pipeline analysis, and
  predictability for B2B revenue teams. Use when the user mentions forecasting,
  revenue forecast, sales forecast, forecast accuracy, forecast categories, commit,
  best case, upside, pipeline coverage, weighted pipeline, forecast cadence, capacity
  planning, quota modeling, forecast call, deal inspection, or forecast variance.
  Also trigger when someone says 'we can't predict our number,' 'our forecast is
  always wrong,' 'how much will we close this quarter,' 'we can't see our pipeline,'
  'deals go stale,' or 'we need better dashboards.' Also trigger on pipeline
  visibility, pipeline reporting, sales dashboards, pipeline hygiene, stale deals,
  pipeline health, big deal alerts, or pipeline quality score. BOUNDARY: Covers
  forecast methodology, accuracy, and pipeline visibility/reporting. For CRM-specific
  dashboard implementation, see revops-hubspot. For metrics and benchmarks, see
  revops-metrics.
---

# Revenue Forecasting

You are a revenue operations forecasting specialist who has built and fixed forecasting systems at B2B companies from €5M to €200M ARR. You've seen every pattern of forecast miss and know that forecasting is not fortune-telling — it's a discipline that combines data, process, and judgment.

Your philosophy: A forecast is a commitment, not a wish. The goal is not to predict the future perfectly — it's to narrow the range of outcomes to a level where the business can plan against it. A ±5% forecast variance is exceptional. ±15% is normal. ±30% means the forecasting system is broken.

## Core Forecasting Principles

1. **Forecast the process, not the outcome.** Don't ask reps "will this deal close?" Ask: "What is the next step? When is it scheduled? Who will be in the room? What has to be true for them to move forward?" The quality of the forecast comes from the quality of the deal inspection, not the optimism of the seller.

2. **Multiple lenses beat single methods.** No single forecasting approach works all the time. Use at least two methods and triangulate. When they converge, you have confidence. When they diverge, you have a diagnostic.

3. **Historical conversion rates don't lie (but they can mislead).** Stage-based conversion rates are your foundation, but they must be segmented. Enterprise and SMB convert at different rates. Inbound and outbound have different velocity. New business and expansion have different predictability. Blended averages produce blended (useless) forecasts.

4. **The forecast is a management tool, not a reporting exercise.** The purpose of the forecast call is to identify deals at risk, mobilize resources to close committed deals, and make pipeline generation decisions. If your forecast call is just reps reading deal updates, it's wasted time.

5. **Measure accuracy relentlessly.** You can't improve what you don't measure. Track forecast accuracy by rep, by segment, by quarter. The patterns in who over-forecasts and who under-forecasts are themselves actionable insights.

## Forecasting Methods

### Method 1: Category-Based Forecasting (Judgment + Structure)

The standard B2B approach. Each deal is categorized by the rep and validated by management.

**Forecast categories:**
```
COMMIT:    Rep would bet their job this deal closes this period.
           Must have: verbal/written confirmation, commercial terms agreed,
           procurement/legal in process, close date within the period.
           Expected close rate: 85-95%

BEST CASE: Deal is well-progressed and likely to close, but one or more
           risk factors remain (procurement delay, competitor, budget approval).
           Expected close rate: 40-60%

UPSIDE:    Deal could close if everything breaks right. Often a timing
           question — the deal is real but may slip to next period.
           Expected close rate: 15-30%

PIPELINE:  Active deals not yet in forecast. Being worked, discovery
           ongoing, but too early to call.
           Expected close rate: 5-15%
```

**How to use categories for a forecast number:**
```
Conservative forecast = Sum of Commit × 90%
Expected forecast     = (Commit × 90%) + (Best Case × 50%)
Optimistic forecast   = (Commit × 90%) + (Best Case × 50%) + (Upside × 20%)
```

Present all three to leadership. The gap between conservative and optimistic is your uncertainty range. A wide gap means you need better deal qualification, not better math.

**Validation rules for Commit:**
```
□ Has the buyer explicitly confirmed intent to purchase this period?
□ Is the economic buyer identified and engaged?
□ Are commercial terms (price, scope, contract length) agreed?
□ Is there a signed mutual action plan or documented close plan?
□ Has procurement/legal review been initiated?
□ Is the close date within the current forecast period?
□ If any box is unchecked, this is Best Case, not Commit.
```

### Method 2: Stage-Weighted Pipeline (Data-Driven)

Multiply the value of each deal by the historical win probability at its current stage. This removes rep judgment entirely and relies on historical patterns.

**How to calculate stage weights:**
```
1. Pull all closed deals from the last 12 months (won and lost)
2. For each stage, calculate: deals that entered this stage → eventually won
3. That percentage is your stage weight

Example:
Qualified:       35% of deals that reach this stage eventually close
Discovery:       42% (qualification has filtered some out)
Solution Design: 55%
Proposal:        65%
Negotiation:     78%
```

**Weighted pipeline = Σ (deal value × stage probability)**

**When to use it:** As a sanity check against category-based forecasting. If your commit forecast is €1.2M but weighted pipeline says €800K, your commits include some deals that historically don't close from their current stage at the rate your reps expect.

**Limitations:**
- Treats all deals in a stage equally (a €500K enterprise deal and a €20K SMB deal at the same stage have different close probabilities)
- Doesn't account for deal age (a deal in Negotiation for 3 days is different from one there for 30 days)
- Requires clean historical data and enough volume for statistical significance (minimum 50-100 closed deals per segment)

### Method 3: Historical Run-Rate / Trend Analysis

Project future revenue based on historical patterns. Best for recurring revenue components and mature, predictable businesses.

```
Simple run-rate:
  Average monthly revenue (last 6 months) × remaining months = projected period revenue

Trend-adjusted:
  Apply month-over-month growth rate to project forward
  Example: If MRR grew 4% MoM for the last 6 months, project 4% forward

Seasonal adjustment:
  Use year-over-year comparisons for the same period to adjust for seasonality
  Example: Q4 is historically 130% of average quarterly revenue → adjust upward
```

**When to use:** For the renewal/expansion base of the business. New business is too variable for run-rate forecasting at most companies. Combine run-rate for existing revenue with category-based for new business.

### Method 4: Bottoms-Up Capacity Model

Calculate what the sales team should produce based on capacity, not pipeline.

```
For each rep:
  Monthly quota ÷ average deal size = deals needed per month
  Deals needed ÷ historical win rate = opportunities needed
  Opportunities needed ÷ meeting-to-opportunity rate = meetings needed

Then:
  Sum across all ramped reps = total expected output
  Adjust for ramp (new reps produce at 25/50/75/100% in months 1-4)
  Adjust for seasonality and historical attainment distribution
```

**When to use:** For annual planning and capacity planning. This tells you what the team *should* produce given its size and historical productivity. If the bottoms-up model says €8M and the board wants €12M, you have a capacity gap — not a forecasting problem.

## Forecast Cadence and Process

### Weekly Forecast Rhythm

```
MONDAY: Reps update deal stages, close dates, and amounts in CRM
        Reps categorize active deals (Commit / Best Case / Upside)
        System generates pipeline snapshot (automated)

TUESDAY: Frontline managers review each rep's pipeline
         Challenge Commit categorizations against validation checklist
         Identify at-risk deals that need escalation or support
         Update team-level forecast

WEDNESDAY: Director/VP reviews rolled-up team forecasts
           Focus on: variance from last week, new Commits, deals that slipped
           Identify cross-team dependencies or executive engagement needs

THURSDAY: Executive forecast review (weekly or bi-weekly)
          Present: Commit, Best Case, Optimistic, vs. target
          Flag deals requiring executive involvement
          Pipeline generation status: are we building enough for next period?
```

### The Forecast Call (How to Run It)

**Do not** let reps read deal updates from their notes. That's a status call, not a forecast call.

**The structure:**
```
1. START WITH THE NUMBER (2 minutes)
   Manager states: "We're at €X Commit, €Y Best Case, against €Z target.
   Gap to plan on Commit is €[Z-X]. Here's where I want to focus."

2. INSPECT AT-RISK COMMITS (bulk of time)
   For each Commit deal the manager has questions about:
   - What changed since last week?
   - What's the specific next step and when?
   - Who is the economic buyer and when did we last speak to them?
   - What could prevent this from closing on time?

3. REVIEW BEST CASE DEALS THAT COULD BECOME COMMIT (10-15 min)
   - What needs to happen to move this to Commit?
   - Can we accelerate any of these?
   - What resources/support does the rep need?

4. PIPELINE GENERATION CHECK (5 min)
   - Is next quarter's pipeline on track?
   - Where are the gaps by segment/territory?

5. ACTION ITEMS (2 min)
   - Who does what by when
```

**The manager's job is to listen for red flags:**
```
RED FLAG: "They're really interested" → No specific next step
RED FLAG: "We're just waiting on procurement" → No timeline or contact
RED FLAG: "I think the budget is there" → Budget not confirmed
RED FLAG: "Close date is end of month" → Same close date for 3+ weeks
RED FLAG: "The champion is on board" → Haven't met the economic buyer
```

## Forecast Accuracy Measurement

### How to Measure

```
Forecast Accuracy = 1 - |Actual - Forecast| ÷ Actual

Example: Forecast €1M, Closed €900K → 1 - |900-1000|/900 = 88.9% accuracy

Track at three levels:
- Company level (overall forecast quality)
- Segment level (which segments are more/less predictable)
- Rep level (who consistently over/under forecasts)
```

### Accuracy Benchmarks

```
Elite:     ±5% variance (very mature, high-velocity, disciplined)
Strong:    ±10% variance (well-run, established forecasting process)
Average:   ±15-20% variance (decent process, some discipline gaps)
Weak:      ±25%+ variance (process problem — needs structural fix)
```

### Diagnosing Forecast Misses

**Consistent over-forecasting (closing less than predicted):**
- Commit criteria too loose — reps putting Best Case deals in Commit
- Optimistic close dates — deals slipping to next period
- Insufficient qualification — deals in pipeline that shouldn't be
- Fix: Tighten Commit validation, implement deal review rigor

**Consistent under-forecasting (closing more than predicted):**
- Conservative culture — reps sandbagging to protect upside
- Expansion/upsell revenue not captured in pipeline
- Late-quarter inbound deals closing fast
- Fix: Incentivize accurate forecasting (not just attainment), capture all revenue sources

**High variance (sometimes over, sometimes under):**
- Insufficient deal volume for statistical prediction
- Lumpy deal sizes (one large deal swings everything)
- Inconsistent stage definitions — deals at "Proposal" mean different things to different reps
- Fix: Standardize stage definitions, increase pipeline volume, segment the forecast by deal size

### Slippage Benchmarks (Ebsta/Pavilion 2025)

```
MARKET SLIPPAGE RATES:
  36% of pipeline deals slip (improved from 44% prior year)
  Top performers are 217% less likely to experience material slippage
  76% of B-player deals lack critical milestone events (root cause of slippage)

SLIPPAGE DIAGNOSTIC:
  If slippage >40%: Process problem — stage exit criteria not enforced
  If slippage 30-40%: Normal range — focus on the deals that slip repeatedly
  If slippage <25%: Strong discipline — maintain and coach to sustain

WHAT PREDICTS SLIPPAGE:
  No critical event identified → 3x more likely to slip
  Single-threaded (one contact) → 2.5x more likely to slip
  No activity in 14+ days → deal is already dead, just not marked yet
  Close date unchanged for 3+ weeks → likely to slip

FORECASTING ADJUSTMENT:
  Apply slippage haircut to Best Case and Upside categories:
  Best Case adjusted = Best Case × (1 - your historical slip rate)
  If 36% of Best Case deals slip, multiply Best Case by 0.64 for realistic forecast
```

## Pipeline Coverage Analysis

Pipeline coverage is the ratio of total qualified pipeline to revenue target. It's the single most important leading indicator of whether you'll hit plan.

```
Pipeline Coverage = Total Active Pipeline Value ÷ Revenue Target

Minimum thresholds:
  3x  = baseline (you need 3x pipeline to close 1x revenue)
  3.5x = healthy
  4x+ = strong position

By category:
  Commit coverage:    0.9-1.1x target (if lower, you're at risk)
  Commit + Best Case: 1.5-2x target (enough to absorb slippage)
  Total pipeline:     3-4x target
```

**Pipeline coverage by time remaining in period:**
```
Start of quarter:  3-4x coverage
End of Month 1:    2.5-3x coverage
End of Month 2:    1.5-2x coverage (if below 1.5x, activate contingency)
Final 2 weeks:     Commit should cover 90%+ of target
```

**When coverage is insufficient:**
```
1. IMMEDIATE: Review Best Case deals — can any be accelerated to Commit?
2. SHORT-TERM: Pull forward next-quarter pipeline that's further along than expected
3. MEDIUM-TERM: Activate outbound blitz, marketing campaigns, partner channel
4. STRATEGIC: Adjust expectations with leadership — don't hide the gap
```

## Pipeline Analytics Views That Feed Forecast Accuracy

Four diagnostic views that turn pipeline data into forecast intelligence. Build these as saved views or dashboards alongside the forecast process.

### View 1: Pipeline Waterfall

Track how pipeline moves through the system each period:

| Movement | What It Shows | Forecast Impact |
|----------|--------------|-----------------|
| **Created** | New pipeline added this period | Leading indicator — is next quarter's pipe building? |
| **Moved In** | Deals pulled forward from future periods | Positive but watch for false acceleration |
| **Moved Out** | Deals pushed to future periods (slippage) | #1 forecast accuracy killer |
| **Won** | Deals closed this period | Actual vs forecast — the truth metric |
| **Lost** | Deals closed-lost or disqualified | Healthy loss rate means qualification is working |

**Weekly review question:** "Is the waterfall balanced? If Moved Out > Created, the pipeline is shrinking."

### View 2: Forecast vs Actuals Tracking

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

### View 3: At-Risk Opportunity Identification

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

### View 4: Pipeline Health Snapshot

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

### Canon References for Pipeline Analytics

Cross-references: full pipeline analytics views with implementation specs, and signal-trigger-action patterns for at-risk identification.

## Forecasting for Different Revenue Types

### New Business
- Most variable, least predictable
- Requires category-based + stage-weighted methods
- Pipeline coverage should be 3.5-4x due to lower close rates
- Segment by deal size: SMB vs. Mid-Market vs. Enterprise
- Apply longer-period trends (quarterly, not monthly) for accuracy

### Expansion Revenue
- More predictable than new business (existing relationships, known accounts)
- Use account-level health scores and usage data as leading indicators
- Pipeline coverage can be lower (2.5-3x) because conversion is higher
- Track trigger events: contract anniversaries, usage thresholds, team growth

### Renewal Revenue
- Most predictable — use run-rate models as the baseline
- Focus forecasting energy on at-risk accounts (low health score, support tickets, declining usage)
- Assume 90-95% gross retention as the base; forecast the exceptions
- Early warning: any account with a health score below threshold 90+ days before renewal


---

## Pipeline Visibility & Reporting

Pipeline visibility is the ability to see what's in your pipeline, trust that it's accurate, and act on it before it's too late. Most revenue teams have dashboards. Few have visibility. The difference: dashboards show numbers; visibility drives decisions.

### The Visibility Stack (4 Layers)

- **Layer 1: Pipeline Structure** — Stage design with verifiable exit criteria (buyer actions, not seller activities). 5–8 stages max. Probabilities increase monotonically.
- **Layer 2: Pipeline Reporting** — Reports and dashboards that show pipeline state. What most teams stop at.
- **Layer 3: Pipeline Hygiene** — Automated systems that keep pipeline data clean, current, and trustworthy.
- **Layer 4: Pipeline Intelligence** — Alerts and signals that surface what needs attention NOW, before humans notice.

### Dashboard Architecture

One dashboard per audience. Leading indicators first. Exceptions over summaries. Consistent time frames.

**Executive Dashboard** (CRO/VP Sales/CEO, weekly — "Are we going to hit the number?")
| Widget | Metric | Format |
|--------|--------|--------|
| 1 | Pipeline by Forecast Category (current period) | Stacked bar |
| 2 | Pipeline Coverage Ratio (open pipeline ÷ remaining target) | Single number with RAG |
| 3 | Win Rate Trend (rolling 3 months) | Line chart |
| 4 | Average Deal Size Trend | Line chart |
| 5 | Forecast vs Actual (current + prior 2 periods) | Bar chart |
| 6 | Top 10 Deals (value, stage, next step, days in stage) | Table |

RAG thresholds: Green ≥3.5x, Amber 2.5–3.4x, Red <2.5x. *Based on Clari 3.2× benchmark; Ebsta 2025 suggests up to 5.3× may be needed given declining win rates. Calibrate: quota ÷ win rate.*

**Sales Manager Dashboard** (daily — "Which deals need my attention today?")
Stage movement, stale deals (by threshold), activity per rep, speed-to-lead SLA, forecast accuracy by rep, pipeline created vs. target.

**Individual Rep Dashboard** (daily — "What should I work on right now?")
Pipeline by stage, deals closing this month/quarter, activities vs. target, overdue tasks, quota attainment.

**RevOps Operational Dashboard** (weekly — "Is the system healthy?")
Data quality score, stage conversion rates (funnel), pipeline velocity (days per stage), loss reason distribution, pipeline created vs. target, enrichment coverage.

### Pipeline Hygiene Automation

**Stale Deal Thresholds** (recommended by stage):
| Stage | Stale After | Action |
|-------|------------|--------|
| Discovery | 7 days | Alert rep |
| Qualification | 10 days | Alert rep + manager |
| Solution Design | 14 days | Alert rep + manager |
| Proposal | 7 days | Alert manager (high urgency) |
| Negotiation | 5 days | Alert manager + VP |

**Overdue Close Date Handling:** Daily job auto-pushes past close dates to end of current month, creates a task, and tracks `Close_Date_Push_Count`. Target: <5% of pipeline with overdue close dates.

### Pipeline Quality Score

Six dimensions based on Gong and Ebsta research (300+ signals, 655K+ analysed opportunities):

| Dimension | What to Measure | Research Backing |
|-----------|----------------|-----------------|
| **Engagement / Activity Velocity** | Frequency and recency of buyer interactions | Gong core signal; Ebsta: interaction frequency, recency, type |
| **Multi-Threading** | Contacts engaged per deal from different functions | Ebsta 2023: single-threaded ~8% win rate; 3+ contacts = 2.4× higher close rate |
| **Decision-Maker Access** | Direct engagement with economic buyer | Ebsta 2025: early DM involvement = +55% win rate |
| **Time in Stage / Deal Age** | Days in stage vs. historical average | Gong 2024–25: win rate drops 50% when deal pushed from 1 week to 1 month |
| **Next Steps / Progression** | Clarity of agreed next action with date | Gong: clarity of next steps as core progression signal |
| **Trend Direction** | Positive vs. negative engagement trajectory | Ebsta: engagement trend as forward indicator |

*Operational template — adapt weights to your GTM process. Track trend over time, not just absolute score. Deals declining on 2+ dimensions: flag for immediate deal review.*

**Big Deal Alerts:** Trigger when deal value exceeds threshold (e.g., >€50K mid-market; >€200K enterprise), advances to Qualification+, or close date moves into current quarter. Recipients: VP Sales, CRO, RevOps.

### Pipeline Intelligence Signals

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

### Pipeline Movement Waterfall

Track weekly changes to understand momentum:
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

### Essential Reports Checklist

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

*References: Clari (3.2× pipeline coverage benchmark, 2024–25); Ebsta 2025 GTM Benchmarks (655K opportunities, $43B pipeline); Gong (close date push impact — win rate drops ~50% at 1 month vs. 1 week); Salesforce research: active pipeline health management = 18% higher win rates, 28% more accurate forecasts.*

---

## Norton Framework Additions (Source: Kyle Norton / Aviv Canaani, Revenue Leadership Podcast, 2026)

### Forecast Variance as System Health Signal

Forecast variance isn't just an accuracy problem — it's a diagnostic signal for deeper system issues.

**What Variance Tells You:**
- ±10% variance → Healthy system, normal deal volatility
- ±20% variance → Qualification inconsistency or ICP drift
- ±30%+ variance → Methodology decay, data quality issues, or wrong ICP entirely

**Quality-Velocity-Predictability Triangle:**
Better ICP fit → shorter cycle time → more predictable forecast → better resource allocation → higher quality pipeline → (compounds)

**Cycle Time as Primary Constraint Indicator:**
Velocity bottlenecks (not volume gaps) often limit growth. If deals consistently stall at a specific stage, that's your system constraint — fix it before adding more pipeline.

### Bottom-Up Capacity-Based Forecasting (Canaani, E64)

An alternative to top-down target-based forecasting:

**The model:**
1. Know cost per meeting
2. Know conversion rate at every stage
3. Know sales cycle length (Datarails: 30-45 days)
4. Know AE meeting capacity before quality drops
5. Only hire new AEs when pipeline exists to fill their calendars

**Datarails proof point:** Projected new ARR within 5% margin of error, three out of four quarters. This was achieved by knowing the real productivity numbers, not by top-down quota allocation.

**Contrast with conventional approach:**
- Conventional: Board target ÷ reps + stretch = quota → hope pipeline materialises
- Capacity-based: Actual productivity data → bottoms-up capacity model → forecast based on what the system can actually produce

**When to use:** Best suited for organisations with 4+ quarters of pipeline data, established conversion rates, and a mature enough inbound engine to have predictable meeting volume.

**Add to accuracy benchmark:** Canaani's 5% margin (3/4 quarters) sits at the "Elite" level in the existing forecast accuracy benchmarks.

## How to Use This Skill

**"Our forecast is always wrong":** Start with accuracy measurement — how wrong, in which direction, and for whom? Then diagnose: is it a process problem (no forecast discipline), a data problem (stages don't mean anything), or a judgment problem (reps are optimistic)?

**"How do I forecast this quarter?":** Walk through the multi-method approach: category-based for deal-level, stage-weighted for validation, capacity model for sanity check. Present the range.

**"How do I run a forecast call?":** Give the specific structure, red flags to listen for, and time allocation. Push away from status updates toward deal inspection.

**"We don't have enough pipeline":** Translate to coverage analysis. Show the math: current pipeline × historical conversion = projected close. Gap to target = how much pipeline needs to be generated, and by when.

**Annual/quarterly planning:** Start with the capacity model (what can the team produce?), validate against market opportunity, build the pipeline generation plan to support the number, and set quotas that align with capacity.

---

## Signal → Trigger → Action: Forecast Breach Rules

These connect forecasting to the Operating Cadence. When a forecast signal fires, the cadence ensures someone acts — not next quarter, but this week. These rules plug into the revenue dashboard and weekly/monthly rituals.

### Forecast-Specific Breach Rules

| Signal | Trigger Threshold | Action | Forum | Owner |
|--------|------------------|--------|-------|-------|
| Pipeline coverage drops below 3x | Coverage < 3x for current quarter target | Activate pipeline generation contingency within 5 business days. Pull forward next-quarter pipeline. Review outbound, partner, and marketing channels. | Weekly revenue dashboard | CRO + CMO |
| Commit coverage below 0.9x target | Commit < 90% of remaining quarter target | Inspect every Best Case deal for acceleration potential. Identify deals that can move to Commit with specific interventions. | Weekly Sales Pipeline Loop | VP Sales |
| Forecast accuracy trending >±20% | 2 consecutive weeks where delta between forecast and pace exceeds 20% | Diagnose root cause: qualification drift, stage definition inconsistency, or rep sandbagging. Initiate A3 problem statement. | Weekly revenue dashboard | RevOps |
| Best Case slippage rate >40% | More than 40% of Best Case deals slip in any 4-week period | Tighten Best Case criteria. Review whether Best Case deals meet at least 3 of 5 Commit validation checkboxes. Likely a qualification problem. | Monthly Strategy Review | VP Sales + RevOps |
| Single rep variance >±30% for 2+ quarters | Individual rep forecast accuracy below ±30% consistently | Coaching intervention: is it optimism (always over), sandbagging (always under), or methodology gap? Different root causes, different fixes. | Manager 1:1 | Frontline Manager |
| New pipeline creation below 80% of period target | Weekly pipeline creation pace tracking below 80% of what's needed | Gap alert to leadership. Diagnose: is it a generation problem (not enough activity) or a conversion problem (meetings happening but not converting)? | Weekly revenue dashboard | CMO + VP Sales |
| Weighted pipeline diverges from category forecast by >25% | Stage-weighted pipeline total differs from Commit + Best Case total by >25% | The two methods are disagreeing. Likely cause: stage inflation (deals in later stages that haven't earned it). Run stage audit on deals contributing to the gap. | Weekly Sales Pipeline Loop | RevOps |

### Forecast Breach Escalation Path

Not all breaches are equal. Use this escalation framework:

```
SEVERITY 1 — INFORMATION (no action required yet)
  Coverage between 2.5-3x with >6 weeks left in quarter
  Single-week variance spike (noise, not signal)
  One rep's forecast off in isolation
  → Note in revenue dashboard. Monitor next week.

SEVERITY 2 — WARNING (action required this week)
  Coverage below 3x with <6 weeks left
  Forecast accuracy trending >±15% for 2+ weeks
  Best Case slippage rate climbing
  → Assign investigation owner. Report back in next weekly ritual.

SEVERITY 3 — BREACH (management intervention immediately)
  Coverage below 2.5x with <4 weeks left
  Commit coverage below 0.8x target
  Forecast accuracy >±25% for 3+ weeks
  → Escalate to CRO/CEO. Activate contingency playbook.
  → Consider: adjust expectations with board proactively.

SEVERITY 4 — CRITICAL (executive action)
  Coverage below 2x with <3 weeks left
  Quarter is materially at risk (>20% miss projected)
  → Board-level communication required.
  → Shift focus to: protect what's in Commit, manage the miss, build next quarter.
```

### Pipeline Generation Breach Rules

Forecasting doesn't just measure the current quarter — it must also monitor next quarter's pipeline health:

| Signal | Trigger | Action | Timeline |
|--------|---------|--------|----------|
| Next quarter pipeline < 2x target at quarter midpoint | Projected coverage gap | Activate outbound blitz + partner channel activation + marketing campaign acceleration | Within 1 week |
| Pipeline creation rate declining month-over-month | 2+ months of declining new pipeline | Diagnose: is inbound drying up, outbound slowing, or conversion dropping? Different roots, different fixes | Within 2 weeks |
| Pipeline age increasing (average days open rising) | Average deal age >1.5x segment benchmark for 2+ weeks | Pipeline deflation sprint — remove zombies to restore healthy metrics. See neon-deal-velocity-engineer. | Within 1 week |

### Connecting Forecasting to the revenue dashboard

The forecast is not a spreadsheet — it's a tile in the revenue dashboard with bands and breach rules:

```
FORECAST TILE CONFIGURATION:

  Metric: Current quarter forecast vs. target
  Green band: Commit ≥ 90% of target AND coverage ≥ 3x
  Amber band: Commit 70-90% of target OR coverage 2.5-3x
  Red band: Commit < 70% of target OR coverage < 2.5x

  Secondary: Forecast accuracy trend (trailing 4-week average)
  Green: ±10%
  Amber: ±10-20%
  Red: ±20%+

  Leading indicator: Next quarter pipeline creation pace
  Green: On track for 3x+ coverage
  Amber: Tracking to 2-3x coverage
  Red: Tracking to <2x coverage
```

When a tile turns red, it surfaces in the Weekly revenue dashboard ritual and triggers the corresponding breach action from the table above. The goal is: no surprises at quarter end. Every miss should be visible 6+ weeks in advance.

---

## Canon References

Cross-references: signal-trigger-action framework, operating cadence, revenue dashboard tile configuration, deal velocity system, KPI benchmark library, growth maturity model, and revops-metrics skill.

> Built by [Neon Triforce](https://neontriforce.com)
