# Revenue Metrics Benchmark Reference

On-demand reference for the revops-metrics skill. Use these to calibrate dashboard thresholds and to quantify the gap when your numbers are off. This file covers seller performance, stakeholder coverage, cycle timing, pipeline composition, and AI impact, framed for dashboard calibration.

Last verified: 2026-09. Figures older than 2025 are kept only where no newer edition exists and are marked as such.

Every figure here is a starting point. Calibrate to your company's stage, ACV, motion, and market before quoting it as a target. Evidence types: survey, vendor platform data, analyst, practice-based.

## 1. Seller performance

The numbers that reveal whether the revenue system, not the individual rep, is healthy.

| Metric | Industry average | Top performers | Source |
|---|---|---|---|
| Quota attainment | Just under 44% of reps (Q4 2025) to 62% of ramped AEs (2025) | 80%-plus (practice-based plan-design target, not a published figure) | RepVue Cloud Sales Index, Q4 2025, vendor platform data ([repvue.com](https://www.repvue.com/cloud-index/2025/Q4)); ICONIQ State of Go-to-Market 2026, survey of 155+ B2B SaaS executives ([iconiq.com](https://www.iconiq.com/growth/reports/state-of-go-to-market-2026)) |
| Sellers missing quota | 78% missed in 2025 (Ebsta); 78.3% missed in 2025, quotas set about 13% too high (Fullcast) | n/a | Ebsta x Pavilion 2025 GTM Benchmarks, vendor platform data plus survey ([benchmarks.ebsta.com](https://benchmarks.ebsta.com/2025-gtm-benchmarks)); Fullcast 2026 Revenue Benchmark Report, vendor platform data ([fullcast.com](https://www.fullcast.com/content/fullcast-releases-2026-revenue-benchmark-report-analyzing-78-billion-in-revenue-data/)) |
| AEs achieving quota annually | 51% | n/a | Bridge Group SaaS AE Metrics, survey (2024 edition, no newer edition found) ([bridgegroupinc.com](https://blog.bridgegroupinc.com/saas-inside-sales-metrics)) |
| Rep time actually selling | 40% (2026), up from about 30% (2024: 70% of time on non-selling tasks) | 60%-plus (inbound-fed; practice-based) | Salesforce State of Sales, 7th edition 2026, survey of 4,050 sales professionals ([salesforce.com](https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/)); 6th edition 2024, 5,500 respondents ([salesforce.com](https://www.salesforce.com/news/stories/sales-ai-statistics-2024/)) |
| AE ramp time | 5.7 months | Compressing with AI enablement (see section 5) | Bridge Group SaaS AE Metrics, survey (2024 edition, no newer edition found) ([bridgegroupinc.com](https://blog.bridgegroupinc.com/saas-inside-sales-metrics)) |

Read: if quota attainment sits near the 44% floor, the constraint is usually pipeline quality, territory design, or comp design, not rep effort. Diagnose the system before coaching the rep. Note the definitional spread: RepVue measures self-reported rep attainment across its index, ICONIQ measures ramped AEs only, so the two are not the same population.

Single-company cases (podcast-reported by the company's own executives, not benchmarks; not independently verified):

| Metric | Value | Source |
|---|---|---|
| OTE attainment | About 80% typical, about 138% at Owner.com | Owner.com (via Norton, The Revenue Leadership Podcast E64) |
| Revenue per AE versus competitors | 3 to 4x | Owner.com, Datarails (via Norton, E64) |

## 2. Win rate and stakeholder coverage

Multi-threading is now a win-rate lever, not a convenience. Single-threaded late-stage deals are a liability.

| Signal | Effect | Source |
|---|---|---|
| 3 or more engaged contacts per deal versus single-threaded | About 2.4x higher close rates, rising to 3.1x for enterprise deals | Ebsta x Pavilion 2025 GTM Benchmarks, vendor platform data ([joinpavilion.com](https://www.joinpavilion.com/resource/2025-gtm-benchmarks-ebsta-pavilion)) |
| Relationship score with decision makers above 40 through the cycle | Win rate roughly quadruples | Ebsta x Pavilion 2025 GTM Benchmarks, vendor platform data |
| Decision makers involved in the first two stages | Win rate up 55% | Ebsta x Pavilion 2025 GTM Benchmarks, vendor platform data |
| Well-qualified versus poorly qualified deals | 6.3x more likely to win (50% versus 8% win rate) | Ebsta 2025 Sales Qualification Report, vendor platform data, 655,000 opportunities |

Note: secondary summaries also describe the 2.4x multi-threading effect as "close 2.4 times faster". Check the report wording before quoting it as a win-rate figure. Track a multi-threading tile on the manager dashboard and flag any late-stage deal still single-threaded.

## 3. Deal cycle timing

| Metric | Value | Read |
|---|---|---|
| Deals running past two months | Win rates fall sharply (Ebsta reports a 113% drop) | Speed after qualification is a win-rate lever (Ebsta x Pavilion 2025 GTM Benchmarks, vendor platform data) |
| Well-qualified deals | Close 21.6% faster and are 1.9x less likely to slip | Ebsta 2025 Sales Qualification Report, vendor platform data |
| Year-on-year cycle trend | Sales cycles about 7% longer; win rates down 13.5%; average deal value down 11% | Fullcast 2026 Revenue Benchmark Report, vendor platform data (361,000 opportunities, 316 companies) |
| Performance gap | Top performers close deals 11x faster than lower performers (up from 8.9x in 2024) | Ebsta x Pavilion 2025 GTM Benchmarks, vendor platform data |

Practice-based: lost deals typically run much longer than won deals, and a deal far past its segment's normal cycle behaves statistically like a loss. Calibrate absolute cycle length by segment (practice-based: SMB under 30 days, mid-market 60 to 90, enterprise 90 to 150). The won-versus-lost gap is the pattern to watch inside any segment; measure it on your own closed deals.

## 4. Pipeline composition

Healthy composition at maturity (roughly $25M ARR and above). Practice-based operating ranges unless a source is named.

| Component | Healthy range |
|---|---|
| New business ARR | 30 to 50% of gross new ARR (practice-based) |
| Expansion ARR | 30 to 50% of gross new ARR (practice-based) |
| GRR | Over 90% (practice-based target; market medians sit at about 84 to 91%, see below) |
| Pipeline coverage | 3.0x minimum, 3.5 to 4.0x healthy (practice-based) |

GRR market context: median GRR 91% and median NRR 101% for private B2B SaaS (SaaS Capital 2025 retention benchmarks, survey, [saas-capital.com](https://www.saas-capital.com/blog-posts/what-is-a-good-retention-rate-for-a-private-saas-company/)); GRR approaching 90% and NRR above 100% (2025 KeyBanc Capital Markets and Sapphire Ventures SaaS Survey, [sapphireventures.com](https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey)); median GRR 84%, 75th percentile 91% (Benchmarkit and Aleph 2026 SaaS and AI Performance Benchmarks, survey of 342 companies, as summarized at [getaleph.com](https://www.getaleph.com/answers/net-revenue-retention-saas-2026)).

If expansion is under 20% of new ARR, you are leaving money on the table. If new business is over 70%, you are dangerously acquisition-dependent. Above 5x coverage usually signals a qualification problem, not abundance. (All practice-based.)

## 5. AI impact metrics

Where AI is measurably moving GTM numbers, for calibrating AI-native and AI-enabled company dashboards.

| Metric | Value | Source |
|---|---|---|
| Ramp-time reduction, AI-enabled teams | 32.7% faster ramp | Fullcast 2026 Revenue Benchmark Report, vendor platform data |
| Quota attainment, AI fully embedded in GTM versus not | 67% versus 59% of ramped AEs hitting quota (SMB high-adoption teams: 106% versus 80% average attainment) | ICONIQ State of Go-to-Market 2026, survey |
| Revenue per seller, AI deployed across the full revenue lifecycle | +61% | Fullcast 2026, vendor content |
| Close likelihood, manageable versus overloaded deal loads | 57% more likely to close | Fullcast published content, vendor data (not confirmed against the 2026 report text) |
| Win-rate uplift, expertise-based routing | Up to 40% | Fullcast published content, vendor data (not confirmed against the 2026 report text) |
| BDR productivity lift with AI agents (calls and opps) | +85% | Owner.com pilot (via Norton, The Revenue Leadership Podcast E60); single-company case, not verified |
| AI-assisted ramp-compression target | About 3 months | Donnelly / Crescendo (E62); single-company target, not verified |

For AI-native products, shift the leading-indicator tile from pipeline velocity to AI output quality: resolution rate, automation rate, and work completed per user (Poyar four-signal model; practice-based framework). Adoption is not value capture. Measure the work completed, not the seats sold.

## How to use this reference

1. Pull the relevant benchmark for the metric that is off.
2. State the gap in your own numbers (illustrative): "your win rate is 18% against a 25 to 35% benchmark for your segment; that is the gap we are closing."
3. Use the gap to size the cost of inaction in the proposal.

## Sources and caveat

Compiled from: Ebsta x Pavilion 2025 GTM Benchmarks ($48 billion pipeline, 655,000 opportunities, 2,000+ CRO survey; the most recent edition found at 2026-09) and the Ebsta 2025 Sales Qualification Report; Fullcast 2026 Revenue Benchmark Report ($78 billion pipeline, 361,000 opportunities, 2,500 reps, 316 companies; published with Pavilion); ICONIQ State of Go-to-Market 2026; RepVue Cloud Sales Index Q4 2025; Salesforce State of Sales 2024 and 2026; Bridge Group SaaS AE Metrics (2024 edition); SaaS Capital 2025; KeyBanc and Sapphire 2025; Benchmarkit and Aleph 2026; The Revenue Leadership Podcast E60 to E64 (single-company cases only).

Removed at the 2026-09 verification pass (no traceable primary source found): the stakeholder-count win-rate ladder (1 contact 0.2x through 10-plus 2.4x) and the "relationship score 91 to 100 wins at 2.2x" figure; won-deal 115 days versus lost-deal 225 days and the momentum-decay multipliers; "11.2 months to full productivity" attributed to the Sales Management Association; "70% of reps miss quota due to poor commission design" (the traceable Fullcast wording does not claim causation); "+10% growth from quarterly comp reviews"; the "5%" floor of the routing uplift range.

Caveat: Ebsta, Fullcast and RepVue figures are vendor platform data or vendor-run surveys; use directionally, not as independent third-party research. Several Ebsta and Fullcast figures were checked against the vendors' published summaries rather than the gated full reports. Where a decision hinges on an exact figure, verify against the full report before quoting it.
