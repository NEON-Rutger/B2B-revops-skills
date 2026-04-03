# Handoff SLAs, Benchmarks & Measurement

Complete SLA targets, research-backed benchmarks, metrics per handoff point, leading indicators of failure, and dashboard architecture for the full bow-tie model.

---

## 1. Speed-to-Lead Research

### Landmark Studies

**MIT/InsideSales.com (Dr. James Oldroyd, 2007; 15,000+ leads across 6 companies)**:
- 5-minute response: 21× more likely to qualify vs 30 minutes
- 100× more likely to make contact vs 30 minutes
- Optimal window: 1–5 minutes

**Velocify**: responding within 1 minute increases conversion by 391%.

**HBR (2,241 companies)**: average B2B response time is 42 hours. 23% of companies never responded at all.

**Workato (2024, 114 B2B companies tested)**: only 1 company sent personalised email within 5 minutes. Average personalised response: 11 hours 54 minutes. Companies using routing tools: 3 hours 32 minutes.

**Chili Piper (2025, 4M form submissions)**: instant booking converts 66.7% of qualified submissions to meetings vs ~30% industry average.

### Response SLA Framework by Lead Type

| Lead Source | Response SLA | Rationale |
|---|---|---|
| Demo requests / pricing page visits | < 5 minutes | Highest intent; actively comparing options |
| Paid advertising leads | < 3 minutes | Hottest, highest cost-per-lead |
| Partner referrals | < 30 minutes | Warm but relationship-dependent |
| Organic inbound (search) | < 10 minutes | Moderate intent |
| Content downloads / webinars | 3–4 days (nurture first) | Low-to-mid intent; premature outreach damages trust |
| Event / trade show leads | Same business day | Context fades quickly |

### Follow-Up Cadence

5–10 contact attempts yield 90% of lead value. Recommended pattern:
- Attempt 1: within SLA (call + email)
- Attempt 2: 4 hours later (different channel)
- Attempt 3: next business day
- Attempts 4–6: every 2 days
- Attempts 7–10: weekly

After 10 attempts with no response: return to marketing nurture with disposition noted.

---

## 2. Lead Scoring Benchmarks

### Conversion Rates

| Metric | Industry Average | Best-in-Class |
|---|---|---|
| MQL-to-SQL conversion | 15–21% | 39–40% (with behavioural scoring) |
| SQL-to-Opportunity | 50–60% | 70%+ |
| Lead scoring adoption | 44% of orgs | — |
| ML scoring vs manual | — | 75% higher conversion with ML |

### Scoring Model Dimensions

| Dimension | Weight | Components |
|---|---|---|
| Firmographic fit | 40% | ICP match: industry, size, geography, title, tech stack |
| Behavioural intent | 40% | Pricing page (+30–40), demo request (+50, auto-route), content (+15–20), email engagement (+5–10), decay (-10/14d inactivity) |
| Third-party intent | 20% | 6sense/Bombora/Breeze signals, anonymous research behaviour |

Output quadrant: High Fit + High Intent = immediate sales. High Fit + Low Intent = nurture. Low Fit + High Intent = monitor. Low Fit + Low Intent = deprioritise.

### MQL vs Buying Group

Forrester data: lead-centric MQL process has 99% failure rate from inquiry to close. <5% of MQLs convert to opportunities. 93% of B2B buyers participate in buying groups of 2+ people, generating 27 engagements on average.

Pragmatic approach: maintain sharp MQL definitions but layer in account-level engagement signals and hand-raiser prioritisation. Full buying-group motions are operationally complex on HubSpot/Salesforce.

---

## 3. Marketing-Sales SLA Framework

### SLA Components

**Marketing commits to**:
- X qualified MQLs per month/quarter meeting agreed definitions
- Pipeline contribution: typically 4× coverage for current quarter
- Lead quality: defined firmographic and behavioural thresholds
- Data completeness: minimum enrichment before handoff

**Sales commits to**:
- Respond within defined time windows (by lead type)
- Minimum 5–10 follow-up attempts per lead
- CRM disposition within 48 hours of last attempt
- Feedback on lead quality (accept/reject with reason)

**Enforcement**:
- Auto-escalation at 1× SLA breach
- Auto-reassignment at 2× SLA breach
- Weekly SLA compliance dashboard
- Monthly SLA review meeting

**Impact**: companies with formal SLAs achieve 31% higher close rates and 24% faster revenue growth (SiriusDecisions).

---

## 4. Sales → Implementation SLAs

| Milestone | Target | Measurement |
|---|---|---|
| Internal AE → CSM/Impl briefing | 24–48h post-signature | Timestamp delta: closed_won_date to briefing_date |
| Customer introduction email | Within first week | Workflow completion date |
| Kickoff call scheduled | 48–72h post-signing | Calendar event creation date |
| First implementation meeting | 2 days (best) to 7 days (standard) | implementation_kickoff_date - closed_won_date |

### Handoff Information Completeness

Required fields at Closed Won (gate stage advancement):
- SPICED: situation, pain, impact, critical event, decision criteria
- Business goals with measurable success criteria
- Onboarding POC email
- Stakeholder list (champion, economic buyer, end users)
- Technical requirements (integrations, migration, compliance)
- Contract dates (start, end)
- Competing solutions considered
- Partner sourced (Y/N) + partner company if applicable

Target: >90% of required fields populated. Measure via calculated property.

### Handoff Quality Score

Receiving team (CSM/implementation lead) rates 1–5:
1. Information completeness — were all fields populated and accurate?
2. Promise alignment — do commitments match what was documented?
3. Customer expectations — were expectations set realistically?
4. Stakeholder access — can we reach the right people?
5. Technical readiness — are requirements clear and feasible?

Target: ≥4.0 average. Review weekly. Trend quarterly.

---

## 5. Implementation → CS SLAs

| Metric | Target | Notes |
|---|---|---|
| Time to first value (TTFV) | Segment-dependent | Enterprise 30–90d, Mid-market 14–30d, SMB 1–7d |
| Go-live rate (on time) | >85% within contracted timeframe | Track by segment and implementation complexity |
| Onboarding completion | >95% | All training modules, configuration, data migration |
| Implementation velocity | Trending down QoQ | Duration from kickoff to go-live |
| Onboarding churn | <3% | Customers who churn before or during onboarding |

### Go-Live Readiness Criteria

Five conditions, all must be true:
1. **Tasks work** — critical processes complete end-to-end
2. **People trained** — key users completed training, admin certified
3. **Data migrated** — clean, validated, accessible
4. **Support plan** — escalation paths, contact points, SLAs defined
5. **Rollback plan** — contingency if go-live fails

### Implementation Health Indicators

Start measuring during implementation, not after:
- Onboarding milestone completion rate (% on schedule)
- Stakeholder engagement (right people showing up to calls?)
- Customer responsiveness (time to respond to requests)
- Admin login frequency (early adoption signal)
- Training session attendance (% of target users)

Health score below 30 correlates with ~7% churn risk. Above 50: <1% (HBR).

---

## 6. CS → Sales Expansion SLAs

| Metric | Target | Notes |
|---|---|---|
| Expansion pipeline from CS | Growing QoQ | Track both volume and conversion |
| CS-to-sales handoff time | <48h from signal to AE engagement | Signal date to first AE activity |
| Expansion win rate (upsell) | >40% | Same DMU, shorter cycle |
| Expansion win rate (warm cross-sell) | >30% | Partial DMU overlap |
| Expansion win rate (new-DMU cross-sell) | >20% | Full discovery cycle |
| NRR | 110–130%+ | Best-in-class |
| GRR | 85–95% | Enterprise should be >95% |
| Expansion as % of new ARR | 50–60% (top performers) | Track trend QoQ |
| Expansion CAC vs new-logo CAC | 4–5× cheaper | $0.27 vs $1.16 per dollar ACV |
| Probability of selling to existing customer | 60–70% | vs 5–20% for new prospects |

### Expansion Economics

Every 1% increase in revenue retention increases company value by 12% after 5 years (SaaS Capital). Expansion revenue payback: ~1 quarter vs 12+ months for new logos (Pacific Crest Survey).

---

## 7. Leading Indicators of Handoff Failure

| Indicator | Threshold | Probable Cause | First Response |
|---|---|---|---|
| Rising unworked lead rate | >10% | SDR overload or routing failure | Audit routing rules, check capacity |
| Increasing MQL rejection rate | >30% | Marketing-sales ICP misalignment | Joint ICP review session |
| Growing time-to-kickoff | >14 days | Sales-to-CS bottleneck | Pre-close resource planning |
| Declining onboarding completion | <90% | Capacity or product complexity | Segment by complexity, adjust staffing |
| Dropping 30-day CSAT | <70% | Poor expectation-setting during sales | Audit promise alignment scores |
| Shrinking expansion pipeline from CS | Declining 2+ quarters | CS not identifying/surfacing signals | Train CS on signal recognition, instrument triggers |
| Rising first-year churn | >15% | Systemic handoff failure | Segment churn by handoff quality scores to isolate root cause |

---

## 8. Dashboard Architecture

Six dashboards monitor the full bow tie:

### Dashboard 1: Lifecycle Funnel Performance
- Stage-to-stage conversion rates (VM1–VM8 / CR1–CR7)
- Volume and time per stage
- Cohort views by source, segment, motion

### Dashboard 2: Sales Handoff & Follow-Up
- Speed-to-lead by rep, source, date range
- SLA compliance rate (% within target)
- Unworked leads (count and aging)
- Follow-up activity rate
- Most requested by sales managers

### Dashboard 3: Pipeline Health
- Deal velocity by stage
- Forecast by team (commit, best case, upside)
- Weighted pipeline vs target
- Aging deals (>2× average cycle time)

### Dashboard 4: Customer Success & Expansion
- Onboarding status (milestone completion)
- Health score distribution (green/yellow/red)
- Expansion opportunities by type and source
- TTFV by segment and implementation path

### Dashboard 5: Executive Bow-Tie Overview
- Full-funnel VM/CR/Δt mapped to WbD framework
- NRR, GRR, CAC payback
- Expansion vs new-logo ARR contribution
- Forecast accuracy trend

### Dashboard 6: Handoff Quality Monitor
- Quality scores by transition point (1–5 scale)
- SLA compliance heat map
- Promise alignment rate
- Leading indicator alerts (from table above)
- Information completeness by deal

---

## 9. Territory & Routing Design

### Four Models

| Model | Best For | Tradeoff |
|---|---|---|
| Geographic | Travel-heavy, local market knowledge needed | Less relevant in digital SaaS |
| Vertical/Industry | Domain expertise drives faster deals | Uneven opportunity sizes |
| Named accounts | Deep strategic relationships | Requires strong ABM infra |
| Hybrid (recommended) | Most B2B SaaS scale-ups | Segment × vertical × geography |

### EU-Specific Clusters

Start with language-based routing:
- **DACH** — German required, formal buying processes
- **Nordics** — high digital fluency, English-friendly
- **UK & Ireland** — closest to US patterns
- **Western Europe** — French critical for France
- **Southern Europe** — relationship-driven
- **CEE** — emerging, cost-sensitive

Route by language of form submission as first-pass filter.

### Routing by Lead Type

| Lead Type | Routing | SLA |
|---|---|---|
| Hand-raiser (demo, pricing) | Direct to territory AE | 5 minutes |
| MQL (score-qualified) | To SDR for qualification | 4 hours |
| Partner referral | Via partner manager to territory AE | 24 hours (priority flag) |
| Expansion signal | CSM to AE with context | 48 hours |
| PQL (usage-based) | Auto-route by account | Same business day |

**Account-based override**: when a lead from a known account enters, route to existing account owner regardless of rotation. Non-negotiable.

### Capacity-Based Routing

Factor current pipeline load. Rep at 120% capacity shouldn't receive new leads. Use weighted round-robin with capacity adjustment at scale.

### Territory Design by ARR Stage

- **€15M ARR** (5–15 AEs): simple geographic clusters, round-robin, generalist AEs
- **€50M ARR** (30–60 AEs): weighted round-robin with territory rules, hunter/farmer split, cluster-based EU coverage
- **€150M ARR** (100+ AEs): full matrix (segment × vertical × geography), capacity-based + AI-assisted routing, country-level local-language reps

Apply the ±10% rule: no territory should have more than 10% higher or lower total workload than team average.
