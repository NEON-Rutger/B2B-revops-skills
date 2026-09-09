# Stage guide: which skill at which company stage

Most skills in this library were written for a company that already has a repeatable sales motion and named owners. Since v1.7.0, 16 of them open with a stage check that sorts the company into one of four situations and says what to run at each. This page holds the shared definition and the map across those 16 skills.

## The four situations

This skill was written for a company that already has a repeatable motion and named owners. Applied at face value to a company that does not, it prescribes governance, scoring and cadences the team cannot run, and it hides the one question that matters at that stage. Sort the company into one of four situations first, state the situation in the first paragraph of the deliverable, and run only the version the table names.

1. Start-up, pre product-market fit. Fewer than roughly 30 comparable customers (practice-based threshold). Wins came from the founders' network or referrals, not from a process anyone could repeat. No segment has a measured win rate or cycle time. Retention is not tracked. The CRM, if there is one, is a contact list. Nobody carries a quota. The only question that matters: do existing customers get the outcome they were promised, and would they buy again? Run the minimum version of this skill, or do not run it.

2. Start-up, product-market fit. At least one segment with 10 or more customers won the same way (practice-based threshold). A known win rate and cycle time for that motion. Retention measured monthly. The founders still do most of the selling, with a few early reps. One person owns the CRM and can trace how recent deals moved. Run the skill for that one motion only; treat thresholds as guidance, not rules.

3. Scale-up. Sales, marketing, customer success and operations each have a named owner. The CRM holds stage history the team trusts. Reps carry quota. There is a forecast that someone is held to. Growth is a question of capacity and constraints: which function breaks first when volume doubles. Run the full skill.

4. Enterprise. Everything in situation 3, plus more than one revenue organisation: business units, regions or product lines with their own plan and their own leader. A governance layer sits above go-to-market decisions (steering committee, works council, legal or compliance gates). Finance owns the revenue target that goes to the board. The CRM may run as several instances or with many administrators. Run the full skill with the enterprise deltas named in the table: aggregation across units, governance and change management, longer decision paths.

If the evidence is thin, ask three yes or no questions: Is there a segment with 10 or more customers won the same way? Is retention measured monthly? Does someone own the CRM as part of their job? Three no answers means situation 1. One or two yes answers means situation 2. Three yes answers means situation 3 or 4; then ask three more: Is there more than one business unit or region with its own revenue plan and leader? Do go-to-market decisions pass through a formal governance layer? Does finance own the revenue target for board reporting? Two or more yes answers means situation 4; otherwise situation 3.

The full skill applies to both scale-up and enterprise. Not every skill applies at every stage; the table below says what this skill does at each, and "do not run" is a valid answer.

## What the four ratings mean

"Do not run" means the skill would produce structure the company cannot use yet. "Minimum version" is the cut-down form described in the skill's own stage table. "One motion" means run it for the single repeatable motion only, with thresholds as guidance. "Full" means the whole skill; enterprise adds the deltas named in the skill's table (aggregation across units, governance and change management, longer decision paths).

## Stage to skill map

| Skill | Start-up, pre PMF | Start-up, PMF | Scale-up | Enterprise | Use it when |
|---|---|---|---|---|---|
| `cs-operations` | minimum version | one motion | full | full | When renewal conversations are reactive or accounts churn unpredictably, build a proactive health scoring system and CS playbooks to identify at-risk customers and drive retention revenue. |
| `deal-qualification-gates` | do not run | one motion | full | full | When pipeline is full of zombie deals or forecast accuracy suffers, install evidence-quality gates to kill unqualified deals early and accelerate closure on real ones. |
| `expansion-revenue-architect` | do not run | minimum version | full | full | When NRR is below 110% or GRR is stable but expansion revenue is minimal, design an expansion system to grow customer lifetime value through upsell, cross-sell and vertical expansion. |
| `gtm-planning` | do not run | one motion | full | full | When scaling revenue org or entering new markets, design GTM motions aligned to customer segments, calculate sales capacity needed to hit targets, and structure territories and teams to execute. |
| `onboarding-activation` | minimum version | one motion | full | full | Customers stall between contract signature and first realised value, and you need a clock and a detection system so stalls surface before they become churn. |
| `partner-channel-operations` | do not run | full | full | full | Partners can significantly accelerate revenue (co-selling, reselling, integration) and you need the operating system to make partner-sourced deals scale without chaos. |
| `pipeline-visibility` | do not run | one motion | full | full | A revenue team loses confidence in its pipeline numbers and cannot predict whether it will hit the target, usually because deals go stale and close dates drift. |
| `pricing-monetization-ops` | do not run | minimum version | full | full | Your customers are charged based on usage rather than a flat fee, and you need to ensure the invoices are accurate, auditable, and reflect what they actually consumed. |
| `renewal-save-motion` | do not run | minimum version | full | full | A customer is at risk of cancelling their contract, and you need a structured intervention plan that goes beyond offering a discount to understand and address the real problem. |
| `revops-data-governance` | do not run | minimum version | full | full | CRM reports do not match, fields are a mess, and nobody trusts the data; this skill builds the standards and processes to keep it clean so decisions are reliable. |
| `revops-metrics` | do not run | minimum version | full | full | You need to understand what metrics matter for your business growth and what your numbers are actually telling you about where to improve next. |
| `revops-revenue-planning` | do not run | one motion | full | full | You need to build or reconcile an annual revenue plan and lock it with your finance team. Scale-ups build one bottoms-up plan; enterprise teams build multiple unit plans, consolidate, and reconcile against a finance target through formal governance. |
| `revops-strategy` | do not run | one motion | full | full | You need to diagnose what is blocking revenue growth or design a complete revenue strategy. At scale-up: one motion, one set of KPIs. At enterprise: multiple units, aggregate constraints, formal governance over changes to the strategy. |
| `sales-methodology` | do not run | one motion | full | full | You need to standardise how your team discovers, qualifies, and closes deals. At scale-up: one methodology, CRM, and deal-review rhythm. At enterprise: canonical methodology across regions or products, with formal governance over deviations and procurement involvement in deal progression. |
| `trial-poc-conversion` | minimum version | full | full | full | You need to convert product trials or proofs of concept into closed deals at higher velocity. At scale-up: one activation model, manual discipline. At enterprise: scaled instrumentation across multiple products or regions, formal governance on trial terms and success criteria, financial involvement in evaluation budgets and contingent revenue. |
| `win-loss-program` | minimum version | one motion | full | full | You need to understand why deals close or why they don't, so you can fix positioning, product, and sales process. At scale-up: Lane 1 on every deal, Lane 2 on samples. At enterprise: formalised cadence across regions, multiple interviewers, cross-unit synthesis, findings integrated into formal roadmap and strategy processes. |

## How to use this with an agent

Any prompt that assigns one of these skills should require the agent to state the situation in its first paragraph and to list which sections of the skill it skipped because of it. A deliverable that does not name the situation is incomplete.

## Sources

- Customer-count thresholds (roughly 30 comparable customers; 10 or more won the same way): practice-based, no public source claims them
- Monthly retention measurement as the product-market fit marker: practice-based (SaaS convention)
- Enterprise markers (more than one revenue organisation with its own plan, formal governance layer, finance owns the board number): practice-based; the OECD scale-up definition (20 percent growth for three years, 10 or more employees, OECD 2007) is about growth rate and does not separate scale-up from enterprise

