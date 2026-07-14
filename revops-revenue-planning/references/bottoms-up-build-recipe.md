# Bottoms-Up Build Recipe

A step-by-step guide to building the revenue plan from capacity and current-state pipeline, independent of top-down targets.

## Step 1: Segment Your Business

Divide total addressable revenue into segments that have different unit economics, sales processes, or conversion rates.

**Typical segmentation dimensions:**
- Revenue type (New Business / Expansion / Renewal)
- Customer size (SMB / Mid-Market / Enterprise)
- Go-to-market motion (self-serve / sales-assisted / sales-led)
- Product line or vertical (if applicable)

**Example segmentation:**

```
New Business - SMB (self-serve + sales-assist):        20% of target revenue
New Business - Mid-Market (sales-led):                 35% of target revenue
Expansion (usage-based upsell + success-driven):       25% of target revenue
Renewal (contractual + health-based retention):        15% of target revenue
Professional Services (delivery + implementation):     5% of target revenue
```

**Why segment:** Blended forecasts hide reality. SMB renewal rates (95% GRR) behave completely differently from Enterprise churn (88% GRR). Self-serve new business converts at 5x the velocity of sales-led enterprise. By segment, you see where the business is stable and where it is fragile.

## Step 2: Document Current-State Baseline

For each segment, lock the prior-year actual or current-year run-rate.

**Template:**

```
Segment                  Current ARR/Bookings    % of Total    Data Source
---------------------------------------------------------------------
New Business - SMB       €1.2M                   20%           CRM closed-won 2025
New Business - MM        €2.1M                   35%           CRM closed-won 2025
Expansion                €1.5M                   25%           CRM expansion bookings
Renewal                  €0.9M                   15%           Contract database
Professional Services    €0.3M                   5%            Project tracking
---------------------------------------------------------------------
TOTAL                    €6.0M                  100%
```

Lock this baseline. Do not adjust it during the planning process. This is your anchor.

## Step 3: Build the Capacity Model

The capacity model answers: "If our sales team does exactly what they did last year, how much revenue should we produce?"

### The Capacity Model Formula

```
Annual Bookings Capacity = (FTE Available) × (Ramp Factor) × (Annual Quota per AE)
```

**Detailed formula with adjustments:**

```
STARTING POINT:
  Tenured AE headcount (100% productive):            5 FTE
  New AE hires (expected to ramp):                   2 FTE
  Ramp timeframe for new hires:                      6 months
  
RAMP ADJUSTMENT:
  Tenured productivity:                              5 FTE × 100% = 5.0 FTE
  New hire ramp (assume 50% avg over 6-month):     2 FTE × 50% = 1.0 FTE
  Total effective FTE for year:                      6.0 FTE

QUOTA ASSIGNMENT:
  Annual quota per tenured AE:                       €850K
  Annual quota per new AE (after full ramp):         €850K
  
BOTTLENECK ANALYSIS:
  Is pipeline constrained by available opportunities? YES (pipeline generation is the constraint)
  Haircut for pipeline availability:                 ×85% (historical fill rate)
  
CAPACITY CALCULATION:
  Base capacity: 6.0 FTE × €850K/AE = €5.1M
  Pipeline constraint haircut: €5.1M × 85% = €4.335M
  Territory overlap / allocation efficiency:         ×95% = €4.118M
  
FINAL CAPACITY ESTIMATE:                            €4.1M annual bookings
```

### Capacity Model Components in Detail

#### Headcount Plan

Start with committed headcount (approved budget) by role:

```
Role              Current    Hiring (Year 1)    Net Change    End-of-Year
---------------------------------------------------------------------
Account Executives    7            2                 +2            9
SDRs (pipeline gen)   4            1                 +1            5
Sales Engineers       2            0                  0            2
Sales Manager         1            0                  0            1
```

#### Ramp Profile by Role

Each role has a ramp curve. Ramp period is the time until 100% productivity. Production during ramp is typically:

```
ACCOUNT EXECUTIVE (6-month ramp):
  Month 1:    0% of full quota     (onboarding, territory learning)
  Month 2:    25% of full quota    (first deals in pipeline)
  Month 3:    50% of full quota
  Month 4:    70% of full quota
  Month 5:    85% of full quota
  Month 6:    100% of full quota   (fully ramped)

SDR (3-month ramp):
  Month 1:    20% of pipeline target
  Month 2:    60% of pipeline target
  Month 3:    100% of pipeline target

Sales Engineer (2-month ramp):
  Month 1:    50% of typical deal-support load
  Month 2:    100% of typical deal-support load
```

**Calculate effective FTE for the year:**

If you hire 2 AEs in Month 1 (January) with 6-month ramp:
- Jan-Jun: producing 0% + 25% + 50% + 70% + 85% + 100% = 330% total over 6 months = 55% average
- Jul-Dec: producing 100% × 6 months = 600% total over 6 months = 100% average
- Annual contribution: (330% + 600%) / 12 months = 77.5% of a full FTE

Alternatively, use a simplified approach: average new-hire at 80% of a full-year tenured rep. This is conservative.

#### Annual Quota by Role

Set quotas based on historical achievement or benchmarks:

```
Role                   Quota per Rep    Number of Reps    Total Quota
---------------------------------------------------------------------
Account Executive      €850K            9 (7 + 2 ramping) €7.65M
SDR (pipeline gen)     €400K meetings   5 (4 + 1 ramping) €2M meetings created
Sales Engineer         Support role     2                 €0 direct
```

**Quota setting guardrails:**
- Set based on historical attainment (if last year AEs hit €800K at 78% attach rate, quota is €800K, not €1M)
- Adjust for known market changes (new product launch, new vertical entry, lost customer)
- Do NOT set quotas to match top-down targets until bottoms-up is done

#### Productivity Assumptions

Document the assumptions that connect headcount and quota to bookings:

```
Assumption                              Value      Source/Confidence
-------------------------------------------------------------
Deal close rate (overall)               60%        CRM last 12 months
Average deal size (New Biz SMB)         €25K       CRM average 2025
Average deal size (New Biz MM)          €85K       CRM average 2025
Sales cycle length (SMB)                45 days    Salesforce field audit
Sales cycle length (MM)                 90 days    Salesforce field audit
Pipeline velocity                       35% per month  CRM reporting
% of quota from self-sourcing           35%        Activity tracking
% of quota from marketing-sourced       50%        Lead source report
% of quota from channel/partnerships    15%        Partner tracking
Win rate vs competition                 35%        Competitor intel
Pipeline available per AE (coverage)    €3.2M      CRM stage analysis
```

**Check: Does the math connect?**

```
SMB AE capacity test:
  - Pipeline available: €3.2M (from CRM)
  - Historical win rate: 38%
  - Expected closure: €3.2M × 38% = €1.216M
  - Assigned quota: €850K
  - Implicit assumption: rep is only using 70% of available pipeline
  
Question: Is the other 30% low-quality, stale, or delayed-close?
Action: Audit pipeline health; improve pipeline generation if quality is good
```

## Step 4: Calculate Segment-Specific Growth Assumptions

For each segment, determine what "nothing changes" looks like, then model growth independently.

### New Business Segment

```
Prior-year closed new-business bookings:     €3.3M
Current-year pipeline for new business:      €4.8M (1.45x coverage)

Capacity-based forecast:
  AE headcount available for new biz:        6.5 FTE (effective)
  Quota per AE:                              €850K (blended SMB + MM)
  Base capacity:                             €5.525M
  Pipeline constraint (only €4.8M pipeline):  €4.8M
  Haircut for slippage (36% slip rate):      €4.8M × 64% = €3.072M
  
Scenario analysis:
  Base (no pipeline generation investment): €3.1M
  +Scenario A (ABM spend +€100K invested):  +€250K pipeline → €3.25M
  +Scenario B (new AE hire):                +€680K capacity → €3.65M if pipeline exists
```

### Expansion Segment

```
Current expansion ARR:                       €1.5M
Historical gross retention rate (GRR):       92%
Historical net expansion rate:               12% (upsell + cross-sell net of downgrade)

Bottoms-up forecast:
  Renewal base (92% of €1.5M):              €1.38M
  Expansion growth (12% of €1.5M):          +€0.18M
  New expansion from new-customer base:      +€0.05M (only 3-4 new customers ready to expand)
  
Total expansion forecast:                    €1.61M

Variance analysis:
  If retention drops to 88% (2-year churn acceleration): €1.32M (miss of €0.29M)
  If new-customer base expands faster (10 vs 4 ready):   €1.71M (beat of €0.1M)
```

### Renewal Segment

```
Current renewal ARR:                         €0.9M
Historical gross retention (GRR):            97%
Known renewals at risk:                      €80K (customer feedback indicates low NRR)
Contraction from existing (downsells):       -€20K (expected downgrades)

Bottoms-up forecast:
  Base at-risk (€0.9M - €0.08M) × 97%:     €0.795M
  At-risk book (€0.08M with intervention):  €0.06M (75% save rate expected)
  Contraction risk (-€0.02M):               -€0.02M
  
Total renewal forecast:                      €0.835M

Confidence level:                            HIGH (renewal base is most predictable)
```

## Step 5: Consolidate Segment Forecasts into Bottoms-Up Plan

Create a summary table with segment forecasts, assumptions, and confidence levels:

```
Segment                    Forecast    Assumptions              Confidence  Owner
---------------------------------------------------------------------------
New Business - SMB         €1.5M       AE capacity, pipeline    MEDIUM      VP Sales
New Business - MM          €1.65M      AE capacity, pipeline    MEDIUM      VP Sales
Expansion                  €1.61M      GRR 92%, expansion 12%   HIGH        VP CS
Renewal                    €0.835M     GRR 97%, save rate 75%   HIGH        VP CS
Professional Services      €0.35M      Implementation capacity  MEDIUM      VP Services
---------------------------------------------------------------------------
BOTTOMS-UP TOTAL           €6.035M
```

**Narrative commentary:**

"Our bottoms-up plan of €6.035M assumes our sales team produces at historical productivity levels, existing customer base retains and expands as historically expected, and pipeline is generated at current rates. Key risks: New Business pipeline (€4.8M) is below 2-year average (€5.2M), suggesting pipeline-generation investment is not currently sufficient. Expansion assumes no change in customer health; if CS team delivers on success initiatives, upside exists."

## Step 6: Compare Bottoms-Up Against Capacity Model

Reconcile the two approaches:

```
Capacity Model Estimate:                €4.1M
Bottoms-Up Segment Sum:                 €6.035M
Variance:                               +€1.935M (bottoms-up is higher)

Analysis:
  - Capacity model assumes only new-business forecasting
  - Expansion + Renewal segments not captured in AE-quota model (separate CS metrics)
  - Bottoms-up correctly separates revenue types
  
Interpretation:
  - Capacity model baseline (AE productivity): €4.1M in new bookings
  - Expansion from retention: +€1.61M
  - Renewal from existing: +€0.835M
  - Total: €6.545M (theoretical if all segments hit)
  
Current bottoms-up (€6.035M) is conservative relative to capacity model
because pipeline-generation is a bottleneck in new business.
```

**Red flag:** If bottoms-up is significantly lower than capacity suggests, investigate:
- Is pipeline generation weak? (pipeline available per rep is below historical)
- Is deal velocity slowing? (sales cycle lengthened, win rate dropped)
- Is the team actually underperforming? (quota attainment is below 70%)

## Step 7: Document Assumptions in Shared Assumption Template

Transfer all key assumptions to a shared spreadsheet so Finance can validate and challenge. See `planning-assumptions-template.md` for the format.

**Example:** 

```
Assumption: New Business Win Rate 38%
Owner: VP Sales
Data Source: CRO School case analysis (Pavilion, 2025; €65K ACV, 8 customers won, 21 opportunities in pipeline)
Historical data: Last 12 months: 42%, Last 24 months: 40%, 3-year avg: 39%
Adjustment for 2026: -1% (one major competitor entering market)
Confidence: MEDIUM (competitive risk introduced)
Linked to: New Business capacity and pipeline coverage models
```

## Appendix: Pavilion Capacity Model (from CRO School Class 4)

For a worked example from Pavilion CRO School (original source: Pavilion CRO School Forecasting Worksheet, Class 4), the model structure is:

**Inputs:**
- AE headcount by tier (Mid-Market vs Enterprise)
- Monthly quota per tier
- Start dates for each rep (hire dates)
- Ramp period in months
- Quota achievement rate (e.g. 78% = expectation that reps will achieve 78% of quota)

**Outputs:**
- Monthly quota per rep (adjusted for ramp)
- Monthly quota by team (sum of reps)
- Period quota (3-month, 6-month, annual)

**Formula (per Pavilion):**

```
Monthly Quota for Rep = 
  IF(ramp_month_passed, full_monthly_quota, 
     full_monthly_quota * (days_into_ramp_month / total_days_in_month))
```

This allows fractional ramp when a hire date falls in the middle of a month.

**Example (from Pavilion worksheet):**

Hire date: 1 October
Ramp period: 3 months
Full ramp date: 1 January
Monthly quota: €50K

- October 1-31: Ramp in progress. Days into month = 31/31 = 100%. But ramp month = 1. Prorated: €50K × (31/31) = €50K (or 0%, depending on ramp model)
- November: Full month in ramp. Ramp month = 2. Partial output: €50K × 33% = €16.67K
- December: Full month in ramp. Ramp month = 3. Partial output: €50K × 67% = €33.33K
- January onwards: Ramped. Full quota: €50K/month

Total in ramp year: Jan-Sep = 9 × €50K + Oct-Dec = €150K = €600K annual
Annual contribution of this hire in first year = €600K (9 full months at quota + fractional ramp months)

**When to use this model:**
- Forecasting new-hire contribution to bookings
- Calculating team-wide capacity with turnover/hiring
- Adjusting annual targets for mid-year hiring decisions
- Modelling what-if scenarios (e.g. hire 3 AEs in Q2 vs Q1)

---

**Attribution:** Pavilion CRO School Class 4 (Forecasting and Financial Modeling), original authors Carter/Nalbandian/Dick, adapted by Neon Triforce 2026. Practitioner input from Louis Fumey (Atscale, 2026).
