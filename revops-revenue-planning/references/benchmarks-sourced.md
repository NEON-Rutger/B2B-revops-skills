# Benchmarks and Operating Defaults

Two classes of numbers, kept deliberately separate. **Part A** is sourced market research: every figure carries a named publisher and year, and figures that could not be verified against their source were removed at the 2026-07-14 verification pass. **Part B** is practice-based operating defaults: practitioner heuristics applied in planning, labeled as exactly that. Never present a Part B number to your executive team as market research.

---

## Part A: Sourced market benchmarks

### Forecast accuracy

- Only 7% of companies reach 90%+ forecast accuracy (Gartner, as cited by ORM Technologies, Forecast Accuracy Guide, 2025)
- 80% of sales organizations do not exceed 75% forecast accuracy (Ebsta 2025 GTM Benchmarks Report)
- Median forecast accuracy: 75% (Ebsta 2025 GTM Benchmarks Report)
- Companies with weekly pipeline velocity tracking report 87% forecast accuracy vs 52% for teams tracking irregularly (Digital Bloom, 2025 B2B SaaS Funnel Benchmarks; single agency study, treat as indicative)

### Quota attainment

- 43-57% of B2B sales reps hit quota in any given quarter (Pavilion Revenue Collective, Salesforce State of Sales, Bridge Group)
- 2024: 52% of reps hit quota; 2025: 46% (Ebsta 2025 GTM Benchmarks Report, based on EUR 48 billion in pipeline data from 2,000 CROs)
- 78% of sellers missed their quotas in 2025, up from 69% in 2024 (Ebsta 2025 GTM Benchmarks Report)

### Pipeline coverage, quality and slippage

- 3x to 5x pipeline coverage is the typical B2B SaaS range (Abacum; Runway; MetricGen, 2025-2026)
- 36% of pipeline deals slip in any given quarter (Ebsta 2025 GTM Benchmarks Report)
- Highly qualified deals close 20% faster and are 1.9 times less likely to slip (Ebsta 2025 GTM Benchmarks Report)
- 11x pipeline velocity delta between top and bottom performers in the same pipeline, which is why blended conversion rates mislead (Ebsta/Pavilion, 2025)
- Commit close rate 85%, best case close rate 50% (Ebsta 2025 GTM Benchmarks Report); together with the slippage rate, this is why 3x coverage is the floor for reliably hitting a quarterly target

### Reforecasting cadence

- Weekly forecast calls focused on material changes, late-stage deals and slippage, paired with a monthly full-pipeline commit, for most growth-stage SaaS (ORM Technologies, 2025)
- Monthly rolling cadence to prevent drift; weekly or bi-weekly operational forecasting supported by monthly reviews and quarterly rollups (Fincome, "How to Master Reforecasting in SaaS", 2025)
- Revenue or expense deviation of 10% or more from budget for two consecutive periods triggers a reforecast (Fincome, 2025)
- For B2B marketing: 10% cumulative variance in media spend or a 20% shortfall in pipeline conversion should trigger a reforecast meeting (Fincome, 2025)

### Compensation

- The gap between top and average Account Executive compensation reached $200,000 USD in 2025, the widest spread in five years (Xactly 2026 State of Sales Compensation Report; report is gated, figure from its published summary). Relevant to planning because capacity plans that assume average-rep productivity while paying for top-rep retention misprice the plan. Comp design itself belongs to gtm-compensation.

### Source register

- **Ebsta**, 2025 GTM Benchmarks Report (EUR 48 billion pipeline, 2,000 CROs); benchmarks.ebsta.com; report gated behind registration, figures from its published summaries.
- **Gartner** forecast accuracy figure via **ORM Technologies** Forecast Accuracy Guide, 2025; orm-tech.com.
- **Pavilion** Revenue Collective and CRO School (Forecasting and Revenue Modeling curriculum, 2026); joinpavilion.com/pavilion-university/cro-school.
- **Salesforce** State of Sales (with Pavilion, quota attainment range); **Bridge Group** rep attainment research.
- **Fincome**, How to Master Reforecasting in SaaS, 2025; fincome.co.
- **Digital Bloom**, 2025 B2B SaaS Funnel Benchmarks; thedigitalbloom.com.
- **Abacum** (abacum.ai), **Runway**, **MetricGen**: pipeline coverage guidance.
- **Xactly**, 2026 State of Sales Compensation Report; xactlycorp.com (gated).
- **Atscale** practitioner input: Louis Fumey, RevOps practice lead, 2026 (plan versioning and scenario ownership doctrine).
- Podcast extractions: RevOps Lab episode 57 (Shantanu Shekhar, Personio); FP&A Today; Run Revenue Show (Clari). Frameworks only, no benchmark figures taken from audio.

Removed at verification (2026-07-14), do not reintroduce without a checkable source: Clari Labs "87% of enterprises missed revenue targets"; all GrowthSpree figures (gated agency reports); Optifai sales cycle medians (source unreachable); "sales cycles lengthened 22% since 2022" (no attributable source).

---

## Part B: House operating defaults (practitioner doctrine, not market research)

These are the defaults applied in planning. They come from practitioner experience, the sibling skills (revops-forecasting, gtm-planning) and widely used SaaS operating conventions. Present them to your leadership team as "our operating standard", never as a study result.

### Coverage and trigger thresholds

- Coverage below 2.5x: critical risk, immediate reforecast trigger. 2.5x to 3.0x: at risk, escalate. 3.0x to 3.5x: healthy baseline. Above 3.5x: strong.
- Forecast accuracy variance beyond plus or minus 20% for two consecutive months: reforecast.
- CAC payback beyond 14 months, NRR below 105%, or burn 15% over plan: reforecast review.
- Slippage adjustment: apply a 0.64 factor to Best Case and Upside forecasts (derived from the sourced 36% slippage rate).

### Attainment and productivity defaults

- Plan design target: 70-80% of reps at quota. A plan where fewer than half the team can attain is a quota problem, not a talent problem.
- SDR attainment expectation band: 60-80%. SDR activity default: 100-150 conversations per month, tuned to ACV and motion. SDR-sourced share of new-business pipeline: 30-50% in blended motions.

### Planning calendar defaults

- Recommended planning runway: 12 weeks before fiscal year start; 6 weeks is the compressed minimum and not recommended; high-complexity businesses take 16.
- Product and budget pre-work starts 6-8 weeks before the cycle; the first fortnight is retrospective and data work, not target debates.

### Efficiency ratio conventions

- Magic Number (net new ARR divided by prior quarter GTM spend): below 0.75 inefficient, 0.75-1.0 good, above 1.0 excellent. Widely used SaaS convention; treat the banding as convention, not research.
- GTM efficiency framing as popularized by SBI and the Pedowitz Group: each euro of GTM spend should produce a defensible multiple in revenue; when it does not, the plan has a structural problem, not a stretch problem.

### Stage-based defaults (capacity and structure)

High-variance heuristics; always validate against your company's own cohort data before putting them in a plan.

- EUR 1-5M ARR: founder or VP-led sales; forecast accuracy of 75%+ is achievable with basic discipline; AE ramp 6-9 months (SMB motion) to 9-12 (enterprise).
- EUR 5-25M ARR: dedicated sales leadership, sales ops emerging; SDR:AE ratio 1:3 to 1:4; AE ramp 4-6 months in established motions.
- EUR 25-100M ARR: formal RevOps and FP&A collaboration; one front-line manager per 6-8 AEs; one RevOps FTE per 50-75 GTM FTE; ramp 3-4 months in proven motions.
- Per-rep bookings capacity varies too much by vertical, ACV and motion to carry a house default; build it bottoms-up from your company's own ramped-rep cohort (see references/bottoms-up-build-recipe.md).

---

**Last updated:** 2026-07-14, after the adversarial verification pass. Part A is sourced and was verified claim by claim; Part B is house doctrine and says so.
