# Planning Diagnostic: Full Interpretation and Remediation

Use this guide to interpret answers to the 10-question diagnostic from the main skill. Each question exposes a specific planning-process risk. This document provides interpretation, root cause, and remediation steps per question.

---

## Question 1: Do you have a formal planning calendar with locked dates for each phase?

### What this measures

Disciplines: Calendar discipline. Planning becomes ad-hoc if dates are not locked in advance. Reforecasts become reactive (driven by crisis, not data).

### If you answer YES

**Evidence of health:**
- Calendar is published to the revenue team 6 months in advance (e.g. in July, planning calendar for next year is locked)
- Each phase has clear entry and exit criteria (bottoms-up phase ends when all segment owners have submitted final numbers)
- Leadership respects the calendar; no "let's compress planning because Q3 got busy"

**What you still need to check:**
- Are phase gates actually enforced? Or does Finance still collect assumptions in week 8 when planning "ends" in week 7?
- Are time allocations realistic? (Typical mistake: allocate 2 weeks for reconciliation; takes 4 because assumptions are not locked)

### If you answer NO

**Root causes (check which apply):**
- Finance and Revenue run planning on different schedules (Finance fiscal year vs Revenue calendar year)
- CEO or board has not locked the approval date (so planning deadline floats)
- Previous year's planning was painful; team defaulted to ad-hoc to avoid repeating the pain

**Remediation (12 weeks to full discipline):**

**Week 1: Lock approval date**
- "What is the board approval deadline for next year's plan?" (Typically: Q4 of current year, e.g. October for calendar-year business)
- "If board approves in October, when must we have the plan ready?" (Typically: last week of September)
- "Working backwards, when do we start data gathering?" (Typically: 12 weeks before approval)

**Weeks 2-3: Design calendar**
- Use the planning calendar template from `references/planning-calendar-checklist.md`
- Map your fiscal year to the template (calendar year vs fiscal year)
- Assign phase owners (RevOps owns bottoms-up, Finance owns top-down, CFO owns reconciliation)
- Publish calendar to the team with clear deadlines per phase

**Weeks 4-12: Execute first cycle on new calendar**
- Measure adherence: did bottoms-up complete on schedule?
- Collect feedback: what phases were rushed? What needed more time?
- Adjust calendar for next cycle (but do not abandon it; consistent calendar beats perfect-but-inconsistent process)

**Success metric:** By end of Year 1, planning starts and finishes within one week of the published calendar, 90% of the time.

---

## Question 2: Can you produce the bottoms-up plan without Finance input?

### What this measures

Disciplines: Revenue team's understanding of capacity and pipeline independent of board expectations or aspirations. If you cannot produce bottoms-up without Finance, the team does not understand what it can actually produce.

### If you answer YES

**Evidence of health:**
- Every sales manager can articulate what their segment will produce this year and why
- Bottoms-up is data-driven (capacity model + known pipeline + segment assumptions)
- Sales feels ownership over the number; they made it, not Finance

**What you still need to check:**
- Is bottoms-up actually conservative? (Healthy: bottoms-up is 5-15% below strategic target, leaving room for stretch scenarios)
- Or is bottoms-up already optimistic? (Unhealthy: bottoms-up assumes productivity uplift that is not yet earned)

### If you answer NO

**Root causes (check which apply):**
- Sales team has never run a capacity model; they do not know their own production capacity
- Finance has historically set revenue targets top-down, and Sales has not built the discipline to work bottoms-up
- Pipeline data quality is poor (CRM is a dumping ground, not a source of truth)

**Remediation (8 weeks to bottoms-up discipline):**

**Weeks 1-2: Audit capacity**
- Run a bottleneck analysis: What constrains how much the sales team can produce?
  - Headcount? (How many AEs, SDRs, SEs do you have?)
  - Pipeline? (How much qualified pipeline are you generating monthly?)
  - Productivity? (How much does an average AE close annually?)
- Document the constraint. If headcount is not the constraint, it is usually pipeline generation or productivity assumptions.

**Weeks 3-4: Build capacity model (see bottoms-up-build-recipe.md)**
- Calculate: FTE × Ramp factor × Annual quota = Base capacity
- Adjust for: Known customer losses, expansion assumptions, new product adoption
- Document assumptions per segment (New Business, Expansion, Renewal)

**Weeks 5-6: Overlay known pipeline**
- Audit CRM for deals at or above threshold (e.g. >€50K ACV)
- Probability-weight each deal
- Compare named pipeline against capacity model expectation
- If named pipeline significantly exceeds or falls short of expectations, diagnose why

**Weeks 7-8: Lock bottoms-up**
- Consolidate capacity model + segment assumptions + named pipeline into a single bottoms-up forecast
- Every sales manager signs off on their segment
- Finance receives bottoms-up as a data input, not Finance-created number

**Success metric:** By end of Year 1, Sales can present bottoms-up forecast to Finance without Finance having participated in building it. Finance's role is validation, not creation.

---

## Question 3: Do you preserve three versions of the plan?

### What this measures

Discipline: Version control and audit trail. If you only keep the "final" plan, you cannot diagnose variance or learn from misses. You cannot see if the plan was wrong at the start or if execution failed.

### If you answer YES

**Evidence of health:**
- Bottoms-up original (BO) from Week 5 of planning calendar is locked in a file
- Finance stretch iteration (FS) from Week 7 is locked
- Plan of Record (POR) from Week 10 is the single source of truth, and it is clearly marked "Do not modify mid-year"
- Monthly reforecasts are saved as separate files (plan-reforecast-M3.md, etc.), not overwrites

**What you still need to check:**
- Are versions actually accessible to the team? (Healthy: shared drive, wiki, or CMS; Unhealthy: buried in email or inaccessible vault)
- Do people know which version to execute against? (Every rep should know: "We execute against the Plan of Record, not the BO")

### If you answer NO

**Root causes:**
- No version-control discipline established (each cycle's plan overwrites the previous one)
- Reforecasts are treated as "updates" to the plan, not separate snapshots
- File naming is inconsistent (plan.xls, plan-2.xls, final-plan.xls) making it unclear which is current

**Remediation (4 weeks to version control):**

**Week 1: Establish naming convention**
- Bottoms-Up Original: `annual-plan-2026-bottoms-up-original.md` (locked after reconciliation)
- Finance Stretch: `annual-plan-2026-finance-stretch.md` (locked after reconciliation)
- Plan of Record: `annual-plan-2026-plan-of-record.md` (locked after board approval)
- Reforecasts: `annual-plan-2026-reforecast-M5.md`, `annual-plan-2026-reforecast-Q2.md` (each locked after completed)

**Week 2: Migrate existing plans to new naming**
- If last year's plan exists, copy and rename to the versioning convention
- Create a "Plan Archive" folder with all prior years

**Weeks 3-4: Lock each version after creation**
- After bottoms-up is finalised, move to read-only or mark "Locked: do not modify"
- After reconciliation, mark FS and POR as locked
- Only allow reforecasts to create new dated files

**Success metric:** By end of Year 1, team can retrieve any version of the plan from the last 2 years and compare forecast vs actual. Variance analysis is possible.

---

## Question 4: Can you explain every euro of stretch target with a named scenario?

### What this measures

Discipline: Accountability for stretch goals. If Finance adds a stretch without owners, it is a wish, not a plan. Sales will not believe it and will not execute it.

### If you answer YES

**Evidence of health:**
- Stretch breakdown document exists: €8.5M POR = €7.8M BO + €0.5M Scenario A + €0.2M Scenario B
- Each scenario has: name, owner, explicit assumptions, and dependencies
- Examples:
  - Scenario A: "Hire 2 AEs in Q1, achieve €850K quota each = +€350K" (Owner: VP Sales)
  - Scenario B: "Improve expansion velocity 15% vs 12%, requires CS investment = +€200K" (Owner: VP CS)
- Scenarios are tracked monthly: "Scenario A hiring on schedule (2 AEs hired Jan 1)"; "Scenario B CS playbook launched Feb 1"

**What you still need to check:**
- Do reps know about scenarios? (Healthy: scenarios communicated to revenue team as "these are the ways we close the gap"; Unhealthy: only leadership knows)
- Are scenarios dependent on each other or independent? (Clarify to avoid double-counting)

### If you answer NO

**Root causes:**
- Finance sets top-down target, Sales negotiates, they meet in the middle, everyone forgets why
- Stretch is spread across teams without conversation ("Sales, your quota is +15%; Marketing, yours is +20%"; no logic to distribution)
- Stretch is vague ("We just need to do better this year")

**Remediation (4 weeks to scenario discipline):**

**Week 1: Identify the gap**
- Bottoms-up: €7.8M
- Top-down target: €8.5M
- Gap: €0.7M
- Question: "If we do nothing different, we produce €7.8M. What specific actions close the €0.7M gap?"

**Week 2: Brainstorm scenarios (no filters)**
- Hiring: "If we hire 2 AEs in Q1, add €350K"
- Expansion: "If CS team improves retention and expansion, add €150K"
- Pipeline: "If ABM campaign runs, add €100K in pipeline (Year 1 close rate TBD)"
- Pricing: "If we raise prices 5%, add €390K"
- New product: "If new product launches on schedule, add €200K"
- Other: "Churn reduction, partner channels, etc."

**Week 3: Assign owners and validate**
- For each scenario, assign an explicit owner
- Owner validates: "Yes, this is achievable with these assumptions and this cost"
- Document: Scenario card with scenario name, owner, assumptions, cost/investment, timeline

**Week 4: Build scenario matrix**
- Scenarios that complement each other (can both happen): Group A (Hiring + Expansion)
- Scenarios that substitute (can only do one): Pricing OR new product
- Required vs optional scenarios: Which scenarios must happen to hit plan?
- Likely scenario combination: Most probable mix given constraints

Example outcome: €8.5M plan = €7.8M BO + Hiring (€350K) + Expansion (€150K) + 50% of ABM upside (€50K). All scenarios are independent and execution is on different timelines.

**Success metric:** By end of Year 1, every stretch in the plan has an owner and a documented scenario. Reps know "we're hitting plan if we hire on schedule, improve CS metrics, and start ABM". No mystery.

---

## Question 5: Does every reforecast compare current projection against POR AND bottoms-up?

### What this measures

Discipline: Learning from variance. If you only compare forecast vs plan, you miss diagnostics. Comparing forecast vs bottoms-up tells you if capacity changed or if execution slipped.

### If you answer YES

**Evidence of health:**
- Monthly reforecast template includes three columns:
  - Plan of Record (€8.5M)
  - Bottoms-Up Original (€7.8M)
  - Current Forecast (€7.9M)
- Analysis: "Forecast is down €0.6M from POR. Versus BO, forecast is up €0.1M. Meaning: capacity is slightly better than expected, but we're down vs plan because of deal slippage or lower-than-expected pipeline generation."

**What you still need to check:**
- Does the team actually use this comparison? (Healthy: monthly sync discusses "why forecast vs BO changed"; Unhealthy: team only stares at "we're down vs plan")

### If you answer NO

**Root causes:**
- Reforecasting template only tracks "Plan vs Actual/Forecast"; no comparison to bottoms-up
- Bottoms-up is locked and forgotten; reforecasts never reference it
- Team does not know the difference between capacity miss (production lower than capacity), execution miss (production lower than forecast), and planning error (forecast was wrong)

**Remediation (2 weeks to reforecast comparison):**

**Week 1: Redesign reforecast template**
- Add three columns:
  - Original Bottoms-Up (locked, read-only)
  - Plan of Record (locked, read-only)
  - Current Forecast (most recent data)
- Add calculation columns:
  - Variance from POR: (Current - POR) / POR %
  - Variance from BO: (Current - BO) / BO %

**Week 2: Pilot new template in next reforecast**
- Use template to compare forecast vs both anchors
- Discuss interpretation: If forecast is between BO and POR, what explains the position?
  - Forecast closer to BO: Execution is lagging capacity (fix: improve conversion, deal velocity, pipeline generation)
  - Forecast closer to POR: Execution is tracking plan (status quo)
  - Forecast above POR: Upside is real; upside scenarios are materialising (opportunity to stretch further)

**Success metric:** By end of Year 1, reforecasts include three-way comparison (BO, POR, Current). Team can articulate "we're down vs plan because pipeline generation missed, not because of productivity loss".

---

## Question 6: Have you documented what may NOT change mid-year?

### What this measures

Discipline: Stability and accountability. If everything can change, the plan is not a plan; it is a wish list. Mid-year reforecasts should be updates to projections, not rewrites of the entire strategy.

### If you answer YES

**Evidence of health:**
- Document exists: "Locked Parameters (do not change mid-year)"
  - Quota targets (change only at annual reset)
  - Headcount plan (hiring pace already committed to board)
  - Compensation structure (changes only at annual reset)
  - Strategic positioning / ICP (changes only with GTM strategy refresh)
- Document also lists "Flexible Parameters (reforecast freely)"
  - Revenue target (adjust up or down based on actual)
  - Pipeline assumptions (conversion rates, velocity)
  - Stretch scenarios (can reassign owners if dependencies shift)

**What you still need to check:**
- Does leadership respect these parameters? (Healthy: CEO pushes back on mid-year comp structure change; Unhealthy: comp structure gets re-levered every quarter)

### If you answer NO

**Root causes:**
- No explicit distinction between "plan" (stable) and "forecast" (current projection)
- Leadership treats all plan elements as flexible
- Team reacts to every variance by changing targets or structures instead of improving execution

**Remediation (3 weeks to locked-parameter discipline):**

**Week 1: Define locked parameters for your business**
- Quota targets: Typically locked (rep behaviour anchors to quota; changing mid-year creates chaos)
- Headcount plan: Typically locked (hiring takes time; plan assumes certain hire dates and ramp curves)
- Comp structure: Typically locked (changes mid-year are demoralising and legally complex)
- Strategic positioning: Typically locked (changing ICP mid-year cascades to every team)

- **Exception**: If the business faces existential crisis (major customer churn, competitor disruption), reconsider locked parameters as a special gate

**Week 2: Define flexible parameters**
- Revenue target: Can reforecast down (or up) based on new data
- Pipeline assumptions: Can adjust conversion rates and velocity if market conditions change
- Stretch scenarios: Can reassign owners or extend timelines if dependencies slip
- Reforecast cadence: Can shift from monthly to quarterly if business stabilises

**Week 3: Publish "What Cannot Change" to the team**
- Frame it as stability and clarity: "Here is what we are committing to; here is what we will adjust as we learn."
- Tie locked parameters to business stability: "We lock comp structure mid-year to avoid rep chaos. We will adjust it once a year."
- Clarify exceptions: "If [specific major event], we will revisit locked parameters with a 2-week evaluation window."

**Success metric:** By end of Year 1, reforecasts change projections and scenarios, not fundamentals. Comp structure, headcount plan, and quota targets remain stable Q1-Q4.

---

## Question 7: Do FP&A and RevOps jointly review every material forecast change in real time?

### What this measures

Discipline: Collaboration and trust. If one function surprises the other mid-quarter, plans unravel. Sync discipline prevents that.

### If you answer YES

**Evidence of health:**
- Weekly 30-min sync scheduled (every Monday or Tuesday, same time)
- Agenda: "Any forecast signals this week? Any pipeline red flags? Any reforecast triggers firing?"
- Format: RevOps reports key signals (pipeline coverage, conversion rates, deal slippage); FP&A models financial implications
- Follow-up: If signal is material, it goes into next monthly reforecast (scheduled at quarter-end)

**What you still need to check:**
- Does the sync prevent surprises? (Healthy: CFO hears about coverage drop before board meeting; Unhealthy: CFO learns about it from board in real-time)

### If you answer NO

**Root causes:**
- RevOps and FP&A do not have a relationship; they meet only during formal planning/reforecasting
- One function does not trust the other's data or judgment
- Sync happens, but it is one-directional (one function reports; the other does not engage)

**Remediation (4 weeks to joint review discipline):**

**Week 1: Calendar the sync**
- 30 minutes, recurring, same day/time every week
- Attendees: VP RevOps (or Head of Sales), CFO or Finance lead
- Format: Standing agenda + time for ad-hoc signals

**Week 2: Design agenda template**
- Pipeline signals (coverage ratio, velocity, slippage %, at-risk deals)
- Forecast signals (last week's close rate, pipeline conversion trend, deal-size movement)
- Reforecast triggers (is any trigger firing? E.g. coverage dropped below 2.5x, variance exceeded ±20%)
- Financial implications (if forecast is revised, what is working-capital impact?)
- Next steps (any escalation needed? Any reforecast warranted?)

**Week 3: Run first 3 syncs, refine agenda**
- Week 1 sync: Likely awkward (people do not know what to discuss)
- Week 2 sync: Smoother (patterns emerge: what signals matter most)
- Week 3 sync: Productive (both functions come with data and questions)

**Week 4: Lock sync into operating cadence**
- Sync is now "normal operating rhythm", not optional
- If a participant misses, they get notes (sync still happens)
- Quarterly reforecasts reference prior 12 weeks of sync signals (creates continuity)

**Success metric:** By end of Year 1, CFO never learns about material forecast changes from external sources (board, investors) before hearing from RevOps in the sync.

---

## Question 8: Can you articulate the specific triggers that force a reforecast?

### What this measures

Discipline: Data-driven reforecasting, not reactive panic. If triggers are undefined, reforecasting is ad-hoc ("We reforecast when leadership asks, or when we miss, or when we feel like it").

### If you answer YES

**Evidence of health:**
- Trigger list exists: "We reforecast when any of these fire:"
  - Pipeline coverage falls below 2.5x
  - Month-end close rate drops below 60% of plan
  - Forecast accuracy variance exceeds ±20% for two consecutive months
  - Named-deal slippage exceeds 50%
  - NRR drops below 105%
  - CAC payback exceeds 14 months
  - Actual revenue variance from plan exceeds 15% for two consecutive periods
- Process: When a trigger fires, the team has 5 business days to reforecast and update the Plan of Record

**What you still need to check:**
- Are triggers actually monitored? (Healthy: RevOps dashboard tracks all triggers weekly; Unhealthy: triggers are theoretical, no one watches them)

### If you answer NO

**Root causes:**
- No defined triggers (reforecasting is "when leadership wants it")
- Triggers exist, but they are not monitored (no dashboard, no weekly review)
- Triggers are too loose (e.g. "forecast changes more than 5%", which fires constantly)

**Remediation (3 weeks to trigger discipline):**

**Week 1: Define triggers for your business**
- Revenue-side triggers: Pipeline coverage, close rate, forecast accuracy, deal slippage
- Unit-economics triggers: NRR, CAC payback, gross margin
- Execution triggers: Actual variance from plan, headcount plan slippage
- External triggers: Competitor disruption, macro changes

**Week 2: Set threshold values**
- Pipeline coverage threshold: Below 2.5x (critical)
- Close rate threshold: Below 60% of expected monthly rate
- Forecast accuracy threshold: ±20% variance for 2 consecutive months
- Deal slippage threshold: >50% of named pipeline slips

**Week 3: Wire triggers into dashboard**
- RevOps dashboard flags when a trigger threshold is breached
- Weekly review: Scan dashboard for any red flags
- If trigger fires: 5-day reforecast window; RevOps + FP&A reforecast and update plan

**Success metric:** By end of Year 1, reforecasting is data-driven. You can show that every reforecast was triggered by a specific metric breach, not by ad-hoc leadership request.

---

## Question 9: Do your reps know the plan and understand their targets?

### What this measures

Discipline: Plan communication. A plan that only the leadership team knows is not a plan; it is a secret. Reps need to understand what they are being held accountable to and why.

### If you answer YES

**Evidence of health:**
- Every sales manager can articulate: "Our team target is €X. Here is why. Here is how it breaks down by territory/segment."
- Reps can answer: "What are we stretching on this year?" (Example: "We're investing in ABM; that's +€250K of uplift if it works")
- Reps know: "Which customers are we trying to retain?" "Which segments are we pushing?" "What is our pipeline generation target?"

**What you still need to check:**
- Does the plan feel real to reps? (Healthy: reps believe they can hit it; Unhealthy: reps think it is aspirational fantasy)

### If you answer NO

**Root causes:**
- Plan is communicated top-down without context (reps receive a number; they do not understand drivers)
- Plan is not communicated to reps at all (it lives in executive slides)
- Plan communication is generic ("We need to grow 20%") instead of specific ("Here is what each territory needs to produce")

**Remediation (2 weeks to plan communication):**

**Week 1: Create segment-specific plan comms**
- For New Business team: "Plan is €X. Here is the breakdown by account tier and territory. Here is the pipeline we have today and what we need to generate."
- For Expansion team: "Plan is €X. We are assuming 92% GRR and 12% net expansion. Here are the accounts and customers where we need to move the needle."
- For Renewal team: "Plan is €X. We are assuming 97% GRR with 75% save rate on at-risk books. Here are the 10 highest-risk renewals."

**Week 2: Present plan to revenue team**
- VP Sales or VP CS presents bottoms-up build (data-driven, not aspirational)
- Explain scenarios (e.g. "We're stretching because of ABM, because of hiring, because of CS investment; here is what each scenario requires")
- Invite questions: "Does this feel achievable? Are we missing a lever? Do you have data that contradicts our assumptions?"

**Success metric:** By end of Year 1, reps can recite their segment target and explain in their own words how it was built (capacity + known pipeline + growth assumptions).

---

## Question 10: When the plan misses, can you trace the miss to an assumption?

### What this measures

Discipline: Root-cause learning. If you cannot diagnose plan misses, you will repeat them. This is the ultimate health check.

### If you answer YES

**Evidence of health:**
- Year-end variance analysis exists: "Projected €8.5M, closed €7.9M, miss of €0.6M"
- Analysis traces miss to assumptions:
  - "New Business pipeline was €4.8M; we expected 60% close, got 52%. Pipeline conversion was the miss, not headcount." (Implication: Next year, invest in pipeline generation earlier or improve qualification)
  - "Renewal GRR was 94%, not 97%. We lost 3 large accounts. Root cause analysis: CS team was under-resourced in Q2." (Implication: Next year, hire CS capacity earlier)
  - "Expansion grew 10%, not 12%. Customers did not adopt new product as expected." (Implication: Next year, assume 8-10% until product adoption improves)

**What you still need to check:**
- Are learnings actually incorporated into next year's plan? (Healthy: bottoms-up for Year 2 uses 94% GRR and 52% new-business close rate; Unhealthy: team repeats the same assumptions)

### If you answer NO

**Root causes:**
- Plan miss is blamed on "market" or "execution" (generic) instead of specific assumptions (diagnostic)
- Plan is never compared to actual (no formal variance analysis)
- Variance is documented, but learnings do not flow into next year's planning

**Remediation (ongoing, 52 weeks to full cycle):**

**At plan miss (quarter/year end):**

1. **Variance analysis (week 1)**
   - Plan vs actual by segment
   - Compare forecast from each month-start to actual that month (reveals forecast accuracy decay)
   - Identify which segments hit, which missed, by how much

2. **Assumption audit (week 2)**
   - Return to original plan document
   - For each segment, compare original assumptions to actual results
   - Create assumption-miss table:

```
Assumption               Original    Actual    Variance    Impact (€)
---
New Biz close rate       60%         52%       -8ppts      -€380K
Expansion rate           12%         10%       -2ppts      -€180K
Renewal GRR              97%         94%       -3ppts      -€69K
New hires (FTE/ramp)     1.8 FTE     1.5 FTE   -0.3 FTE    -€255K
---
Total plan miss:                                            -€884K
```

3. **Root-cause analysis (week 3)**
   - For each assumption miss, diagnose why:
     - New Biz close rate: Longer sales cycle? Higher deal complexity? Competitor pressure?
     - Expansion rate: Customer adoption delay? Capacity constraints? Pricing resistance?
     - Renewal GRR: Specific customer losses or broad churn acceleration?
   - Gather supporting data: deal length, product usage, customer NPS, win/loss analysis

4. **Learning summary (week 4)**
   - Document for the record: "What did we learn this year that changes how we plan next year?"
   - Example: "Sales cycles have lengthened from 60 to 75 days. Next year's plan should assume longer sales cycles, which means either higher pipeline or earlier pipeline generation."

**For next year's planning:**

5. **Incorporate learnings into bottoms-up (week 5 of next planning cycle)**
   - Updated assumptions for segment forecasts:
     - New Biz close rate: 52% (down from 60% assumption; now data-driven)
     - Expansion rate: 10% (down from 12% assumption; actual pace)
     - Renewal GRR: 94% (down from 97%; one large loss is now historical data)
   - Updated headcount plan: If ramp is slower than expected, account for it in hiring plan

6. **Document the improvement**
   - Comparison: "Last year we assumed 60% close rate; we got 52%. This year we are assuming 52%, +2% upside for process improvements."
   - Rationale: "We are being more conservative because sales cycle lengthened; if we improve pipeline velocity (specific initiative), we can reach 55%."

**Success metric:** By end of Year 2, every significant assumption miss from Year 1 is corrected in Year 2's plan, with documented rationale for any changes.

---

## Scoring Rubric

**8-10 YES answers: Strong planning discipline**
- Revenue planning is a competitive advantage for your company
- You have the infrastructure to scale: you understand capacity, you forecast accurately, and you learn from variance
- Continue to refine and maintain discipline (it can erode under pressure)

**5-7 YES answers: Process gaps exist**
- You have some discipline, but there are blind spots
- Pick the two lowest-scoring questions and build remediation into next planning cycle
- Expect improvement over 12 weeks for each gap you tackle

**Fewer than 5 YES answers: Plan for the planning process itself**
- Your process is ad-hoc or reactive
- Do not try to build a perfect plan; focus first on building a disciplined process
- Recommended sequence:
  1. Establish planning calendar (locked dates)
  2. Build bottoms-up capability (team understands capacity)
  3. Lock versions (audit trail, learning)
  4. Communicate plan (reps know targets)
  5. Then iterate on reconciliation, reforecasting triggers, FP&A partnership
- Target: Reach "5-7 YES answers" by end of Year 1. Reach "8-10 YES answers" by end of Year 2.

---

## Common Mistake: "We'll improve planning next year"

Do not wait. Pick one question where you scored NO. Remediation takes 2-4 weeks. Run a pilot on this year's reforecasting (or on next year's planning cycle if the year is over). By the time you finish pilot, you will have built the discipline to make it permanent.

---

**Attribution:** FP&A Today podcast (Aaron Sallade, Michelle Govindsamy, Zachary Rial), RevOps Lab podcast #57 (Shantanu Shekhar), Pavilion CRO School, Atscale practitioner input (Louis Fumey, 2026).
