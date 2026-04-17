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

When a client uses the SPICED qualification framework, replace the generic Fit Score with a SPICED ICP Fit Matrix. This produces more accurate MQL scoring because it uses the same language sales uses to qualify deals.

**The ICP Fit Matrix: Selection × Urgency**

Instead of a single "fit" number, score two independent dimensions:

**Selection Fit (Is this our ICP?):**

| Criterion | Weight | Data Source | Score 0-3 |
|-----------|--------|-------------|-----------|
| Company size (ARR/employees in ICP range) | 25% | Enrichment (Apollo, ZoomInfo) | 0=outside, 1=adjacent, 2=close, 3=bullseye |
| Industry/vertical match | 20% | Enrichment + self-reported | 0=wrong, 1=tangential, 2=adjacent, 3=core |
| Technology stack signals | 20% | Enrichment (technographic) | 0=no signals, 1=some, 2=strong, 3=exact match |
| Growth stage / funding | 15% | Enrichment + news | 0=wrong stage, 1=early, 2=approaching, 3=ideal |
| Geography (in-market) | 10% | Enrichment | 0=excluded, 1=secondary, 2=primary, 3=core |
| Role/title of contact | 10% | Form data + enrichment | 0=wrong dept, 1=adjacent, 2=right dept, 3=decision-maker |

**Selection Fit Score** = Weighted average × 33.3 (scales to 0-100)

**Urgency Fit (Are they ready now?):**

| Signal | Weight | Data Source | Score 0-3 |
|--------|--------|-------------|-----------|
| Engagement recency (last 7 days) | 25% | MAP behavioral data | 0=none, 1=>30d, 2=7-30d, 3=<7d |
| Content depth (pricing, case studies, demo) | 25% | MAP page tracking | 0=blog only, 1=mid-funnel, 2=bottom-funnel, 3=pricing/demo |
| Critical event signals | 20% | Form data, intent, news | 0=none, 1=implied, 2=mentioned, 3=confirmed |
| Repeat visits / multi-session | 15% | MAP tracking | 0=1 visit, 1=2-3, 2=4-6, 3=7+ |
| Direct request (demo, call, trial) | 15% | Form submission type | 0=content only, 1=newsletter, 2=webinar, 3=demo/trial |

**Urgency Fit Score** = Weighted average × 33.3 (scales to 0-100)

**Qualification Tier Assignment:**

| Tier | Selection Fit | Urgency Fit | MQL Action |
|------|-------------|-------------|------------|
| **T1 — Perfect Fit** | ≥70 | ≥60 | Immediate routing to AE. Speed-to-lead <1 hour. |
| **T2 — Good Fit** | ≥50 | ≥40 | Route to SDR for qualification call. Standard SLA. |
| **T3 — Opportunistic** | ≥30 | ≥30 | Add to nurture sequence. Re-score monthly. |
| **Below threshold** | <30 | Any | Do not route. Passive nurture only. |

**Why this is better than generic scoring:** Selection Fit uses ICP-specific criteria, not generic firmographics. Urgency Fit captures buying intent, not just engagement volume. The tier system (T1/T2/T3) aligns with how sales qualifies deals using SPICED. SDRs and AEs speak the same qualification language as marketing.

**Implementation note:** The scoring weights above are starting points. Calibrate quarterly by running a correlation analysis: which scoring dimensions best predict Closed-Won? Increase weight on predictive dimensions, decrease on noise.

See [[neon-spiced-icp-library-v1]] for the full ICP Fit Matrix framework and cluster-specific criteria.

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

### Campaign Taxonomy

Structure drives reporting. Build a naming system:

```
[CHANNEL]-[YEAR]-[QUARTER]-[SEGMENT]-[OFFER]

Examples:
  PAID-SOCIAL-2026-Q1-SCALEUP-DEMAND-GEN
  WEBINAR-2026-Q2-ENTERPRISE-PRODUCT-DEMO
  CONTENT-2026-Q1-SEO-REVOPS-GUIDE
  EVENT-2026-Q3-SAAS-NORTH-SUMMIT

This taxonomy flows through: MAP folders → CRM campaigns → attribution → budget
```

### Campaign-to-Revenue Dashboard

The one table that matters:

```
Campaign Name | Spend | Leads | MQLs | SAL | SQL | Pipeline | Revenue | ROI
EMAIL-Q1...   | €8K   | 450   | 180  | 135 | 98  | €2.1M    | €680K   | 8.5x
```

Track four layers: Volume (reach) → Quality (MQL/SAL rates) → Pipeline (influenced) → Revenue (attributed). Campaigns can look good on volume but terrible on quality.

## 4. Demand Generation Operations

### Channel Mix

```
Channel              | Typical Pipeline % | Time to Mature | CAC Efficiency
Inbound/Content      | 20-35%             | 6-12 months    | High (€5-15/lead)
Outbound/SDR         | 25-40%             | 2-3 months     | Medium (varies)
Paid Digital         | 10-20%             | 3-4 months     | Medium (€30-150/lead)
Events/Webinars      | 5-15%              | 3-6 months     | Low-Medium
Partnerships         | 5-15%              | 6-12 months    | High
Product-Led          | 5-20%              | Depends         | Highest

RECOMMENDED MIX (€30-80M ARR):
  Outbound 30% | Inbound 30% | Paid 15% | Events/Partners 15% | PLG 10%
  Reduces concentration risk. Enables scaling without hiring armies of SDRs.
```

### Budget Allocation

Three methods, blend all three:

```
1. HISTORICAL ROI:   Weight budget by channel ROI (inbound 12x → give it more)
2. PIPELINE CONTRIBUTION: Allocate proportional to where pipeline comes from
3. STRATEGIC GOALS:  Reduce sales cost → increase inbound. Hit number now → surge outbound.
```

### ICP-Fit Tracking for Inbound

Track: "Of inbound leads, % that match ICP." If 68% of inbound are outside your ICP (wrong geography, wrong size), retarget keywords and channels. One firm improved inbound-to-SAL from 38% to 54% by optimising for ICP-fit keywords.

### AI-Assisted Inbound Qualification

When AI is deployed for inbound lead qualification (via Qualified, Agentforce, or custom agents), the lead scoring model needs to adapt:

**AI qualification adds two new dimensions to scoring:**

1. **Behavioural intent signals** — not just "downloaded a whitepaper" but "visited pricing page 3 times in 2 days, opened 4 emails, attended webinar, then hit the contact form." AI can score multi-touch behaviour patterns that humans miss.

2. **Real-time qualification** — AI can run SPICED-style qualification questions via chat before a human gets involved. The lead arrives at the rep pre-qualified with Situation, Pain, and Impact already captured.

**SaaStr result:** 71% of October 2025 closed-won deals came from AI-qualified inbound. Historic baseline was 29-34%. The AI didn't just qualify faster — it qualified BETTER by catching signals humans overlooked.

**Implementation pattern:**
- AI handles first response (speed-to-lead becomes instant)
- AI asks 3-5 qualification questions (mapped to SPICED or BANT)
- AI scores based on responses + behavioural data + firmographic fit
- T1 leads routed to rep immediately with AI-generated brief
- T2 leads entered into AI nurture sequence
- T3 leads deprioritised or recycled

**Lead segmentation for AI qualification** — segment by behaviour, not demographics:
- Website visitors (high-intent pages) → immediate AI engagement
- Content downloaders → educational nurture sequence
- Event registrants → event-specific follow-up sequence
- Returning visitors (previously cold) → re-engagement with context
- Free trial signups → onboarding + qualification hybrid

Source: SaaStr AI Agent Playbook, Part 14; SaaStr inbound case study

### Customer Interviews as a Marketing Data Source

Marketing operations teams typically rely on enrichment data and behavioral data to score and segment leads. But the highest-signal data source — structured customer interviews — is almost never fed back into the marketing data model.

**The gap:** Sales and CS talk to customers daily. That intelligence rarely flows back into lead scoring, segmentation, or campaign targeting. The result: marketing optimizes for proxy signals instead of the real buying criteria.

**The interview→marketing pipeline:**

| Interview Output | Marketing Use | How to Operationalize |
|-----------------|--------------|----------------------|
| **SPICED language** (verbatim words) | Ad copy, email subjects, landing page headlines | Store in SPICED library; feed to copywriting briefs |
| **Pain priorities** (ranked by frequency) | Lead scoring weight adjustment | If 80% of best customers mention pain X, increase score for leads showing pain X signals |
| **Decision criteria** (what actually mattered) | Nurture content strategy | Create content addressing real criteria, not assumed ones |
| **Channel attribution** (how they found you) | Budget allocation | Compare self-reported to system-attributed; adjust channel mix |
| **Objection patterns** (what almost stopped them) | Objection-handling content, FAQ pages | Create targeted content for top 3 objections |

**The math:** 10 customer interviews produce 40+ content assets AND validate/refine your lead scoring model. This is the highest-ROI activity in marketing operations.

**Process:**
1. CS or Sales conducts structured interviews (see `neon-icp` skill for the 8-step process)
2. Interview outputs are tagged and stored in the SPICED library
3. MarOps reviews quarterly: Which scoring criteria align with interview findings? Which don't?
4. Adjust scoring weights based on what real customers say, not what you assumed

See [[neon-icp-building-reference]] for the full customer interview methodology and GAP method.

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

### Speed-to-Lead SLA

Research consistently shows that response time is the single biggest lever in inbound conversion. After 5 minutes, contact rates drop by 10x.

```
TIER     RESPONSE SLA     ESCALATION
────     ────────────     ──────────
T1 MQL   < 5 minutes      If no response in 5 min → escalate to sales manager
                           If no response in 15 min → re-route to backup rep
T2 MQL   < 30 minutes     If no response in 30 min → escalate
                           If no response in 2 hours → re-route
T3 MQL   < 4 hours        If no response in 4 hours → auto-nurture sequence

MEASUREMENT:
  - Track: time from MQL creation to first rep outreach (call/email)
  - Target: median < 10 minutes for T1
  - Report: weekly, by rep and by lead source
  - Enforce: include in rep performance metrics
```

### Lead Routing Rules

```
RULE TYPE         LOGIC                                   IMPLEMENTATION
─────────         ─────                                   ──────────────
Geographic        Route by country/region/timezone         MAP workflow → CRM owner
Named Account     If account in named list → assigned rep  MAP lookup → CRM account owner
Round Robin       Equal distribution within territory      MAP rotation + weighted by capacity
Segment-Based     Route by ICP tier (T1 → senior rep)     MAP scoring → routing workflow
Product-Based     Route by product interest signal         MAP form field / page visit → workflow

CONFLICT RESOLUTION:
  Named Account always wins over Round Robin.
  If account has existing open opportunity → route to opp owner.
  If account has existing CSM → notify CSM + route to sales.
  If no match → round robin within territory.
```

### Lead Follow-Up Sequence

```
DAY 0 (within SLA):  Phone call attempt + personalised email
                     Reference: specific content consumed, company context
DAY 1:               Second phone attempt (different time of day)
DAY 2:               Email with relevant case study or resource
DAY 3:               Phone attempt #3 + LinkedIn connection request
DAY 5:               Email with value-add (not "just checking in")
DAY 7:               Final attempt email — "Should I close this out?"
DAY 10:              If no response → recycle to nurture. Set re-engagement trigger.

RULES:
  - Never send "just following up" emails. Every touch adds value.
  - Personalise first email based on lead source + content consumed.
  - Log all attempts in CRM. No dark pipeline.
  - If lead responds but isn't ready → set task for 30/60/90 day follow-up.
```

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

### ABM Reporting (When Running Allbound/ABM Motion)

```
ACCOUNT COVERAGE REPORTING:
  - % of target accounts with active engagement (content, ads, outreach)
  - Average touches per account per month (by channel)
  - Account penetration depth (contacts engaged per account)

ACCOUNT GENERATION REPORTING:
  - New accounts entering pipeline from ABM programmes
  - ABM-sourced vs ABM-influenced pipeline split
  - Time from ABM activation to first meeting (by tier)

PIPELINE GENERATION REPORTING:
  - ABM pipeline value vs direct inbound pipeline value
  - Conversion rates by ABM tier (T1 named vs T2 programmatic)
  - ABM deal velocity vs non-ABM deal velocity

ABM/INBOUND REVENUE REPORTING:
  - Closed revenue by motion (ABM, inbound, outbound, partner)
  - Blended CAC by motion
  - LTV by acquisition motion (do ABM customers retain better?)
```


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

### Inbound Flip Strategy (Canaani Model)

How to engineer an inbound-dominant GTM motion that produces 4x revenue per AE.

**The Flip Mechanics:**
1. Start with paid campaigns across LinkedIn, Google, and counterintuitive channels (Facebook/Instagram for B2B worked for Datarails)
2. Build organic engine in parallel: niche podcast, social content, brand presence
3. When inbound holds and outbound drops (as happened in 2022 downturn), lean into inbound
4. Brand as air cover: makes even cold outreach warmer

**Why Inbound Wins (Data):**
- HubSpot: inbound leads cost 61% less
- 6sense: 83% of the time, buyer initiates first contact
- Gartner: self-navigating buyers complete "high-quality deals" 65% vs 24% sales-led
- Signal quality > cost: buyers who come to you close better

**Channel Quality Ranking:**
Don't rank channels by volume or CAC alone. Rank by:
1. Win rate by channel
2. Cycle time by channel
3. AE productivity impact (does this channel require AE time to convert?)
4. Deal size by channel
The channel that produces highest win rate at shortest cycle time with least AE effort = concentrate budget there.

**Brand Protection as Architectural Choice (Canaani):**
- VP of Brand has no number — no MQL targets, no pipeline attribution
- "I want brand to do crazy fun stuff. I don't want them to think about MQLs."
- Protect the creative function from the metrics machine → long-term work that makes everything easier

### Outbound Channel Destruction Data (Donovan, E61)

For client conversations about channel mix:

| Metric | Then (5 years ago) | Now (2026) |
|--------|-------------------|------------|
| Touches per outbound opportunity | 200-400 | 1,000-1,400 |
| Primary outbound channel that still works | Phone + email | Phone (70% of outbound opps) |
| Email as cold outreach channel | Viable | Essentially destroyed |

**Implication for MarOps:** Shift budget allocation models to reflect the reality that outbound email is no longer a viable primary channel. Phone + high-quality content + brand are the surviving outbound motions.

## How to Use This Skill

**"Sales says our leads are garbage":** Run the diagnostic — check acceptance rate, rejection reasons, scoring calibration. Usually it's a scoring problem (wrong fit/engagement thresholds), not a lead volume problem.

**"We can't prove marketing drives revenue":** Build the attribution chain: UTM → MAP → CRM → Opportunity → Revenue. Start with W-shaped. Track both sourced and influenced pipeline.

**"Marketing and sales aren't aligned":** Write the SLA. Define terms together. Install the feedback loop. Most alignment problems are definition problems.

**"Which channels should we invest in?":** Run channel mix analysis. Compare ROI, pipeline contribution, and strategic goals. Don't chase high-ROI niche channels — you need portfolio balance.

**"How do we make lead scoring more accurate?":** Move beyond generic firmographic scoring. Implement the SPICED ICP Fit Matrix: Selection Fit (is this our ICP?) × Urgency Fit (are they ready now?) = Qualification Tier (T1/T2/T3). Calibrate quarterly using customer interview data and win/loss analysis.

## End-to-End Inbound Process

Lead scoring and attribution answer "how good is this lead?" and "where did it come from?" But they only work if the inbound process is well-designed. This section covers the operational model from first touch to qualified opportunity.

### Customer Journey Map (Prerequisite)

Before designing lead qualification rules, map the customer journey. This prevents scoring leads based on what you wish they did instead of what they actually do.

**Minimum journey map elements:**
- Awareness touchpoints (organic search, paid, content, events, social)
- Education touchpoints (blog, case studies, comparison pages, webinars)
- Selection touchpoints (pricing page, demo request, free trial, contact form)
- Each touchpoint mapped to: buyer intent signal, qualification relevance, hand-raise likelihood

Use this map to weight lead scoring attributes. High-intent touchpoints (pricing page, demo request) should drive qualification tier regardless of firmographic fit.

### Speed-to-Lead SLAs

Response speed is the single highest-leverage lever for inbound conversion. Research consistently shows conversion drops sharply after 5 minutes for high-intent leads.

```
LEAD TYPE                   TARGET RESPONSE SLA     CHANNEL
──────────                  ───────────────────     ───────
T1 (High Fit + High Intent)  < 5 minutes            Phone + email
T2 (High Fit + Medium Intent) < 1 hour              Email sequence + phone attempt
T3 (Medium Fit)              < 4 hours              Email sequence
Nurture (Low Fit or Intent)  < 24 hours             Automated nurture sequence only
```

SLA performance should be reported weekly. If T1 SLA miss rate > 10%, escalate immediately — this is a revenue leak, not a process problem.

### Lead Routing Process

Routing rules determine which leads go where. Without defined rules, leads route by accident (whoever picks up first, whoever is online, whoever is the default owner).

**Routing logic hierarchy:**
1. **Geography/territory** — route by region or country first
2. **Account ownership** — if the lead's company has an existing CRM owner, route to that owner
3. **Segment/tier** — route T1 leads to senior reps; T3 leads to SDRs or nurture
4. **Round-robin** — within a qualified pool, distribute evenly to prevent cherry-picking
5. **Capacity cap** — prevent routing to reps above their daily/weekly lead cap

Document routing rules in CRM as explicit automation — not as "the team knows." For operational depth on routing design, see [[lead-routing]].

### Lead Follow-Up Sequence (Inbound Cadence)

Inbound leads are not self-converting. Even high-intent demo requests require structured follow-up.

```
T1 LEAD FOLLOW-UP (High Fit + High Intent)
Day 0:   Phone call (within 5 min) + confirmation email
Day 1:   Follow-up email with case study or relevant social proof
Day 3:   Phone attempt + personalised value email (reference their use case)
Day 5:   "Break-up" email — sets expectation this is final attempt
Day 7:   Move to nurture if no response

T2 LEAD FOLLOW-UP
Day 0:   Confirmation email + 4-hour phone attempt
Day 2:   Follow-up email
Day 5:   Final follow-up
Day 7:   Move to nurture
```

Cadence length and steps should be calibrated against your industry and ACV. High-ACV B2B sales with longer cycles tolerate longer cadences.

### Inbound Conversion Metrics by Stage

Track the full inbound funnel, not just MQL volume.

```
STAGE                   METRIC                          BENCHMARK (B2B SaaS €1M-50M ARR)
─────                   ──────                          ──────────────────────────────────
Lead → MQL              Lead-to-MQL rate                20-40% (depends on channel mix)
MQL → SAL               MQL acceptance rate             60-80% (if scoring is calibrated)
SAL → SQL               SAL-to-SQL rate                 40-60%
SQL → Opportunity       SQL-to-Opp rate                 70-85%
Opportunity → Closed    Win rate (inbound)              25-40% (typically 1.5-2x outbound)
```

Diagnose conversion gaps by stage, not just by volume. A low SAL acceptance rate means scoring is miscalibrated or ICP isn't agreed. A low SQL-to-Opp rate means SDRs are advancing poorly qualified leads.

### ABM Account-Level Inbound Reporting

For accounts in your ABM programme, supplement lead-level reporting with account-level coverage and pipeline metrics.

**Key ABM inbound metrics:**
- **Coverage:** % of target accounts with at least one identified contact (by tier)
- **Engagement:** % of target accounts with activity in last 30/60/90 days
- **Account-level MQL:** at least one T1/T2 lead from a target account in active research
- **Pipeline by ABM tier:** Tier 1 accounts should generate disproportionate pipeline relative to their count

Report ABM inbound at the account level in the monthly Marketing review. Individual lead metrics miss the signal when multiple contacts from one account engage across different channels.

For full pipeline reporting architecture, see [[pipeline-visibility]].

---

## Canon References

- **[[neon-spiced-icp-library-v1]]** — SPICED language library with ICP Fit Matrix framework and qualification tiers (T1/T2/T3)
- **[[neon-icp-building-reference]]** — Full ICP building methodology including customer interview pipeline
- **[[neon-common-pitfalls-by-capability]]** — Common pitfalls including gut-feel ICP that produces inaccurate lead scoring

> Built by [Neon Triforce](https://neontriforce.com)
