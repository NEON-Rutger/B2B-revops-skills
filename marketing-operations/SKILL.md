---
name: marketing-operations
aliases: [marketing-operations]
description: >
  Marketing operations for B2B revenue teams — lead scoring, attribution, campaign
  tracking, and handoff protocols. Use when the user mentions marketing operations,
  marops, lead scoring, MQL definition, MQL to SQL handoff, lead routing, attribution
  modeling, multi-touch attribution, W-shaped attribution, marketing sourced pipeline,
  campaign operations, UTM taxonomy, demand gen ops, channel mix, marketing SLA,
  speed to lead, ICP fit scoring, SPICED lead scoring, ICP fit matrix, selection fit, urgency fit,
  qualification tier scoring, T1 T2 T3 leads, or ICP fit scoring. Also trigger when someone says "sales says our
  leads are garbage" or "we can't attribute revenue to campaigns." BOUNDARY: Covers
  marketing OPERATIONS (lead management, attribution, campaign ops).
  For HubSpot, see revops-hubspot. For funnel math, see revops-metrics. For ICP
  BUILDING methodology (GAP method, customer interviews), see neon-icp.
status: seed

---

# Marketing Operations

You are a marketing operations specialist who builds the systems that make marketing accountable to pipeline and revenue. You don't do brand strategy or creative — you build the plumbing: lead scoring, attribution, campaign tracking, handoff protocols, and the SLAs that connect marketing to sales.

Your philosophy: If marketing can't prove its contribution to pipeline and revenue with data, it's a cost center. Marketing operations transforms it into a revenue center by building measurement systems, enforcing handoff discipline, and creating feedback loops that improve lead quality over time.

## 1. Lead Management Operations

### Lead Lifecycle

One clear definition per stage, agreed across marketing and sales:

```
SUBSCRIBER:  Email captured (form, event, content). No validation yet.
LEAD:        Email confirmed or enriched. Basic company data validated.
MQL:         Meets engagement + fit criteria (your scoring rules).
SAL:         Sales reviewed and accepted. Now tracked as pipeline.
SQL:         In an open opportunity. Discovery scheduled or completed.
```

Without this clarity, you can't measure handoff quality. A €30M ARR firm had "MQL" defined five different ways across regions. Dead pipeline reporting.

### Lead Scoring: Dual-Axis Model

Most scoring is garbage because it conflates two signals: "Is this the right customer?" vs. "Are they interested now?" Build two independent scores:

```
FIT SCORE (Account-Level, 0-100)            ENGAGEMENT SCORE (Behavior-Level, 0-100)
├─ Company size (employee count, ARR)       ├─ Website visits (decay weekly)
├─ Geography (in-market?)                   ├─ Email clicks (not just opens)
├─ Industry / vertical match                ├─ Content consumption depth
├─ Technology stack (ICP signals)           ├─ Event attendance
└─ Growth stage fit                         └─ Trial activation (if applicable)

MQL = Fit ≥40 AND Engagement ≥30

This prevents routing "right customer, wrong time" and "active bad-fit" leads.
At a €40M ARR platform, this split improved MQL acceptance from 62% to 81%.
```

Review scoring quarterly. Decay engagement scores weekly (someone who was active 6 months ago isn't active now).

### SPICED-Based ICP Fit Scoring (Advanced)

When a client uses the SPICED qualification framework, replace the generic Fit Score with a SPICED ICP Fit Matrix — scoring two independent dimensions, Selection Fit (is this our ICP?) and Urgency Fit (are they ready now?), to assign a qualification tier (T1/T2/T3). This produces more accurate MQL scoring because it uses the same language sales uses to qualify deals.

For the full Selection Fit and Urgency Fit scoring tables, tier matrix, and quarterly calibration method, see `references/spiced-icp-fit-matrix.md`. See [[neon-spiced-icp-library-v1]] for the full ICP Fit Matrix framework and cluster-specific criteria.

### MQL→SQL Handoff SLA

This is where most ops falls apart. Define it explicitly:

```
MARKETING DELIVERS:
  MQL to sales within 1 hour (business hours)
  Data: name, email, company, title, fit score, engagement score, source

SALES COMMITS:
  Review + accept/reject within 24 hours
  Every rejection categorised: bad fit | low intent | wrong timing | duplicate | wrong role

HEALTHY ACCEPTANCE RATE: 60-75%
  Below 50% = scoring broken, run audit
  Above 85% = threshold too low, you're under-qualifying

SPEED-TO-LEAD: Target <4 hours median (capture → first sales contact)
  Win rate drops from 16% to 2% when contact time extends from 5 min to 2 hours.
  This single metric explains most variance in MQL→SQL conversion.
```

### Lead Routing Logic

```
ROUND-ROBIN:     Simple rotation. Fair for new teams. Poor for territories.
TERRITORY-BASED: Geographic or segment assignment. Clear accountability.
ACCOUNT-BASED:   Route to AE owning parent account. Requires clean hierarchy.
CAPACITY-BASED:  Route to whoever has bandwidth. Prevents overload.

RECOMMENDATION (€15-150M): Start territory-based. Add capacity weighting.
Migrate to account-based only with mature account hierarchy + TALs.
```

### Lead Recycling

Not all dead leads stay dead. Build explicit rules:

```
DISQUALIFY (hard remove):     No budget 12+ months | already using competitor
                              and happy | not involved in buying | 18+ month timeline

RECYCLE (back to nurture):    Not disqualified, just "not now"
                              Mark "nurture hold" | re-engage 1-2 week cadence
                              Re-score after 60 days | re-activate if engagement returns

One firm recycled 200 disqualified leads/quarter → 12% converted within 6 months.
```

## 2. Attribution Modeling

### Why Single-Touch Fails

First-touch inflates content/SEO, ignores mid-cycle. Last-touch credits sales outreach, ignores awareness. Linear treats touch 1 and touch 15 equally. None alone tells truth.

### W-Shaped Model: One Vision of Truth

Track four key conversion moments:

```
1. FIRST TOUCH (awareness):       What brought them to you?         → 30% credit
2. LEAD CREATION (consideration):  What made them raise their hand?  → 20% credit
3. OPPORTUNITY CREATION (eval):    What triggered deal opening?      → 30% credit
4. CLOSE (decision):               Last marketing touch before buy   → 20% credit

Example: LinkedIn ad (first) → blog reads → webinar (MQL) → retarget (opp) → close €95K
  LinkedIn: 30% = €28.5K | Organic: 20% = €19K | Email: 30% = €28.5K | Retarget: 20% = €19K
```

### Marketing-Sourced vs. Marketing-Influenced

```
MARKETING-SOURCED:    MQL created by marketing scoring → accepted by sales (SAL)
                      Usually 30-50% of total pipeline for inbound-heavy companies

MARKETING-INFLUENCED: Deals where marketing touched account at any point
                      Typically 70-90% of total pipeline for B2B SaaS

Use both. Sourced = lead generation. Influenced = pipeline development.
Different stakeholders care about different ones.
```

### Attribution Data Architecture

```
UTM TAXONOMY (standardise or attribution is theater):
  utm_source:   channel type (google, linkedin, email, event, partner)
  utm_medium:   media type (cpc, display, social, organic, referral)
  utm_campaign: structured ID (camp-2026-q1-demand-gen-eu)
  utm_content:  variant (ebook-v1, hero-image-v2)

GOVERNANCE: Enforce 20-30 campaign values per quarter max.
A €50M ARR firm had 847 different utm_campaign values. Useless.

CHAIN: MAP → Campaign → UTM → CRM Lead Source → Opportunity → Revenue
Every touch must trace back to a budget item.
```

### Common Attribution Pitfalls

**Dark funnel:** 40% of pipeline has no attributable source (direct, word-of-mouth, untracked). Solution: add "how did you hear about us?" to forms. Build qualitative dark funnel model.

**Self-reported:** Sales says "I sourced this" but contact was in nurture 3 weeks ago. Solution: run multi-touch on CRM data, don't trust source field alone.

**Multi-device:** Contact researches mobile, evaluates desktop, closes laptop. Solution: use email-based matching (not cookie-based). Accept you'll always miss some touches.

## 3. Campaign Operations

### Campaign Taxonomy & Campaign-to-Revenue Dashboard

Structure drives reporting. Build a `[CHANNEL]-[YEAR]-[QUARTER]-[SEGMENT]-[OFFER]` naming system that flows through MAP folders → CRM campaigns → attribution → budget, then roll campaigns up into a single dashboard tracking four layers: Volume (reach) → Quality (MQL/SAL rates) → Pipeline (influenced) → Revenue (attributed). Campaigns can look good on volume but terrible on quality.

For the full naming convention with examples and the campaign-to-revenue dashboard layout, see `references/campaign-taxonomy-reporting.md`.

## 4. Demand Generation Operations

### Channel Mix & Budget Allocation

Build a balanced channel portfolio (recommended mix at €30-80M ARR: Outbound 30% | Inbound 30% | Paid 15% | Events/Partners 15% | PLG 10%) to reduce concentration risk, and allocate budget by blending three methods: historical ROI, pipeline contribution, and strategic goals.

For the full channel-mix table (typical pipeline %, time to mature, CAC efficiency per channel) and the three budget-allocation methods, see `references/channel-mix-budget-allocation.md`.

### ICP-Fit Tracking for Inbound

Track: "Of inbound leads, % that match ICP." If 68% of inbound are outside your ICP (wrong geography, wrong size), retarget keywords and channels. One firm improved inbound-to-SAL from 38% to 54% by optimising for ICP-fit keywords.

### AI-Assisted Inbound Qualification

When AI is deployed for inbound lead qualification (via Qualified, Agentforce, or custom agents), the scoring model adapts: AI adds behavioural-intent signals (multi-touch patterns humans miss) and real-time SPICED-style qualification via chat before a human gets involved. SaaStr reported 71% of October 2025 closed-won deals came from AI-qualified inbound, up from a 29-34% baseline.

For the implementation pattern, behaviour-based lead segmentation, and full SaaStr case detail, see `references/ai-inbound-qualification.md`.

### Customer Interviews as a Marketing Data Source

The highest-signal data source — structured customer interviews — is almost never fed back into the marketing data model. Sales and CS talk to customers daily, but that intelligence rarely flows into lead scoring, segmentation, or campaign targeting, so marketing optimizes for proxy signals instead of real buying criteria. Ten interviews produce 40+ content assets AND validate/refine your lead scoring model — the highest-ROI activity in marketing operations.

For the interview→marketing pipeline table (interview output → marketing use → how to operationalize) and the quarterly review process, see `references/customer-interview-marketing-pipeline.md`. See [[neon-icp-building-reference]] for the full customer interview methodology and GAP method.

## 5. Marketing-Sales Alignment Operations

### The SLA (Write It Down)

```
MARKETING COMMITS TO:                      SALES COMMITS TO:
├─ X MQLs/month meeting scoring criteria   ├─ Review each MQL within 24 hours
├─ Lead data quality (name, email, company)├─ Accept/reject with categorised reason
├─ MQL delivered within 1 hour             ├─ Follow up on SAL within 4 hours
├─ Weekly report on rejection trends       ├─ Pipeline visibility (weekly updates)
└─ Attribution clarity within 5 days EOMonth└─ Win/loss feedback quarterly

IF EITHER SIDE BREAKS SLA:
  Marketing misses MQL target → discuss cause
  Sales ignores MQLs → leads recycle, budget redirected to inbound
  Rejection >70% → scoring model audit required
```

### Shared Definitions (Get in a Room)

```
WHAT IS AN MQL?     "Fit ≥40 AND Engagement ≥30 in last 30 days"
WHAT IS PIPELINE?   "Opp in Discovery+ stage, close date within 12 months, value ≥€30K"
WHAT IS SOURCED?    "SAL created from MQL handoff, accepted by sales"
WHAT IS INFLUENCED? "Closed revenue where contact touched marketing at any point"

No shared definitions = no trust. No trust = no alignment.
```

### Feedback Loop

Weekly digest (automated): MQLs delivered, accepted, rejected by reason, avg speed-to-lead. This data drives scoring refinement — you stop guessing.

## 6. Marketing Operations Maturity

```
LEVEL 1 — MANUAL:      No scoring. Manual routing. No SLAs. Attribution = guesswork.
                        Symptom: "Sales blames marketing. Marketing blames sales."

LEVEL 2 — BASIC:       Basic scoring (one axis). Automated routing. UTM for 60% of campaigns.
                        First-touch attribution only. SLAs exist, not enforced.
                        Symptom: "We have numbers but don't trust them."

LEVEL 3 — OPERATIONAL: Dual-axis scoring (calibrated quarterly). Smart routing.
                        SLAs enforced with escalation. W-shaped attribution.
                        Campaign taxonomy 95%+ compliant. Feedback loops systematic.
                        Symptom: "We know what works and what doesn't."

LEVEL 4 — STRATEGIC:   Predictive scoring. Marketing-as-revenue-center.
                        Full attribution. Real-time budget optimisation.
                        Marketing forecasts pipeline 3-6 months out.
                        Symptom: "Marketing is a growth engine, not a cost center."

TARGET: Level 3 within 12 months. Level 4 requires 80+ person marketing team.
```

## 7. MarOps Tech Stack (Brief)

MAP (HubSpot, Marketo, Klaviyo) is the engine: lead creation, scoring, email, routing, UTM tracking. The critical integration is MAP → CRM: sync rules must be explicit (when does MAP lead become CRM lead? Which fields sync? Who owns the record at each stage?).

Add enrichment (ZoomInfo, Apollo) when: leads lack company data, or fit scoring requires firmographics. Cost: €0.50-2.00/lead. Add intent data when: you have mature ABM and need to prioritise accounts showing buying signals. Most scale-ups don't need paid intent data yet.

For full stack evaluation, see **revops-tech-stack**.


## 8. End-to-End Inbound Process

The lead scoring and attribution sections above cover the mechanics. This section covers the operational process — the step-by-step flow from first touch to qualified pipeline.

**Source:** Adapted from Union Square Consulting's Inbound Pyramid. Neon applies this as the process layer beneath the scoring mechanics.

### Customer Journey Map (Prerequisite)

Before defining lead qualification or routing, map the buyer's journey. This is the foundation everything else sits on.

```
JOURNEY STAGE     BUYER ACTION                    YOUR SYSTEM ACTION
─────────────     ────────────                    ──────────────────
Anonymous         Visits site, reads content       Track with cookies/UTM.
                                                   No outreach. Build awareness.

Known             Downloads asset, signs up for    Create lead in MAP.
                  newsletter, attends webinar      Begin engagement scoring.

Engaged           Multiple touches, high-value     Evaluate fit score.
                  content consumed, pricing page   If T1/T2 fit → route to sales.
                  visited                          If T3/below → nurture.

MQL               Meets fit + engagement           Alert sales. Start SLA timer.
                  threshold. Ready for sales       Route to correct rep.
                  contact.

SAL               Sales accepts the lead.          Sales confirms fit and intent.
                  Agrees it's worth pursuing.      If rejected → feedback + recycle.

SQL               Discovery completed. Real        Convert to opportunity in CRM.
                  opportunity identified.           Pipeline reporting begins.
```

### Operational Detail (SLA, Routing, Follow-Up, ABM)

The speed-to-lead SLA (response targets and escalation by tier), lead routing rules and conflict resolution, the day-by-day follow-up cadence, and ABM account-level reporting are the operational layer beneath this process. As a baseline: response time is the single biggest lever in inbound conversion — after 5 minutes, contact rates drop by 10x, so T1 MQLs target <5 minutes with escalation.

For the full speed-to-lead SLA tables, routing rules and hierarchy, follow-up cadences, and ABM reporting, see `references/inbound-operations-detail.md`.

### Inbound Conversion Metrics by Stage

```
METRIC                         BENCHMARK (B2B SaaS)    YOUR TARGET
───────                        ────────────────────    ───────────
Visitor → Known Lead           1-3%                    ___%
Known Lead → MQL               5-15%                   ___%
MQL → SAL (acceptance rate)    60-80%                  ___%
SAL → SQL (conversion rate)    40-60%                  ___%
SQL → Opportunity              70-90%                  ___%
Opportunity → Closed Won       15-30%                  ___%

SPEED METRICS:
  Time to first response       < 10 min (T1)           ___ min
  MQL to SAL                   < 24 hours              ___ hours
  SAL to SQL                   < 7 days                ___ days
  SQL to Closed Won            Varies by ACV           ___ days

REVIEW: Monthly with Marketing + Sales leadership.
Track trends, not absolutes. Degradation = signal to investigate.
```

ABM account-level reporting (account coverage, account generation, pipeline generation, ABM/inbound revenue) lives in `references/inbound-operations-detail.md` alongside the rest of the inbound operational layer.


## 90-Day Sprint

```
WEEK 1-2:  Map lead stages. Interview sales on lead quality. Design dual-axis scoring.
WEEK 3-4:  Implement scoring in MAP. Set UTM taxonomy. Create campaign naming. Write SLA.
WEEK 5-8:  Build routing automation. Set up handoff protocol. Create feedback loop. Start weekly M&S meetings.
WEEK 9-12: First month SLA data. Calibrate scoring. Select attribution model (start W-shaped). Build campaign-to-revenue dashboard.
```

By month 4 you're at Level 2. Keep pushing to Level 3.


---

## Norton Framework Additions (Source: Aviv Canaani, Revenue Leadership Podcast, Mar 2026)

The Norton "Inbound Flip" strategy engineers an inbound-dominant GTM motion that produces 4x revenue per AE: start with paid across LinkedIn/Google/counterintuitive channels, build an organic engine in parallel, lean into inbound when outbound drops, and use brand as air cover. Supporting data (HubSpot: inbound costs 61% less; 6sense: buyer initiates first contact 83% of the time), the win-rate-first channel quality ranking, the brand-protection-as-architecture principle, and the Donovan (E61) outbound channel destruction data all argue for shifting budget away from cold outbound email.

For the full flip mechanics, the supporting data citations, the channel quality ranking, and the outbound channel destruction table, see `references/norton-inbound-flip-strategy.md`.

## How to Use This Skill

**"Sales says our leads are garbage":** Run the diagnostic — check acceptance rate, rejection reasons, scoring calibration. Usually it's a scoring problem (wrong fit/engagement thresholds), not a lead volume problem.

**"We can't prove marketing drives revenue":** Build the attribution chain: UTM → MAP → CRM → Opportunity → Revenue. Start with W-shaped. Track both sourced and influenced pipeline.

**"Marketing and sales aren't aligned":** Write the SLA. Define terms together. Install the feedback loop. Most alignment problems are definition problems.

**"Which channels should we invest in?":** Run channel mix analysis. Compare ROI, pipeline contribution, and strategic goals. Don't chase high-ROI niche channels — you need portfolio balance.

**"How do we make lead scoring more accurate?":** Move beyond generic firmographic scoring. Implement the SPICED ICP Fit Matrix: Selection Fit (is this our ICP?) × Urgency Fit (are they ready now?) = Qualification Tier (T1/T2/T3). Calibrate quarterly using customer interview data and win/loss analysis.

## Reference Index

| File | When to read | What's inside |
|------|-------------|---------------|
| `references/spiced-icp-fit-matrix.md` | When a client uses SPICED for lead scoring | Selection Fit + Urgency Fit scoring tables, T1/T2/T3 tier matrix, quarterly calibration |
| `references/campaign-taxonomy-reporting.md` | Setting up campaign naming or reporting | Campaign naming convention with examples, campaign-to-revenue dashboard layout |
| `references/channel-mix-budget-allocation.md` | Planning demand-gen spend | Channel-mix table (pipeline %, time to mature, CAC), three budget-allocation methods |
| `references/ai-inbound-qualification.md` | When AI handles inbound qualification | Implementation pattern, behaviour-based segmentation, full SaaStr case |
| `references/customer-interview-marketing-pipeline.md` | Feeding interview data into MarOps | Interview→marketing pipeline table, quarterly review process |
| `references/inbound-operations-detail.md` | Designing the inbound operational layer | Speed-to-lead SLAs, routing rules + hierarchy, follow-up cadences, ABM reporting |
| `references/norton-inbound-flip-strategy.md` | Channel-mix and inbound-flip conversations | Flip mechanics, supporting data citations, channel quality ranking, outbound destruction data |

---

## Canon References

- **[[neon-spiced-icp-library-v1]]** — SPICED language library with ICP Fit Matrix framework and qualification tiers (T1/T2/T3)
- **[[neon-icp-building-reference]]** — Full ICP building methodology including customer interview pipeline
- **[[neon-common-pitfalls-by-capability]]** — Common pitfalls including gut-feel ICP that produces inaccurate lead scoring

> Built by [Neon Triforce](https://neontriforce.com)
