---
name: cs-operations
aliases: [cs-operations]
description: >
  Customer success operations for B2B SaaS — the post-sale revenue engine that
  prevents churn, drives expansion, and compounds customer value. Use when the user
  mentions customer success, CS ops, health scoring, renewal management, churn
  prevention, expansion playbook, expansion signals, onboarding orchestration, time
  to first value, QBR, customer segmentation, coverage model, high-touch, low-touch,
  tech-touch, CSM ratios, NPS, CSAT, save plays, red accounts, CS-Sales handoff,
  churn autopsy, renewal discount governance, discount sunset, renewal pricing,
  or save plays with pricing components. Also trigger when someone says "we keep
  losing customers" or "our CS team is reactive" or "we have no idea which accounts
  will churn" or "discounts are expiring and customers are pushing back" or
  "renewal price increase resistance."
metadata:
  version: 1.1.0
status: seed

---

# Customer Success Operations

You are a CS operations architect. CS Ops is the post-sale revenue engine — it sits in the ICP Value Loops layer of the revenue operating system, owning Adopt → Realise Value → Renew → Expand. Without it, you're relying on individual heroics instead of systems.

## The CS Ops Operating Model

Four pillars. Neglect any one and the system breaks.

```
PROCESS DESIGN          TECHNOLOGY & SYSTEMS
├─ Playbooks            ├─ CS Platform (Gainsight, ChurnZero, Vitally, Planhat)
├─ Workflows            ├─ Product analytics (Pendo, Amplitude)
├─ Escalation paths     ├─ Support (Zendesk, Intercom)
├─ Governance           ├─ Survey tools (NPS, CSAT)
└─ Swimlanes            └─ Data warehouse integration

DATA & ANALYTICS        ENABLEMENT
├─ Health scores        ├─ CSM onboarding (2 weeks, not 2 months)
├─ Churn prediction     ├─ Playbook documentation
├─ Expansion scoring    ├─ Tools training
├─ Cohort analysis      ├─ Certification on key processes
└─ Team efficiency      └─ Knowledge base
```

## CS Maturity Model

```
┌────────────┬──────────────┬────────────────┬───────────────┬──────────────┐
│ Stage      │ Health Score │ Renewals       │ Expansion     │ Governance   │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ REACTIVE   │ None. React  │ Ad-hoc,        │ Accidental    │ CS isolated, │
│            │ to churn.    │ customer-led   │               │ no loops     │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ DEFINED    │ Manual, CSM  │ Playbook, 60d  │ Signals ID'd  │ Handoff doc  │
│            │ judgment     │ before expiry  │ inconsistently│ exists       │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ PROACTIVE  │ Composite,   │ Automated 90d  │ Scoring model │ Quarterly    │
│            │ weekly auto  │ process + save │ + targeted    │ CS-Product   │
│            │ alerts       │ playbooks      │ outreach      │ forums       │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ PREDICTIVE │ ML model,    │ Preventive     │ Expansion     │ Real-time    │
│            │ >80% churn   │ interventions, │ scoring feeds │ feedback     │
│            │ accuracy     │ <5% churn      │ Sales pipeline│ loops        │
└────────────┴──────────────┴────────────────┴───────────────┴──────────────┘
```

If you're Reactive: stop everything else and move to Defined first.

## Health Score Framework

The single most important CS Ops tool. Composite scores with weighted dimensions:

```
HEALTH SCORE = Weighted average of 5 dimensions

PRODUCT USAGE (35%)
  Login frequency, feature adoption, depth of use, usage trend
  Weight rationale: usage is the strongest churn predictor

RELATIONSHIP (25%)
  Executive sponsor engaged, NPS response, meeting cadence, org adoption %
  Weight rationale: champions save accounts

SUPPORT (18%)
  Ticket volume trend, severity, resolution time, CSAT
  Weight rationale: pain signals churn

COMMERCIAL (17%)
  Contract value trend, payment history, expansion conversations
  Weight rationale: money doesn't lie

OUTCOMES (5%)
  Achieving stated goals, ROI realization, milestone completion
  Weight rationale: data often incomplete early on
```

### Traffic Light System

```
GREEN (80+):  Expand. Growth partner posture. 2-5% churn risk.
YELLOW (40-79): Intervene. Increase touchpoints. 15-30% churn risk.
RED (<40):    Save mode. Executive intervention. 60%+ churn risk.
```

### Health Score Anti-Patterns

```
Binary scores ("healthy" vs "at risk")  → Use 0-100 scale with thresholds
Usage-only scores                       → Composite with multiple signals
Manual, updated quarterly               → Automated, updated weekly minimum
Score says green but they churn          → Calibrate against actual outcomes
Nobody acts on red accounts              → CS Manager reviews reds weekly
```

## Segmentation & Coverage Models

```
┌──────────────┬─────────────────┬─────────────────┬────────────┐
│ Segment      │ Criteria        │ Coverage Model   │ CSM Ratio  │
├──────────────┼─────────────────┼─────────────────┼────────────┤
│ HIGH-TOUCH   │ >€50K ARR       │ Named CSM        │ 1:10-30    │
│ (Strategic)  │ Complex product │ Quarterly EBRs   │            │
│              │ High expansion  │ Dedicated onboard│            │
├──────────────┼─────────────────┼─────────────────┼────────────┤
│ MID-TOUCH    │ €10-50K ARR     │ Pooled CSM       │ 1:30-80    │
│ (Scaled)     │ Moderate complex│ Templated touches│            │
│              │ Growth potential│ Triggered playbks│            │
├──────────────┼─────────────────┼─────────────────┼────────────┤
│ LOW-TOUCH    │ <€10K ARR       │ Automated        │ 1:100-500+ │
│ (Digital-led)│ Self-serve      │ In-app guidance  │            │
│              │ Simple use case │ Community/webinar│            │
└──────────────┴─────────────────┴─────────────────┴────────────┘
```

Reassess tiers quarterly based on usage growth, health, and expansion potential.

## Renewal Management

Start 120 days before contract end. Not 30.

```
T-120 days: PREP
  CSM reviews health, Finance pulls contract terms, Product flags blockers
  Output: Renewal strategy (standard / at-risk save play / expansion)

T-90 days: HEALTH CHECK
  QBR conducted, executive alignment, pulse on value delivery
  Score: Likely / At-risk / Needs work

T-60 days: PROPOSAL
  Standard: Renewal proposal sent
  At-risk: Executive sponsor conversation, barrier removal
  Expanding: Sales/CSM joint upsell conversation

T-30 days: NEGOTIATION
  Handle objections, escalate if needed

T-0: CLOSE
  Revenue booked, post-renewal thank you, reset for next cycle
  Feed learnings to Product
```

**Track:** On-time renewal rate, early renewal rate, save rate (red accounts renewed), renewal velocity.

## Expansion Playbooks

### Expansion Signals

```
USAGE:        Hitting seat limits, new feature adoption, DAU increasing
RELATIONSHIP: Champion promoted, new stakeholder engaged, positive NPS
COMMERCIAL:   Org headcount growth, new budget cycle, cross-functional interest
OUTCOMES:     Value achieved ahead of schedule, ROI exceeded, new use cases
```

### Expansion Ownership Model

```
Small expansion (<20% ACV):  CS owns end-to-end
Medium expansion (20-50%):   CS identifies, Sales closes
Large expansion (>50% ACV):  Sales owns, CS supports
```

CS-to-Sales handoff: CS prepares customer context, decision-maker, timeline, needs. Sales accepts or declines. If accepted, CS introduces Sales to champion and stays involved through close.

## Onboarding Orchestration

```
DAY 1-7: ACTIVATION
  Welcome email (within 2 hours), license activation, kickoff scheduled
  Success criteria defined: "What does success look like?"

DAY 8-30: IMPLEMENTATION
  Configuration, data migration, user training
  Weekly status calls, blocker resolution
  Milestone: Go-live readiness confirmed

DAY 31-60: STABILIZATION
  Go-live, first-week support surge (daily check-ins)
  Usage monitoring, issue resolution, user adoption tracking
  First value delivered: "Here's the impact you're seeing"

DAY 61-90: OPTIMIZATION
  Performance vs. success criteria, advanced feature rollout
  Executive check-in, health score baseline set
  Transition to business-as-usual CSM cadence
```

**Automation triggers:** No kickoff by day 3 → reminder. Not go-live by day 30 → alert manager. Usage <20% by day 60 → intervention. Health <50 by day 90 → yellow playbook.

**Track:** Time to kickoff (<3d), time to first login (<7d), time to first value (<30d), go-live on schedule (90%+).

## Event-Based Playbooks

```
USAGE DROP (WAU drops >30% week-over-week)
  Action: CSM outreach within 24 hours
  Root cause: Change, vacations, budget freeze, support issue?

NPS DETRACTOR (Score <6)
  Action: Call within 48 hours
  Document specific complaint, not generic dissatisfaction

CHAMPION DEPARTURE
  Action: Identify new stakeholder within 1 week
  Risk mitigation: Involve next-level executive immediately

SUPPORT ESCALATION (Sev-1 OR 3+ tickets in 7 days)
  Action: Triage within 2 hours, CS + Support Manager
```

## Renewal Discount Governance

### The Discount Sunset Problem

The #1 cause of contentious renewals: the initial deal had a discount that was never documented to expire. At renewal, the customer's anchor is what they paid — not what the product is worth. Every CSM dreads the conversation: "Why is my renewal 25% higher?"

This is a governance failure, not a customer problem. The fix is structural.

**Prevention (at deal close):**

- Every discounted deal must have a `Discount_Expiry_Date` in CRM
- T-120 renewal workflow must flag expiring discounts automatically
- CSM must prepare value justification BEFORE the renewal conversation, not after the customer complains

### Renewal Pricing Conversation Framework

**Step 1: Lead with value, not price (T-90).** Before any pricing conversation, deliver a value realisation report: usage data, business outcomes achieved, ROI vs. original business case. The customer needs to see the value before they see the price.

**Step 2: Frame the step-up (T-60).** "Your initial agreement included a first-year pricing benefit as part of [commitment/early adoption]. The renewal reflects the full value of the platform, which has [added X features / expanded Y capabilities / supported Z% more users than originally scoped]."

**Step 3: Offer graduated step-up if needed (T-30).** If the customer pushes back hard: 50% of the price increase in Year 1, full price Year 2. This is a save play, not a negotiation tactic — use only when the alternative is churn.

### Save Plays with Pricing Components

| Scenario | Save play | Pricing element | Approval |
|----------|-----------|----------------|----------|
| Discount expiring, customer at risk | Graduated step-up (50% Yr 1, full Yr 2) | Time-limited bridge | Sales Mgr |
| Usage dropped, customer underutilising | Scope reduction to lower tier | Retain at lower ARR; plan re-expansion | CSM |
| Feature gap blocking renewal | 90-day trial of higher tier at current price | Expansion play as save | CSM + Sales Mgr |
| GPO member threatening churn | Validate GPO terms. Confirm volume commitment. | Per GPO framework | Deal Desk |
| Budget genuinely cut | Split billing or deferred payment | Cash flow accommodation, not discount | Finance |

**Key rule:** Save plays with pricing components must be tracked separately from standard renewals. Tag with reason code. Track: what % of save-play renewals expand back to full price within 12 months? This tells you whether the save was effective or just delayed churn.

### GPO Renewal Coordination

For accounts under GPO/consortium agreements:

- **T-120:** Check GPO master record for current tier and volume status
- **T-90:** Validate actual volume against committed volume
- **T-60:** If volume below commitment, prepare tier adjustment conversation with GPO account owner
- **T-30:** Renewal terms must align with GPO agreement. No ad-hoc deviations without Deal Desk

For the full GPO handling framework (admin fees, volume tiers, negotiation rules), see pricing-strategy skill.


## Structured Onboarding-to-Renewal Process

This section operationalises the full post-sale lifecycle as a step-by-step process. The health scoring and playbooks above define what to monitor and when to act. This section defines the process backbone.

**Source:** Adapted from Union Square Consulting's Renewals + Expansion Pyramids. Neon applies this as the process layer beneath the health scoring framework.

### Sales → CS Handoff Process

```
TRIGGER:        Deal moves to Closed Won in CRM

T+0 (Day 0):   Automated handoff notification to assigned CSM
                CRM creates CS record with:
                  - SPICED summary (from sales discovery)
                  - Key stakeholders and roles
                  - Contractual commitments and timeline
                  - Known risks or open items from sales
                  - Product configuration / tier purchased
                  - Discount terms and expiry dates (if any)

T+1 (Day 1):   CSM reviews handoff document
                CSM schedules internal prep call with AE (15 min)

T+2 (Day 2):   Internal handoff call: AE briefs CSM
                  - What was promised? What wasn't?
                  - Who's the champion? Who's the blocker?
                  - What does success look like for this customer?
                  - Any landmines? (technical, political, budget)

T+3-5:         CSM sends welcome email to customer
                Schedules kickoff call
                Creates onboarding project plan

HANDOFF QUALITY CHECK:
  - Is SPICED summary complete? (If not → AE must fill gaps before handoff)
  - Are all stakeholders in CRM? (If not → CSM adds during kickoff)
  - Are discount terms documented with expiry? (If not → flag for renewal)
```

### Onboarding Process

```
PHASE 1: KICKOFF (Week 1)
  - Welcome call with key stakeholders
  - Confirm success criteria and timeline
  - Assign customer-side project owner
  - Share onboarding project plan
  - Set expectations for first value milestone

PHASE 2: TECHNICAL SETUP (Weeks 2-4)
  - Product configuration / environment setup
  - Data migration (if applicable)
  - Integration setup
  - Admin training
  - Document known issues or customisation needs

PHASE 3: USER ENABLEMENT (Weeks 3-6)
  - End-user training sessions
  - Create internal documentation / guides
  - Identify power users / internal champions
  - Validate initial adoption metrics

PHASE 4: FIRST VALUE (Weeks 4-8)
  - Confirm first value milestone achieved
  - Customer success story captured (even informal)
  - Transition from onboarding to ongoing CS cadence
  - Health score baseline established
  - First QBR/check-in scheduled

METRICS:
  Time to First Value (TTFV)      Target: < 30 days
  Onboarding completion rate      Target: > 90%
  Onboarding NPS/CSAT             Target: > 8/10
  Feature adoption at T+30        Target: > 3 core features
```

### Renewal Process Timeline

```
T-120 DAYS:  Renewal flag auto-created in CRM
             CSM reviews account health, usage, and expansion signals
             If health < 40 (Red): escalate immediately, don't wait

T-90 DAYS:   Renewal kickoff
             CSM reviews value delivered (prepare ROI summary)
             Internal alignment: any pricing changes, product updates?
             If discount expiring: begin value-led conversation (see Renewal Discount Governance)

T-60 DAYS:   Renewal conversation with customer
             Present: value delivered, roadmap alignment, proposed terms
             If upsell/expansion: present expansion proposal alongside renewal
             If at risk: activate save playbook

T-30 DAYS:   Contract sent
             If not signed: escalate to CS leader
             If discount negotiation: use graduated step-up (see Save Plays)
             Daily tracking of renewal pipeline

T-0:         Contract signed or churned
             If churned: initiate churn autopsy within 7 days
             If renewed: update CRM, notify team, celebrate

T+7:         Post-renewal check-in
             Confirm satisfaction with terms
             Set next QBR date
             Update health score
```

### Expansion Process Definition

```
EXPANSION SIGNALS (auto-tracked):
  - Usage approaching plan limits (>80% utilisation)
  - New departments/teams using the product
  - Feature requests for premium-tier functionality
  - Champion promoted or new exec sponsor engaged
  - Positive health trend (score increasing 3+ months)
  - Customer referral or case study participation

EXPANSION SCORING MODEL:
  Score 0-100 based on:
    Usage growth (30%)         — is usage increasing month-over-month?
    Stakeholder breadth (25%)  — are new people engaging?
    Feature depth (20%)        — are they using advanced features?
    Health trajectory (15%)    — is health score trending up?
    Contract headroom (10%)    — is there room to expand (seats, usage, products)?

EXPANSION OWNERSHIP:
  Score 0-40:   CSM monitors. No active sell.
  Score 41-70:  CSM plants seeds. Shares relevant content. Mentions capabilities.
  Score 71-100: CSM initiates expansion conversation. If deal > threshold → hand to AE.

  Handoff threshold: Varies by org. Typical: expansion > 30% of current ACV → AE involved.
  Below threshold: CSM closes expansion directly (with approval).

WHITESPACE ANALYSIS:
  For each account, map:
    Products purchased vs available    → product whitespace
    Users/seats vs potential           → seat whitespace
    Departments using vs total         → department whitespace
    Features adopted vs available      → feature whitespace
    Stakeholders engaged vs org chart  → relationship whitespace

  Review in QBR. Update quarterly. Use to prioritise expansion plays.
```


## CS-Product Feedback Loop

```
QUARTERLY ADVISORY BOARD
  3-5 key customer executives + Product VP
  Topics: Roadmap, feature priorities, competitive gaps
  Output: Customer priorities feed product planning

CHURN AUTOPSY (100% of churned accounts)
  Owner: CS Manager + Product Manager
  Questions: Why? When was decision made? Could we prevent it?
  Output: Product backlog item, process change, or competitive intel

FEATURE REQUEST TAGGING
  Every request tagged with: customer ARR, use case, competitive
  pressure, expansion impact, adoption blocker (Y/N)
  Product uses tags to prioritize backlog

ADOPTION BLOCKER LOG (Monthly review)
  Features blocking renewal/expansion get separate Product queue
  Quick fixes (<2 weeks) as hotfixes; larger items to quarterly planning
```

## Key Metrics

```
REVENUE                          TARGETS
  GRR                            >90% (>95% enterprise)
  NRR                            >110%
  Logo retention rate            >90%
  Expansion rate (% ARR growth)  >15%/year

OPERATIONAL
  Time to first value            <30 days
  Health score distribution      >70% green
  QBR completion (high-touch)    100%
  Renewal on-time rate           >90%
  Save rate (red accounts)       >40%

EFFICIENCY
  Accounts per CSM (by tier)     See coverage model
  Admin time (% of total)        <30%
  CSM attrition rate             <15%/year

LEADING INDICATORS
  Accounts with declining usage  Track weekly
  Accounts without exec sponsor  <5%
  Days to complete renewal       <60 days
  Core feature adoption rate     >70%
```

## Diagnostic Assessment

Score your CS Ops maturity. Count YES answers:

```
PROCESS:     Documented playbooks? Defined renewal timeline? Health scoring
             framework? Escalation paths? QBRs for all high-touch?
TECHNOLOGY:  Dedicated CS platform? Integrates with product analytics?
             Automated health scoring? Usage data visible to CSMs?
DATA:        Can forecast churn 30+ days out? Health dashboards? Track
             expansion signals? Segment by tier? Measure team efficiency?
ENABLEMENT:  Structured CSM onboarding? Accessible playbooks? Process
             certification? Monthly training?
GOVERNANCE:  CS-Product feedback loop? CS-Sales handoff process? Exec
             reviews CS metrics monthly? Churn autopsies? Expansion
             ownership clear? Discount sunset tracking in place?

0-6 YES  = Reactive.  Fix: Define playbooks, build basic health scoring
7-13 YES = Defined.   Fix: Integrate tech, automate playbooks
14-19 YES = Proactive. Fix: Build predictive models, optimize coverage
20-25 YES = Predictive. Fix: AI-assisted coaching, autonomous workflows
```

## Structured Onboarding-to-Renewal Process

Health scoring and renewal frameworks answer "who is at risk?" and "how do we retain them?" But they depend on a structured operational process from handoff to renewal. This section covers the end-to-end CS process model.

### Handoff and Onboarding Process (Sales → CS Transition)

The handoff is where retention is won or lost. A weak handoff creates context loss, broken promises, and a customer who feels like they're starting over.

**Pre-handoff (Sales responsibility):**
- Complete the SPICED summary in CRM (especially: Situation, Pain, Impact, Critical Event)
- Document committed outcomes — what did the customer buy the product to achieve?
- Identify the champion and economic buyer — who owns success internally?
- Flag any non-standard terms, pricing exceptions, or promised professional services

**Handoff meeting (Sales + CS):**
- Three-way call: Sales rep, CS lead, and customer champion
- Agenda: review committed outcomes, introduce CS team, confirm implementation timeline
- Transfer of relationship, not just account

**Onboarding process (CS responsibility):**
- Week 1: Kick-off call with success criteria defined (use SPICED Impact as baseline)
- Week 2-4: Implementation milestones tracked and reported to customer
- Day 30: First value checkpoint — has the customer experienced any tangible outcome?
- Day 60: Adoption checkpoint — is the product embedded in their workflow?
- Day 90: First health score review; confirm or redefine success criteria for Year 1

### Customer Health Monitoring Cadence

Health scoring defines the score. The cadence defines what you do with it.

```
FREQUENCY       ACTIVITY                                    OWNER
─────────       ────────                                    ─────
Weekly          Review accounts with score drop > 10pts     CSM (automated alert)
                Flag any Green → Yellow or Yellow → Red     CSM + CS Lead
Monthly         Full health score review for all accounts   CSM per account
                Escalation: any Red account reviewed with   CS Lead + AE
                CS Lead and AE
                Update health scores based on new data       CSM
Quarterly       Portfolio health review (CS team)           CS Lead
                QBR preparation for T1 accounts             CSM
                Red account recovery planning               CS Lead + AE
```

A health score without a review cadence is a dashboard no one acts on. The cadence is the operating system; the score is the signal.

### Process for Unhealthy Customers (Red Account Playbook)

Signals aren't enough. Define the playbook triggers — what happens automatically when a customer turns Red.

**Immediate actions (within 24 hours of Red flag):**
1. CSM notifies CS Lead
2. CS Lead reviews health breakdown — which dimension is driving Red? (Usage? Engagement? NPS? Adoption?)
3. CS Lead and AE jointly decide: rescue mode or renewal risk conversation

**Rescue mode (if > 90 days until renewal):**
- Executive outreach: CS Lead or Head of CS calls the economic buyer directly
- Root cause session: structured call to understand what went wrong
- Recovery plan: documented list of 3-5 actions with owners and deadlines
- Weekly check-in until back to Yellow

**Renewal risk mode (if < 90 days until renewal):**
- Activate renewal process (see below) immediately — do not wait for the standard T-90 trigger
- Consider commercial options: downgrade path, implementation support extension, POC of new features

### QBR Process Design

Quarterly Business Reviews are the highest-leverage CS touchpoint for T1 accounts. Most fail because they look backwards (usage reports) rather than forwards (strategic alignment).

**QBR agenda structure (45-60 minutes):**
1. **Their goals (10 min)** — What has changed in the business since the last QBR? Are the success criteria still right?
2. **Progress review (15 min)** — Outcomes delivered vs. committed outcomes. Use data, not anecdotes.
3. **Usage + health (5 min)** — Keep this short. It's context, not the point.
4. **Roadmap alignment (15 min)** — What's coming that's relevant to their goals? Use this to reinforce retention and create expansion hooks.
5. **Joint plan (10 min)** — 2-3 actions they commit to, 2-3 actions you commit to.

Not every account needs a formal QBR. T1 accounts: quarterly. T2 accounts: semi-annual or on-demand. T3 accounts: no QBR — use health score cadence only.

### Renewal Process

Renewal should start at T-90 (90 days before contract end). Starting at T-30 is too late for anything except discounting.

```
RENEWAL TIMELINE    ACTION
────────────────    ──────
T-90               CS initiates internal renewal review: health score, usage, expansion signals
                   AE and CS agree on renewal strategy: flat, uplift, or expansion
                   Identify key stakeholders — is the champion still in role?
T-60               First renewal conversation with champion: frame on value delivered
                   Share renewal proposal or pricing (if standard terms)
                   Surface any risk signals that could block renewal
T-30               Follow-up on open items from T-60 conversation
                   Escalate if no response or active objection
                   Deploy save plays only now: discount, terms flexibility, add-on gift
T-0                Contract signed
T+7                Post-renewal debrief: document what drove the outcome (win/loss reason)
```

For discount governance at renewal (approval matrices, ACV tiers, sunset policies), see pricing-strategy skill.

### Expansion Process

Expansion is a process, not an event. Most expansion dies because nobody owns the handoff from CS to Sales — or because the signal was visible but nobody acted on it.

**Account scoring for expansion readiness:**
- Consistent Green health score for 2+ quarters
- Usage of 80%+ of contracted capacity (quantitative trigger)
- Champion has expressed interest in additional use cases
- Stakeholder whitespace: contacts in departments not yet using the product

**Whitespace analysis — two dimensions:**
1. **Stakeholder whitespace:** Which teams or business units could benefit from the product but aren't using it? Map against org chart.
2. **Product whitespace:** Which features or modules is the customer licensed for but not using? Which complementary products are they not yet on?

**Expansion motion:**
- CS identifies and documents expansion signal in CRM
- CS-Sales handoff meeting: warm intro from CSM to AE or expansion AE
- AE runs commercial conversation; CSM provides customer context and stays on call initially
- CS role post-expansion: implement the expanded scope and track value delivery on expanded commitment

For full expansion architecture including NRR improvement methodology, see the expansion revenue architect skill. For handoff design and routing logic, see revops-handoffs skill.

---

## How to Use This Skill

**"We keep losing customers but don't know why":** Start with health scoring. Build the 5-dimension composite score. You'll see patterns within 4 weeks.

**"Our CS team is drowning":** Segmentation problem. Build the 3-tier coverage model. Most teams try to high-touch everyone — that doesn't scale past 50 accounts.

**"Expansion is left on the table":** Build expansion signals and scoring. Define the CS-Sales handoff. Most expansion dies because nobody owns the handoff.

**"Product doesn't listen to CS":** Install the feedback loop: churn autopsies, feature request tagging with ARR impact, quarterly advisory board. Product responds to revenue data.

**"We need to build CS Ops from scratch":** Run the diagnostic. Score your maturity. Fix the weakest pillar first. Month 1: playbooks + basic health scoring. Month 2: renewal process. Month 3: automation.

**"Discounts are expiring and customers are pushing back":** Install the renewal discount governance framework. Document every discount with an expiry date. Lead with value at T-90, frame the step-up at T-60, and have graduated step-up as a save play only at T-30. For discount governance policy (approval matrices, ACV tiers), see pricing-strategy skill.

**"GPO/consortium accounts coming up for renewal":** Check GPO master record. Validate actual vs. committed volume. Coordinate with Deal Desk. No ad-hoc terms outside the GPO framework.

> Built by [Neon Triforce](https://neontriforce.com)

---

## WbD Impact Journey — CS Action Framework

The Impact Journey maps the post-Mutual Commit customer journey into structured CS actions. Source: WbD Operating Model PDF, Chapter 08, pages 143-148.

### The 8 Stages (post-Mutual Commit focus)

| Stage | What's happening | CS Action |
|---|---|---|
| Mutual Commit | Contract signed — ownership transfers from Sales to CS | O1. Handoff from Sales |
| Onboarding | Setup, training, implementation begins | O2. Customer Kickoff; O3. Joint Impact Plan; O4. Achieve First Impact |
| Adoption / Retention | Customer uses product, realises core value | A1. Drive Impact Process; A2. Impact Review; A3. Health Scoring; A4. Trigger Plays |
| Renewal | Customer decides whether to continue | A5. Renewal using SPICED reassessment |
| Expansion | Customer adds scope, users, or capabilities | E1–E5: Whitespace Planning → Expansion Execution |
| Advocacy | Customer becomes promoter and reference | Implied: reference requests, case study participation |

### Health score interpretation by stage

- **Onboarding:** Track against Joint Impact Plan milestones. Red flag: first impact not achieved within agreed timeline.
- **Adoption:** Monitor active usage, CRM engagement, champion responsiveness. Score drops ≥20% in 30 days = trigger play.
- **Expansion readiness:** Customer has achieved consistent impact AND has whitespace (additional use cases or departments).

### Trigger plays by stage

| Trigger | Signal | Play |
|---|---|---|
| First Impact at risk | Onboarding >120% of agreed timeline | Executive sponsor call + revised Joint Impact Plan |
| Adoption plateau | Usage flat for 60+ days post-onboarding | Impact Review meeting, identify blockers |
| Churn risk | Health score <40, no champion engagement | Escalation play: CS + Sales + exec touch |
| Expansion signal | Consistent adoption, stakeholder growth, whitespace identified | Whitespace Planning session |

### Expansion timing guardrail

**Do not expand before First Impact (Stage O4).** Customers who are still in onboarding and asked about expansion create distrust. The signal to start expansion conversations: customer has achieved the core Impact documented in the Joint Impact Plan AND usage is spreading across the team (multiple stakeholders engaged).

Customers achieving impact in a **single area only** are more at risk of churn than customers with **widespread stakeholder usage** — expand to cover multiple Impact areas wherever possible.

*Source: WbD Operating Model PDF, Chapter 08, pages 143-148. Jacco van der Kooij, Revenue Architecture.*

---

## Operator Templates — Forecasting Worksheet (Renewals Tab)

The Renewals tab of the forecasting worksheet is specifically useful for CS operations modelling:
`Frameworks/Templates/cro-school/forecasting-worksheet-neon.xlsx`

Use the Renewals tab to model: renewal cohort sizing, churn impact on ARR, expansion uplift scenarios.

Original source: `Sources/Courses/CRO-School/Forecasting Worksheet _ Class #4_ Forecasting and Financial Modeling.xlsx`
Attribution: Adapted from Pavilion CRO School. Original author: Carter/Nalbandian/Dick.
