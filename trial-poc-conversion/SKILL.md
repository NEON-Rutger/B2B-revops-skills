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
