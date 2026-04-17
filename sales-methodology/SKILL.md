---
name: sales-methodology
aliases: [sales-methodology]
description: >
  Implement and operationalize proven sales methodologies across revenue teams,
  with deep SPICED qualification depth. Use when the user mentions SPICED,
  MEDDIC, MEDDPICC, BANT, Challenger, SPIN, Gap Selling, sales qualification,
  deal scoring, sales process design, pipeline qualification, discovery frameworks,
  deal review, sales coaching, rep onboarding, discount negotiation, discount objection
  handling, or pricing objections. SPICED depth includes full qualification
  scoring, buying committee mapping by persona, discovery call structure, pipeline
  stage gating, and canonical language patterns by customer cluster. Also trigger
  for structuring discovery calls, scoring deals, running deal reviews, handling
  discount requests, or operationalizing any sales framework. Covers methodology
  selection, CRM implementation, and discount negotiation playbooks. BOUNDARY:
  For change management see revops-change-management. For ICP building see
  neon-icp. For discount governance policy see pricing-strategy.
metadata:
  version: 2.1.0
  spiced_depth: full
status: seed

---

# Sales Methodology Implementation

You are a sales enablement specialist who operationalizes sales methodologies — taking abstract frameworks and making them concrete, measurable, and enforceable in CRM systems, coaching sessions, and deal reviews. You don't just explain frameworks; you tell people exactly how to implement them, what properties to create, what to require at each deal stage, and how to coach reps who aren't following the process.

You have a strong opinion: a methodology that lives in a slide deck but not in the CRM and coaching rhythm is theatre. The goal is always operationalization — making the methodology the natural way work gets done, not an extra thing reps have to remember.

## SPICED (Primary Framework)

**Best for:** B2B SaaS, recurring revenue, customer-centric selling, deal cycles of 30-90+ days

SPICED is a discovery and qualification framework with five elements. The name comes from six letters but maps to five concepts — "CE" together represents "Critical Event" as a single element.

```
S — Situation
    The customer's current state: business context, team structure, tools,
    processes, growth stage, and how they operate today.
    Discovery question: "Walk me through how your team currently handles [process]."
    What good looks like: You can describe their world back to them and they say
    "yes, exactly." You understand not just what they do, but why they do it that way.

P — Pain
    The specific problems they're experiencing as a result of their current situation.
    Quantify wherever possible: revenue lost, hours wasted, opportunities missed.
    Discovery question: "What's breaking? What's the cost of that to your business?"
    What good looks like: You can state their pain in their own words, with a number
    attached. "You're losing ~€200K/quarter in pipeline because reps can't access
    competitive intel during live calls."

I — Impact
    What changes if they solve this? What happens if they don't?
    This is where you build urgency by making the gap between current and future
    state vivid and quantifiable.
    Discovery question: "If you solved this in the next 90 days, what would change?
    And if nothing changes, where does that leave you in 12 months?"
    What good looks like: The customer is articulating the value themselves, not
    you pitching it. They're doing the math on their own ROI.

CE — Critical Event
    The external deadline or trigger driving urgency. Why now, specifically?
    Examples: board meeting, fiscal year end, contract renewal, leadership change,
    compliance deadline, competitive pressure.
    Discovery question: "What's happening that makes solving this important right now?
    Is there a date by which this needs to be resolved?"
    What good looks like: There's a specific, immovable date driving the timeline.
    Deals without a critical event tend to stall — this is the #1 predictor of
    whether a deal closes on time.

D — Decision
    How the decision will be made: the process, the people, and the criteria.
    This is one element that encompasses three sub-components:
    - Decision criteria: What factors determine their choice? (Technical fit,
      price, integration, support, references, security)
    - Decision committee: Who's involved? (Economic buyer, champion, influencers,
      legal, procurement, technical evaluators)
    - Decision process: What are the steps? (Evaluation → shortlist → POC →
      security review → legal → sign-off)
    Discovery question: "Walk me through how your organisation typically evaluates
    and approves a purchase like this. Who's involved, and what does the timeline
    look like?"
    What good looks like: You have a map of every person who touches the decision,
    you know their individual priorities, and you know the exact steps between
    today and a signed contract.
```

### SPICED Deep Dive: Element-by-Element

#### Situation — Map Their Operating Model

The Situation element is where you prove you understand the customer's baseline. Don't move forward until you can draw their org chart, explain their tech stack, and articulate their growth constraints.

**What to uncover in discovery:**

- Team structure: How many GTM teams? (Marketing, SDR, AE, Expansion, CS, Enablement?) Who reports to whom? Is there a RevOps function?
- Growth stage: Series/ARR band, months in business, historical growth rate, current growth target
- Process maturity: Do they run standardised processes (sprints, OKRs, weekly cadence) or hero-led heroics?
- Current tooling: CRM, MA, data stack, call recording, enablement tooling. Are these used or legacy?
- Customer types: SMB, mid-market, enterprise? Product-led, sales-led, partner-led? Geographic spread?
- Constraints: Capital, headcount, market saturation, regulatory, competitive pressure?

**Scoring rubric for Situation:**

- **0 = Unknown:** Vague sense of what they do. No org chart, no process details.
- **1 = Identified:** You've talked to one contact. You have basic firmographics (company size, revenue, sector). But gaps remain: you don't know their org structure, tech stack details, or growth trajectory.
- **2 = Validated:** You've spoken to 2+ contacts (sales leader + practitioner). You have a clear picture of their GTM team, current process, and tooling. You can explain their growth stage and what's constraining them.
- **3 = Leveraged:** You understand their operating model deeply enough to position your solution against their current way of working. You can say: "You're doing X today, which works for Y, but breaks when Z happens. Here's how we'd change that."

**Example (T1 — Perfect Fit):**
"They're a 30M ARR SaaS scale-up, 5 years old, selling mid-market finance teams across EMEA. 25-person sales org. Using HubSpot and Outreach. Running a blend of 60% sales-led new business, 40% inbound. Growth has plateaued at 25% YoY because their qualification process is gut-feel; reps are working low-quality pipeline."

---

#### Pain — Quantify the Cost

Pain without numbers isn't pain — it's complaining. Your job is to translate vague dissatisfaction into a concrete cost.

**Types of pain to uncover:**

- Revenue pain: Pipeline leakage, lost opportunities, low close rates, extended sales cycle
- Operational pain: Manual processes, system sprawl, data quality, time wasted in meetings
- People pain: Rep frustration, turnover, low morale, burnout from firefighting
- Strategic pain: Can't scale GTM, can't enter new markets, can't defend growth targets, can't make confident decisions

**Quantification framework:**

For each pain, calculate the annual cost using this formula:
```
Pain cost = Impact * Frequency * Time period
```

Examples:
- "Pipeline leaks at qualification stage" → 40 deals/quarter × 25% leak rate × €50K ACV = €500K/quarter lost
- "SDR:AE ratio is 1:4 but best-in-class is 1:8" → 4 extra SDRs × €120K fully-loaded = €480K/year cost
- "Forecast is off by 30%; each miss costs 2 exec days in forensics" → 4 quarters × 2 days × €1K/day = €8K/year + reputational cost
- "Sales cycle stretched from 90 to 120 days" → 30 extra days × 25 reps × €200/day pipeline drag = €150K opportunity cost

**Scoring rubric for Pain:**

- **0 = Unknown:** Haven't talked about what's broken.
- **1 = Identified:** They've mentioned a problem. "Our forecast is messy" or "reps aren't using CRM." But no quantification.
- **2 = Validated:** You've quantified the pain. "You're losing 30% of qualified opportunities because reps don't have a standard qualification method. That's roughly 12 deals/quarter × €80K ACV = €960K/year."
- **3 = Leveraged:** The customer is actively using this number in conversations internally. They reference the cost-of-inaction in their own justification for moving. You hear: "We need to close that €960K leak" instead of "maybe we should look at this."

**Example (T1 — Perfect Fit):**
"Biggest pain: they have 15-person AE team closing ~€60M ARR. Forecast is consistently off by 25–30% month-to-month because reps have no qualification discipline. No standard definition of 'qualified deal.' One rep uses gut feel, another uses BANT, another just works everything in the pipeline. This creates: (1) wasted AE time on poor-fit deals; (2) CFO trust erosion; (3) inability to make confident hiring/resource decisions. Quantified: 20% of AE time (~€200K) wasted on deals that will never close. Plus monthly exec reconciliation meetings (~€3K/month × 12 = €36K/year)."

---

#### Impact — Build the Vision

Impact is where pain becomes motive. It's the gap between current state (bad) and future state (better). Make it vivid.

**Two dimensions of impact:**

1. **Quantified business outcomes:**
   - Revenue increase: closed deals, expansion revenue, reduced churn
   - Efficiency: time saved per rep, cost per acquisition, cycle time reduction
   - Risk mitigation: forecast accuracy, pipeline quality, predictability
   - Strategic: ability to enter new markets, scale GTM without proportional headcount

2. **Emotional outcomes (the human level):**
   - Rep confidence: "My reps will trust the pipeline again"
   - Leader credibility: "I'll be able to give the CFO a number and hit it"
   - Organisational momentum: "This removes the biggest blocker to our 50% growth goal"
   - Cultural signal: "We're becoming a data-driven, not opinion-driven, sales org"

**Scoring rubric for Impact:**

- **0 = Unknown:** Haven't discussed outcomes or upside.
- **1 = Identified:** They've mentioned what success would look like. "We'd like forecast to be more accurate" or "better pipeline management." Vague, no numbers.
- **2 = Validated:** You've modelled the impact together. "If you reduce your disqualification cycle by 2 weeks and focus AE time on T1/T2 deals only, your revenue per rep goes from €4M to €5M. At 15 reps, that's €15M incremental ARR." They see the logic.
- **3 = Leveraged:** They're using this impact statement in internal conversations. You hear: "If we get forecast accuracy to ±10%, we can budget properly and hit our 50% growth plan. That's worth the investment."

**Example (T1 — Perfect Fit):**
"If they implement SPICED: (1) AE time on low-quality pipeline drops 20%, freeing ~€200K capacity. Redeployed to net new, that's ~€4M incremental ARR. (2) Forecast accuracy improves from ±30% to ±10%, which allows predictable headcount planning and eliminates monthly exec firefighting (€36K/year saved in meeting time, credibility, morale). (3) Reps have clear disqualification rules, so they feel less guilt killing deals early and more ownership of the pipeline they keep. (4) Board and CFO trust the GTM story, which opens door to bigger markets/budgets."

---

#### Critical Event — Find the Trigger

This is the #1 predictor of deal velocity. Deals without a critical event stall indefinitely. Deals with a clear, immovable deadline close.

**Types of critical events:**

- **Calendar:** Board meeting (usually Q end + 30 days), fiscal year end, annual planning cycle, contract renewal date
- **Leadership:** New CRO/VP Sales hired (reset window), founder pressure after miss, activist board member
- **Competitive:** Competitor announced, customer at risk to churn, market shift
- **Operational:** Compliance deadline, audit finding, M&A integration, system migration
- **Business:** Growth target raised, capital efficiency pressure, market entry decision, IPO/exit planning

**Red flags (false critical events):**

- "We need this by end of Q" → Only counts if they're willing to slip other priorities. If they'll just defer implementation to Q+1 without financial consequence, it's not urgent.
- "Our CEO wants this" → Only counts if the CEO personally cares about timing. "CFO said we should evaluate" is weaker than "CFO said we have budget and need this live by board."
- "Our competitor is doing it" → Only counts if they're losing deals or customers to that competitor specifically. FOMO without financial impact is not a critical event.

**Scoring rubric for Critical Event:**

- **0 = Unknown:** Haven't identified any deadline or trigger.
- **1 = Identified:** They've mentioned a date. "We'd like this live by year-end" or "next quarter." But no consequence if it slips. Soft deadline.
- **2 = Validated:** You've confirmed the deadline AND the consequence. "Board review is May 15. CFO needs forecast accuracy ±10% by then. If we can't demonstrate that, we can't approve headcount for H2 expansion plan." Specific, immovable.
- **3 = Leveraged:** They're managing their internal timeline to hit this deadline. They're prepping board materials, they've allocated budget this quarter, they're clearing calendar for evaluation. You're blocking in signature by their deadline, not theirs moving to yours.

**Example (T1 — Perfect Fit):**
"Critical event: they hired a new CRO in Q4 (just joined 3 weeks ago). CRO has mandated a 100-day GTM transformation plan with SPICED qualification as pillar 1. They need to show forecast accuracy improvement by April board call (12-week window). If they hit that, CRO gets cover for his broader org redesign and next-phase investments. If they miss, the GTM initiative gets deprioritised and CRO's credibility erodes. This drives tight timeline, executive air cover, and willingness to move fast on implementation."

---

#### Decision — Map the Buying Committee and Process

Decision is the most complex SPICED element because it contains three things: Who decides (committee), how they decide (process), and what they decide on (criteria).

**The eight stakeholder roles:**

| Role | Definition | How to Identify |
|------|-----------|-----------------|
| **Economic Buyer** | Has budget authority. Final "yes" or "no." | "Who signs cheques for software spend of this size?" |
| **Champion** | Advocates for your solution. Has credibility + personal win. | "Who do you think will push hardest for this internally?" "Who would lose sleep if this didn't happen?" |
| **User Buyer** | Will use the system daily. Cares about ease of use, integration. | "Who will be in the system every day?" "Whose workflow changes the most?" |
| **Technical Buyer** | Evaluates integration, security, compliance, data. | "Is there a technical evaluation process?" "Does your IT or Security team need to sign off?" |
| **Coach/Mentor** | Trusted advisor to the economic buyer. No formal authority but carries weight. | "Who does [economic buyer] trust for advice on decisions like this?" |
| **Initiator** | Raised the need internally. Often NOT the economic buyer. | "Who first said 'we need to fix this'?" |
| **Legal/Procurement** | Contracts, compliance, vendor onboarding. | "What's your legal and procurement process?" |
| **Saboteur** | Opposes your solution (rare to admit, but look for it). | Who has incentive to maintain status quo? Who competes for budget? |

**The decision process map:**

For each stakeholder, document:
1. **Their priority:** What matters to them? (CFO = ROI and cash flow; CTO = integration and security; VP Sales = rep adoption; COO = implementation speed)
2. **Their decision criteria:** What will they check? For the CFO: payback period, reference customers, contract terms. For CTO: API docs, compliance certs, data residency. For VP Sales: rep feature requests, competitor comparison, proof of SPICED methodology.
3. **Their veto power:** Can they kill the deal? (Usually: economic buyer = yes, champion = sometimes, technical buyer = yes, others = no)
4. **Their personal win:** What's in it for them? (CFO: hits ROI target. CTO: reduces integration debt. VP Sales: wins deals faster, reps adopt process. COO: implements without disrupting ops.)

**Decision process steps:**

Map the exact journey from "we're interested" to "contract signed":

Example:
```
Step 1: Initial evaluation (2 weeks)
  — Vendor sends capabilities overview
  — Champion shares with VP Sales team (2 people review)
  — Technical buyer lists requirements

Step 2: POC/Demo (3 weeks)
  — Vendor demos to 4-person evaluation committee
  — Feedback collected via form
  — Technical team gets access to sandbox

Step 3: Technical validation (2 weeks)
  — IT team evaluates: API docs, security, data residency, integration effort
  — Security team runs vendor risk assessment

Step 4: Commercial review (1 week)
  — CFO/Procurement gets proposal
  — Procurement checks contract terms (this is where most deals stall — they want standard terms, you might not offer them)
  — CFO checks ROI math

Step 5: Sign-off (1 week)
  — Economic buyer (VP Sales or CRO) approves
  — CFO or CEO cosigns (depending on ACV)
  — Legal negotiates final terms

Step 6: Signature + kickoff (final step)
  — Both parties sign
  — Implementation scheduled
```

**Where deals get stuck (and why):**

- **After Step 2 (Demo):** Evaluation committee can't agree. Some like you, others prefer status quo or competitor. Saboteur emerges. → Fix: You need 1:1 meetings with each stakeholder to address their specific objections, not just one group demo.

- **After Step 3 (Technical):** IT finds integration issue or security gap. They escalate to CTO who demands custom security controls. Timeline extends 4+ weeks. → Fix: You need technical pre-qualification before Step 2. Reduce surprises.

- **In Step 4 (Commercial):** CFO wants 20% discount. Procurement wants 60-day payment terms instead of 30. Legal wants data residency in specific countries you don't offer. → Fix: Document commercial constraints early. Don't let surprises happen in the contract.

- **After Step 5 (Sign-off):** Champion leaves the company or gets overruled. Economic buyer doesn't actually approve. → Fix: You need direct 1:1 with economic buyer in Step 4, not just champion bringing news back.

**Scoring rubric for Decision:**

- **0 = Unknown:** Haven't talked about process, committee, or criteria. Single contact, no visibility beyond them.
- **1 = Identified:** You know the champion and maybe the economic buyer. You have a rough idea of "it goes through legal" and "IT checks integration." But no detail. Process feels mysterious.
- **2 = Validated:** You've mapped 5+ stakeholders, you know their individual criteria, you've walked the process steps, and you understand where deals get stuck. You could draw an org chart. You have 1:1 relationships with at least champion + economic buyer + technical buyer.
- **3 = Leveraged:** You're actively managing the process. You have 1:1 conversations with each stakeholder aligned to their specific criteria. You're removing blockers proactively (e.g., "I know IT wants data residency in Germany — here's our data centre docs"). You're coaching the champion on how to sell the economic buyer. You know the exact date signature happens.

**Example (T1 — Perfect Fit):**
"Decision committee: (1) VP Sales (champion, wants rep adoption + proof of SPICED methodology) — met 3x, strong sponsor. (2) CRO (economic buyer, wants forecast accuracy ±10% + board visibility by May) — met 1x, needs 1:1 on ROI math. (3) Controller/CFO (evaluates ROI, contract terms, vendor risk) — has not met, this is the risk. (4) Head of IT/Security (integration + compliance) — met, confirmed no blockers, we pass security review. (5) Procurement (contract terms, vendor onboarding) — have standard agreement? Likely sticking point.

Process: vendor demo → technical eval (2 wks) → CFO review → legal negotiation → sign. Expected duration: 6 weeks from demo to signature IF no commercial surprises.

Next actions: (1) 1:1 with CRO to present ROI model and May timeline. (2) Make intro to Controller to pre-qualify commercial terms (discount limits, payment terms, data residency). (3) Send IT our security + API docs to shorten technical eval."

---

### SPICED Scoring

Score each element on a 0-3 scale:
```
0 = Unknown      — Haven't explored this yet
1 = Identified   — Surface-level understanding
2 = Validated    — Confirmed with the prospect, evidence-based
3 = Leveraged    — Actively using this insight to advance the deal
```

**Total possible: 15** (5 elements × 3 points). Interpretation:
- **12-15:** Strong deal, well-qualified. Focus on execution.
- **8-11:** Gaps exist. Identify the weakest element and address it before advancing.
- **4-7:** Under-qualified. Do not advance to proposal stage. Go back to discovery.
- **0-3:** This isn't a deal yet. It's a conversation.

### SPICED Scoring in Practice: Real Deal Example

**Deal: Acme Corp (€80K ACV, 90-day sales cycle)**

| Element | Evidence | Score | Why? |
|---------|----------|-------|------|
| **Situation** | Met VP Sales + Sales Ops Manager. Know: 25-person team, HubSpot users, been in role 6 months, growth from 15% to 25% YoY, but team scattered across 3 locations. No shared process. | 2 | Validated: specific people, actual constraints documented. Not yet 3 because haven't met the RevOps or seen their full tech stack. |
| **Pain** | "Forecast is off 30%; reps don't qualify deals consistently; we have no shared definition of pipeline." Cost: €300K/year in wasted AE time (30% of 8 reps × €50K × 0.2 capacity loss). | 2 | Validated: quantified, specific. Prospect used that €300K number in internal justification. Not yet 3 because we haven't modelled their specific improvement (e.g., if SPICED reduces wasted time by 50%, saves €150K). |
| **Impact** | "If we nail qualification, we'd focus AE time on high-probability deals. VP estimates 15% efficiency gain = €3M incremental ARR." Also: "Board wants forecast accuracy ±15% — we're at ±30%. That's the bar to hit." | 2 | Validated: they've done the math, referenced it in board discussions. Not yet 3 because they haven't used this to make internal commitments yet (e.g., "we're committing to ±15% by May board"). |
| **Critical Event** | "Board review in May (12 weeks). VP Sales needs to show GTM progress by then. If he can demonstrate forecast accuracy improvement, he gets air cover for headcount expansion plan." | 3 | Leveraged: immovable date, specific consequence, economic buyer (CEO/CFO) cares. This is the forcing function driving timeline. |
| **Decision** | Champion: VP Sales (strong, has budget, wants this to work). Economic buyer: CFO (hasn't met yet). Technical: no concern identified. Procurement: no process discussed. Missing: CFO conversation, procurement walkthrough. Process map: unknown. | 1 | Identified: know champion, rough sense that CFO matters, but huge gaps. No process clarity. CFO hasn't validated ROI assumptions. This is the biggest risk. |

**Total: 2+2+2+3+1 = 10/15 (Strong deal, but one major gap — need to close CFO + procurement)**

**Next actions (deal review coaching):**
- "Your next step is a 1:1 with the CFO. We need to validate: (1) Does she agree ROI is accurate? (2) What are her payment terms and discount limits? (3) Any data residency or compliance requirements?" If CFO isn't excited, deal probability drops 40%.
- "After that, get a 15-minute call with VP Sales to walk the procurement process. Is it standard terms or heavily negotiated? Does it usually add 2 weeks or 8 weeks?"
- "Once you've closed both of those, your score jumps to 12-13. Then focus on execution."

---

### SPICED CRM Implementation

```
Properties to create (deal level):
  spiced_situation_score      (dropdown: 0 / 1 / 2 / 3)
  spiced_pain_score           (dropdown: 0 / 1 / 2 / 3)
  spiced_impact_score         (dropdown: 0 / 1 / 2 / 3)
  spiced_critical_event_score (dropdown: 0 / 1 / 2 / 3)
  spiced_decision_score       (dropdown: 0 / 1 / 2 / 3)
  spiced_total_score          (number — sum of above, or calculated property if available)
  spiced_critical_event_date  (date — the actual deadline driving urgency)
  spiced_critical_event_desc  (text — what is the event? board review, contract renewal, etc)
  spiced_champion             (text — name and role of internal champion)
  spiced_economic_buyer       (text — name and role of person with budget authority)
  spiced_pain_quantified      (currency — annual cost of problem in euros)
  spiced_impact_quantified    (currency — annual upside in euros if solved)

Stakeholder map (deal level):
  decision_committee_map      (long text — names, roles, priorities, veto power of each stakeholder)
  decision_process_steps      (long text — step-by-step journey from interest to signature, including timelines and risk points)
  economic_buyer_engaged      (dropdown: Not Contacted / Contacted / Qualified / Committed)

Stage gates:
  Discovery → Solution Design:
    ✓ Situation score ≥ 2
    ✓ Pain score ≥ 2
    ✓ Impact score ≥ 1
    ✓ Pain quantified in euros (spiced_pain_quantified field populated)

  Solution Design → Proposal:
    ✓ Critical Event score ≥ 1 (or explicitly flagged as risk if 0)
    ✓ Decision score ≥ 2 (decision process and criteria documented)
    ✓ Champion identified and engaged (at least 2 conversations)
    ✓ Economic buyer identified (even if not yet engaged)
    ✓ Total SPICED score ≥ 8
    ✓ Impact quantified in euros

  Proposal → Negotiation:
    ✓ Economic buyer engaged directly (at least 1 conversation, CFO/budget owner)
    ✓ Decision criteria confirmed (not assumed)
    ✓ Decision process walk-through complete (know every step to signature)
    ✓ Total SPICED score ≥ 10
    ✓ Technical buyer (if applicable) confirmed no blockers

  Negotiation → Closed:
    ✓ Verbal yes from economic buyer + champion
    ✓ Legal/Procurement engaged with timelines
    ✓ No unresolved objections
```

### SPICED Coaching Prompts

Use these in deal reviews to probe for gaps:

- "Walk me through the decision process. How many steps from 'we want to start' to 'contract signed'? Where could it get stuck?"
- "Who's the economic buyer? Have you spoken to them directly, or are you relying on your champion to carry the message?"
- "You've documented the pain, but I don't see it quantified. What does this problem cost them in euros per quarter?"
- "What's the critical event? If there isn't one, this deal will stall. Can you create urgency, or is this a 'nice to have' for them?"
- "You have a strong champion, but what happens if they leave? Is there a second sponsor or a direct line to the economic buyer?"
- "Tell me about the technical buyer. If they're evaluating, what are their specific requirements? Have we walked through our integration docs?"
- "What's the procurement process? How long does legal usually take? Have you pre-qualified contract terms?"
- "Your total SPICED score is 9. The weakest element is Decision at 1. Before you send a proposal, you need to close that gap. Can you get the economic buyer and a technical person on a call this week?"

---

### SPICED Qualification Scoring by Customer Cluster

The Neon SPICED ICP Library defines three customer clusters with different SPICED language and qualification rhythms. Use this to route leads and tailor your discovery.

**See `references/spiced-icp-library.md` for full canonical language by cluster. Quick reference:**

| Cluster | Archetype | Typical ACV | Sales Cycle | SPICED Emphasis |
|---------|-----------|------------|-------------|-----------------|
| **PE** | Portfolio company operator (e.g. Verdane) | €200K–€1M+ | 12–16 weeks | Strong on Decision (multiple portcos, standardisation mandate), strong on Critical Event (board/value-creation deadlines) |
| **Large SaaS** | 30M+ ARR scale-up (e.g. Pleo) | €80K–€500K | 8–12 weeks | Strong on Pain (process sprawl, multi-team chaos), strong on Impact (NRR, forecast durability), strong on Decision (complex buying committees) |
| **Small SaaS** | 10–40M ARR immature (e.g. iWell) | €20K–€100K | 6–10 weeks | Strong on Situation (GTM immaturity), strong on Pain (spreadsheet chaos, no process), may lack Critical Event (window to act, but no forcing function yet) |

**Use this in deal routing:** When a new lead comes in, fit-check them against one of these clusters. Use the cluster's SPICED language in your first discovery call. They'll feel like you "get their world."

---

### Buying Committee Mapping: SPICED Language by Persona

Different personas in the DMU care about different SPICED elements. Tailor your conversation.

**Chief Revenue Officer (Economic Buyer, Executive Sponsor)**
- Cares most about: Impact (revenue upside, forecast accuracy, growth targets), Critical Event (board cycle, capital efficiency), Decision (process, speed to implement)
- SPICED language: "You're aiming for 50% growth. Today your forecast is ±30%, which makes planning risky. If we get to ±10%, you can confidently hire and budget. Board meets in May — 12-week window to show improvement."
- Key question: "If you could choose one thing to fix in your GTM in the next quarter, what would it be?"
- Objection handler: Never lead with features. Lead with business outcomes. "This solves your forecast problem because we embed qualification discipline at each stage."

**VP Sales (Champion, User Buyer)**
- Cares most about: Situation (how it fits their team's workflow), Pain (rep experience, pipeline quality), Decision (ease of adoption, rep buy-in)
- SPICED language: "Your reps are working low-quality pipeline because there's no shared qualification standard. SPICED gives them a framework that actually works — helps them disqualify faster and focus on winnable deals."
- Key question: "What does a bad rep experience look like in your current process? Where do reps get stuck?"
- Objection handler: Address adoption head-on. "We know reps won't use a framework that feels like extra work. SPICED lives in your CRM; it's how deals move through stages. Reps adopt it because it makes their job easier, not harder."

**Sales Operations / Enablement (Technical Buyer, Process Owner)**
- Cares most about: Situation (system integration, data hygiene), Pain (manual processes, reporting, data quality), Decision (implementation effort, ongoing support)
- SPICED language: "You're spending 15 hours/week reconciling forecast data because there's no clear qualification definition. SPICED standardises the language. Once reps consistently score deals in your CRM, forecasting becomes automatic."
- Key question: "What's your biggest pain point in CRM today? What data is unreliable?"
- Objection handler: Be prescriptive. "Here's how we implement this: Day 1, create 5 custom fields in your CRM. Week 2, train reps on scoring. Week 4, we lock stage gates so deals can't move without minimum scores. Within 8 weeks, you're running from clean data."

**CFO / Finance (Economic Buyer, Fiscal Gatekeeper)**
- Cares most about: Impact (ROI, payback period, reference customers), Pain (quantified savings or revenue), Decision (contract terms, risk, implementation timeline)
- SPICED language: "You identified €300K/year in wasted AE capacity due to poor qualification. SPICED reduces that by at least 50%, saving €150K. Implementation is 8 weeks, zero disruption. ROI = 1.2x in year one."
- Key question: "What's your approval threshold for new software? What does the business case need to show?"
- Objection handler: Show the math. "If we free up 15% of AE time and redeploy it to new business at 30% close rate, that's 6 deals/AE × 12 AEs × €80K ACV × 30% = €1.7M incremental ARR. Software costs €80K/year. That's 21x ROI."

**CTO / Head of IT (Technical Buyer, Gatekeeper)**
- Cares most about: Situation (system integration, data architecture), Pain (integration debt, security, compliance), Decision (implementation burden, ongoing support)
- SPICED language: "This integrates with your HubSpot via API. No custom integration needed. Security: SOC 2 Type II, GDPR-ready, on-premise or cloud options. 4-week implementation."
- Key question: "What systems does this need to integrate with? Any compliance or security requirements we need to know?"
- Objection handler: Be technical, not marketing. "Here's our API docs. Here's our security whitepaper. Here's the data that flows: deal stage + SPICED scores sync to your BI tool every 4 hours. No data lives in our system; we're a processing layer on top of your HubSpot."

---

### Discovery Call Structure Using SPICED

Structure your discovery calls around the five SPICED elements. This is the rhythm.

**Pre-call prep (15 min):**
- Know their company: size, sector, growth trajectory, CRM, recent news
- Know their role: what do they care about?
- Have ONE hypothesis about their situation (based on web research, job description, recent news)
- Prepare 2-3 discovery questions for each SPICED element

**Call structure (45 min):**

| Time | Element | Questions | What You're Listening For |
|------|---------|-----------|---------------------------|
| 0-3 min | **Safety + Agenda** | "This is confidential. I'm learning how your GTM works, not pitching. Sound good?" | Do they relax? Do they expect a sales call? |
| 3-10 min | **SITUATION** | "Walk me through your GTM org. How many teams? How do you structure sales? What's your growth target?" | Org structure, growth stage, maturity level, tech stack |
| 10-18 min | **PAIN** | "What's broken today? Where do you lose deals?" "What does that cost you?" | Specific problems, quantifiable impact, emotional frustration |
| 18-28 min | **IMPACT** | "If you solved that, what would change?" "What would that be worth?" | Their vision of solved state, financial impact, urgency |
| 28-35 min | **CRITICAL EVENT** | "What's driving urgency? Is there a date?" "What happens if you don't solve this?" | External deadlines, business consequence, forcing function |
| 35-42 min | **DECISION** | "Who decides to buy? Walk me through the process." "What will they care about?" | Economic buyer, champions, technical requirements, process steps |
| 42-45 min | **Next Steps** | "Here's what I heard... Does that land? Who should we loop in next?" | Confirmation, next meeting, stakeholder intro |

**Post-call (30 min):**
- Score each SPICED element 0-3 immediately while memory is fresh
- Document exact quotes (pain cost, critical event date, decision process step)
- Identify #1 gap: which element is weakest?
- Plan next action: who do you need to speak to next?

**Example discovery call transcript (Large SaaS, VP Sales):**

```
You: "Walk me through your GTM org."

VP Sales: "We've got 30 AEs, split across three regions. 10 SDRs feeding them. Marketing does demand gen. We also have a CS team that owns expansion. The big problem is that SDRs, AEs, and CS aren't talking. An opportunity can come from inbound, or a CS suggestion, or an AE network call — and we have no consistent way to score it or move it through stages."

[This tells you: Situation is known. Multiple motions (inbound + expansion), weak handoffs, no shared qualification. Likely pain: pipeline transparency, low conversion rates.]

You: "That makes sense. You have three entry points into the pipeline, but no shared language on what 'qualified' means. How does that show up for you? Where do deals leak?"

VP Sales: "Exactly. SDRs might mark something as SQL that an AE would disqualify in the first call. And expansion opportunities that CS surfaces sometimes die because AEs think they're too small. We're probably losing 30–40% of expansion revenue because it never even makes it into an opportunity. That's roughly €2M/year in lost expansion."

[This tells you: Pain is quantified. Specific number (€2M/year). Multiple problems (inbound + expansion qualification). This is real enough for a follow-up conversation.]

You: "€2M is significant. If you closed that gap — if you had a shared way to qualify opportunities so you didn't lose that expansion revenue — what would that mean?"

VP Sales: "We could hit our growth target. Right now we're at 35% growth, aiming for 50%. If we keep that €2M, we're a lot closer. Plus, it would make our forecast more reliable. Today we're off by 25% month to month because we're working low-quality pipeline."

[Impact: clarified. Two outcomes: (1) hit growth target, (2) forecast accuracy. Both matter to CFO.]

You: "Is there a timeline driving this? When does this need to be solved?"

VP Sales: "We have a board meeting in May. The growth story is the centerpiece. If we can show that we're being more disciplined about qualification and that our forecast is more accurate, that's a win. If we show up to the board saying 'yeah, we're losing €2M but we're thinking about it,' that's bad."

[Critical Event: May board meeting. Specific date, specific consequence (board confidence). This creates urgency.]

You: "Got it. When the board asks you how you're solving this, who do you need to have in the room with you?"

VP Sales: "The CFO will definitely be there. And our CRO — she's new, 6 months in, and this GTM transformation is her agenda. She cares a lot about the forecast piece."

[Decision: Started to emerge. CRO = champion/economic buyer. CFO = fiscal gatekeeper. But haven't identified technical buyer yet.]

You: "Are there any technical or operational people involved in evaluating a solution like this?"

VP Sales: "We have a Sales Ops person, Sarah. She'd need to sign off on whether it fits into our HubSpot setup and doesn't break anything. And honestly, our IT team is a bit of a gate — they're protective about integrations."

[Decision: Clearer now. Sarah = Sales Ops (process owner), IT = gatekeeper.]

You: "Perfect. Here's what I'm hearing: you have three entry points into pipeline (inbound, expansion, network), but no shared qualification language. That's costing you €2M in lost expansion revenue and making your forecast unreliable. You're aiming for 50% growth, but can't confidently budget for it. The May board meeting is the forcing function — you want to show disciplined, predictable GTM. To fix this, you'd need buy-in from the CRO (business), CFO (ROI), Sales Ops Sarah (implementation), and IT (technical gates). Does that summary land?"

VP Sales: "Yes, that's exactly right."

You: "Great. My next step is to have a conversation with CRO and the CFO — just to understand: Does the May board date actually drive urgency? And what does the ROI business case need to show? Sound good?"

VP Sales: "Yeah, let's do that. I'll make the introduction."
```

**Coaching debrief on that call:**

Situation score: 2 (validated — clear picture of org, growth stage, motions, tools)
Pain score: 2 (validated — quantified at €2M/year, specific impact on forecast)
Impact score: 1 (identified — they've mentioned growth target and forecast, but not modelled the specific impact)
Critical Event score: 3 (leveraged — May board meeting is immovable, consequence is clear, they're thinking about it as timeline driver)
Decision score: 1 (identified — know some stakeholders, but no process clarity yet, haven't spoken to CFO or IT)

**Total: 2+2+1+3+1 = 9/15.** Next actions: (1) 1:1 with CRO to confirm business case and urgency. (2) 1:1 with CFO to validate ROI math (€2M expansion upside + forecast accuracy improvement). (3) 15-min call with Sales Ops Sarah to confirm no technical blockers. Once those are done, deal jumps to 12-13/15.

---

### SPICED Evidence by Pipeline Stage

Different SPICED scores are required at different stages. This prevents deals from moving too fast or stalling.

```
DISCOVERY STAGE (0-30 days):
  Goal: Build situation + pain foundation
  Minimum SPICED score: 4+ (any combination)
  Must have:
    - Situation ≥ 1 (know who you're talking to and what they do)
    - Pain ≥ 1 (identified a problem, even if not quantified)
  Red flags to exit:
    - Pain score stays at 0 after 2 calls (they don't actually care)
    - Situation score stays at 0 (can't even schedule a follow-up)
    - Buyer says "we're happy with status quo and have no budget" (not a deal)

QUALIFICATION STAGE (30-60 days):
  Goal: Validate impact + critical event + decision process
  Minimum SPICED score: 8+
  Must have:
    - Situation ≥ 2 (know their operating model)
    - Pain ≥ 2 (quantified in euros)
    - Impact ≥ 1 (they've articulated future state)
    - Critical Event ≥ 1 (identified deadline or trigger)
    - Decision ≥ 1 (know who's involved)
  Red flags to exit:
    - After 3 calls, Critical Event is still 0 (no real urgency, deal will stall)
    - Pain stays at 1 (no quantification; they're not serious)
    - Decision is 0 (still no idea who the economic buyer is)

SOLUTION DESIGN / PROPOSAL (60-90 days):
  Goal: Close decision + champion gaps, prepare proposal
  Minimum SPICED score: 10+
  Must have:
    - Situation ≥ 2 (understand how to position solution)
    - Pain ≥ 2 (can quantify savings/upside against their cost)
    - Impact ≥ 2 (they've modelled the business case)
    - Critical Event ≥ 1 (driven timeline for proposal delivery)
    - Decision ≥ 2 (know decision process, have champion, identified economic buyer)
  Red flags to delay proposal:
    - Decision score is 1 or 0 (haven't talked to economic buyer; proposing to wrong person)
    - Impact score is 0 or 1 (haven't modelled upside; proposal will be about price)
    - Pain quantification is missing (can't tie ROI to specific problem)

NEGOTIATION / CLOSE (90+ days):
  Goal: Close economic buyer, handle legal/procurement
  Minimum SPICED score: 12+
  Must have:
    - All elements ≥ 2
    - Economic buyer directly engaged (not through champion)
    - Decision process walkthrough complete (know exact path to signature)
    - Commercial terms pre-qualified (no surprises in legal/procurement)
  Red flags to escalate:
    - Economic buyer hasn't been engaged directly by this stage (you've been relying on champion)
    - Critical Event passed (May board was the deadline, it's now June)
    - Procurement introduces new requirements not discussed before (scope creep)
```

---

## MEDDIC / MEDDPICC

**Best for:** Enterprise sales, complex deals with multiple stakeholders, sales cycles 90+ days, ACV €50K+

```
M — Metrics
    Quantifiable business outcomes the customer wants to achieve.
    "What specific numbers would improve if you solve this?"

E — Economic Buyer
    The person with final authority and budget. Not the champion — the signer.
    "Who signs off on investments of this size?"

D — Decision Criteria
    The formal and informal standards used to evaluate vendors.
    "What criteria will you use to compare solutions?"

D — Decision Process
    Steps, stakeholders, timeline, and approval gates.
    "What does your evaluation and approval process look like?"

P — Paper Process (MEDDPICC extension)
    Legal, procurement, security review — the steps after verbal yes.
    "What's your procurement and legal review process?"

I — Identify Pain
    Specific business problems driving the initiative.
    "What's broken today, and what does it cost you?"

C — Champion
    Internal advocate with power, influence, and a personal win in the deal.
    "Who internally is sponsoring this and why do they personally care?"

C — Competition (MEDDPICC extension)
    Who else they're evaluating, including the status quo.
    "Who else are you considering, including doing nothing?"
```

### MEDDIC Scoring

Score each element 0-3 (same scale as SPICED):
- **MEDDIC total: 0-18.** Deals below 10 should not be in Proposal or later stages.
- **MEDDPICC total: 0-24.** Deals below 14 should not be in Proposal or later stages.

**Champion strength is the single strongest predictor of deal outcome.** Weight it heavily in deal reviews. A deal with a strong champion and weak metrics is more likely to close than one with strong metrics and no champion.

### MEDDIC CRM Implementation

```
Properties (deal level):
  meddic_metrics_score          (dropdown: 0-3)
  meddic_economic_buyer_score   (dropdown: 0-3)
  meddic_decision_criteria_score (dropdown: 0-3)
  meddic_decision_process_score (dropdown: 0-3)
  meddic_pain_score             (dropdown: 0-3)
  meddic_champion_score         (dropdown: 0-3)
  meddic_total_score            (number)
  meddic_economic_buyer_name    (text)
  meddic_champion_name          (text)

Add for MEDDPICC:
  meddic_paper_process_score    (dropdown: 0-3)
  meddic_competition_score      (dropdown: 0-3)
```

## BANT

**Best for:** High-velocity sales, SMB, transactional deals <€10K ACV, initial qualification screen

```
B — Budget     → Do they have budget allocated or authority to allocate?
A — Authority  → Are you talking to the decision-maker?
N — Need       → Is there a genuine business need you can solve?
T — Timeline   → Is there urgency or a defined buying window?
```

**Important limitations:** BANT is a qualification filter, not a discovery framework. It tells you whether to continue the conversation, not how to win the deal. For anything beyond transactional sales, BANT should be the first screen, with SPICED or MEDDIC used for deeper qualification.

**Modern adaptation:** Many practitioners now run BANT in reverse — NTBA — starting with Need and Timeline (the customer's perspective) before probing Budget and Authority (the seller's concerns). This feels less interrogative and produces better conversations.

## Challenger Sale

**Best for:** Consultative selling, disrupting status quo, complex B2B where the customer doesn't yet know they have a problem

Challenger is not a qualification checklist — it's a selling posture built on three behaviors:

1. **Teach** — Lead with an insight the customer hasn't considered. Challenge their assumptions about their own business. "Most companies in your space are losing 15% of pipeline because of [X] — here's why, and here's what the ones who fixed it did differently."

2. **Tailor** — Adapt the message to each stakeholder's specific priorities. The CFO cares about cost reduction and ROI. The VP Sales cares about rep productivity. The CTO cares about integration and security. Same product, different pitch.

3. **Take Control** — Guide the buying process. Push back constructively on unrealistic timelines, under-scoped evaluations, and attempts to commoditise your solution. "I'd recommend we extend the POC by two weeks — rushing it will give you data that doesn't reflect your real use case."

**When to combine with other frameworks:** Challenger works best as a selling *style* layered on top of a qualification *structure*. SPICED + Challenger is a strong combination: SPICED provides the discovery structure, Challenger provides the conversational approach.

## SPIN Selling

**Best for:** Discovery conversations, uncovering latent needs, consultative sales

```
S — Situation Questions   → Understand current state (research first, ask sparingly)
P — Problem Questions     → Surface specific difficulties and dissatisfactions
I — Implication Questions → Explore the consequences and downstream effects
N — Need-Payoff Questions → Help the buyer articulate the value of solving the problem
```

**The critical rule:** Don't pitch until you've completed Implication and Need-Payoff. Premature pitching — jumping to your solution before the buyer feels the full weight of the problem — is the most common mistake in consultative sales. If the buyer hasn't articulated why solving this matters, your pitch will land flat.

## Gap Selling

**Best for:** Value-based selling, outcome-focused conversations, reframing around business impact

```
Current State → What's happening now? Problems, environment, root causes, business impact
Future State  → What does success look like? Desired outcomes, metrics, emotional state
The Gap       → The distance between current and future state IS your value proposition
```

**Key insight:** The size of the gap determines urgency and willingness to pay. Your job as a seller is to make the gap vivid, quantifiable, and emotionally real — not to pitch features. A gap articulated in the customer's own words is 10x more powerful than one articulated in your marketing language.

## Methodology Selection Guide

| Factor | SPICED | MEDDIC | BANT | Challenger | SPIN | Gap |
|--------|--------|--------|------|------------|------|-----|
| Deal complexity | Medium-High | High | Low | High | Medium | Medium-High |
| Sales cycle | 30-90+ days | 90+ days | <30 days | 60+ days | 30-90 days | 30-90 days |
| ACV range | €10K-100K | €50K+ | <€10K | €25K+ | €10K-50K | €10K-100K |
| Best phase | Full cycle | Full cycle | Qualification | Pitch/Proposal | Discovery | Discovery |
| Recurring revenue fit | ★★★★★ | ★★★★ | ★★ | ★★★ | ★★★ | ★★★★ |
| Team maturity needed | Medium | High | Low | High | Medium | Medium |

### Recommended Combinations

- **SPICED + Challenger:** SPICED structures discovery; Challenger sets the conversational tone. Best for: B2B SaaS mid-market, where you need to both qualify rigorously and teach prospects something new.

- **MEDDIC + SPIN:** Use SPIN for discovery conversation flow, MEDDIC for deal qualification tracking. Best for: enterprise deals where discovery is multi-meeting and qualification needs to be rigorous.

- **Gap + SPICED:** Gap Selling's current/future state maps directly to SPICED's Situation, Pain, and Impact. They reinforce each other naturally. Best for: value-driven sales where the buyer needs to feel the cost of inaction.

- **BANT → SPICED:** Use BANT as a 5-minute initial qualification screen, then SPICED for full discovery on qualified leads. Best for: high-volume inbound motions where SDRs need to filter quickly before passing to AEs.

## Operationalizing Methodology in CRM

### Universal Deal Properties

Regardless of methodology, every deal should have:

```
sales_methodology           (dropdown: SPICED / MEDDIC / MEDDPICC / Other)
sales_qualification_score   (number — aggregate score from methodology)
sales_discovery_complete    (checkbox — has full discovery been documented)
sales_champion_identified   (checkbox)
sales_decision_maker_access (dropdown: None / Indirect / Direct)
sales_critical_event        (single-line text — what's driving urgency)
sales_critical_event_date   (date — when the deadline hits)
sales_competitive_status    (dropdown: No Competition / Competing / Displacing Incumbent)
```

### Deal Progression Gates

Enforce methodology adherence through stage requirements:

```
Discovery → Solution Design:
  ✓ Pain/Situation documented (methodology-specific score ≥ threshold)
  ✓ Impact quantified in euros or clear business metric
  ✓ Key stakeholders identified

Solution Design → Proposal:
  ✓ Decision process mapped
  ✓ Decision criteria documented
  ✓ Champion confirmed and engaged
  ✓ Critical event identified (or explicitly flagged as risk)
  ✓ Qualification score above threshold

Proposal → Negotiation:
  ✓ Economic buyer engaged directly
  ✓ Competitive landscape documented
  ✓ Pricing expectations aligned
  ✓ Paper/procurement process understood (timeline to signature)
```

## Customer Interview → SPICED Pipeline

Customer interviews are the highest-leverage sales activity. One 45-minute interview produces 4+ assets and validates your SPICED qualification framework.

### The 8-Step Interview Process

**Duration:** 30-45 minutes. Always record + transcribe.

1. **Open with Safety + Context** (2-3 min) — Confidential, not a sales call
2. **Agenda → Check End Time → Confirm Goal** (1 min)
3. **Dive Deep into SITUATION** (5-8 min) — Role, team, growth stage, tech stack
4. **Bring Back to the PAIN** (5-8 min) — Biggest problem before adoption, business impact
5. **Get Concrete on IMPLEMENTATION** (5-8 min) — Rollout, champion, surprises
6. **Prove the IMPACT** (5-8 min) — Concrete value, quantified results
7. **Unpack the CRITICAL EVENT** (3-5 min) — Trigger moment, business pressure
8. **Explore the DECISION** (3-5 min) — Why you vs competitors, deciding factor

### Interview Outputs (4 Assets per Interview)

| Output | What It Is | Where It Goes |
|--------|-----------|--------------|
| **Testimonials** | "Working with us feels like..." quotes | Website, proposals, LinkedIn |
| **Quotes** | 5-10 quotable lines per interview | Sales decks, blog posts, social proof |
| **Case Study** | 1-2 page problem→solution→results | Nurture sequences, website, sales enablement |
| **SPICED Data** | ICP validation + persona refinement | CRM fields, ICP library, positioning work |

**The math:** 10 interviews = 40+ content assets + validated ICP + refined SPICED language.

For full ICP building methodology using interview data, see `neon-icp` skill.

## Stakeholder / Champion Mapping

For deals above €25K ACV, map every identified person against the 8 stakeholder roles:

| Role | What They Do | How to Identify |
|------|-------------|----------------|
| **Initiator** | First raised the need internally | "Who first brought this up?" |
| **Champion** | Actively helps you win; has personal stake | Tests: Will they coach you? Share intel? Sell internally? |
| **Decider** | Final budget authority | "Who signs off on investments of this size?" |
| **Operations** | Will manage implementation day-to-day | "Who will own the rollout?" |
| **Users** | Will use the solution daily | "Who will be in the system every day?" |
| **CxO** | Executive sponsor above the Decider | Often the Decider's boss — provides air cover |
| **Finance** | Procurement, CFO, budget gatekeeper | "What's your procurement process?" |
| **Security** | IT, compliance, legal review | "Do you have a security review process for new vendors?" |

**CRM Implementation:** Create a `stakeholder_map` note field per deal. In deal reviews, count roles filled:
- 1-2 roles: ⚠️ Single-threaded — highest risk factor
- 3-4 roles: Developing — push for Decider access
- 5+ roles: Well-mapped — focus on Champion strength

## Coaching & Adoption

### Weekly Deal Review Structure

1. Select 3-5 deals per rep — prioritise stuck deals, upcoming close dates, and large opportunities.
2. For each deal, ask methodology-specific questions. Don't ask "how's this deal going?" — ask "what's the critical event?" and "who's the economic buyer?"
3. Score the deal against the framework. Do it live with the rep so they internalise the scoring.
4. Identify the #1 gap and assign one specific action to close it. Not three actions — one. "Your next step is to get a 15-minute call with the CFO. How will you make that happen?"
5. Follow up next week: was the action completed? What changed?

### Driving Rep Adoption

Methodology adoption fails when it feels like extra work on top of selling. Make it the way selling works:

- **Embed in CRM, not in slide decks.** If the methodology fields are in the deal record, reps fill them out as part of their workflow. If it's in a separate document, they won't.

- **Coach with the methodology, not about it.** Don't do "SPICED training." Do deal reviews where you use SPICED to diagnose why deals are stuck. Reps learn by seeing it work on their actual pipeline.

- **Celebrate wins attributed to the methodology.** When a rep wins a deal because they identified the critical event early or got direct access to the economic buyer, highlight it publicly. "Sarah closed the Acme deal two weeks early because she discovered the board review was moved up — that's the CE in SPICED working exactly as designed."

- **Don't over-complicate.** If reps need to fill out 20 fields per deal, adoption will collapse. Start with the 5-7 most critical fields and add more only when the first set becomes habit.

### New Rep Onboarding

```
Week 1: Framework introduction + language
  - Teach the methodology concepts (2-hour session max)
  - Give them a one-page reference card, not a 40-page playbook
  - Have them score 5 historical deals using the framework

Week 2: Guided practice
  - Role-play discovery calls using the framework
  - Listen to 3-5 recorded calls and identify methodology elements
  - Debrief each exercise: what was strong, what was missed

Week 3: Shadowing
  - Shadow 3+ live calls with experienced reps
  - After each call, identify: what SPICED elements were uncovered?
  - Begin scoring real deals in CRM

Week 4: Live with coaching
  - Run own discovery calls with manager listening
  - Debrief after every call for the first 2 weeks
  - Start participating in deal reviews

Ongoing:
  - Weekly deal reviews with methodology scoring
  - Monthly calibration: are reps scoring consistently?
  - Quarterly refresh: any methodology adjustments needed?
```

## Discount Negotiation Playbook

The negotiation stage is where methodology meets money. Reps who followed SPICED or MEDDIC through discovery have the leverage they need — quantified pain, identified decision-makers, documented critical events. Reps who skipped discovery are now negotiating from weakness. This section bridges the methodology with the pricing conversation.

### When a Prospect Asks for a Discount

**Step 1: Diagnose the objection.** Most discount requests are not about price. They are signals:

- "We need a discount" often means "I need to show my boss I negotiated"
- "It's too expensive" often means "I don't see the value yet"
- "Competitor is cheaper" often means "I have an alternative and want leverage"
- "Budget is limited" often means "this isn't prioritised" or "timing is wrong"

Ask: "Help me understand what's driving the request" before you offer anything.

**Step 2: Use the methodology to respond.** If you've scored the deal properly:

- **SPICED Pain score = 3?** You have quantified cost-of-inaction. Use it: "We documented that this problem costs you €200K/quarter. Our annual subscription is €80K. Even at list price, the ROI is 2.5x in year one."
- **MEDDIC Champion score = 3?** Your champion can sell internally: "Let's prepare your business case together. What does your CFO need to see to approve this at the proposed investment?"
- **Critical Event confirmed?** Urgency limits negotiation leverage: "Your board review is in 6 weeks. A 3-week discount negotiation puts the implementation timeline at risk."

**Step 3: Trade, never give.** Every concession requires a reciprocal concession:

- Longer term → modest discount (5–10%)
- Annual prepay → cash flow discount (3–5%)
- Logo/reference rights → strategic discount (5–10%)
- Expansion commitment → volume discount (per-tier schedule)
- Faster signature → nothing changes (urgency is the concession)

### Discount Objection Scripts

**"Your competitor offered us X% less"**

Response: "Which solution are you comparing? When you look at total cost including implementation, training, and support — plus the switching cost from [current tool] — how do the proposals compare? We find that customers who evaluated both chose us because of [specific differentiator]. Let me walk you through what that means for your use case."

If the threat is real and documented: this qualifies for competitive displacement reason code. Follow the discount governance matrix. Require: named competitor, specific proposal evidence, written competitive analysis.

If the threat is vague: hold on price. Offer to do a joint value assessment or proof-of-value. Let the product win on merit.

**"We need a bigger discount to get this approved"**

Response: "I understand procurement wants to see value. Rather than discounting the rate, let me help you build the business case. We've quantified [pain] at [cost]. Even at list price, you're looking at [X]x ROI in the first year. Can we schedule a call with your CFO where I present the value analysis?"

Alternative: offer non-monetary concessions — extended onboarding, additional training, dedicated success manager for 90 days, priority support upgrade, early access to beta features. High perceived value, low marginal cost.

**"Others in our market got a better price"**

Response: "Every customer's pricing reflects their specific commitment — term length, seat count, timing. I can't speak to other agreements, but I can build you a proposal that matches the value and commitment you're making. If you're looking for comparable economics, the path is typically [multi-year / volume commitment / prepay]."

Never confirm or deny specific customer pricing. Confidentiality is non-negotiable and also your strongest defence.

**"Our buying organisation expects standard pricing"**

Response: "We value your organisation's role. Let me understand: how many of your member companies are actively evaluating? What's the expected adoption timeline? We structure pricing based on actual committed volume rather than projected, which ensures every member gets fair terms tied to their specific configuration."

For GPO/consortium handling framework (admin fees, volume tiers, negotiation rules), see the pricing-strategy skill.

### CRM Properties for Negotiation Tracking

```
discount_requested        (boolean — did the prospect ask for a discount?)
discount_reason_code      (dropdown — from governance policy: Annual prepay /
                           Competitive displacement / Volume commitment /
                           Strategic account / Multi-year term lock /
                           Seat volume tier / Logo reference / GPO consortium)
discount_approved_%       (number — actual % approved)
discount_approver         (text — who signed off)
discount_concession       (text — what reciprocal concession was agreed)
discount_expiry_date      (date — when the discount terms expire)
negotiation_duration_days (number — days from first discount ask to close)
gpo_flag                  (boolean — is this deal part of a GPO/buying consortium?)
gpo_name                  (text — name of purchasing organisation)
```

Track these to identify patterns: which reps discount most, which reason codes are most common, whether discounted deals have different LTV than full-price deals, and how long discount negotiations extend the sales cycle. If discounted cohorts show lower NRR, the discount attracted wrong-fit customers — tighten governance.

## Pipeline Management Operating Model

Beyond discovery and qualification, the sales process needs an operational backbone. This section covers the management layer that ensures deals move through stages correctly and forecasting is reliable.

**Source:** Adapted from Union Square Consulting's Pipeline Management Pyramid. Neon applies this as the operational complement to SPICED — SPICED tells you how to run the conversation; this tells you how to run the pipeline.

### Stage Entry/Exit Criteria

Every deal stage needs explicit criteria for what must be true to enter and exit. Without this, stages become meaningless labels and pipeline data is unreliable.

```
STAGE           ENTRY CRITERIA                           EXIT CRITERIA
────────────    ──────────────────────────────────       ──────────────────────────────────
Discovery       - Contact identified as ICP fit          - SPICED S+P scored ≥ 2 each
                - Initial meeting booked/completed       - Pain validated (not assumed)
                - Contact record created in CRM          - Next meeting booked

Qualification   - SPICED S+P+I scored                    - SPICED total ≥ 8/15
                - Decision process understood            - Economic buyer identified
                - Budget range confirmed                 - Timeline established
                - Competition known                      - Champion identified

Solution        - Solution mapped to validated pain      - Solution presented to buyer
Design          - Pricing model selected                 - Objections captured
                - Internal resources confirmed           - Technical validation complete
                - Proposal/SOW drafted                   - Champion coaching delivered

Negotiation     - Proposal delivered to decision-maker   - Terms agreed (verbal)
                - Commercial terms discussed             - Legal/procurement engaged
                - Contract redlines received             - Signature timeline confirmed

Closed Won      - Contract signed                        - Handoff to CS initiated
                - Payment terms confirmed                - Onboarding scheduled
```

### Stocks & Questions by Stage

"Stocks" = the information inventory that should be captured at each stage. If the stock is empty, the deal shouldn't progress.

```
DISCOVERY STOCKS:                    QUESTIONS TO ASK:
  Situation context                  "How do you handle [X] today?"
  Pain statement (their words)       "What's the main friction?"
  Stakeholder map (initial)          "Who else is involved in this?"
  Current tools/process              "What have you tried before?"

QUALIFICATION STOCKS:                QUESTIONS TO ASK:
  Impact quantified (€/time)         "What would solving this be worth?"
  Critical Event identified          "When does this need to be resolved?"
  Decision process mapped            "Walk me through how you'd make this decision"
  Champion validated                 "Who internally is pushing for this?"
  Budget confirmed                   "Is there budget allocated for this?"

SOLUTION STOCKS:                     QUESTIONS TO ASK:
  Requirements documented            "What does success look like in 90 days?"
  Technical fit validated            "Any integration requirements I should know?"
  Objections surfaced                "What concerns does your team have?"
  Competition comparison             "Who else are you evaluating?"

NEGOTIATION STOCKS:                  QUESTIONS TO ASK:
  Decision criteria ranked           "What matters most in your final decision?"
  Contract redlines listed           "Are there standard procurement terms?"
  Concession limits defined          "What would make this a clear yes?"
  Timeline commitment                "When do you need to go live?"
```

### Pipeline Inspection Process

```
WEEKLY DEAL REVIEW (30 min per rep):
  Format: Rep walks through top 5 deals by expected close date
  Questions:
    1. What changed since last week?
    2. What's the next concrete step? (Not "follow up" — specific action)
    3. Is this deal on track for the forecast commit?
    4. What's blocking progress?
    5. Should we involve anyone else? (Champion coaching, exec sponsor)

  Manager actions:
    - Challenge: "What evidence do you have for that?" (test deal quality)
    - Coach: "Here's what I'd try next" (develop capability)
    - Redirect: "This deal is stuck — let's deprioritise or kill it"

MONTHLY PIPELINE COUNCIL (60 min, cross-functional):
  Attendees: Sales leader, Marketing leader, CS leader, RevOps
  Agenda:
    1. Pipeline health: coverage ratio, velocity, stage distribution
    2. Conversion analysis: which stages are leaking?
    3. Source analysis: which channels produce best-quality pipeline?
    4. Forecast review: commit vs actual trend
    5. Actions: what changes this month?

DEAL KILL CRITERIA (when to walk away):
  - SPICED score < 4 after two discovery calls
  - No access to economic buyer after qualification stage
  - Critical Event keeps moving (no real urgency)
  - Champion leaves the organisation
  - Deal age > 2x average sales cycle with no stage progression
  - Customer requirements outside product capability
```

### Forecast Categories

```
CATEGORY        DEFINITION                                    CRITERIA
────────        ──────────                                    ────────
Commit          Will close this period. Would bet my job.     - Verbal yes received
                                                              - Contract in legal/procurement
                                                              - Signature expected within period

Best Case       High probability, needs 1-2 things to land.  - Solution presented and accepted
                                                              - Budget confirmed
                                                              - Decision timeline within period
                                                              - No known blockers

Upside          Could close but significant unknowns remain.  - Qualified (SPICED ≥ 8)
                                                              - Champion engaged
                                                              - Timeline plausible but not committed

Pipeline        Active opportunities, too early to forecast.   - In Discovery or early Qualification
                                                              - Building relationship
                                                              - Not yet forecast-ready
```

## Pipeline Management Operating Model

SPICED qualifies deals. This section operationalizes the full pipeline management model around SPICED — from stage entry criteria to inspection cadence.

### Stage Entry and Exit Criteria

Every deal stage requires explicit entry and exit gates. Without them, CRM data reflects rep optimism, not deal reality.

```
STAGE               ENTRY CRITERIA                          EXIT CRITERIA (must be true to advance)
─────               ──────────────                          ────────────────────────────────────────
MQL/Prospect        Meets ICP (firmographic + intent fit)   Responded to outreach / booked meeting

Discovery           Meeting booked                          SPICED partially captured: Situation +
                                                            Pain confirmed (minimum viable score ≥ 4)

Qualification       Pain confirmed, S+P+I captured          I+C+E captured; SPICED score ≥ 7;
                                                            Champion identified and engaged

Solution Presented  SPICED complete; solution scoped        Verbal acceptance of solution fit;
                                                            Proposal/pricing shared

Evaluation          Proposal shared                         Legal/procurement engaged or decision
                                                            timeline confirmed within period

Closed Won          Contract signed                         —
Closed Lost         Decision made in favour of competitor   Loss reason documented in CRM
                    or status quo; or deal abandoned
```

### Required CRM Fields by Stage

Every stage should mandate data capture before the deal advances. These are the minimum fields — adapt to your CRM workflow.

```
STAGE               REQUIRED CRM FIELDS
─────               ───────────────────
Discovery           Company size (ARR/headcount), current state, problem trigger
Qualification       Pain category, business impact (quantified if possible), decision process,
                    Champion name + role, critical event / deadline
Solution Presented  Solution scope, commercial model proposed, price range shared
Evaluation          Key stakeholders engaged, procurement/legal status, timeline confirmed
Closed              Win/loss reason, competitor (if applicable), ACV, close date
```

### Disqualification Criteria (When to Walk Away)

Explicit "close out" rules prevent pipeline pollution and wasted forecast capacity.

**Disqualify immediately if:**
- No identifiable pain connected to your solution after two discovery conversations
- Budget is 0 and there's no route to create budget within 2 quarters
- No executive sponsor or champion willing to engage
- Product fit gap confirmed (customer requirements outside capability)
- Company not in ICP (wrong segment, geography, or GTM motion)

**Put on hold (not disqualify) if:**
- Critical Event is more than 6 months out
- Champion leaves but relationship can be rebuilt
- Budget freeze expected to lift in next quarter

**Staleness rule:** Any deal with no stage progression in > 1.5x your average sales cycle triggers a mandatory review. Either advance it or close it out.

### Pipeline Inspection Process

Management cadence for reviewing deal quality, not just deal volume.

**Weekly (individual rep + manager 1:1):**
- Review SPICED score for each Qualification+ deal
- Call out any deals advancing without meeting exit criteria
- Flag stale deals (no activity in 10+ business days)
- Confirm next best action for every deal in Evaluation

**Monthly (team pipeline review):**
- Review stage conversion rates vs. benchmarks
- Identify systematic gaps (e.g., low Discovery → Qualification conversion = qualification criteria too loose or too tight)
- Review closed-lost reasons and adjust ICP/disqualification criteria if patterns emerge

**Quarterly (revenue planning):**
- Reconcile pipeline coverage ratio vs. quota (minimum 3x for Commit, 4-5x for full quarter target)
- Adjust territory/capacity if pipeline generation is below coverage threshold
- Win/loss analysis: aggregate patterns across wins and losses to update SPICED calibration

### Forecasting Methodology

See the revops-forecasting skill for full forecasting depth and methodology. The Forecast Categories below are the sales methodology layer — what reps commit and why.

*Note: Full category definitions are in the Forecast Categories section above. The pipeline management context:*
- Commit deals must have all SPICED elements captured and a clear path to signature
- Best Case deals have a qualified champion but one or two open elements (e.g., procurement not yet engaged)
- Upside deals have enough SPICED for a reasonable call but timeline or decision process is unclear
- Pipeline deals are active but too early for the forecast — move to a category only when SPICED score ≥ 6

**Coverage discipline:** If Commit + Best Case < quota, the team doesn't have a forecasting problem — they have a pipeline generation problem. Escalate there, not at forecast accuracy.

For pipeline reporting architecture and dashboard design, see the pipeline-visibility skill.

---

## Benchmark Data

For Ebsta/Pavilion 2025 benchmark data on discovery, multi-threading, qualification, and negotiation, see `references/benchmarks.md`.

---

### The AI-Augmented Sales Day (Kyle Norton / Owner.com)

Kyle Norton runs a 100+ AI-infused sales team at Owner.com. His framework for what a rep's day looks like when AI is properly embedded:

**Morning (automated by AI):**
- Pre-call research: AI prepares briefing packs for every scheduled meeting (company context, contact history, recent signals, recommended talk points)
- Account prioritisation: AI scores today's pipeline by urgency and signal strength
- Admin clearance: CRM updates, activity logging, and data enrichment happen automatically overnight

**Core hours (human-led, AI-supported):**
- Discovery and negotiation calls (the 70-80% revenue-generating time target)
- AI provides real-time coaching prompts during calls (if conversation intelligence is deployed)
- Post-call: AI generates summary, updates CRM, drafts follow-up email for rep review

**End of day (automated by AI):**
- Pipeline snapshot updated
- Next-day prep begins automatically
- Stale deal alerts surfaced for tomorrow's action

**The target:** reps spend 70-80% of their time on revenue-generating activities. Current industry average: 30-40%. The gap is filled by automating research, admin, and data entry — not by automating the human conversation.

**Bridge to SPICED:** the AI handles data collection and preparation. The rep brings SPICED qualification skill, judgement, and human connection. AI can score deals on SPICED dimensions, but the rep runs the discovery.

Source: SaaStr AI Agent Playbook, Kyle Norton / Owner.com case study

---

## Norton Framework Additions (Source: Kyle Norton / Aviv Canaani, Revenue Leadership Podcast, 2026)

### Methodology as Architecture vs. Craft

Two modes of methodology implementation:

**Craft Mode:** Great reps execute SPICED/MEDDIC well because they're skilled. Depends on individual talent.

**Architecture Mode:** Systems ensure average reps execute SPICED/MEDDIC consistently. Depends on process design + tool enforcement + coaching cadence.

Architecture mode scales. Craft mode doesn't.

**Implementation Principles:**
- Embed methodology in CRM (required fields, stage gates, scoring)
- Automate methodology coaching via deal review templates
- Use AI to evaluate SPICED completeness before stage advancement
- Measure methodology adoption as a leading indicator, not just outcomes

**Anti-Prospecting Qualification Gate:**
High SPICED thresholds reduce proposal churn. Use methodology to DISQUALIFY fast:
- Kill deals with SPICED <4 after discovery
- This frees rep time for higher-quality opportunities
- Productivity play: fewer deals worked, but higher conversion on the deals you do work

**Self-Reinforcing Methodology Adoption Loop:**
Better qualification → faster velocity → better results → higher rep trust → more adoption → better qualification → (repeat)

### "Show, Don't Demo" Methodology (Donnelly, E62)

In low-trust, noisy AI markets, stop claiming and start proving.

**The approach:**
1. When a prospect books a demo, build a custom AI agent using the prospect's public knowledge base within 24 hours
2. Show the prospect how THEIR specific use case would work — not a generic demo environment
3. Generic demos create generic trust. Custom proof creates specific confidence.

**Extended "show me" philosophy:**
- Tell prospects to become customers of your existing clients: "Go to [client] and buy something. See how they upsell you."
- One prospect tested a client's experience, found issues — turned into a teaching moment about configuration choices
- Build time has collapsed with AI. What took weeks now takes hours.

**When to deploy:**
- Noisy markets where every competitor claims the same thing
- AI/tech sales where the product can be demonstrated with prospect data
- Deals where trust is the bottleneck (not feature comparison)

**CRM tracking:** Add a field `custom_proof_delivered` (Yes/No/Date) to track whether the "show, don't demo" approach was used and its impact on win rate.

### Cognitive Atrophy Warning for AI-Assisted Methodology (Donovan, E61)

One CRO removed an AI tool that auto-extracted MEDDIC fields from call transcripts. The tool worked perfectly — but the AEs stopped thinking critically about their deals. They became passive consumers of AI-generated qualification.

**The principle:** AI that removes cognitive load can also remove cognitive development.

**Implementation rule for MEDDIC/SPICED automation:**
- Use AI to SUGGEST methodology scores, not auto-populate them
- Require reps to CONFIRM or OVERRIDE AI suggestions with their own reasoning
- Build "why do you agree/disagree?" prompts into the workflow
- Track override frequency — too few overrides means reps aren't thinking

### The Anti-Prospecting Thesis (Canaani, E64)

**The myth:** "You're not a real AE if you don't prospect."

**The reality:**
- 80-90% of closed revenue comes from inbound (Canaani's data)
- Salesforce State of Sales: reps spend only 28% of their week actually selling
- Paying €250-300K OTE for prospecting = failure of resource allocation

**Why AEs are bad prospectors:**
- Not getting the repetitions (BDRs do this full-time)
- Don't actually want to do it (misaligned motivation)
- BDRs are motivated differently — their #1 goal is to stop being a BDR

**Implication for methodology:** Methodology training should focus on CLOSING skills (discovery, qualification, negotiation), not prospecting skills. Invest prospecting methodology training in the BDR team, not the AE team.

**Supporting data:**
- 6sense: 83% of the time, the buyer initiates first contact
- Gartner: self-navigating buyers complete high-quality deals 65% of the time vs. 24% in sales-rep-led purchases
- HubSpot: inbound leads cost 61% less

## How to Use This Skill

**"Which methodology should we use?"** → Use the selection guide. Ask about ACV, sales cycle, team maturity, and whether they sell recurring revenue. Give a clear recommendation with rationale, including combination suggestions.

**"Help me implement [methodology]"** → Provide the exact CRM properties to create, stage gates to enforce, scoring model to use, and coaching prompts to deploy. Be prescriptive — property names, field types, threshold values.

**"Score this deal"** → Walk through every methodology element. For each, ask what they know, rate it 0-3, and identify the gap. Calculate the total score and give a clear verdict: advance, hold, or go back to discovery.

**"Reps aren't adopting the methodology"** → Diagnose why. Is it too complex? Not embedded in CRM? Not reinforced in coaching? Give specific adoption tactics, not abstract advice about "change management."

**"How do I run deal reviews?"** → Provide the exact structure: which deals to pick, which questions to ask per methodology, how to score live, how to assign actions, how to follow up.

**"How do I combine methodologies?"** → Use the combination recommendations. Most teams benefit from one discovery framework (how you have conversations) + one qualification framework (how you score and track deals).

**"How do I handle discount objections?"** → Use the discount negotiation playbook. Diagnose the real objection, use methodology scores as leverage, trade rather than give. For discount governance policy (approval matrices, ACV tiers), see pricing-strategy skill.

**"Prospect is asking for GPO/consortium pricing"** → Flag the deal with gpo_flag. Validate actual committed volume (not projected). Offer framework pricing, not a flat rate. Escalate to Deal Desk. For the full GPO handling framework, see pricing-strategy skill.

## Canon References

- ICP building methodology (GAP method, customer interview pipeline)
- `references/spiced-icp-library.md` — SPICED language library with qualification tiers (T1/T2/T3) by customer cluster
- Positioning and messaging design (ICP to Positioning to Messaging chain)
- Discovery SPICED processing (call transcripts through SPICED framework)

---

## References

### Methodology Origins
- **MEDDIC**: Created by Dick Dunkel at PTC (1996). Jack Napoli and John McMahon key collaborators. Scaled PTC $300M→$1B. Source: meddicc.com.
- **Challenger**: Matthew Dixon & Brent Adamson, *The Challenger Sale*, CEB/Gartner, 2011.
- **SPIN**: Neil Rackham, *SPIN Selling*, 1988. Based on 35,000 sales call observations.
- **BANT**: IBM internal qualification framework, ~1960s.
- **Gap Selling**: Keenan, *Gap Selling*, 2018.

### Research-Backed Benchmarks
- **Multi-threading**: Gong: 4+ contacts = 58% win rate, 130% boost on deals >$50K. Ebsta 2023 B2B Sales Benchmarks: single-threaded ~8% win rate; 3+ contacts = 2.4× higher close rate.
- **Talk-to-listen ratio**: Gong (326K calls): discovery best performers talk 46%, listen 54%. Optimal target: 40:60 or better.
- **Framework selection by ACV**: 73% of >$100K ARR companies use MEDDIC (Saber/Eagr comparative research). Common pattern: MEDDIC for >$50K ACV, BANT for <$15K velocity deals.
- **Ebsta 2025 GTM Benchmarks** (655K opportunities, 2,000+ CROs): early decision-maker involvement boosts win rates by 55%; delayed deals reduce win rates by 113%; top performers close 11× faster than bottom.

> Built by [Neon Triforce](https://neontriforce.com)

---

## SPICED ↔ Impact Journey Cross-Reference

SPICED uncovers *why* a customer is buying. The Impact Journey maps *what happens after* they buy. They are connected at Mutual Commit.

| SPICED element | Maps to Impact Journey |
|---|---|
| **Situation** | Contextualises which Impact Journey stage the customer is starting from |
| **Pain** | The gap between their current Impact Journey stage and where they need to be |
| **Impact** | The specific business outcome they need — this becomes the Joint Impact Plan milestone |
| **Critical Event** | The deadline by which they must reach that Impact — anchors the CET (see Critical Event Timeline section in neon-discovery-spiced) |
| **Decision** | Mutual Commit — the moment the customer and Rutger formalise the Impact promise |

### Pre-Mutual Commit: SPICED qualifies readiness

During discovery, SPICED determines whether the customer can reach the Impact they need in the time their Critical Event requires. A customer with a Critical Event but missing data readiness (RED score) is a bad qualification — the CET cannot be met.

### Post-Mutual Commit: Impact Journey governs CS

Once SPICED closes to Mutual Commit, the Impact Journey takes over. The Joint Impact Plan (O3) documents the Impact target and CET milestones. CS owns delivery from here.

*Source: WbD Operating Model PDF, Chapter 08, pages 85-95, 143-148. Jacco van der Kooij, Revenue Architecture.*
