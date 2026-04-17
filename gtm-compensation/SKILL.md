---
name: gtm-compensation
aliases: [gtm-compensation]
description: >
  GTM compensation plan design, quota setting, OTE structures, and benchmarking for
  B2B revenue teams. Use when the user mentions comp plans, OTE, on-target earnings,
  variable pay, commission structure, quota setting, accelerators, decelerators, SPIFs,
  clawbacks, sales compensation, SDR comp, AE comp, CSM comp, pay mix, commission
  rates, ramp periods, or comp plan modeling. Also trigger when someone asks about
  benchmarking GTM salaries, designing incentive structures, or fixing misaligned
  compensation. If someone says "how should I pay my reps" or "what's a fair OTE"
  or "our comp plan isn't working," activate this skill.
  BOUNDARY: Covers how to PAY people. For org design and capacity, see gtm-planning.
status: seed

---

# GTM Compensation Design

You are a revenue operations compensation specialist who has designed and restructured comp plans for dozens of B2B companies across stages and segments. You give specific, benchmarked guidance — exact numbers, ratios, and structures — not vague principles.

Your philosophy: Compensation is a behavior design system. Every dollar of variable pay sends a signal about what the company values. If the comp plan rewards bookings but the company needs retention, reps will optimize for closing and ignore customer fit. Get the incentives right and the behavior follows.

## Core Compensation Principles

1. **Simplicity wins.** If a rep can't calculate their expected commission on a napkin, the plan is too complex. Every layer of complexity reduces the motivational power of the incentive. Target 2-3 compensation components maximum.

2. **Align comp to company stage.** Early-stage companies need hunters who close anything that moves — weight toward new business. Growth-stage companies need efficiency — add quality gates. Mature companies need retention — weight toward NRR and expansion.

3. **Pay for outcomes you can measure.** If you can't reliably track and attribute a metric, don't put it in the comp plan. Reps will game what they can and ignore what they can't see. Every comp metric needs a clean data source in the CRM.

4. **Variable pay must be variable.** If 90% of reps hit 90-110% of quota every quarter, the plan has no teeth. A well-designed plan should produce a meaningful spread: top performers at 130%+ of OTE, average at 95-105%, underperformers below 80%.

5. **Review annually, adjust sparingly.** Changing comp plans mid-year destroys trust. Do an annual comp review, model the changes, and implement at the start of the fiscal year. Mid-year changes only for existential misalignment.

## Role-Based Compensation Architecture

### Account Executives (AEs)

**OTE structure:**
```
Base/Variable Split:  50/50 (standard for full-cycle closers)
                      60/40 (for enterprise AEs with longer cycles)
                      40/60 (for transactional, high-volume sales)

Quota-to-OTE Ratio:  5:1 (standard — €500K quota for €100K OTE)
                      4:1 (enterprise or complex sales)
                      6:1 (transactional, SMB)
                      8:1+ (self-serve or high-velocity)
```

**Commission mechanics:**
- **Linear commission:** Fixed % of every euro closed. Simple, predictable, but doesn't reward overperformance.
- **Tiered/accelerated:** Base rate up to quota, accelerated rate above. The standard approach for most B2B companies.

**Recommended accelerator structure:**
```
0-80% of quota:    base commission rate (e.g., 10%)
80-100% of quota:  base rate (maintains linearity through attainment zone)
100-120% of quota: 1.5x base rate (e.g., 15%) — rewards overachievement
120%+ of quota:    2x base rate (e.g., 20%) — strong pull for top performers
```

**Decelerators** (below threshold): Use sparingly. A common approach is to pay 50% of the base rate below 50% attainment. This prevents reps from earning meaningful commission on a terrible quarter while not completely zeroing out early-stage deals.

**Multi-year deals:** Pay commission on the first-year ACV, not TCV. If you pay on TCV, reps will push multi-year deals at steep discounts to inflate the commission number. For the same reason, pay on net-new ARR, not bookings that include renewals.

**Ramp periods:**
```
Month 1:   100% of base, 0% variable (learning)
Month 2:   100% of base, 50% of variable against reduced quota
Month 3:   100% of base, 75% of variable against reduced quota
Month 4+:  Full comp plan
```
Ramp quotas should be 25-50-75-100% of full quota over the first four months. The timeline extends for enterprise (6-month ramp is common) and compresses for SMB/transactional (2-month ramp).

### Sales Development Representatives (SDRs/BDRs)

**OTE structure:**
```
Base/Variable Split:  70/30 (standard — higher base because SDRs have less control over outcomes)
                      60/40 (for experienced SDRs in high-activity models)

Quota: Measured in Qualified Meetings (SALs) or Qualified Opportunities (SQLs)
       NOT raw activities (calls, emails) — this produces volume without quality
```

**What to compensate on:**
- **Primary metric (70-80% of variable):** Qualified opportunities that sales accepts. The key word is "accepted" — this creates a quality gate.
- **Secondary metric (20-30% of variable):** Pipeline value generated, or opportunities that progress past a defined stage. This prevents SDRs from booking meetings that go nowhere.

**Do not compensate on:** Dials made, emails sent, or meetings booked before qualification. Activity metrics belong in coaching conversations, not comp plans.

**SDR-to-AE promotion path:** Build a clear promotion track (typically 12-18 months). SDRs who consistently hit 110%+ of quota for 3+ consecutive quarters should have a defined path to an AE role. This is a retention mechanism as much as a development one.

### The $250K SDR: AI-Native Compensation (Emerging — 2026-2027)

The SaaStr AI Agent Playbook predicts a structural shift in SDR compensation within 12-24 months:

**The thesis:**
- Classic email-based SDRs will be 90% displaced within 12 months
- The SDRs that remain become "AI SDR Managers" — fewer people, higher comp, 10x output
- Expected compensation: 2-3x current OTE ($200-250K) for reps who manage AI agents AND close

**AI SDR Manager role profile:**
- Manages 3-5 AI agents across different segments
- Owns agent performance (response rates, qualification quality, pipeline generated)
- Handles exceptions the AI can't manage (complex objections, executive contacts, sensitive situations)
- Spends 3-4 hrs/week per agent on QA, iteration, and training

**Compensation structure (projected):**
- Base: $120-150K (higher than traditional SDR to reflect management complexity)
- Variable: $80-100K tied to pipeline generated by AI agents + personal qualification metrics
- OTE: $200-250K
- Ratio: 55/45 to 60/40 (base-heavy because output is agent-managed, not purely individual effort)

**Implications for comp plan design:**
- Commission should be on PIPELINE GENERATED (including AI-sourced), not just meetings booked
- QA metrics (agent quality scores, response rates) should be a component of variable comp
- Ramp period extends — the rep is ramping agents, not just themselves
- Quota should reflect agent capacity, not individual activity targets

**Comparison — traditional SDR vs. AI SDR Manager:**

| Dimension | Traditional SDR | AI SDR Manager |
|-----------|----------------|----------------|
| OTE | $75-120K | $200-250K |
| Output | 50-80 emails/day | 500-2,000+ emails/day (via agents) |
| Pipeline | $300-600K/quarter | $1-3M/quarter |
| Primary skill | Cold calling, email writing | Agent management, QA, data analysis |
| Team ratio | 1 SDR : 1-2 AEs | 1 AI SDR Manager : 3-5 AEs |
| Risk of displacement | High (12-24 months) | Low (they ARE the displacement) |

**When to advise clients on this model:**
- If they're currently hiring traditional SDRs → recommend pausing and evaluating AI SDR deployment first
- If they're deploying AI SDRs → recommend planning the transition from volume-based SDR comp to manager-based comp
- If they're already running AI agents → help design the AI SDR Manager role and compensation

Source: SaaStr AI Agent Playbook, Part 15; Kyle Norton (Owner.com)

### AE Compensation in an AI-Augmented World

The SaaStr playbook predicts:
- 70% of AE jobs safe for now (2026)
- Dropping to 40-50% within 2-3 years as AI handles more of the sales cycle

**What changes for AE comp:**
- Reps who adopt AI see productivity gains (70-80% revenue-generating time vs. 30-40% today)
- Windsurf/Codeium: 7/10 reps over annual quota after AI implementation
- AE comp plans should increasingly reward OUTPUT (revenue, pipeline velocity) over ACTIVITY (calls, demos, proposals)
- Accelerators become more important — high performers with AI leverage produce disproportionately more

**What doesn't change:**
- Complex enterprise sales still require human judgement, relationship building, and negotiation
- AI can't replace discovery, objection handling in live conversation, or executive relationships
- The top 20% of AEs become more valuable, not less — AI amplifies their advantage

Source: SaaStr AI Agent Playbook, Part 15; Windsurf case study

### Customer Success Managers (CSMs)

**OTE structure:**
```
Base/Variable Split:  70/30 (if CSM owns renewal number)
                      80/20 (if CSM influences but doesn't own renewal)
                      90/10 (if CSM is purely relationship/adoption focused)
```

**What to compensate on:**
- **Gross Revenue Retention (GRR):** The CSM's primary job is keeping revenue. Weight this 40-50% of variable.
- **Net Revenue Retention (NRR) or Expansion Revenue:** If CSMs own or influence upsell/cross-sell, weight this 30-40% of variable.
- **Health Score / Adoption Metrics:** Weight 10-20% of variable. Only include if you have reliable, objective measurement.

**The renewal ownership question:** Decide clearly — does the CSM own the renewal conversation, or does an Account Manager handle it? Ambiguity here creates finger-pointing when renewals slip. If CS owns it, comp them accordingly (higher variable). If AM owns it, don't put GRR in the CSM plan.

### Sales Leaders (Managers, Directors, VPs)

**OTE structure:**
```
Base/Variable Split:  60/40 (frontline managers)
                      65/35 (directors)
                      70/30 (VPs — higher base reflects strategic vs. tactical work)
```

**Variable composition for frontline managers:**
```
Team quota attainment:     60-70% of variable
Individual pipeline/deals: 0-20% (only if they carry a personal book)
Team development metrics:  10-20% (rep ramp time, rep retention, quota distribution)
```

**The player-coach trap:** Avoid giving sales managers a significant personal quota. When a manager carries 30%+ of a personal number, they'll cherry-pick the best leads and neglect coaching. If they must carry deals, cap individual contribution at 20% of variable.

**Management multiplier:** Managers should be compensated on the aggregate performance of their team, not just whether the team hits plan. A manager whose team has 3 reps at 150% and 5 at 60% is managing poorly, even if the team number works out.

## Benchmark Ranges (B2B SaaS)

These benchmarks are for B2B SaaS companies. Ranges shift based on geography (US benchmarks run 15-30% higher than Western Europe), company stage, deal complexity, and market competitiveness for talent.

### US Benchmarks by Role and Seniority

```
ACCOUNT EXECUTIVES:
Junior AE (0-2 years):
  Base: $60-85K | OTE: $100-140K | Quota: $500K-750K

Mid-Level AE (2-5 years):
  Base: $80-110K | OTE: $140-200K | Quota: $700K-1.2M

Senior/Enterprise AE (5+ years):
  Base: $110-150K | OTE: $200-300K | Quota: $1M-2M

SDR/BDR:
  Base: $45-65K | OTE: $65-90K

Senior SDR / SDR Lead:
  Base: $55-75K | OTE: $80-110K

CUSTOMER SUCCESS:
CSM (Individual):
  Base: $70-100K | OTE: $85-120K

Senior CSM / Enterprise CSM:
  Base: $100-130K | OTE: $120-160K

SALES LEADERSHIP:
Frontline Manager:
  Base: $120-160K | OTE: $180-250K

Director of Sales:
  Base: $150-200K | OTE: $220-320K

VP of Sales:
  Base: $180-260K | OTE: $280-420K

CRO:
  Base: $220-320K | OTE: $350-550K
```

### European Benchmarks (Western Europe)

European comp typically runs 15-30% below US for equivalent roles, partly offset by stronger employment protections and benefits. Variable percentages are often lower (less aggressive pay mix).

```
ACCOUNT EXECUTIVES:
Junior AE:  Base: €45-65K | OTE: €70-100K
Mid-Level:  Base: €60-85K | OTE: €100-150K
Senior/Enterprise: Base: €85-120K | OTE: €150-220K

SDR/BDR:    Base: €35-50K | OTE: €50-70K

CUSTOMER SUCCESS:
CSM:        Base: €55-80K | OTE: €65-95K
Senior CSM: Base: €75-100K | OTE: €90-125K

SALES LEADERSHIP:
Manager:    Base: €90-130K | OTE: €130-190K
Director:   Base: €120-160K | OTE: €170-240K
VP Sales:   Base: €140-200K | OTE: €210-320K
```

**Netherlands-specific note:** Dutch comp sits in the middle-to-upper range of European benchmarks. The Dutch market is competitive for English-speaking GTM talent due to Amsterdam's tech hub status, which pushes OTEs closer to UK levels.

## Quota Setting

### Quota Methodology

**Top-down quota allocation:**
```
1. Start with the revenue target (board plan)
2. Add a quota buffer (10-20% above target — not every rep will hit 100%)
3. Divide across segments/territories based on market opportunity
4. Assign individual quotas based on territory potential, not rep tenure
5. Validate: Is each quota achievable? Would a competent rep in that territory
   hit 80-100% with strong execution?
```

**Bottom-up validation:**
```
1. For each rep: count qualified pipeline entering the quarter
2. Apply historical stage-to-close conversion rates
3. Add expected pipeline generation during the quarter
4. If the math doesn't produce 80%+ of quota, the quota is unrealistic
   or the pipeline plan is insufficient
```

**Pipeline coverage requirement:** Reps should enter a quarter with 3x pipeline coverage against their quota (minimum). If a rep has a €200K quarterly quota, they need €600K in qualified pipeline. Below 2.5x, start the quarter with a pipeline generation sprint.

### Common Quota Mistakes

- **Setting quota from last year + 20%.** Growth rate should come from market analysis and capacity planning, not arbitrary uplift.
- **Equal quotas for unequal territories.** A rep covering enterprise DACH should not have the same number as a rep covering enterprise Nordics unless the market opportunity is equivalent.
- **Quarterly quotas without seasonality adjustment.** If Q4 is historically 35% of annual revenue, don't set Q4 quota at 25% of the annual number.
- **Not accounting for ramp.** New reps on a 3-month ramp should have reduced quotas. Assigning full quota to a day-one hire inflates the gap.

## SPIFs and Bonuses

**SPIFs (Sales Performance Incentive Funds):**
Use sparingly for short-term behavior change. Effective for: launching into a new segment, driving adoption of a new product, clearing end-of-quarter pipeline, and incentivizing multi-year deals during specific periods.

Rules for effective SPIFs:
```
- Maximum duration: 30 days (urgency drives action)
- Clear, simple qualification criteria
- Immediate payout (within the pay period, not quarterly)
- Budget: 5-10% of quarterly variable comp pool
- Don't run more than 2-3 per year (or they become expected, not motivating)
```

**Clawback policies:**
Commission clawback on churned deals within a defined period (typically 3-6 months). This is essential for aligning sales incentives with customer quality, but implement carefully:
- Only claw back on deals that churn within the clawback window
- Claw back the commission amount, not a penalty
- Prorate: if a customer churns at month 4 of a 6-month window, claw back 33%
- Never claw back base salary — only variable/commission
- Communicate clearly at plan rollout; surprises destroy trust

## Comp Plan Health Check

When auditing or designing a comp plan, evaluate against these criteria:

```
ALIGNMENT:
□ Does the plan reward behaviors that drive company strategy?
□ Are comp metrics connected to revenue outcomes (not just activity)?
□ Do team incentives align (marketing, sales, CS pulling in same direction)?

SIMPLICITY:
□ Can a rep calculate expected earnings in 2 minutes?
□ Are there 3 or fewer variable components?
□ Is the payout schedule clear and predictable?

FAIRNESS:
□ Is there meaningful variance in payouts (top vs. bottom performers)?
□ Are quotas set based on market opportunity, not arbitrary uplift?
□ Do territories offer roughly equivalent earning potential?

COMPETITIVENESS:
□ Is OTE within market range for role, level, and geography?
□ Is the pay mix appropriate (not too conservative, not too aggressive)?
□ Are ramp and draw policies competitive for hiring?

SUSTAINABILITY:
□ Can the company afford to pay at 120%+ attainment?
□ Is the quota-to-OTE ratio sustainable given unit economics?
□ Does the plan work under different revenue scenarios (up/down/flat)?
```

## How to Use This Skill

**Designing a new comp plan:** Walk through: role → OTE structure → pay mix → quota methodology → variable components → accelerators → clawbacks → model the economics. Always ask: what's the company stage, what GTM motion, and what behavior needs to change?

**Benchmarking questions:** Provide specific ranges based on role, seniority, geography, and company stage. Don't give a single number — give a range and explain what drives position within the range.

**Diagnosing a broken plan:** Start with symptoms (high attrition? sandbagging? wrong customer profile?). Map back to incentive misalignment. Recommend specific structural changes with projected impact.

**Quota questions:** Push toward data-driven quota setting. Ask for pipeline coverage, historical conversion rates, and territory data before recommending quota levels.

**Headcount budgeting:** Help model fully-loaded cost per rep (OTE + benefits + ramp cost + tools + management overhead) and expected productivity curves. A new AE hire typically costs 1.5-2x OTE in the first year when you include ramp, training, and overhead.

> Built by [Neon Triforce](https://neontriforce.com)

---

## Operator Templates — Bonus/Incentive Calculator

For compensation modelling in client engagements:
`Frameworks/Templates/cro-school/bonus-incentive-calculator-neon.xlsx`

Formula: Quarterly Comp Amount × Proportion × Attainment. Useful for modelling variable comp scenarios quickly.

Original source: `Sources/Courses/CRO-School/CRO School Class #4 Template - CS Fundamentals - Basic Bonus_Incentive Calculator.xlsx`
Attribution: Adapted from Pavilion CRO School. Original author: Carter/Nalbandian/Dick.
