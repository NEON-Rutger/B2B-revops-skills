# Diagnosing Forecast Misses

On-demand reference for the revops-forecasting skill.

The accuracy formula and benchmarks remain in the body. This file holds the diagnosis patterns for over-forecasting, under-forecasting, and high variance.

**Consistent over-forecasting (closing less than predicted):**
- Commit criteria too loose: reps putting Best Case deals in Commit
- Optimistic close dates: deals slipping to next period
- Insufficient qualification: deals in pipeline that shouldn't be
- Fix: Tighten Commit validation, implement deal review rigor

**Consistent under-forecasting (closing more than predicted):**
- Conservative culture: reps sandbagging to protect upside
- Expansion/upsell revenue not captured in pipeline
- Late-quarter inbound deals closing fast
- Fix: Incentivize accurate forecasting (not just attainment), capture all revenue sources

**High variance (sometimes over, sometimes under):**
- Insufficient deal volume for statistical prediction
- Lumpy deal sizes (one large deal swings everything)
- Inconsistent stage definitions: deals at "Proposal" mean different things to different reps
- Fix: Standardize stage definitions, increase pipeline volume, segment the forecast by deal size
