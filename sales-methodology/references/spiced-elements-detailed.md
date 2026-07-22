# SPICED Deep Dive: Element-by-Element

On-demand reference for the sales-methodology skill.

## Situation: Map Their Operating Model

The Situation element is where you prove you understand the customer's baseline. Don't move forward until you can draw their org chart, explain their tech stack, and articulate their growth constraints.

**What to uncover in discovery:**

- Team structure: How many GTM teams? (Marketing, SDR, AE, Expansion, CS, Enablement?) Who reports to whom? Is there a RevOps function?
- Growth stage: Series/ARR band, months in business, historical growth rate, current growth target
- Process maturity: Do they run standardized processes (sprints, OKRs, weekly cadence) or hero-led heroics?
- Current tooling: CRM, MA, data stack, call recording, enablement tooling. Are these used or legacy?
- Customer types: SMB, mid-market, enterprise? Product-led, sales-led, partner-led? Geographic spread?
- Constraints: Capital, headcount, market saturation, regulatory, competitive pressure?

**Scoring rubric for Situation:**

- **0 = Unknown:** Vague sense of what they do. No org chart, no process details.
- **1 = Identified:** You've talked to one contact. You have basic firmographics (company size, revenue, sector). But gaps remain: you don't know their org structure, tech stack details, or growth trajectory.
- **2 = Validated:** You've spoken to 2+ contacts (sales leader + practitioner). You have a clear picture of their GTM team, current process, and tooling. You can explain their growth stage and what's constraining them.
- **3 = Leveraged:** You understand their operating model deeply enough to position your solution against their current way of working. You can say: "You're doing X today, which works for Y, but breaks when Z happens. Here's how we'd change that."

**Example (T1; Perfect Fit):**
"They're a 30M ARR SaaS scale-up, 5 years old, selling mid-market finance teams across EMEA. 25-person sales org. Using HubSpot and Outreach. Running a blend of 60% sales-led new business, 40% inbound. Growth has plateaued at 25% YoY because their qualification process is gut-feel; reps are working low-quality pipeline."

---

## Pain: Quantify the Cost

Pain without numbers isn't pain. It's complaining. Your job is to translate vague dissatisfaction into a concrete cost.

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
- "Pipeline leaks at qualification stage" → 40 deals/quarter × 25% leak rate × $50K ACV = $500K/quarter lost
- "SDR:AE ratio is 1:4 but best-in-class is 1:8" → 4 extra SDRs × $120K fully-loaded = $480K/year cost
- "Forecast is off by 30%; each miss costs 2 exec days in forensics" → 4 quarters × 2 days × $1K/day = $8K/year + reputational cost
- "Sales cycle stretched from 90 to 120 days" → 30 extra days × 25 reps × $200/day pipeline drag = $150K opportunity cost

**Scoring rubric for Pain:**

- **0 = Unknown:** Haven't talked about what's broken.
- **1 = Identified:** They've mentioned a problem. "Our forecast is messy" or "reps aren't using CRM." But no quantification.
- **2 = Validated:** You've quantified the pain. "You're losing 30% of qualified opportunities because reps don't have a standard qualification method. That's roughly 12 deals/quarter × $80K ACV = $960K/year."
- **3 = Leveraged:** The customer is actively using this number in conversations internally. They reference the cost-of-inaction in their own justification for moving. You hear: "We need to close that $960K leak" instead of "maybe we should look at this."

**Example (T1; Perfect Fit):**
"Biggest pain: they have 15-person AE team closing ~$60M ARR. Forecast is consistently off by 25-30% month-to-month because reps have no qualification discipline. No standard definition of 'qualified deal.' One rep uses gut feel, another uses BANT, another just works everything in the pipeline. This creates: (1) wasted AE time on poor-fit deals; (2) CFO trust erosion; (3) inability to make confident hiring/resource decisions. Quantified: 20% of AE time (~$200K) wasted on deals that will never close. Plus monthly exec reconciliation meetings (~$3K/month × 12 = $36K/year)."

---

## Impact: Build the Vision

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
   - Organizational momentum: "This removes the biggest blocker to our 50% growth goal"
   - Cultural signal: "We're becoming a data-driven, not opinion-driven, sales org"

**Scoring rubric for Impact:**

- **0 = Unknown:** Haven't discussed outcomes or upside.
- **1 = Identified:** They've mentioned what success would look like. "We'd like forecast to be more accurate" or "better pipeline management." Vague, no numbers.
- **2 = Validated:** You've modeled the impact together. "If you reduce your disqualification cycle by 2 weeks and focus AE time on T1/T2 deals only, your revenue per rep goes from $4M to $5M. At 15 reps, that's $15M incremental ARR." They see the logic.
- **3 = Leveraged:** They're using this impact statement in internal conversations. You hear: "If we get forecast accuracy to ±10%, we can budget properly and hit our 50% growth plan. That's worth the investment."

**Example (T1; Perfect Fit):**
"If they implement SPICED: (1) AE time on low-quality pipeline drops 20%, freeing ~$200K capacity. Redeployed to net new, that's ~$4M incremental ARR. (2) Forecast accuracy improves from ±30% to ±10%, which allows predictable headcount planning and eliminates monthly exec firefighting ($36K/year saved in meeting time, credibility, morale). (3) Reps have clear disqualification rules, so they feel less guilt killing deals early and more ownership of the pipeline they keep. (4) Board and CFO trust the GTM story, which opens door to bigger markets/budgets."

---

## Critical Event: Find the Trigger

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

**Example (T1; Perfect Fit):**
"Critical event: they hired a new CRO in Q4 (just joined 3 weeks ago). CRO has mandated a 100-day GTM transformation plan with SPICED qualification as pillar 1. They need to show forecast accuracy improvement by April board call (12-week window). If they hit that, CRO gets cover for his broader org redesign and next-phase investments. If they miss, the GTM initiative gets deprioritized and CRO's credibility erodes. This drives tight timeline, executive air cover, and willingness to move fast on implementation."

---

## Decision: Map the Buying Committee and Process

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
  > Vendor sends capabilities overview
  > Champion shares with VP Sales team (2 people review)
  > Technical buyer lists requirements

Step 2: POC/Demo (3 weeks)
  > Vendor demos to 4-person evaluation committee
  > Feedback collected via form
  > Technical team gets access to sandbox

Step 3: Technical validation (2 weeks)
  > IT team evaluates: API docs, security, data residency, integration effort
  > Security team runs vendor risk assessment

Step 4: Commercial review (1 week)
  > CFO/Procurement gets proposal
  > Procurement checks contract terms (this is where most deals stall. They want standard terms; you might not offer them)
  > CFO checks ROI math

Step 5: Sign-off (1 week)
  > Economic buyer (VP Sales or CRO) approves
  > CFO or CEO cosigns (depending on ACV)
  > Legal negotiates final terms

Step 6: Signature + kickoff (final step)
  > Both parties sign
  > Implementation scheduled
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
- **3 = Leveraged:** You're actively managing the process. You have 1:1 conversations with each stakeholder aligned to their specific criteria. You're removing blockers proactively (e.g., "I know IT wants data residency in Germany; here's our data center docs"). You're coaching the champion on how to sell the economic buyer. You know the exact date signature happens.

**Example (T1; Perfect Fit):**
"Decision committee: (1) VP Sales (champion, wants rep adoption + proof of SPICED methodology). Met 3x; strong sponsor. (2) CRO (economic buyer, wants forecast accuracy ±10% + board visibility by May). Met 1x; needs 1:1 on ROI math. (3) Controller/CFO (evaluates ROI, contract terms, vendor risk). Has not met; this is the risk. (4) Head of IT/Security (integration + compliance). Met; confirmed no blockers; we pass security review. (5) Procurement (contract terms, vendor onboarding). Have standard agreement? Likely sticking point.

Process: vendor demo → technical eval (2 wks) → CFO review → legal negotiation → sign. Expected duration: 6 weeks from demo to signature IF no commercial surprises.

Next actions: (1) 1:1 with CRO to present ROI model and May timeline. (2) Make intro to Controller to pre-qualify commercial terms (discount limits, payment terms, data residency). (3) Send IT our security + API docs to shorten technical eval."
