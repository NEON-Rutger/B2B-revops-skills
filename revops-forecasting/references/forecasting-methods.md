# Forecasting Methods (Detailed Mechanics)

On-demand reference for the revops-forecasting skill.

This file holds the detailed mechanics of forecasting Methods 2-4 (the body keeps Method 1 in full plus one-line summaries of these), and the full Commit validation checklist.

## Method 1: Commit Validation Rules (full checklist)

**Validation rules for Commit:**
```
□ Has the buyer explicitly confirmed intent to purchase this period?
□ Is the economic buyer identified and engaged?
□ Are commercial terms (price, scope, contract length) agreed?
□ Is there a signed mutual action plan or documented close plan?
□ Has procurement/legal review been initiated?
□ Is the close date within the current forecast period?
□ If any box is unchecked, this is Best Case, not Commit.
```

## Method 2: Stage-Weighted Pipeline (Data-Driven)

Multiply the value of each deal by the historical win probability at its current stage. This removes rep judgment entirely and relies on historical patterns.

**How to calculate stage weights:**
```
1. Pull all closed deals from the last 12 months (won and lost)
2. For each stage, calculate: deals that entered this stage → eventually won
3. That percentage is your stage weight

Example:
Qualified:       35% of deals that reach this stage eventually close
Discovery:       42% (qualification has filtered some out)
Solution Design: 55%
Proposal:        65%
Negotiation:     78%
```

**Weighted pipeline = Σ (deal value × stage probability)**

**When to use it:** As a sanity check against category-based forecasting. If your commit forecast is €1.2M but weighted pipeline says €800K, your commits include some deals that historically don't close from their current stage at the rate your reps expect.

**Limitations:**
- Treats all deals in a stage equally (a €500K enterprise deal and a €20K SMB deal at the same stage have different close probabilities)
- Doesn't account for deal age (a deal in Negotiation for 3 days is different from one there for 30 days)
- Requires clean historical data and enough volume for statistical significance (minimum 50-100 closed deals per segment)

## Method 3: Historical Run-Rate / Trend Analysis

Project future revenue based on historical patterns. Best for recurring revenue components and mature, predictable businesses.

```
Simple run-rate:
  Average monthly revenue (last 6 months) × remaining months = projected period revenue

Trend-adjusted:
  Apply month-over-month growth rate to project forward
  Example: If MRR grew 4% MoM for the last 6 months, project 4% forward

Seasonal adjustment:
  Use year-over-year comparisons for the same period to adjust for seasonality
  Example: Q4 is historically 130% of average quarterly revenue → adjust upward
```

**When to use:** For the renewal/expansion base of the business. New business is too variable for run-rate forecasting at most companies. Combine run-rate for existing revenue with category-based for new business.

## Method 4: Bottoms-Up Capacity Model

Calculate what the sales team should produce based on capacity, not pipeline.

```
For each rep:
  Monthly quota ÷ average deal size = deals needed per month
  Deals needed ÷ historical win rate = opportunities needed
  Opportunities needed ÷ meeting-to-opportunity rate = meetings needed

Then:
  Sum across all ramped reps = total expected output
  Adjust for ramp (new reps produce at 25/50/75/100% in months 1-4)
  Adjust for seasonality and historical attainment distribution
```

**When to use:** For annual planning and capacity planning. This tells you what the team *should* produce given its size and historical productivity. If the bottoms-up model says €8M and the board wants €12M, you have a capacity gap, not a forecasting problem.
