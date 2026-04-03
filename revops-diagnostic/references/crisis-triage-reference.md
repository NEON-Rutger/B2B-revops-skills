# Revenue Crisis Triage & Emergency Response — Reference

*Converted from revops-crisis skill. This content is now a reference for revops-diagnostic. When multiple systems break simultaneously, use this crisis triage framework before running standard diagnostics.*

---

## Crisis Recognition

A crisis is not "we missed a number." A crisis is when multiple system layers break simultaneously and you can no longer trust the basic machinery.

### Threshold Triggers (Any ONE = Crisis Mode)

```
FORECAST:  ±30%+ variance for 2+ consecutive quarters
WIN RATE:  Declined 5+ points over 3 quarters
PIPELINE:  Coverage below 3x AND falling month-over-month
RETENTION: NRR below 90% OR GRR below 80%
DATA:      Critical deal fields <70% complete; CRM ≠ finance by >10%
TRUST:     Sales blames marketing blames CS blames product (3+ parties)
PEOPLE:    2+ top performers leaving in one quarter; open cynicism
```

### The Multi-System Failure Pattern

```
DATA BREAKS ──┬── PROCESS FAILS ──┬── PEOPLE FRACTURE
              │                    │
         NOBODY CAN EXECUTE RELIABLY
              │
         TRUST COLLAPSES → CRISIS MODE
```

If you see data corruption + unclear process + silent wars between functions, you're in crisis mode.

---

## The Emergency Triage Protocol (4 Weeks)

### Week 1: DATA AUDIT — Can You Trust Your Data?

**The Rule:** If data quality <70% on critical fields, STOP. Nothing else matters.

```
EMERGENCY DATA AUDIT (sample 200 random open deals):

CRITICAL FIELDS                                   TARGET
□ Deal amounts populated?                         95%+
□ Close dates updated in last 14 days?            95%+
□ Stage assigned and makes sense?                 98%+
□ Contact role(s) assigned?                       80%+
□ Activity logged in last 30 days?                85%+
□ Next step documented?                           80%+
□ Won/lost reason populated (closed deals)?       95%+
□ Customer name matches finance system?           99%+

SCORING:
<70% at target = DATA CRISIS. Run 5-day blitz before anything else.
70-85%         = ACCEPTABLE. Proceed with caveats on all forecasts.
>85%           = GOOD. Proceed with confidence.
```

**The 5-Day Data Blitz (if <70%):**
- Day 1: Sort deals by completeness. Find worst teams/reps. Root cause: lazy? unclear definitions? tool issue?
- Day 2-3: RevOps + CRM admin run bulk updates on objective data. Pull in worst-data reps to update their own deals. Fix validation rules.
- Day 4-5: Establish daily data standup (15 min). Weekly data audit report. Assign data owner per team.

### Week 1-2: CASH DIAGNOSIS — What's the Immediate Revenue Risk?

**The Rule:** In a crisis, protect cash first. Senior people on the top 10 at-risk deals.

```
THE 2-HOUR CASH DIAGNOSIS:

1. Pull all open deals closing in 30-60 days + renewals due in 30-90 days
2. Stack rank by € amount
3. Flag at-risk: no recent activity, no champion, competitive threat,
   economic buyer not engaged
4. Top 10 at-risk = your downside exposure number for leadership
5. Assign executive owner to each (CRO or VP level, not deal owner)
6. Define next tangible action + deadline (this week, not "soon")
```

**Start the Daily Cash Standup (Monday of Week 2):**
15 minutes. Every day. CRO + VP Sales + VP CS + RevOps.
One line per deal: status, next action, owner, date. This is a war room. Run for 60 days.

### Week 2-3: ROOT CAUSE — Six Stages of Check in FAST Mode

Reference: For full methodology, see revops-diagnostic skill.

```
DAY 1: PURPOSE    — Clear, agreed definition of success? Target conflict?
DAY 2: DEMAND     — Real market demand? Right ICP? Problem still urgent?
DAY 3: CAPABILITY — Skills, tools, structure match the motion we're running?
DAY 4: FLOW       — Pick 20 random deals. Where do they stall? Bottleneck?
DAY 5: SYSTEM CONDITIONS & THINKING
       Data trusted? Stage exit criteria defined? Leadership mental model
       matches reality?
```

**Output: One-Page Root Cause Summary**

```
CRISIS:     [One-line description with numbers]
EVIDENCE:   [Data that proves it's real]
ROOT CAUSE: □ Purpose □ Demand □ Capability □ Flow □ System □ Thinking
IMMEDIATE FIX: [The ONE thing that unblocks everything else]
OWNER:      [Name]
TIMELINE:   [1-3 weeks]
```

### Week 3-4: CONSTRAINT IDENTIFICATION

Reference: For full framework, see revops-four-capability-maturity-assessment skill.

Score each 1-2 (crisis mode; nuance comes later):

```
GOVERNANCE:       Decisions being made? Steering mechanism exists?
ENABLEMENT:       Data/process/tool stack working?
REVENUE ENGINE:   Sales/CS engine producing?
CUSTOMER INSIGHT: Understand ICP and why you're winning/losing?

Emergency constraint = the ONE scoring 1 when others are at 2.
All four at 1? Start with Governance (you need a steering mechanism first).
```

**Constraint Unlock Logic:**

```
Governance = 1:  Install daily standup. Assign decision driver (CRO).
                 Unlock: Everything clearer because leadership knows what matters.

Enablement = 1:  Data audit (done Week 1) + define 3 non-negotiable processes.
                 Unlock: Teams can execute consistently.

Revenue = 1:     Win rate analysis. Talk to 5 lost deals fast.
                 Unlock: Know where to focus (discovery? closing? multi-threading?)

Insight = 1:     Pull top 5 wins and 5 losses. Pattern-match.
                 Unlock: Stop guessing about ICP.
```

---

## The 30-60-90 Crisis Response Plan

### Days 1-30: STABILISE

```
□ Data quality audit complete; blitz if needed (target: 85%+)
□ Top 10 at-risk deals identified with exec sponsors
□ Daily cash standup running
□ Root cause identified (which Six Stage is broken)
□ First structural fix in place (stage criteria, validation rules, or governance)
□ One quick win executed (visible improvement, however small)
□ All non-essential projects killed
```

### Days 31-60: DIAGNOSE & FIX

```
□ Full IFA diagnostic complete (reference revops-diagnostic)
□ Capability maturity assessed (reference revops-four-capability-maturity-assessment)
□ Fix roadmap drafted: 3 initiatives max, prioritised by constraint unlock
□ First major structural change: design complete, stakeholders mapped
□ Change management started (reference revops-change-management)
□ Weekly leadership update: "Here's what broke. Here's how we fix it."
□ Measure Day 1 baseline vs. now (data quality, forecast accuracy, win rate)
```

### Days 61-90: REBUILD

```
□ First structural change at 70%+ adoption
□ Initiatives #2-3 in design (NOT launched yet — don't launch 3 at once)
□ Operating cadence established (reference revenue-cadence skill):
  Weekly ops review (30 min), monthly deep-dive (90 min), quarterly reset
□ Forecast rebuilt with proper methodology (reference revops-forecasting)
□ Metrics dashboard live and trusted (reference revops-metrics)
□ Team sentiment: pulse survey shows improved trust
□ Hand off to revops-diagnostic and revops-four-capability-maturity-assessment for deeper work
```

---

## Four Crisis-Specific Playbooks

### A: THE FORECAST CRISIS — "Missed 3 quarters in a row"

```
ROOT CAUSE PATTERNS:
1. Bad data (amounts missing, close dates stale, wrong stages)
2. Sandbagging (reps entering deals late, hiding pipeline)
3. Pipeline inflation (stalled deals still counted, no stage exit criteria)
4. Wrong methodology (rep confidence instead of data-driven)

EMERGENCY FIX (Week 1-2):
• Build shadow forecast from scratch (CRM data × finance validation)
• Compare to current forecast. Variance >15% = data problem.
• Run 3 methods: rep probability, historical conversion, high-confidence only
• Take the lowest number. That's your realistic forecast.
• Daily: "How many deals closed that were/weren't in forecast?"

STRUCTURAL FIX (Week 3-8): reference revops-forecasting skill
• Define stage exit criteria (what moves a deal forward)
• Choose forecast method (start Conservative, move to Blended after 2Q)
• Weekly deal inspection (manager validates every deal in qualified stages)
• Monthly accuracy measurement: target ±10% (takes 2-3 quarters)
```

### B: THE PIPELINE CRISIS — "Coverage at 2.1x and falling"

```
ROOT CAUSE PATTERNS:
1. Top-of-funnel dried up (lead volume down, channels underperforming)
2. ICP drift (selling to wrong people; lots of leads, few convert)
3. AEs not prospecting (no pipeline generation from existing accounts)
4. Qualification too strict (over-screening legitimate opportunities)
5. Slow velocity (deals stuck in early stages, capacity full of Discovery)

EMERGENCY FIX (Week 1-2):
• Pipeline audit: coverage, composition by source, velocity check
• IF top-of-funnel: Activate dormant prospects, refocus SDRs to outbound
• IF ICP drift: Pull win/loss for 10 deals, identify winning attributes
• IF AEs passive: Pull high-usage existing customers, create upsell list
• IF qualification wrong: Blinded test with 20 rejected leads
• IF velocity slow: Manager sweep of 60+ day stalled deals

STRUCTURAL FIX (Week 3-8): reference gtm-planning + revops-metrics skills
• Pipeline generation plan with source owners and weekly accountability
• ICP enforcement: score every lead, only ≥60% accepted as SQL
• Velocity targets by stage (Discovery 21-35d, Proposal 14-21d)
• Quarterly pipeline planning: [target ÷ win rate × 1.3] = pipeline needed
```

### C: THE CHURN CRISIS — "NRR crashed to 85%"

```
ROOT CAUSE PATTERNS:
1. Product-market fit erosion (competitor better, market shifted)
2. CS under-resourced (bad onboarding, no health checks, slow support)
3. No health scoring (can't identify at-risk accounts, surprise churn)
4. Renewal process broken (starts too late, single-threaded)
5. Acquisition quality (winning wrong-fit customers, over-promising)

EMERGENCY FIX (Week 1-2):
• Churn diagnosis: rate by cohort, timing, reason, segment
• At-risk identification: all renewals due in 90 days, flag 2+ risk indicators
  (no activity 30d, usage declining, unresolved tickets, no contact 60d)
• Executive save calls on >€50K ARR at-risk accounts (CRO/VP, not CSM)
• Quick fix based on pattern:
  CS under-resourced → Senior CSM on highest-risk accounts
  No health scoring → Build simple score this week (5-7 indicators)
  Renewal process → Start renewals 120 days out (not 30)
  Acquisition quality → Pre-flight check before deal close

STRUCTURAL FIX (Week 3-8): reference cs-operations skill
• Health scoring system with escalation rules
• Renewal calendar visible 120 days in advance
• CS coverage model by segment with right ratios
• Expansion sourcing: monthly identification of growth signals
```

### D: THE TRUST CRISIS — "Sales blames marketing, CS blames product"

```
ROOT CAUSE: No shared metrics, no shared cadence, no shared accountability.
Functions optimise independently → metrics conflict → blame cycle.

EMERGENCY FIX (Week 1-2):
• ONE shared dashboard all functions see daily (ARR, pipeline, churn, CAC)
• Shared definitions: Get all VPs in a room. "What is a qualified lead?"
  Agree on ONE definition per handoff. Make it rule.
• ONE weekly meeting: CRO + VP Sales + VP Marketing + VP CS + RevOps
  45 min fixed time. Metrics → issues → last week's actions → next actions.
• Break finger-pointing: 1:1 with loudest voices. "What would need to be true
  for you to trust this team?" Fix the specific gap, not the politics.
• Quick win: Fix ONE handoff visibly (e.g., lead scoring with Sales input)

STRUCTURAL FIX (Week 3-8): reference revenue-cadence skill
• Shared metrics dashboard (RevOps owns, all functions see)
• Shared definitions document (one-pager per major concept)
• Weekly governance meeting with decision log
• Cross-functional playbooks for major motions
```

---

## What NOT To Do In A Crisis

```
✗ Change comp plans mid-quarter — adds chaos on chaos. Lock it; announce next Q.
✗ Fire the VP Sales immediately — 75% of the time it's a system problem.
  Do the diagnostic first. If it IS a person problem, you'll know in 2 weeks.
✗ Buy a new tool — technology doesn't fix broken processes. Fix process first.
✗ Launch 10 initiatives — scattered focus amplifies crisis. Fix ONE thing hard.
✗ Hide numbers from the board — they'll find out. Show the bad numbers + the plan.
✗ Blame external factors — "market is down" explains variance but doesn't fix revenue.
✗ Skip the daily standup — it IS your information gathering. Commit for 60 days.
✗ Fix data + process + people simultaneously — pick ONE. Usually: data first,
  then process (now you have clean data), then people (trust rebuilds when
  data + process work).
```

---

## How to Use This Reference

**"Everything is broken":** Start with Crisis Recognition → Emergency Triage (4 weeks) → 30-60-90 plan.

**"Forecast is unreliable":** Playbook A. Shadow forecast → identify pattern → structural fix.

**"Not enough pipeline":** Playbook B. Audit composition → root cause → targeted activation.

**"Losing customers":** Playbook C. At-risk identification → executive save calls → structural CS fix.

**"Teams don't trust each other":** Playbook D. Shared dashboard → shared definitions → weekly meeting.

**"Data is garbage":** Run the Data Quality Checklist first. Nothing else works until data is clean.

**After Day 90:** Hand off to revops-diagnostic and revops-four-capability-maturity-assessment for the deeper work. Crisis mode is about stabilisation. Long-term improvement is a different skill set.
