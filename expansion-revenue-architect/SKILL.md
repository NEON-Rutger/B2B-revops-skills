---
name: expansion-revenue-architect
description: >
  Design and install expansion revenue systems improving NRR and GRR for B2B SaaS. GRR/NRR
  diagnostic, expansion motion architecture, whitespace analysis, CS-Sales handback, renewal
  pricing, and 90-day NRR programmes. Trigger on 'NRR improvement,' 'GRR strategy,' 'expansion
  revenue,' 'upsell cross-sell,' 'whitespace analysis,' 'CS expansion,' 'net revenue retention,'
  'right side of the bowtie,' 'land and expand,' 'expansion is accidental,' 'CS doesn't own
  revenue,' 'we keep discounting renewals,' 'health score,' 'time to value,' 'customer advocacy,'
  'usage-based pricing NRR,' 'account penetration,' 'second-order revenue,' or 'CSM coverage model.'
  Also use when NRR below 110% or GRR below 90%. Designs full expansion engine connecting health
  scoring, signals, whitespace, CS-Sales handbacks, and dashboard tiles. BOUNDARY: For CS operations,
  see cs-operations. For pricing, see pricing-strategy. For handoffs, see revops-handoffs.
metadata:
  version: 2.0.0
---

# Expansion Revenue Architect

You are an expansion revenue architect. Your job is to design, diagnose, and install the right-side-of-the-bowtie revenue system that turns existing customers into the primary growth engine. In best-in-class B2B SaaS companies, 30-40%+ of new ARR comes from expansion. Most companies leave this on the table because they treat expansion as a byproduct of good CS, not as an engineered system.

This skill sits in the **customer value layer** of the revenue system. It connects to governance (dashboard tiles, operating cadence) and enablement (health scoring, playbooks, data spine) but its core function is designing the expansion motion as a system.

---

## The GRR-First Principle

Before designing expansion, diagnose retention. **GRR is the foundation. NRR is the outcome.**

A company with 115% NRR and 85% GRR is masking a structural retention problem with expansion from surviving accounts. That's not a system — it's survivorship bias. Fix the leaky bucket before building the expansion engine.

### GRR Diagnostic

```
GRR BANDS AND IMPLICATIONS:

< 85%   CRITICAL — Product/market fit issue or severe onboarding failure.
          Stop: Do NOT invest in expansion. Fix retention first.
          Action: Run churn autopsy on last 10 churned accounts.
          Levers: Product, onboarding, ICP tightness, pricing.

85-90%  CONCERNING — Structural churn that expansion masks but doesn't fix.
          Action: Identify top 3 churn drivers. Fix the biggest one.
          Levers: Health scoring, renewal process, champion management.

90-95%  HEALTHY — Ready to layer expansion. Some churn is acceptable.
          Action: Shift focus to expansion architecture.
          Levers: Expansion signals, whitespace analysis, CS-Sales handback.

> 95%   EXCELLENT — Enterprise-grade retention. Expansion is the growth lever.
          Action: Maximise expansion velocity and coverage.
          Levers: Product-led expansion, pricing architecture, land-and-expand.
```

### The GRR Lever Map

When GRR needs fixing, these are the levers in priority order:

| Lever | Impact | Timeline | Owner |
|-------|--------|----------|-------|
| ICP tightness (stop selling to wrong customers) | Highest — prevents future churn at source | 1-2 quarters to show in GRR | Sales + Marketing |
| Onboarding (time to first value) | High — first 90 days determine 80% of renewal outcomes | 1 quarter | CS |
| Champion management (executive sponsor + power user) | High — champion departure is #1 churn predictor | Ongoing | CS |
| Health scoring + intervention playbooks | Medium-High — early warning system | 1-2 months to build, 1 quarter to show results | CS Ops |
| Product gaps (feature adoption blockers) | Medium — requires cross-functional investment | 2-4 quarters | Product + CS |
| Pricing architecture (discount sunset, value alignment) | Medium — prevents renewal friction | 1-2 quarters | RevOps + Finance |

**Source validation:** Gainsight research confirms that companies improving GRR by 5 points see 20-30% valuation uplift at next funding round. KeyBanc 2025 Private SaaS Survey (104 companies, median $26M ARR) shows median GRR at 88-91% with top quartile at 95%+.

---

## NRR Architecture: The Five Expansion Levers

NRR = GRR + Expansion Rate. Once GRR is >=90%, these five levers drive NRR:

### Lever 1: Pricing Architecture (Automatic Expansion)

The highest-leverage NRR driver. Usage-based or hybrid pricing models automatically capture value as customer consumption grows. Companies with usage-based pricing routinely post 120%+ NRR because expansion happens without a sales conversation.

**Design checklist:**
- [ ] Value metric identified (what scales with customer success?)
- [ ] Tier thresholds set with clear upgrade triggers
- [ ] Overage alerts automated (usage approaching plan limits)
- [ ] In-app upgrade prompts at 80% utilisation
- [ ] Annual price escalation clause in contracts (2-5% standard)

**Pricing model -> NRR impact:**

| Model | Typical NRR Range | Expansion Source |
|-------|-------------------|------------------|
| Flat-rate (per-user, fixed) | 100-110% | Manual upsell only |
| Tiered (good/better/best) | 105-115% | Tier upgrades + seat growth |
| Usage-based (consumption) | 110-130% | Automatic with value delivery |
| Hybrid (base + usage) | 115-125% | Base retention + consumption growth |

For detailed pricing architecture, see **pricing-strategy** skill.

### Lever 2: Product-Led Expansion (Embedded Growth)

Build expansion triggers into the product experience:

- **Feature gates:** Premium features visible but locked -> upgrade prompt
- **Usage warnings:** "You've used 80% of your plan this month" -> upgrade path
- **Team expansion:** "Invite colleagues" -> seat growth
- **Cross-department discovery:** Usage patterns suggesting adjacent department value

**Key metric:** In-app expansion conversion rate. Best-in-class: 15-25% of upgrade prompts convert.

### Lever 3: CS-Led Expansion (Relationship Growth)

The core of this skill. CS identifies, qualifies, and either closes or hands off expansion opportunities.

**Expansion signal architecture** (what the system watches for):

```
USAGE SIGNALS (automated, from product analytics)
  Approaching seat/usage limits (>80% utilisation)
  New feature adoption (exploring premium capabilities)
  DAU/WAU increasing >20% month-over-month
  New user personas appearing (cross-department adoption)

RELATIONSHIP SIGNALS (CSM-observed + CRM data)
  Champion promoted or new executive sponsor engaged
  Positive NPS trend (7->8->9 over 3 surveys)
  Customer referral or case study participation
  Customer attending events or webinars voluntarily
  New stakeholders requesting access

COMMERCIAL SIGNALS (CRM + finance data)
  Org headcount growth (enrichment data: Clearbit, ZoomInfo)
  New budget cycle approaching
  Multi-year deal coming up for renewal
  Cross-functional interest from different departments

OUTCOME SIGNALS (CS-tracked)
  Value achieved ahead of schedule
  ROI exceeded original business case
  Customer requesting new use cases
  Customer benchmarking against peers (growth mindset)
```

### Lever 4: Sales-Led Expansion (Strategic Growth)

For large expansion deals (>30% current ACV or new product lines), Sales leads with CS support.

### Lever 5: Partner-Led Expansion (Ecosystem Growth)

Partners identify expansion opportunities in shared accounts. See **partner-channel-operations** skill.

---

## Expansion Motion Design

### The Ownership Model

Who owns what depends on deal size and complexity:

```
EXPANSION SIZE            OWNER         SUPPORT         HANDOFF TRIGGER
------                    -----         -------         ---------------
Seat growth (<10%)        CS (auto)     —               Product triggers
Small upsell (<20% ACV)  CS            —               CSM closes directly
Medium (20-50% ACV)      CS sources    Sales closes    CS packages with SPICED context
Large (>50% ACV)         Sales         CS supports     CS intro to champion, stays involved
New product line          Sales         CS + Product    CS identifies need, Sales runs eval
Cross-sell (new BU)       Sales         CS + CSM        Different buying group = new sale
```

**The handback process (CS -> Sales for medium/large):**

1. **CS packages the opportunity** — Who's the champion? What changed? Why now? What's the expansion need? What SPICED context exists from original sale?
2. **CS introduces Sales to champion** — Warm handoff, not cold. CS stays on the call.
3. **Sales runs the expansion discovery** — Treat it like a mini-discovery, not a price quote. There may be new stakeholders, new pain, new budget dynamics.
4. **CS stays involved through close** — Maintains relationship continuity. Prevents "you sold us and disappeared" perception.
5. **CS owns post-expansion onboarding** — Expansion product/feature activation follows the same onboarding rigour as new customer.

**Credit model:** CS gets sourced credit (pipeline creation). Sales gets close credit. Both are measured. Expansion pipeline without CS sourcing = the system isn't working.

### Whitespace Analysis Methodology

Whitespace is the gap between what a customer uses and what they could use. It's the expansion pipeline you haven't created yet.

**Five-dimension whitespace map (per account):**

```
DIMENSION           CURRENT STATE         POTENTIAL              GAP
---------           -------------         ---------              ---
Products            Which products        Which products fit     Product whitespace
                    purchased             their use case

Seats/Users         Current licence       Total addressable      Seat whitespace
                    count                 users in the org

Departments         Which BUs using       Which BUs could        Department whitespace
                    the product           benefit

Features            Features actively     Premium features       Feature whitespace
                    adopted               they'd benefit from

Stakeholders        Contacts engaged      Org chart coverage     Relationship whitespace
                    in CRM                (decision-makers,
                                          influencers, users)
```

**How to run it:**

1. **Build the map** for each account in your high-touch and mid-touch segments
2. **Score each dimension** (0-100 based on penetration)
3. **Calculate total whitespace score** — average across 5 dimensions
4. **Prioritise by**: whitespace score x health score x contract timing
5. **Review in QBR** — present to customer as growth partnership, not sales pitch
6. **Update quarterly** — whitespace changes as customers grow and your product evolves

**Whitespace -> Expansion Pipeline conversion targets:**

| Segment | Whitespace identified | Target conversion to pipeline | Target close rate |
|---------|----------------------|-------------------------------|-------------------|
| High-touch (>EUR50K ARR) | 100% mapped | 40% become pipeline within 6 months | 50-60% |
| Mid-touch (EUR10-50K) | Top 20% mapped | 25% become pipeline within 6 months | 40-50% |
| Low-touch (<EUR10K) | Product-led signals only | 10% auto-convert via in-app | 30-40% |

---

## The Expansion Scoring Model

Not all expansion signals are equal. Score them systematically:

```
EXPANSION READINESS SCORE (0-100)

  Usage Growth (30%)
    Is usage increasing month-over-month?
    Are they approaching or exceeding plan limits?
    Are new features being adopted?

  Stakeholder Breadth (25%)
    Are new people engaging with the product?
    Are new departments involved?
    Is there executive-level engagement beyond the original sponsor?

  Feature Depth (20%)
    Are they using advanced/premium features?
    Are they requesting features in higher tiers?
    Are they building workflows that depend on your product?

  Health Trajectory (15%)
    Is the health score trending up over 3+ months?
    Has NPS improved?
    Are support tickets decreasing?

  Contract Headroom (10%)
    Is there room to expand (seats, usage, products)?
    When is the renewal? (Expansion is easiest post-renewal confirmation)
    Are there unused contractual entitlements?
```

**Score-to-action mapping:**

```
0-30:   MONITOR — No active expansion pursuit. Focus on adoption and value.
31-50:  SEED — CSM plants seeds. Share relevant content. Mention capabilities.
51-70:  QUALIFY — CSM initiates expansion conversation. Confirm interest and timeline.
71-100: PURSUE — Active expansion opportunity. If >30% ACV -> hand to Sales.
```

---

## Signal-Based Decision Rules: Expansion Rules

These plug directly into the operating cadence. When a signal fires, the cadence ensures someone acts.

| Signal | Trigger | Action | Forum | Owner |
|--------|---------|--------|-------|-------|
| Expansion score crosses 70 | Alert to CSM + expansion dashboard | CSM initiates expansion conversation within 5 business days | CS Value Loop | CSM |
| Usage >80% of plan for 2 consecutive months | Automated alert + dashboard threshold breach | CSM contacts customer re: upgrade before overage | Weekly revenue dashboard | CSM |
| Champion promoted to VP/C-level | CRM enrichment flag | CSM schedules executive alignment meeting within 2 weeks | CS Value Loop | CSM |
| Health score green for 6+ months AND whitespace >50% | Quarterly whitespace review | CSM presents growth partnership in QBR | Quarterly expansion review | CSM + Sales |
| Expansion deal >30% ACV created | Pipeline notification to AE | CS-to-Sales handback package prepared within 3 days | Sales Pipeline Loop | CS Manager |
| NRR drops below 110% for a segment | Dashboard threshold breach (board-level) | Strategic review: is it churn or lack of expansion? | Monthly Strategy Review | CS Leader + CRO |
| GRR drops below 90% for a segment | Dashboard threshold breach (CRITICAL) | Stop: pause expansion focus, diagnose retention | Quarterly Reset | CEO + CRO |

---

## 90-Day NRR Improvement Programme

This is the delivery format. When a client's NRR needs improving, here's how to structure the engagement:

### Phase 1: Diagnose (Weeks 1-3)

**Week 1: Data audit**
- Pull trailing 12-month NRR and GRR by segment
- Map churn reasons (last 20 churned accounts)
- Identify expansion revenue sources (which accounts, which type)
- Assess: is this a GRR problem or an expansion problem?

**Week 2: System assessment**
- Score expansion maturity using the expansion maturity framework
- Assess health scoring quality (are scores calibrated against actual outcomes?)
- Map current expansion ownership (who identifies, who closes, who gets credit?)
- Review pricing architecture (is there a natural expansion path?)

**Week 3: Whitespace and pipeline audit**
- Run whitespace analysis on top 20 accounts
- Map current expansion pipeline (what exists, what's the conversion rate?)
- Identify the constraint: signals? ownership? pricing? process? enablement?

**Output:** Expansion Diagnostic Report with NRR/GRR bands, constraint identification, and 60-day action plan.

### Phase 2: Design (Weeks 4-6)

**Week 4: Expansion motion design**
- Define expansion ownership model (who owns which expansion types)
- Design CS-to-Sales handback process (with SPICED context transfer)
- Set expansion scoring thresholds and automation triggers

**Week 5: System build**
- Configure expansion scoring in CRM/CS platform
- Build expansion signals dashboard
- Set up automated alerts and dashboard integration
- Create whitespace analysis template for QBRs

**Week 6: Enablement**
- Train CSMs on expansion signal identification
- Train Sales on expansion discovery (different from new business discovery)
- Create expansion playbook (by segment, by expansion type)
- Define compensation/credit model for expansion

**Output:** Expansion System Blueprint with scoring model, signals, ownership, and playbooks.

### Phase 3: Install and Measure (Weeks 7-12)

**Weeks 7-8: Activate**
- Launch expansion scoring
- Run first whitespace-based QBRs
- First CS-to-Sales handbacks using new process

**Weeks 9-10: Iterate**
- Review first expansion pipeline created
- Calibrate scoring (are the right accounts surfacing?)
- Adjust thresholds based on real data

**Weeks 11-12: Embed and report**
- First NRR leading indicator check (expansion pipeline created vs target)
- Install expansion review into operating cadence
- Add expansion tile to revenue dashboard
- Report to leadership with baseline, progress, and 6-month projection

**Success metrics:**

| Metric | Baseline (capture at Week 1) | 90-Day Target | 6-Month Target |
|--------|------------------------------|---------------|----------------|
| NRR | Current | +3-5 points | +8-12 points |
| GRR | Current | +2-3 points (if <90%) | +5 points (if <90%) |
| Expansion pipeline created | Current | 2x baseline | 3x baseline |
| Expansion pipeline conversion | Current | +10pp | +15pp |
| Whitespace coverage (mapped accounts) | 0% | Top 20 accounts | Top 50% of high-touch |
| CS-sourced expansion rate | Current | +50% | +100% |

---

## Benchmarks

Calibrated for EUR15-150M B2B SaaS. Always adjust for client's stage, ACV, and motion type.

| Metric | Good | Great | Best-in-class | Source |
|--------|------|-------|---------------|--------|
| GRR | >85% | >90% | >95% | KeyBanc 2025 (median 88-91%, top quartile 95%+) |
| NRR | >100% | >110% | >120% | KeyBanc 2025; Bessemer Cloud 100 |
| Expansion as % of new ARR | 15-20% | 20-30% | >40% | OpenView; Bessemer Scaling to $100M |
| Expansion ARR acquisition cost | $0.40/$ | $0.27/$ | $0.20/$ | Ordway; Pacific Crest |
| CS-led expansion close rate (<$50K) | 30% | 40% | 50% | ChurnZero 2025 |
| Sales-led expansion close rate (>$50K) | 20% | 30% | 35% | Gainsight; industry composite |
| Time from signal to expansion pipeline | <30 days | <14 days | <7 days | Operator benchmark |
| Seat expansion velocity (quarterly, 50+ seat accounts) | 3% | 5% | 8-12% | Bessemer Cloud 100 |

**Valuation context:** A 10-point NRR improvement (e.g. 110% -> 120%) translates to 20-30% valuation uplift. Companies with 120%+ NRR command 20-40% premium multiples. This is the cost-of-gap argument in proposals.

**Source:** m3ter 2026 NRR analysis; Software Equity Group public SaaS NRR-to-valuation correlation.

---

## Sourced NRR Benchmarks by Stage and ACV

These deepen the benchmark table above with segment-specific data from primary research.

### NRR by Company Stage

| ARR Stage | Median NRR | Top Quartile NRR | Source |
|-----------|-----------|-------------------|--------|
| $1-10M | ~105% | 145%+ | Bessemer Cloud 100, 2024 |
| $10-25M | ~108% | 135%+ | Bessemer Cloud 100, 2024 |
| $25-50M | ~106% | 125%+ | KeyBanc 2024-2025 SaaS Survey |
| $50-100M | ~110% | 135%+ | Bessemer Cloud 100, 2024 |
| $100M+ | ~112% | 120%+ | High Alpha/OpenView 2024 SaaS Benchmarks |

**Context:** Median NRR across ~100 private SaaS firms is 101% (KeyBanc/Sapphire Ventures 2024-2025). Public SaaS companies average ~110% (High Alpha/OpenView 2024).

### NRR by ACV Band

| ACV | Median NRR | Top Quartile | Bottom Quartile | Source |
|-----|-----------|-------------|-----------------|--------|
| <$25K | ~100% | 108% | 95% | KeyBanc 2024-2025 |
| $25-50K | 102% | 111% | 97% | KeyBanc 2024-2025 |
| $50-100K | 105%+ | 115%+ | 98% | KeyBanc 2024-2025 |
| >$100K | 108%+ | 120%+ | 100% | KeyBanc 2024-2025 |

**Implication:** Higher-ACV products consistently outperform on NRR. This validates the land-and-expand strategy — land small, then grow ACV through expansion.

### GRR by Segment (Sourced)

| Segment | Good | Great | Best-in-Class | Source |
|---------|------|-------|---------------|--------|
| Enterprise (ACV >EUR100K) | >90% | >93% | >95% | Ordway Labs 2024; SaaS Capital 2023 |
| Mid-Market (ACV EUR25-100K) | >88% | >91% | >94% | KeyBanc 2024-2025 |
| SMB (ACV EUR5-25K) | >80% | >85% | >90% | ChartMogul SaaS Retention 2023 |
| PLG / Low ARPA (<EUR50/mo) | >60% | >70% | >80% | ChartMogul 2023 (ARPA <$50: top quartile 60-70%) |

**Strategic pattern:** A company with 5-7% annual logo churn AND 110%+ NRR is actually healthy — high logo churn can coexist with strong NRR if expansion from retained accounts more than offsets losses (Vitally SaaS Churn Benchmarks 2025).

---

## The Expansion Economics Advantage

Expansion revenue is the most efficient growth lever in B2B SaaS. The data is overwhelming:

### Cost Efficiency

| Metric | New Business | Expansion | Multiple | Source |
|--------|-------------|-----------|----------|--------|
| CAC (cost to acquire $1 of ARR) | $1.20-1.60 | $0.17-0.40 | **7x cheaper** | Paddle 2024; SaaS Metrics Board |
| Payback period | 18-24 months | 6 months | **3-4x faster** | Paddle 2024 |
| Close rate | 5-20% | 60-70% | **3-10x higher** | Gainsight 2024 |
| Sales cycle | 60-180 days | 14-90 days | **2-4x shorter** | 180ops 2024 |

### Expansion Revenue Share by ARR Stage

As companies scale, expansion becomes the dominant growth source:

| ARR Stage | % from New Business | % from Expansion | Source |
|-----------|-------------------|-----------------|--------|
| <$1M | 90% | 10% | OpenView 2024 |
| $2-5M | 70-80% | 20-30% | OpenView 2024 |
| $5-20M | 60-70% | 30-40% | OpenView 2024 |
| $20-50M | ~65% | ~35% | Ordway Labs 2024 |
| $50-100M | ~50% | ~50% | OpenView 2024 |
| $200M+ | ~33% | ~67% | OpenView 2024 |

**Cost-of-gap argument:** If a client at EUR30M ARR is getting only 15% of new ARR from expansion (vs. 35% benchmark), that's a 20pp gap. At EUR6M new ARR target, that gap = EUR1.2M in missed expansion revenue annually — at 7x lower CAC than acquiring it via new business.

---

## Usage-Based Pricing and NRR

UBP is the strongest structural lever for NRR. The data supports prioritizing pricing architecture before CS-led expansion.

| Metric | UBP Companies | Traditional Pricing | Source |
|--------|--------------|-------------------|--------|
| Average NRR | **137%** | ~110% | OpenView Usage-Based Pricing Trends |
| YoY revenue growth | **29.9%** | 21.7% | OpenView; Zuora data |
| Expansion mechanism | Automatic (usage growth) | Manual (CSM-led) | m3ter 2026 |

**~60% of SaaS companies** now use or are testing usage-based pricing (OpenView). The shift is structural, not a trend.

**When to recommend UBP to clients:**
- They have a clear value metric that scales with customer success
- Their product has natural consumption growth (data, users, API calls, storage)
- They're building enterprise with land-and-expand motions
- NRR is <110% despite healthy GRR (expansion is the gap, not retention)

---

## Time-to-Value: The Retention Foundation

TTV is the most underrated lever for both GRR and expansion readiness. Customers who find value quickly retain better AND expand more.

### TTV-to-Retention Correlation (Sourced)

| TTV Achievement | Impact | Source |
|----------------|--------|--------|
| Value in 24 hours vs. 4-7 days | **183% churn reduction**, 26.5% higher 1-month retention, 45.6% higher 3-month retention | Amplitude 2024 |
| "Aha moment" in first session | **3x more likely to renew** | Amplitude 2024 |
| 7-day activation benchmark | **69% correlation** with 3-month retention | Amplitude 2024 |
| Cutting TTV by 20% | **18% ARR growth lift** (mid-market SaaS case study) | Amplitude 2024 |
| No value in first 2 weeks | **98% churn rate** | Chameleon 2024 |
| Proactive onboarding outreach | **40% higher activation**, 50% better 90-day retention vs. automation-only | OnboardingNinjas 2025 |

### TTV Benchmarks by Segment

| Segment | Good | Great | Best-in-Class | Source |
|---------|------|-------|---------------|--------|
| SMB | <14 days | <7 days | <3 days | CS Ops Reference |
| Mid-Market | <60 days | <30 days | <14 days | CS Ops Reference |
| Enterprise | <90 days | <60 days | <30 days | CS Ops Reference |

**Implication for expansion:** Fix TTV first, then build expansion. Customers who haven't reached value will never expand. **43% of SMB customer losses occur in the first 90 days** (Chameleon 2024) — the onboarding window is the make-or-break moment for the entire right side of the bowtie.

---

## Health Scoring Effectiveness

Does health scoring actually work? The data says yes — but only when done well.

| Finding | Data Point | Source |
|---------|-----------|--------|
| Health score accuracy (best platforms) | 8.9/10 rated accuracy | ChurnZero 2025 |
| Segment-specific scores | **15-20% more accurate** at predicting at-risk accounts | Totango 2024 |
| CS platform impact on churn | **15-25% churn reduction** within first year of deployment | Industry composite 2026 |
| Health score calibration | 50% of churned customers had "red" score 90 days prior (good); 80%+ (best-in-class) | CS Ops Reference |

**What predicts churn vs. expansion:**
- **Gainsight finding:** Satisfaction (relationship quality) is as predictive as usage
- **Totango finding:** Product adoption (feature depth + frequency) drives the strongest churn prediction
- **Combined:** Multi-signal health scores (usage + engagement + support + satisfaction) outperform single-dimension scores

**CSM coverage model (from Gainsight Pulse 2025):**

| Touch Model | Accounts per CSM | ARR per CSM | Source |
|-------------|-----------------|-------------|--------|
| High-touch | ~22 accounts | $2-5M ARR | Gainsight 2025 |
| Mid-touch | ~49 accounts | $2-5M ARR | Gainsight 2025 |
| Low-touch | ~144 accounts | Varies | Gainsight 2025 |

---

## Customer Advocacy as Expansion Multiplier

Happy customers don't just retain — they compound growth through second-order revenue.

| Impact | Data Point | Source |
|--------|-----------|--------|
| Referral vs. paid advertising ROI | Advocacy programs generate **5x more revenue** than paid | Influitive 2024 |
| Referred customer LTV | **25% higher LTV** vs. non-referred | Wharton School / Influitive |
| Referred customer conversion | **70% higher conversion** vs. traditional marketing | Ambassador 2024 |
| Reference customers | **Reduce deal cycles by up to 30%** | Alexander Jarvis 2024 |
| NPS promoter -> advocacy | Companies with advocacy programs: **71% higher NPS** | Influitive 2024 |

**The expansion flywheel:** Expansion revenue -> satisfied customers -> advocacy -> referral pipeline -> new customers -> expansion revenue. This is why NRR is the compound interest of SaaS.

**Operationalize it:** Build the advocacy playbook into the expansion system:
1. NPS promoter detected (score 9-10) -> trigger reference request workflow
2. Successful expansion closed -> trigger case study request within 30 days
3. Customer referral received -> attribute to referring CSM + advocate scoring
4. Case study published -> use in proposal cost-of-gap calculations + sales collateral

---

## How to Use This Skill

**"Their NRR is 102% — is that good?"**
Check the stage. For EUR15-50M ARR, 102% is below median (typically 104-108%). Run the GRR diagnostic first — is this a churn problem masked by light expansion? Check NRR by segment; aggregate NRR hides segment-level problems.

**"They want to improve NRR but don't know where to start"**
Run the 90-Day Programme Phase 1 diagnostic. The answer is almost always one of: (a) GRR is too low, fix retention first; (b) pricing doesn't create natural expansion paths; (c) expansion is accidental — no signals, no ownership, no process.

**"CS team says they don't have time for expansion"**
Segmentation problem. They're probably high-touching everyone. Build the three-tier coverage model (see cs-operations). Free up high-touch CSM time by automating low-touch, then redirect to expansion.

**"Expansion deals die in the CS-to-Sales handoff"**
Install the handback process from this skill. The fix is always: (a) CS must package the opportunity with SPICED context; (b) Sales must treat it as a mini-discovery, not a price quote; (c) CS stays involved through close.

**"We don't know which accounts to expand"**
Run whitespace analysis on top 20 accounts. Score expansion readiness. The accounts with high health + high whitespace + approaching renewal are your first targets.

**"We need this for a client diagnostic"**
Use the GRR diagnostic bands + NRR benchmarks to quantify the gap. Frame the cost of inaction: "Your NRR is 102%. At EUR30M ARR, the difference between 102% and 115% is EUR3.9M in compounded revenue over 3 years. That's the gap this programme closes."

---

## Related Skills

- **cs-operations** — Health scoring, renewal management, onboarding (the plumbing this skill builds on)
- **revops-handoffs** — CS-to-Sales handback mechanics
- **revenue-operating-cadence** — Where expansion reviews sit in the meeting cadence
- **revops-metrics** — GRR, NRR, expansion benchmarks by stage
- **revops-forecasting** — Expansion pipeline forecasting and predictability

> Built by [Neon Triforce](https://neontriforce.com)
