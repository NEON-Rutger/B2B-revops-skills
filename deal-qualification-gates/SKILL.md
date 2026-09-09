---
name: deal-qualification-gates
aliases: [deal-qualification-gates, qualify-or-kill]
description: >
  Install evidence-gated qualification on a live pipeline: score the QUALITY
  of evidence behind every deal (1-5 per qualification dimension), set
  minimum scores per stage, and enforce qualify-or-kill at each gate.
  Triggers on 'zombie deals,' 'pipeline is full of junk,' 'is this deal
  real,' 'qualify or kill,' 'deals stall at proposal,' 'forecast built on
  hope,' 'reps say every deal is closing,' 'stage criteria,' 'exit
  criteria,' 'MEDDIC scoring,' 'SPICED scoring,' 'qualification framework
  rollout,' or any situation where deals advance on rep optimism instead of
  buyer evidence. Works with SPICED by default and maps to MEDDICC or BANT.
  BOUNDARY: icp-builder owns ACCOUNT-level fit (is this the right company)
  and carries a summary of these gates as its pipeline-enforcement step;
  this skill is the full deal-level operating system (is this deal real).
  deal-velocity-engineer treats slow deals as a speed problem; this skill
  treats false deals as a truth problem, and it runs first, because
  accelerating an unqualified deal just produces a faster loss. Weekly
  pipeline reviews (e.g. pipeline-review) consume the scores this skill
  produces; they read the dashboard, this skill builds the engine under it.
status: stable
---

# Deal Qualification Gates: Evidence, Not Enthusiasm

The 2025 Ebsta x Pavilion benchmark put average B2B win rates at 19%. Most of that waste is not lost at the negotiation table; it is manufactured months earlier, when a conversation gets logged as a deal and nobody ever checks whether the evidence behind it hardened. CRM stages measure where a deal is. Almost nobody measures how WELL you know what you claim to know about it.

This skill installs that second axis: an evidence-quality score per qualification dimension, minimum scores per stage, and a standing qualify-or-kill discipline. Gates, not fields. Adding more CRM fields will not fix a forecast; minimum evidence per stage will.

---

## Stage check: do this before anything else in this skill

This skill was written for a company that already has a repeatable motion and named owners. Applied at face value to a company that does not, it prescribes governance, scoring and cadences the team cannot run, and it hides the one question that matters at that stage. Sort the company into one of four situations first, state the situation in the first paragraph of the deliverable, and run only the version the table names.

1. Start-up, pre product-market fit. Fewer than roughly 30 comparable customers (practice-based threshold). Wins came from the founders' network or referrals, not from a process anyone could repeat. No segment has a measured win rate or cycle time. Retention is not tracked. The CRM, if there is one, is a contact list. Nobody carries a quota. The only question that matters: do existing customers get the outcome they were promised, and would they buy again? Run the minimum version of this skill, or do not run it.

2. Start-up, product-market fit. At least one segment with 10 or more customers won the same way (practice-based threshold). A known win rate and cycle time for that motion. Retention measured monthly. The founders still do most of the selling, with a few early reps. One person owns the CRM and can trace how recent deals moved. Run the skill for that one motion only; treat thresholds as guidance, not rules.

3. Scale-up. Sales, marketing, customer success and operations each have a named owner. The CRM holds stage history the team trusts. Reps carry quota. There is a forecast that someone is held to. Growth is a question of capacity and constraints: which function breaks first when volume doubles. Run the full skill.

4. Enterprise. Everything in situation 3, plus more than one revenue organisation: business units, regions or product lines with their own plan and their own leader. A governance layer sits above go-to-market decisions (steering committee, works council, legal or compliance gates). Finance owns the revenue target that goes to the board. The CRM may run as several instances or with many administrators. Run the full skill with the enterprise deltas named in the table: aggregation across units, governance and change management, longer decision paths.

If the evidence is thin, ask three yes or no questions: Is there a segment with 10 or more customers won the same way? Is retention measured monthly? Does someone own the CRM as part of their job? Three no answers means situation 1. One or two yes answers means situation 2. Three yes answers means situation 3 or 4; then ask three more: Is there more than one business unit or region with its own revenue plan and leader? Do go-to-market decisions pass through a formal governance layer? Does finance own the revenue target for board reporting? Two or more yes answers means situation 4; otherwise situation 3.

The full skill applies to both scale-up and enterprise. Not every skill applies at every stage; the table below says what this skill does at each, and "do not run" is a valid answer.

What this skill does per situation:

| Situation | What this skill does |
|---|---|
| Start-up, pre product-market fit | Score evidence quality only for the conversations you are already having. Run the Evidence-Quality Scale on your last 5-10 customer conversations to identify which dimensions you never ask about. This diagnostic serves your pre-PMF question: do existing customers perceive value and would they buy again? Skip all stage gates, deployment, and rollout sections until you have a repeatable motion. |
| Start-up, product-market fit | Install evidence-quality scoring on a single winning motion with one stage gate (typically Discovery to Demo). Score every deal on SPICED dimensions 1-5 as evidence lands from calls and conversations, not from memory. Build a one-page weekly exception report: which deals above this one gate sit below the minimum evidence threshold (14 total for Demo stage). Run weekly qualify-or-kill reviews on those flagged deals with one verdict per deal (re-qualify, downgrade, or kill). |
| Scale-up | Implement the full skill end-to-end. Install all four stage gates (Inbound to Discovery, Discovery to Demo, Demo to Proposal, Proposal to Commit). Score all six SPICED dimensions on all deals. Build a weekly below-gate exception report and attend a weekly qualify-or-kill review with sales leadership. Automate scoring where your CRM or conversation intelligence tool can extract dimension evidence from call transcripts. Expect to kill 15-30% of your existing pipeline in the first rollout; that trade is the entire point. |
| Enterprise | Qualification gates expand from individual deal truth-telling to cross-unit pipeline governance and regulatory audit trails. The skill gains weight in multi-unit pipeline consolidation and duplicate detection to prevent the same prospect appearing in multiple units' pipelines, legal and compliance gates including procurement checkpoints and security review evidence scoring, deal desk operations where discount approvals require qualification evidence, and revenue recognition gating for ASC 606 compliance. Forecasting accuracy ties directly to evidence-quality maturity across all units. |

Skip before product-market fit: The Stage Gates; Deployment; Rollout Order; Diagnostic Questions.

---

## The Evidence-Quality Scale

Score every qualification dimension 1 to 5. The scale grades evidence, never rep enthusiasm:

| Score | Grade | Meaning |
|---|---|---|
| 1 | Unknown | Never asked. |
| 2 | Weak | Surface mention, uncorroborated ("they said budget shouldn't be an issue"). |
| 3 | Confirmed | Buyer said it explicitly and it is logged (quote, transcript, email). |
| 4 | Quantified | There are numbers behind it (cost of the problem, headcount affected, deadline date). |
| 5 | Validated | Corroborated by a third party or system data (their CFO repeated it, usage data shows it, a signed evaluation plan names it). |

The jump that matters is 2 to 3: from "the rep believes it" to "the buyer said it and we can point at where." A pipeline where most dimensions sit at 2 is a mood, not a forecast.

## The Dimensions

Default lens is SPICED, scored across six letters: Situation, Pain, Impact, Critical Event, Decision (criteria), Decision (process). Total out of 30. If your team runs MEDDICC or BANT, keep the scale and gates identical and swap the dimensions; the mapping table lives in `references/qualification-frameworks.md`. The framework is the vocabulary; the gates are the system.

## The Stage Gates

Per-stage minimum TOTAL scores, calibrated for a six-dimension, 30-point model:

| Transition | Minimum total | What it enforces |
|---|---|---|
| Inbound to Discovery | 7 | You know something real beyond a form-fill. |
| Discovery to Demo | 14 | Pain and situation are confirmed, not assumed. Your demo has something specific to aim at. |
| Demo to Proposal | 19 | Impact is at least quantified. A proposal without a number in it is a brochure. |
| Proposal to Commit | 23 | Critical event and decision process are hard. You know why now and how they buy. |

Two enforcement rules:

1. **No single dimension below its floor.** A deal can hit 19 total while Critical Event sits at 1; that deal does not move. Every dimension needs at least a 3 by proposal stage. One letter under its gate and the deal stays put. No rounding up. Go back, ask again, qualify or kill.
2. **The critical-event forcing question:** "What breaks for this customer if they do nothing until next quarter?" No concrete answer scores Critical Event at 1, and the record is a conversation, not a deal. This single question deflates more zombie pipeline than any dashboard.

Why the paranoia about evidence depth: Gong's analysis of 1.8M opportunities found closed-won deals carry roughly twice as many engaged buyer-side contacts as closed-lost ones, and its call research found reps asking 11-14 targeted discovery questions correlate with the highest win rates (Gong Labs, 2017-2021 datasets). The same Ebsta x Pavilion dataset behind the 19% headline (655K opportunities, $48B pipeline, 2025 edition, still the latest full dataset as of August 2026) shows what the gates buy you: deals that close within ~50 days win at roughly 47% versus roughly 20% for deals that drag past that mark, and early economic-buyer involvement lifts win rates by around 55%. Both map directly onto the gates: qualify-or-kill is what keeps cycle time short, and the decision-process floor is what forces the economic buyer question early. Evidence quality is not bureaucracy; it is the observable difference between deals that close and deals that decay. Benchmark provenance and vintages: read `references/qualification-frameworks.md`.

---

## Deployment

1. **CRM:** one property per dimension (the 1-5 score) plus a computed total next to the account's ICP tier. Deal health = fit tier x evidence total, on one screen.
2. **Enforcement:** stage-transition validation where your CRM supports it; otherwise a weekly below-gate exception report: every deal sitting above a stage its evidence does not support, with the missing dimensions named. The report is short or your pipeline is fiction, and either way you learn something.
3. **Qualify-or-kill review:** each below-gate deal gets one of three verdicts, on a date: re-qualify (a named person asks the missing question by a named day), downgrade (back to the stage its evidence supports), or kill (closed-lost with the loss pattern recorded, see closed-lost-revival for what that record later earns you). "Leave it and hope" is not a verdict.
4. **Scoring hygiene:** score at the moment evidence lands (after calls, from transcripts), not in a Friday batch from memory. If an AI agent processes your call transcripts, dimension scoring belongs in that pipeline; the transcript is the evidence, so the score should come from it, not from recollection.
5. **Expect two weeks of rep resistance,** then adoption once the gates start protecting calendars from deals that were never going to close. The gate is not an audit of the rep; it is armor against wasted evenings.

## Rollout Order

Week 1: score the CURRENT pipeline as-is, no consequences. The distribution is the diagnostic: a healthy pipeline shows scores rising with stage; a hope-based pipeline shows late-stage deals with early-stage evidence.
Week 2: install the gates forward-looking (new stage transitions only). Grandfather existing deals but flag them in the exception report.
Week 4: first qualify-or-kill review over the flagged backlog. Expect to kill 15-30% of "active" pipeline; the forecast gets smaller and true simultaneously, and that trade is the entire point.

## Diagnostic Questions

1. Pick your three biggest deals. For each: what breaks for the buyer if they do nothing this quarter? If the answer starts with "I think," score it honestly.
2. What percentage of proposal-stage deals have a quantified impact number IN THE BUYER'S OWN FIGURES anywhere in the record?
3. When did a deal in this pipeline last move BACKWARD a stage? If the answer is never, stages are being used as a ratchet, and the forecast inherits the fiction.
4. How many deals older than 2x your median cycle time sit in the pipeline, and what evidence score do they carry?
5. Who is allowed to kill a deal, and when did that last happen without a manager forcing it?

> Built by [Neon Triforce](https://neontriforce.com)
