# WbD GTM Cost Model

*Reference file for gtm-planning, neon-benchmark-reference, neon-proposal-generator.*

---

## Section 1: Seven Cost Centres per GTM Motion

Every GTM motion runs seven cost centres. Cost intensity varies by motion type — the further right (higher touch), the heavier the human cost in Selection and post-sale stages.

| Cost Centre | No Touch | Low Touch | Medium Touch | High Touch | Dedicated |
|---|---|---|---|---|---|
| **Cost of Leaders** (Awareness) | Low — content + SEO, minimal human | Low-Medium — paid + content | Medium — field marketing, events | High — field sales, ABM, events | Very High — enterprise field, C-suite selling |
| **Cost of LeadDev** (Education) | Very Low — automated nurture | Low — SDR/BDR lite, sequences | Medium — SDR team, qualification | High — AE + SDR pairs, multi-thread | Very High — enterprise BDR, exec sponsors |
| **Cost of Selling** (Selection) | None / product-led | Low — inside sales, short cycle | Medium — mid-market AE, 30-60d cycle | High — enterprise AE, 60-180d cycle | Very High — dedicated AE + SA, 6-18 month cycle |
| **Order Processing** (Commit) | Very Low — automated contract + payment | Low — e-signature, minimal ops | Medium — RevOps deal desk | High — legal, procurement, deal desk | Very High — complex legal, multi-year negotiation |
| **Cost of Onboarding** | Very Low — self-serve, in-product | Low — CSM pooled, email-led | Medium — dedicated onboarding CSM | High — implementation team, project management | Very High — enterprise PS team, custom integration |
| **Cost of Retention** | Low — in-product health signals, automated | Low-Medium — pooled CSM, tech-touch | Medium — dedicated CSM, QBR cadence | High — strategic CSM, executive relationships | Very High — dedicated account team, CS + AE overlap |
| **Cost of Expansion** | Very Low — in-product upgrade, automated | Low — CSM-led, low touch | Medium — CS-to-Sales handoff | High — expansion AE + CSM joint play | Very High — dedicated expansion AE, enterprise account growth |

**Reading the table:** No Touch and Low Touch compress cost through automation and scale. High Touch and Dedicated compress cost through LTV — higher ACV justifies the spend. The danger zone is Medium Touch misapplied to Low ACV deals — the cost structure breaks unit economics.

---

## Section 2: Cost-to-Serve Benchmarks by ARR

Cost-to-serve = total GTM cost (all seven centres) ÷ ARR. Declines as the company scales through process maturity and automation.

| ARR Stage | Typical Cost-to-Serve Ratio | Notes |
|---|---|---|
| €1M | ~40% | Early-stage: founder-led, high experimentation cost |
| €5M | ~35% | Scaling: hiring into motion, cost not yet leveraged |
| €10M | ~30% | First leverage: playbooks forming, hiring more efficient |
| €25M | ~27% | Process maturity: predictable funnel, automation kicking in |
| €50M | ~25% | Operational efficiency: RevOps function in place |
| €100M | ~20% | Scale: strong automation, specialised roles, comp leverage |
| €200M+ | ~15% | Mature: significant automation, low marginal cost per new €ARR |

**Target range at scale:** 15–25%. Below 15% risks under-investment in retention and expansion. Above 30% at €25M+ signals a broken motion — investigate which cost centre is inflated relative to its contribution.

**Diagnostic use:** If a client's cost-to-serve is higher than benchmark for their ARR stage, the first question is always which cost centre is the outlier. Selling cost and onboarding cost are the most common culprits.

---

## Section 3: Durability Thresholds (GRR by Motion)

GRR (Gross Retention Rate) measures revenue retained from existing customers, net of downgrades and churn, before expansion. GRR is the floor of your NRR — you cannot have sustainable NRR without GRR health.

Target GRR varies by motion because the average customer relationship, switching cost, and product stickiness differ:

| GTM Motion | Target GRR | Rationale |
|---|---|---|
| No Touch | >80% | Self-serve products have higher churn velocity; acceptable at lower ACV |
| Low Touch | >85% | Light CS coverage requires strong in-product stickiness to compensate |
| Medium Touch | >90% | Dedicated CSM relationship justifies higher retention expectation |
| High Touch | >95% | Strategic relationship + deep integration = high switching cost |
| Dedicated | >98% | Enterprise contract + custom integration + exec relationship = near-permanent |

**Warning sign:** GRR below threshold by >3 points in any motion = structural retention problem, not a one-quarter anomaly. Trigger a churn root cause review.

**GRR vs NRR framing for clients:** "GRR is the foundation — you can't build NRR on a leaking bucket. If GRR is below threshold, fix retention before investing in expansion programmes."

---

## Section 4: Throughput Improvement Framework

Three levers exist to improve throughput (output per unit of GTM cost) in any motion. The right lever depends on the cost centre and the ARR stage.

### The Three Levers

**Streamline** — Remove steps, handoffs, and friction from the process. Reduces cost without technology investment. Best for: High Touch and Dedicated motions where process complexity has accumulated over time.

**Automate** — Replace human tasks with AI or tooling. Reduces marginal cost per deal/customer. Best for: No Touch, Low Touch, and Medium Touch motions where volume is high enough to justify tooling investment. Also applies to RevOps tasks (data entry, reporting, QBR prep) in all motions.

**Enhance** — Improve the skill level of the team. Increases output quality and conversion rates without reducing cost. Best for: High Touch and Dedicated motions where conversion rate and deal size are the primary levers. Also applies when ACV is high enough that a 5% conversion improvement outweighs a 20% cost reduction.

### Lever Prioritisation by Motion and Stage

| Motion | €1-10M ARR Priority | €10-50M ARR Priority | €50M+ ARR Priority |
|---|---|---|---|
| No Touch | Streamline (remove signup friction) | Automate (lifecycle, scoring, expansion triggers) | Automate + Streamline |
| Low Touch | Streamline (qualification, handoff) | Automate (SDR sequencing, CRM hygiene) | Automate + Enhance (CSM productivity) |
| Medium Touch | Enhance (AE skill, discovery quality) | Streamline + Automate (deal desk, onboarding) | All three in balance |
| High Touch | Enhance (enterprise selling, multi-threading) | Enhance + Streamline (complex deals) | Enhance + Automate (CS at scale) |
| Dedicated | Enhance (executive relationships) | Enhance + Streamline (account planning) | Enhance + Streamline |

**AI as Automate lever:** AI agents — call prep, pipeline risk, CRM hygiene, renewal alerts — are predominantly Automate lever plays. They apply across all motions but deliver highest ROI in Medium Touch (volume high enough, ACV high enough to justify the integration investment). See neon-ai-readiness-day for use case scoring.

---

*Source: WbD GTM Model and Revenue Architecture frameworks. Use with neon-benchmark-reference for stage-appropriate cost-to-serve targets.*
