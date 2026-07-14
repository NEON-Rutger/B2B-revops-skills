# ABM Measurement Dashboard Specification

## Introduction: What to Report vs. What NOT to Report

ABM dashboards must clearly separate leading indicators (account progression, buying group build) from lagging indicators (pipeline, revenue). They must also ruthlessly exclude vanity metrics that look good but do not predict outcomes.

**Principle: Report only what drives decisions.**

If a metric does not inform a go-no-go decision (handover yes/no, prioritise this account yes/no, resource reallocation yes/no), do not report it. Vanity metrics :  impressions, clicks, reaches :  trigger false confidence and waste board time.

## What NOT to Report (Vanity Metric Exclusion List)

These metrics are explicitly forbidden from any ABM dashboard:

```
METRIC                    WHY NOT
────────────────────────────────────────────────────────────────────────────
Impressions               Volume of ad served. Does not correlate with
                          buying readiness. Cheap to scale; expensive in
                          waste.

Clicks                    Clickthrough rate. Passive interest. Does not
                          predict engagement, consideration, or purchase.

Ad Reach                  Number of people who saw the ad. Breadth does not
                          equal depth. 10,000 people seeing an ad and 1 person
                          buying is still success :  the metric obscures the
                          signal.

Email Open Rate           Opening ≠ reading ≠ considering. Many opens are
                          incidental (preview pane, accidental clicks). Measure
                          engagement by click, reply, or action instead.

Website Traffic / Page    High traffic from non-buyers clouds the data. Traffic
Views                     is passive. Use only if segmented by account (traffic
                          from target accounts) or by action (pricing page
                          traffic from qualified accounts).

Content Downloads         Downloaded by researchers, not buyers. A whitepaper
                          download by a procurement analyst does not mean the
                          company is buying. Measure downstream (demo request,
                          meeting) instead.

Marketing-Generated       Leads are byproducts in ABM, not outputs. "We
Leads (MQLs)              generated 200 MQLs from target accounts" is not a
                          success metric. The success metric is "we created
                          X pipeline from those accounts."

Total Accounts Touched    Breadth without depth is noise. "We touched 500
/ Reach                   accounts this quarter" is meaningless. "We have
                          buying group coverage in 150 accounts" is meaningful.

Campaign Performance      Clicks, impressions, conversion rates on a single
(Campaign-level CTR,      campaign or email. In ABM, success is measured at the
Email metrics)            account level, not campaign level. Report account-level
                          results instead.
```

**If leadership asks for these:** Translate to account-level equivalents.

Example reframe:
- Leadership: "What was our email open rate?" 
- ABM answer: "32 of our target accounts opened the email (engagement signal). Of those, 8 clicked, 5 are now in the hot category (score 100+). Our handover target this month is 15 accounts; we are on track."

## What TO Report (Leading and Lagging Indicator Framework)

### Leading Indicators (Forward-Looking, Account Progression)

Leading indicators answer: "Are target accounts moving toward buying readiness?"

```
METRIC                              CALCULATION             TARGET / HEALTHY
──────────────────────────────────────────────────────────────────────────────
Total Target Accounts               Count of accounts on     200-500 (baseline)
                                    TAM list

Accounts by Stage
  • Unaware                         Count (0 signals)        Shrink steadily
  • Aware                           Count (passive engage)   30-40% of TAM
  • Engaged                         Count (active signals)   20-30% of TAM
  • In-Market                       Count (buying group      5-10% of TAM
                                    visible + score 100+)
  • Handed-to-Sales                 Count (in sales cycle)   Track separately

Accounts with Identified            (Accounts with >=50%     60%+ of TAM
Buying Groups                       role coverage) / TAM     (improve monthly)

Accounts Trending Up                Accounts with rising      15-20% of active
(Engagement Rising)                 engagement score         accounts (30+ point
                                                             rise in 2 weeks)

Accounts Ready for                  (Score >=100 AND         
Handover                            Coverage >=50% AND no    
                                    prior rejection) / TAM   

Accounts Handing Over               Count handed to sales    KPI: target is
                                    this period              based on sales
                                                             capacity

Critical Events                     Count (demo requests,    Trend monthly
(Week-over-week)                    meetings, RFP, trials)

Buying Group Coverage %             (Accounts with >=50%     Month-over-month %
(Average across TAM)                role ID) / TAM × 100     improvement target:
                                                             +3-5% per month
```

### Lagging Indicators (Outcomes, Revenue Attribution)

Lagging indicators answer: "Did the programme create revenue?"

```
METRIC                              CALCULATION             HEALTHY BENCHMARK
──────────────────────────────────────────────────────────────────────────────
Handed Accounts Creating            (Opps created from       60-80% conversion
Opportunities                       handed accounts) /       (within 90 days)
                                    (handed accounts)

Account-to-SQLQuality               (SQL-qualified opps from 60-75% (depends on
(if using SQL concept)              handed accounts) /       sales qualification
                                    (handed accounts)        rigor)

Time to Opportunity                 Days from handover to    <30 days median
                                    opportunity creation
                                    (median, not average)

Opportunity-to-Close Rate           (Closed-won deals from   20-40% (depends on
(ABM Attribution)                   handed accounts with     stage at handover)
                                    closed dates matching)

ABM-Sourced Pipeline                Total pipeline value     €2-3M+ for €15M ARR
(Open Opportunities)                tagged as ABM-sourced    company (baseline)

ABM-Sourced Closed Revenue          Total closed-won revenue €1M+ YTD for €15M
                                    from accounts handed via ARR company
                                    ABM (YTD)

Win Rate (ABM)                      (Closed-won opps from    15-30% (higher than
                                    handed accounts) /       non-ABM baseline)
                                    (handed opportunities)

Average Contract Value              Revenue from ABM opps /  +25-50% vs.
(ABM vs. non-ABM)                   # of closed won opps vs. non-ABM baseline
                                    non-ABM average

ABM Programme ROI                   (Revenue from ABM) /     3:1 minimum
(Simplified)                        (ABM programme cost) OR  5-9:1 elite
                                    (Revenue - Cost) /
                                    Cost
```

## Dashboard Architecture by Audience

Different audiences need different views. Design three separate dashboards.

### Dashboard 1: Executive / Board View (Monthly Review)

**Audience:** CEO, Board, VP Finance, Chief Revenue Officer

**Cadence:** Monthly (refresh first business day of month)

**Time frame:** Month-to-date, year-to-date, quarter-over-quarter

**Purpose:** At a glance: Is ABM working? Is it driving pipeline and revenue?

**Layout and Key Metrics:**

```
╔════════════════════════════════════════════════════════════════╗
║               ABM PROGRAMME :  EXECUTIVE DASHBOARD              ║
║                    July 2026 | YTD Summary                     ║
╚════════════════════════════════════════════════════════════════╝

┌─ HEADLINE NUMBERS ───────────────────────────────────────────┐
│ ABM Pipeline (Open)      €2.4M    ↑ 12% MoM       [Sparkline] │
│ ABM Closed Revenue (YTD) €620K    ↑ 8% vs Q2      [Sparkline] │
│ ABM Programme ROI        4.2:1    (healthy)                    │
│ Win Rate (ABM)           26%      ↑ 3% vs avg                 │
│ Avg Deal Size (ABM)      €310K    ↑ €45K vs avg               │
└──────────────────────────────────────────────────────────────┘

┌─ ACCOUNT STAGE WATERFALL ────────────────────────────────────┐
│                                                                │
│   Unaware        Aware       Engaged    In-Market  Handed-Sales│
│   60 accounts    75 accounts 40 accts   20 accts   5 accts    │
│   (30%)          (38%)       (20%)      (10%)      Closed=2   │
│                                                                │
│   [Visual: waterfall showing progression]                     │
│                                                                │
│   Trend: Engagement stage growing ↑  In-Market steady         │
└──────────────────────────────────────────────────────────────┘

┌─ BUYING GROUP COVERAGE (Key Gate) ──────────────────────────┐
│ Accounts with >=50% role coverage:  120 / 200 = 60%          │
│ Target: 65% by month-end            [Progress bar]           │
│ Trajectory: On track (+3% this month)                         │
└──────────────────────────────────────────────────────────────┘

┌─ HANDOVER & CONVERSION ─────────────────────────────────────┐
│ Accounts handed this month:       16                         │
│ Sales acceptance rate:            89% (14 accepted)          │
│ Accounts creating opps (YTD):     12 / 100 = 12%            │
│ Opp conversion rate:              75%                        │
└──────────────────────────────────────────────────────────────┘

┌─ KPI STATUS ───────────────────────────────────────────────┐
│ ✓ ABM pipeline target: €2.4M / €3.0M target = 80% (on track) │
│ ✓ Handover SLA: 89% acceptance (target >=80%)                │
│ ✓ Win rate: 26% (target >=20%)                               │
│ ⚠ In-Market accounts: 20 / 25 target = 80% (slight lag)     │
│ ✓ Revenue attribution: €620K YTD (tracking to €1.2M annual)  │
└──────────────────────────────────────────────────────────────┘

┌─ NARRATIVE ─────────────────────────────────────────────┐
│ ABM programme generated €620K closed revenue YTD with 4.2:1 │
│ ROI. Pipeline is tracking to target. Buying group coverage  │
│ at 60% :  driving 75% handover conversion. Sales acceptance  │
│ rate (89%) indicates strong handover discipline.            │
└──────────────────────────────────────────────────────────────┘
```

### Dashboard 2: Sales Leadership View (Weekly)

**Audience:** VP Sales, Sales Directors, Account Executive Managers

**Cadence:** Weekly (refresh Friday morning for Monday review)

**Time frame:** This week, last 4 weeks

**Purpose:** Which accounts should sales prioritise? Which accounts are at risk of slipping?

**Layout and Key Metrics:**

```
╔════════════════════════════════════════════════════════════════╗
║           ABM PROGRAMME :  SALES LEADERSHIP DASHBOARD           ║
║                 Week of July 14-18 | This Month               ║
╚════════════════════════════════════════════════════════════════╝

┌─ PRIORITY QUEUE: Ready-for-Handover Accounts ──────────────┐
│ Accounts Ready (Score >=100, Coverage >=50%)                 │
│                                                              │
│ #1  Acme Corp         Score 125  Coverage 60%  NEW HANDOVER  │
│ #2  Tech Solutions    Score 118  Coverage 75%  NEW HANDOVER  │
│ #3  Global Industries Score 145  Coverage 80%  IN SALES      │
│ #4  Startup X         Score 107  Coverage 55%  IN SALES      │
│ #5  Big Corp Div      Score 102  Coverage 52%  IN SALES      │
│                                                              │
│ This month: 5 accounts ready. 2 pending sales acceptance.   │
└──────────────────────────────────────────────────────────────┘

┌─ AT-RISK ACCOUNTS (Currently Handed, Engagement Declining) ──┐
│ These accounts are in sales pipeline but showing low         │
│ engagement. AE should investigate / re-engage.               │
│                                                              │
│ Account         AE          Engagement    Last Signal   Days │
│ ──────────────────────────────────────────────────────────   │
│ Alpha Inc       Mike Chen   Declining     July 8 (6d)   ⚠    │
│ Beta Corp       Sarah Lee   Flat          July 10 (4d)  =    │
│ Gamma Tech      Mike Chen   Healthy       July 16 (0d)  ✓    │
│                                                              │
│ Recommendation: Re-engage Alpha. Check with AE on Beta.    │
└──────────────────────────────────────────────────────────────┘

┌─ BUYING GROUP COVERAGE BY ACCOUNT (In Sales) ───────────────┐
│ Account         Coverage    Missing Role(s)       Action    │
│ ──────────────────────────────────────────────────────────   │
│ Acme Corp       60%         End-User Champion    AE to map   │
│ Tech Solutions  75%         Procurement          :            │
│ Global Ind      80%         :                     :            │
│ Startup X       55%         Technical Buyer,     AE outreach │
│                             Influencer           required    │
│                                                              │
│ MULTI-THREADING: 3 accounts need 2+ champion IDs (risk)     │
└──────────────────────────────────────────────────────────────┘

┌─ HANDOVER SLA THIS WEEK ───────────────────────────────────┐
│ Handovers sent to sales: 3 packets (Mon, Wed, Fri)          │
│ Sales responses received: 2 / 3 (67%) within 48h SLA        │
│ Pending response: 1 (awaiting Sarah Lee review)             │
│                                                              │
│ Action: Chase pending response. Send reminder to Sarah.     │
└──────────────────────────────────────────────────────────────┘

┌─ OPPORTUNITIES CREATED FROM ABM THIS WEEK ─────────────────┐
│ New opps created:  2                                         │
│ - Acme Corp: $310K deal (Mark Johnson intro'd Economic)      │
│ - Startup X: €85K deal (early-stage trial → paid pilot)     │
│                                                              │
│ Total new opps this month (YTD): 5 opps = €750K pipeline   │
└──────────────────────────────────────────────────────────────┘
```

### Dashboard 3: Marketing Operations View (Daily / Weekly)

**Audience:** Marketing Leader, ABM Manager, Marketing Ops

**Cadence:** Daily update (pull signals), Weekly review (Friday)

**Time frame:** This week, last 4 weeks, month-to-date

**Purpose:** Are we keeping accounts engaged? Are we hitting handover targets? Where are the buying group gaps?

**Layout and Key Metrics:**

```
╔════════════════════════════════════════════════════════════════╗
║           ABM PROGRAMME :  MARKETING OPS DASHBOARD              ║
║                    Daily / Weekly Update | July                ║
╚════════════════════════════════════════════════════════════════╝

┌─ ENGAGEMENT SCORE DISTRIBUTION (This Month) ────────────────┐
│                                                              │
│ 0-25 (Watchlist)      ████  45 accts     -8 from last week  │
│ 26-50 (Aware)         ██████████ 75 accts     +5            │
│ 51-100 (Engaged)      ███████ 40 accts       -5            │
│ 101-150 (Hot)         █████ 25 accts        +15 ↑ RISING  │
│ 150+ (In-Market)      ███ 15 accts          +2            │
│                                                              │
│ INTERPRETATION: Accounts accelerating into Hot stage.      │
│ Top mover: Tech Solutions (90->145 in 2 weeks)             │
└──────────────────────────────────────────────────────────────┘

┌─ NEW BUYING GROUP IDENTIFICATIONS (This Week) ──────────────┐
│ New Economic Buyers identified:      3                      │
│ New Technical Buyers identified:     2                      │
│ New End-User Champions identified:  1                      │
│ New Procurement contacts identified: 4                      │
│                                                              │
│ Total new contacts identified: 10                           │
│ Buying group coverage improved: 8 accounts crossed 50%      │
│                                                              │
│ Highest-priority gaps: 12 accounts missing End-User         │
│ Assignment: Prospect for end-user champion (next 2 weeks)  │
└──────────────────────────────────────────────────────────────┘

┌─ CRITICAL EVENTS (This Week) ──────────────────────────────┐
│ Demo requests:            3  (fastest: responded 4h)        │
│ Meetings scheduled:       2  (booked for next week)         │
│ RFP initiated:            1  (Acme Corp :  accelerated)      │
│ Trials activated:         1  (Startup X :  ongoing)         │
│ Proposal requests:        0                                 │
│                                                              │
│ Critical events trending:  ↑ +20% vs last week (positive)  │
└──────────────────────────────────────────────────────────────┘

┌─ HANDOVER TRACKER ─────────────────────────────────────────┐
│ Accounts ready (meet criteria):      5                      │
│ Handover packets prepared:           5                      │
│ Sent to sales:                       5 (this week: 3)       │
│ Sales responses received:            4 (80% response)       │
│ Accepted by sales:                   4 (100% acceptance)    │
│ On-hold pending re-qualification:    1 (awaiting coverage)  │
│                                                              │
│ This month YTD: 16 handed, 14 accepted = 89% rate          │
│ Handover SLA compliance: 95% (targets met within 48h)       │
└──────────────────────────────────────────────────────────────┘

┌─ ACCOUNTS REQUIRING ACTION (Priority List) ─────────────────┐
│ IMMEDIATE (Score declining >50% in 2 weeks):                │
│   • Old Manufacturing: 95 -> 30. Engagement stopped.        │
│     ACTION: Re-engagement campaign + root-cause analysis    │
│                                                              │
│ HIGH (Buying group gap, score >80):                         │
│   • Acme Corp: Missing End-User Champion (3 week gap)       │
│   • Beta Innovations: Missing Technical Buyer               │
│     ACTION: Prospect + warm outreach to identified contacts │
│                                                              │
│ MEDIUM (Score rising, not yet ready):                       │
│   • Growth Tech: 70 -> 85 (trending well, handover 1 week)  │
│   • Startup X: 60 -> 72 (nurture continuing)                │
│     ACTION: Continue targeted nurture. Monitor for critical │
│              event.                                         │
└──────────────────────────────────────────────────────────────┘

┌─ SEGMENT PERFORMANCE (MTD vs. Target) ──────────────────────┐
│ Segment          Target Accts  Engaged  Hot  In-Market  %    │
│ ───────────────────────────────────────────────────────────  │
│ Enterprise (500+) 50            35     8     4         32% ↑ │
│ Mid-Market        100           60    12     8         40% =  │
│ SMB               50            25     5     3         28% ↓  │
│                                                              │
│ INTERPRETATION: Mid-market performing to plan. Enterprise   │
│ above target. SMB lagging :  check for signal capture gap.   │
└──────────────────────────────────────────────────────────────┘

┌─ WEEKLY ACTION ITEMS ──────────────────────────────────────┐
│ ☐ Re-engage Old Manufacturing (low engagement)              │
│ ☐ Prospect for 3 End-User Champions (Acme, Beta, other)   │
│ ☐ Prepare handover packet: Growth Tech (score 85 -> 100)   │
│ ☐ Review SMB segment signals (potential capture gap)       │
│ ☐ Send nurture to 8 accounts trending up (momentum support)│
└──────────────────────────────────────────────────────────────┘
```

## Building Your Dashboard Infrastructure

### Option 1: Spreadsheet with Formulas (Pilot / Manual)

**Setup:** Google Sheets or Excel with linked CRM data

**Columns:** Account name, Engagement Score, Role Coverage %, Champion Y/N, Stage, Handover Ready Y/N, Last Update

**Refresh:** Manual weekly (pull data Friday, update Sunday evening)

**Limitation:** Impractical at >100 accounts or >1 week cadence

### Option 2: Native CRM + BI Tool (Recommended)

**CRM Layer:**
- Salesforce / HubSpot account records
- Custom fields: Engagement Score (formula), Role Coverage % (formula), Handover Ready (formula)
- Account stage (custom picklist: Unaware / Aware / Engaged / In-Market / Handed)
- Campaign/ABM source tags

**BI Tool (Tableau, Looker, Power BI, or native BI):**
- Pull CRM data hourly
- Calculate leading/lagging metrics
- Render dashboards for each audience
- Embed in Slack channels for alerts

**Advantage:** Real-time, scalable, integrated with sales workflow

**Setup effort:** 3-4 weeks

### Option 3: ABM Platform Native (Best for Scale)

**Platforms:** 6sense, Demandbase, RollWorks

**Built-in dashboards:**
- Account stage progression waterfall
- Buying group coverage heatmaps
- Engagement scoring by account
- Handover recommendation engine

**Advantage:** Pre-built logic, third-party intent integration, buying group detection

**Cost:** €50-200K+ annually

## Dashboard Alert Thresholds

Set up automated alerts for conditions that require action:

```
ALERT CONDITION                     TRIGGER                 ACTION
──────────────────────────────────────────────────────────────────────
Account score rising >50%            Score increase in       Assess for
in 2 weeks                           any account             handover readiness

Buying group coverage               Coverage reaches        Prepare handover
reached >=50%                        50% threshold           packet

Critical event detected             Demo / meeting /        Escalate to sales
                                    RFP triggered           within 24h

Handover ready (all gates           All three gates open    Send handover
met)                                (score, coverage,       packet
                                    not rejected)

Account score declining             >50% drop in 2 weeks    Alert marketing;
>50% in 2 weeks                                             assess campaign
                                                            impact

Sales handover SLA breach           >48h without sales      Chase sales for
                                    response                response

Handed account creating              Opp tagged as ABM-      Tag opportunity;
opportunity                          sourced, created        monitor to close

Pipeline attribution                 Opp closed (won/lost),  Calculate ROI;
(post-close)                         matched to ABM account  report to exec
```

---

## Source Attribution

Dashboard architecture and metric definitions adapted from:
- 6sense Predictive Buyer Engagement Framework (2026)
- Demandbase Dashboard and Reporting Best Practices (2024)
- Forrester ABM Metrics and KPI Research (2026)
- HubSpot ABM Measurement Guide (2025)
- Practitioner implementation case studies from Neon Triforce (2025-2026)
