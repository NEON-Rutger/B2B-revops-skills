---
name: trial-poc-conversion
aliases: [trial-poc-conversion, poc-design]
description: >
  Design and run trials, POCs, and pilots that convert: pick the right
  evaluation motion, contract success criteria before granting access, define
  and instrument activation, and run the conversion clock so evaluations end
  in a decision instead of a drift. Triggers on 'trial conversion,' 'POC,'
  'proof of concept,' 'pilot,' 'trial design,' 'trial-to-paid,' 'our trials
  go nowhere,' 'free pilot request,' 'evaluation plan,' 'success criteria,'
  'trial expired without a decision,' 'they want to test it first,' or any
  situation where product access is being traded for a buying decision.
  BOUNDARY: deal-qualification-gates decides whether the deal is real BEFORE
  an evaluation is granted; a POC is a proof vehicle, never a qualification
  substitute, and granting one below the evidence gate is how free consulting
  projects start. onboarding-activation owns everything after signature; this
  skill ends at the conversion decision and hands the activation definition
  forward. Account-health monitoring during a live trial is detection; this
  skill supplies the design those monitors check against.
status: stable
---

# Trial / POC Conversion: Evaluations That End in a Decision

Buyers now default to testing before buying: 70% of enterprise AI buyers prioritize speed of deployment in vendor selection, 57% expect POC ROI within 3 months and 11% expect it immediately, and evaluation is increasingly one-shot, with no second audition for a failed test (a16z Enterprise Survey, 2026). At the same time, most evaluation programs are designed as access grants rather than decision processes, which is why trial pools fill with expired, undecided, silent accounts.

The core rule: **an evaluation is a mutual project with an end date and a definition of done, or it is a giveaway.** Every element of this skill enforces one of those three properties.

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
| Start-up, pre product-market fit | Skip industry benchmarks; they do not apply to this stage or motion. Pick one evaluation motion (self-serve or sales-assisted) and run five customer trials end-to-end. Document which activities preceded activation, which did not, and whether the customer chose to continue. |
| Start-up, product-market fit | Define success criteria in writing before granting trial access; criteria must come from the buyer's pain evidence from discovery. Run trials with a clear end date and a named decision committee on both sides. Establish readout discipline: at expiry, deliver a business case using the buyer's own numbers, not a recap of features. Track activation rate (the share of trials that reach the core value milestone by day three or first working session) and separate conversion rates between activated and un-activated trials. |
| Scale-up | Instrument activation time from day zero and alert on stalls before expiry; un-activated trials by day three predict the lowest-conversion outcomes. Embed evaluation criteria, activation state, and decision dates directly in the CRM so no trial expires silently. Enforce the Entry Gate discipline: no trial access without written success criteria, the then-what agreement, a named evaluation committee, and locked calendar dates. Run mid-point readouts on assisted evaluations to catch drift while there is still time to course-correct, and publish zombie trial hygiene rules so trials expired more than thirty days with no decision are marked closed-lost and re-entry runs on fresh triggers only. |
| Enterprise | Trial and POC programmes scale to hundreds of concurrent evaluations across regions and products, with finance involvement expanding to include procurement approval of evaluation budgets and revenue-recognition timing if trials carry contingent terms, and governance requiring formal approval matrices for deal-size triggers and regional discount floors. Multi-region or multi-product trials require different success criteria; centralised frameworks ensure comparability. The skill gains weight in: Entry Gate Discipline (formal approval workflows across units and geographies), Zombie Trial Hygiene (automated cross-instance reporting of stale trials, weekly escalation to leadership), and Activation Instrumentation (unified dashboard across multiple product instances or regions, flagging stalls by geographic cluster to surface regional training or product-market-fit issues). |

Skip before product-market fit: Pick the Motion Before Setting the Metric; Zombie Trial Hygiene.

## Pick the Motion Before Setting the Metric

Benchmark ranges differ so much by motion that comparing across them is the most common evaluation-metrics mistake (trial-benchmark aggregations, 2025-2026):

| Motion | Typical trial-to-paid range | Median |
|---|---|---|
| Opt-in self-serve trial (no card) | 8-22% | ~14% |
| Opt-out trial (card required) | 35-55% | ~44% |
| Sales-assisted trial / POC | 35-70% | ~55% |

(Ranges are self-reported industry aggregations, not audited surveys; treat the between-motion differences as reliable and the exact figures as indicative. Your own motion's two-quarter cohort beats this table.)

Three consequences:
1. Pick the motion per segment, not per company: self-serve for low-ACV velocity, sales-assisted POC where ACV justifies the human cost, card-required where you deliberately want fewer, hotter evaluations.
2. Benchmark against your own motion's range. A 20% conversion is strong for opt-in and a crisis for sales-assisted.
3. The single biggest conversion lever sits inside the trial, not around it: activation explains 60-75% of conversion variance, with activated trials converting at 35-65% and un-activated ones at 2-8% (same aggregations, 2025-2026). Everything below serves activation.

## The Entry Gate

Before anyone gets a POC, four things exist in writing. If the buyer will not co-author them, you have learned something cheaper than a three-week evaluation:

1. **Success criteria, 2-3, measurable, theirs.** "See if we like it" is not a criterion. "Cut manual triage time on X by half, measured on their own queue" is. Criteria come from the pain evidence gathered in qualification; an evaluation cannot prove value that discovery never quantified.
2. **The then-what.** What happens when criteria are met: commercial terms pre-agreed, signature path named, start date pencilled. An evaluation without a pre-agreed consequence is an aquarium visit.
3. **Named owners on both sides** and the buyer's evaluation committee: who judges, against what, on which date. A POC judged by one enthusiast converts into nothing; the economic buyer sees the readout or the readout is rehearsal.
4. **The clock.** 14 days for self-serve, 30 for sales-assisted as defaults; extensions are earned by activity, never granted by silence (practice-based default; replace with your own cohort data after two quarters). Expiry with no decision is a decision, and it gets logged as one (see the zombie rules below).

## Design for Activation, Not Exploration

- Define the activation milestone per motion: the smallest observable event that proves the buyer experienced the core value on their own data. One milestone, not five.
- Shrink the surface: an evaluation of everything proves nothing. Configure the trial around the one workflow the success criteria name; hide or defer the rest.
- Instrument day-zero-to-activation time and alert on stall: no activation by day 3 (self-serve) or the first working session (assisted) predicts the un-activated 2-8% outcome; intervene then, not at expiry.
- Midpoint readout on assisted evaluations: criteria progress in the buyer's numbers, blockers named, clock restated. This is where drift gets caught while there is still runway.

## The Conversion Close

The readout is a business case delivery, not a demo recap: criteria vs results in their numbers, what it took to get there, and the pre-agreed then-what invoked. Two disciplined endings:

- **Criteria met:** invoke the agreement. Renegotiating from scratch after a successful POC concedes every point of leverage the design bought.
- **Criteria missed:** say so first, plainly. Either the fix is scoped and one dated extension follows, or the evaluation closes honestly with the loss pattern recorded. A vendor who calls their own miss earns the re-entry later.

Deliverable: conversion readout with success criteria met or missed, activation milestones achieved, decision path taken, and calendar-locked end date. Frame results in the buyer's numbers, not in product language.

## Zombie Trial Hygiene

Expired and silent evaluations poison pipeline data and waste outreach:

- Trial expired 30+ days with no decision: mark cold, suppress warm-motion outreach, log the loss pattern. Re-entry runs through the revival lane on a fresh trigger, not through "checking in on your trial."
- Never count un-activated trials in weighted pipeline at the same probability as activated ones; the 35-65% vs 2-8% split (aggregations, 2025-2026) is the strongest single probability signal an evaluation-stage deal carries.

## What Good Looks Like

The best operators treat the POC agreement as the actual close: once success criteria, committee, clock, and then-what are signed, the signature at the end is administration. The common mistake is the mirror image: granting access to seem accommodating, discovering at expiry that nobody agreed what success meant, and calling the resulting silence a pricing objection. You know the system works when every evaluation in the CRM shows its criteria, its activation state, and its decision date, and when "trial expired, no decision" has become a rare, logged event instead of the default outcome.

## Diagnostic Questions

1. List your last ten evaluations. For how many can you produce written success criteria the buyer co-authored?
2. What is your activation rate inside trials, and do you know your conversion split between activated and un-activated accounts?
3. What happens automatically on trial expiry today: a decision process, or nothing?
4. How many "active" POCs have blown past their original clock without a dated extension agreement?
5. When a POC succeeds, how often do commercial negotiations start from zero anyway, and what did that cost last quarter?

Benchmark provenance and vintages: read `references/evaluation-benchmarks.md`.

> Built by [Neon Triforce](https://neontriforce.com)
