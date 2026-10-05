# Stage Conversion Rate Benchmarks

Last verified: 2026-09. Figures older than 2025 are kept only where no newer edition exists and are marked as such.

On-demand reference for the deal-velocity-engineer skill.

These are the system's vital signs. If conversion drops at a specific stage, that's the constraint.

## Full-Funnel Conversion Rates

| Stage Transition | Good | Great | Best-in-Class | Source |
|-----------------|------|-------|---------------|--------|
| Lead → MQL | 15-20% | 20-30% | 30%+ | Practice-based (aggregator blog composite, Altior RevOps 2025; no primary study located) |
| MQL → SQL | 30-40% | 40-50% | 50%+ | Practice-based (aggregator blog composite, Pixelswithin 2026; no primary study located) |
| SQL → Opportunity | 50-60% | 60-75% | 75%+ | Practice-based (aggregator blog composite, Altior RevOps 2025; no primary study located) |
| Opportunity → Closed-Won | 15-22% | 22-30% | 30%+ | Optifai 2024, 939 companies (vendor platform data; older than 2025, no newer edition located) |
| Overall Lead → Customer | 2-3% | 3-5% | 5%+ | Practice-based composite |

Treat the top-of-funnel rows as operating ranges, not statistics: definitions of MQL and SQL vary too much between companies for a cross-company benchmark to be precise.

## Win Rate by Segment

| Segment | Average Win Rate | Top Quartile | Source |
|---------|-----------------|--------------|--------|
| SMB | 30-39% | 45%+ | Aggregator (Digital Bloom 2025); no primary segment split located |
| Mid-Market | 22-30% | 35%+ | Optifai 2024 (vendor platform data; older than 2025) |
| Enterprise | 18-25% | 31%+ | Aggregator (Digital Bloom 2025); no primary segment split located |

**Primary context for win rates (use to sanity-check the table):**
- Win rates fell **13.5%** year on year across the Fullcast/Pavilion 2026 dataset ($78B pipeline, 361,000 opportunities; vendor platform data, as reported by SaaSletter). https://www.saasletter.com/p/ai-nrr-gross-margin-efficient-frontier-2026-gtm-sales-benchmarks-fullcast-pavilion
- Well-qualified deals win at **50%** versus **8%** for poorly qualified deals, are **6.3x** more likely to close, and close **21.6%** faster (Ebsta 2025 Sales Qualification Report, 655,000 opportunities, $48B; vendor platform data). https://www.prnewswire.com/news-releases/new-ebsta-report-reveals-top-sales-teams-win-6-3x-more-often-by-qualifying-smarter-not-harder-302520694.html
- Targeting the wrong customers cuts the chance of closing by up to **75%** (Fullcast 2026 Revenue Benchmark Report, vendor platform data). https://www.fullcast.com/content/fullcast-releases-2026-revenue-benchmark-report-analyzing-78-billion-in-revenue-data/

## Stage-Specific Win Probability

| Stage | Historical Win Probability | Use For |
|-------|--------------------------|---------|
| Discovery | ~40% | Weighted pipeline calculation |
| Solution Presented | ~55% | Forecast sanity check |
| Proposal Sent | ~65% | Pipeline coverage math |
| Negotiation | ~85% | Commit validation |

**Source:** Optifai 2024 (939 companies, opportunity-to-closed analysis; vendor platform data, composite benchmark, no segment breakdown; older than 2025, no newer edition located). Note: These are blended figures across all deal sizes. Adjust expectations downward for SMB/mid-market deals, upward for enterprise strategic deals. Replace with your own historical stage-to-close rates once you have four quarters of clean stage history.
