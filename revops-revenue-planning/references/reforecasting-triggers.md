# Reforecasting Triggers Matrix

A reforecasting trigger is a data-driven signal that business conditions have changed materially. When a trigger fires, the revenue and finance teams have 5 business days to reforecast and update the Plan of Record.

## Trigger Matrix

| Category | Trigger | Threshold | Owner | Response | Timeline |
|---|---|---|---|---|---|
| **Revenue Signals** | | | | | |
| Pipeline Health | Coverage falls below 2.5x | <2.5x of revenue target | RevOps | Escalate to VP Sales; assess pipeline generation plan | 2 days |
| | Coverage falls below 2.0x | <2.0x of revenue target | RevOps | Critical escalation; pause hiring/spend unless pipeline generation plan is reset | 1 day |
| Close Rate | Month-end close rate drops below threshold | <60% of expected rate for 2 consecutive months | RevOps | Reforecast; diagnose cause (deal velocity, qualification, competition) | 5 days |
| Forecast Accuracy | Forecast variance exceeds band | ±20% for 2 consecutive months | RevOps | Reforecast; audit forecast categories and rep calibration | 5 days |
| Deal Slippage | Forecast pipeline slips | >50% of named deals slip past period end | RevOps | Reforecast; assess which scenarios are at-risk | 3 days |
| **Unit Economics** | | | | | |
| Retention | NRR drops below threshold | <105% (Ebsta 2025 benchmark: healthy is 105%+) | VP CS | Reforecast; assess if churn is customer-specific or systemic | 5 days |
| CAC Payback | Payback period exceeds threshold | >14 months (revenue forecasting best practice, 2025-2026) | VP Marketing | Reforecast; evaluate if CAC reduction or ACV increase is needed | 5 days |
| Margin | Gross margin drops below plan | >3% below plan for 1 quarter | VP Services/Delivery | Reforecast; model impact on profitability | 5 days |
| **Execution Signals** | | | | | |
| Variance from Plan | Actual revenue vs Plan of Record | >15% miss for 2 consecutive periods | Revenue + Finance | Full reforecast; update segment forecasts | 5 days |
| Headcount Slippage | Hiring plan misses by >1 FTE | Hire missed by end of planned month | VP Sales | Reforecast; adjust capacity model and expectations | 5 days |
| Customer Loss | Major customer churn | >$100K ACV customer loss (or equivalent % of revenue) | VP CS/VP Sales | Escalate immediately; reforecast if systemic churn emerges | 1 day |
| **External Signals** | | | | | |
| Competition | Major competitor enters market / launches new product | Competitor closes 3+ deals we bid on in month | VP Sales/Marketing | Reforecast; assess win-rate impact | 5 days |
| Market | Macro economic shift with revenue impact | Recession declared, credit market freezes, or industry layoff wave | CEO/CFO | Rapid scenario analysis; reforecast likely | 2 days |
| Product | Product release delay >6 weeks | Feature/product launch slips beyond planned date | VP Product | Reforecast if revenue plan assumes the release | 3 days |

---

## Reforecasting Process by Trigger Type

### Revenue Triggers (Pipeline, Close Rate, Forecast Accuracy, Slippage)

**Timeline:** 5 business days from trigger fire to updated forecast

**Day 1: Diagnosis**
- RevOps meeting: What changed? Is it temporary noise or a signal?
- Example: Close rate dropped from 65% to 55% (trigger fired at 60% threshold). Diagnosis:
  - Are deals taking longer to close? (Yes, sales cycle lengthened from 60 to 75 days)
  - Is deal quality lower? (No, deal-to-close conversion still 38%)
  - Are reps more pessimistic? (No, deals in pipeline are same as prior month)
  - Conclusion: Sales cycle lengthened; forecast should adjust out by 15 days, which pushes some closes into next period.

**Days 2-3: Segment Reforecast**
- For New Business: If close rate is lower because of longer sales cycles, extend pipeline assumed close dates. Result: New Business forecast down 10-15%.
- For Expansion: If close rate is lower due to customer adoption delays, push expansion timing. Result: Expansion forecast down 5-10%.
- For Renewal: If close rate is lower due to longer legal reviews, push renewal close dates but expect higher ultimate close rate. Result: Renewal forecast slight down in near term, recovery in following period.

**Day 4: Finance Impact Analysis**
- Cash implications: If revenue is pushed into next period, what is working-capital impact?
- Expense implications: If we miss plan, do we need to constrain spending?
- Board implications: How do we communicate this to the board?

**Day 5: Updated Forecast + Communication**
- Publish updated forecast: "Reforecast M4: $7.6M (down from $7.9M Plan of Record)"
- Rationale: "Close rate signal suggests sales cycles have lengthened 15 days. We expect recovery next period. See attached scenario analysis."
- Team communication: Sales managers meet with their teams to explain: "Close rates are down this month because of longer sales cycles, not deal quality. Here is what we're doing about it."

### Unit-Economics Triggers (NRR, CAC Payback, Margin)

**Timeline:** 5 business days

**Day 1: Diagnosis**
- Example: NRR dropped from 110% to 102% (trigger fired at 105% threshold)
- Diagnosis: Is churn accelerating? Are customers not expanding?
  - Check customer cohorts: New customers (Year 1) churn rate vs mature customers (Year 3+)
  - Check expansion by segment: SMB expanding? Mid-Market? Enterprise?
  - Conclusion: Year 1 cohorts have higher churn (85% GRR) than expected (92% GRR)

**Days 2-3: Reforecast with Updated Assumptions**
- Renewal forecast: If Year 1 churn is 15%, Year 2 churn is 8%, Year 3+ churn is 3%, apply cohort-specific retention to renewal forecast
- Expansion forecast: If expansion rate is lower (10% instead of 12%) due to adoption delays, revise segment forecast
- Impact: Renewal forecast down 5-8%, Expansion forecast down 3-5%

**Days 4-5: Mitigation Plan**
- CS team proposes: "To reverse NRR decline, we need to: invest in onboarding (reduce Year 1 churn to 92%), accelerate customer success plays (increase expansion to 12%)"
- Cost: +$120K investment
- Timeline: 90 days to see improvement
- Reforecast includes mitigation scenario: "Base case (no change): NRR stays at 102%. Mitigation case (CS investment): NRR recovers to 107% by quarter-end"
- Board communication: "NRR dipped to 102% this quarter. Root cause: Year 1 cohort churn. We are investing $120K in CS to reverse it; expect recovery by Q3."

### Execution Triggers (Variance, Headcount, Customer Loss)

**Timeline:** 5 business days (or 1 day for major customer loss)

**Example: Actual Revenue Misses Plan by 15%+ for 2 Consecutive Months**

**Month 1:** Target $700K, closed $595K (15% miss, trigger not yet fired, but flagged)
**Month 2:** Target $700K, closed $612K (12.5% miss, trigger fires; 2 consecutive months with >12.5% miss)

**Day 1: Emergency diagnosis**
- What changed between months 1 and 2? Did close rate improve? Did velocity improve?
  - Yes: Close rate improved from 45% to 52%, velocity improved from 65 days to 58 days
  - Implication: Issue is not getting worse; it is improving
- But we are still 12%+ behind plan. Why?
  - Pipeline: Month 1 start had $2.8M pipeline (2.8x coverage); Month 2 start had $3.0M (3.0x coverage). Pipeline is healthy.
  - Velocity: Sales cycle improved but still 15 days longer than plan assumed.
  - Conclusion: Sales cycle assumption in plan was too optimistic. At-close forecast needs to adjust.

**Days 2-3: Segment-by-Segment Reforecast**
- Recalculate expected close rate if sales cycle is 15 days longer: use historical stage-to-close timing
- New-business forecast: Down 8% (longer cycle means fewer deals close in-period)
- Expansion forecast: Slight impact (faster motion, but still affected by longer cycles)
- Renewal forecast: Minimal impact (renewal cycles longer anyway, overestimate was small)

**Days 4-5: Updated Forecast + Root-Cause Fix**
- New forecast: $2.1M monthly (annualized: $25.2M vs $27.6M plan; 8.5% below plan)
- Root cause: Sales cycle assumption in original plan was 60 days; actual is 75 days
- Fix: Improve sales cycle by 10 days through: earlier qualification calls, concurrent approvals/legal, customer success escalation on implementation
- Timeline: 30-day pilot; measure if cycle reduces to 68 days
- Board communication: "We missed plan by 12.5% in consecutive months. Root cause: sales cycle lengthened 15 days vs assumption. We are targeting 10-day reduction through process improvements. Revised plan: $2.1M monthly (8.5% below POR)."

### External Triggers (Competition, Market, Product)

**Timeline:** 2-5 days depending on severity

**Example: Major Competitor Enters Market with Aggressive Pricing**

**Day 1: Rapid Assessment**
- Intelligence: "Competitor X launched product at 40% price discount. They have closed 3 of our prospects in the past 2 weeks."
- Market impact: Is this a pricing war, or is it a product/positioning move?
  - If pricing war: Many competitors will follow; our win rate will drop
  - If product positioning: Only affects premium-segment prospects; SMB/mid-market unaffected
- Implication: Depends on assessment

**Day 2: Sales Team Input**
- Sales leadership: "We've lost these 3 deals because of price. But we have 8 more at-risk. How many will we actually lose?"
  - Optimistic (1-2 more losses): Our value prop holds; win rate drops from 38% to 35%
  - Realistic (4-5 more losses): Win rate drops from 38% to 32%
  - Pessimistic (8 more losses): Win rate drops from 38% to 22%; major revenue miss

**Days 3-4: Scenario Analysis**
- Build three reforecast scenarios:
  - Optimistic: Win rate 35%, New Business revenue down 8%, Total plan down 3%
  - Realistic: Win rate 32%, New Business revenue down 12%, Total plan down 5%
  - Pessimistic: Win rate 22%, New Business revenue down 42%, Total plan down 15%
- Model probability: "We assign 20% to optimistic, 60% to realistic, 20% to pessimistic. Weighted forecast: down 6.5% from plan."

**Day 5: Mitigation + Communication**
- Sales: "We are repositioning: we focus on value (time-to-ROI, implementation simplicity) over price. We are not matching the discount; we are changing the conversation."
- Product: "We accelerate two features that are competitive differentiators."
- Marketing: "We launch campaign highlighting our customer success stories and time-to-value."
- Timeline: 60 days to measure if repositioning helps
- Forecast: "Assuming realistic scenario (6.5% miss), we reforecast to $8.0M. If repositioning works, we expect recovery in 60 days. If it doesn't, we face bigger structural challenge."
- Board communication: "Competitive disruption observed. Immediate response: repositioning focus. 60-day outlook: adjusted down 6.5%. Structural response timeline: 90 days."

---

## Locked vs Flexible Parameters (Revisited in Reforecasting Context)

**Do NOT reforecast these (locked mid-year):**
- Quota targets (changing creates rep chaos and sandbagging)
- Headcount plan (hiring takes time; cannot adjust mid-period)
- Compensation structure (mid-year changes are demoralizing and legally complex)

**DO reforecast these (flexible):**
- Revenue targets (adjust down if execution is weaker; adjust up if opportunities emerge)
- Pipeline assumptions (conversion rates, velocity, mix can shift with market conditions)
- Stretch scenario owners (can reassign if dependencies change)

**Rare exceptions to locked parameters:**
- If a major customer churns (>10% of revenue), headcount plan might need to adjust
- If market dramatically shifts (recession), comp structure might need emergency suspension of upside accelerators
- These are escalations to CEO/board; they are not RevOps decisions

---

## Reforecasting Cadence Guardrails

**Minimum reforecasting frequency:** Quarterly (prevents total disconnect from reality)

**Maximum reforecasting frequency:** Weekly forecast reviews (operational check-in), but full reforecasts monthly or quarterly (prevent organizational paralysis)

**Standard rhythm:**
- Weekly forecast call: Check for triggers; do not reforecast unless trigger fires
- Monthly forecast review: Compare current forecast vs Plan of Record; document if gap is widening
- Quarterly full reforecast: Update all segment assumptions; reconcile Finance vs Revenue; lock revised forecast

**Exception:** If multiple triggers fire in one week (e.g. coverage drops + close rate drops + major customer churn), escalate immediately; do not wait for month-end. Single reforecast that addresses all triggers is cleaner than multiple mini-reforecasts.

---

**Attribution:** Fincome (trigger-based reforecasting best practices, 2025), ORM Technologies (forecast accuracy variance thresholds), RevOps benchmarks consensus (unit-economics triggers), Ebsta 2025 GTM Benchmarks Report (NRR, pipeline coverage thresholds), revenue forecasting best practices (2025-2026).
