---
name: procurement-navigation
aliases: [procurement-navigation, security-review-navigator]
description: >
  Navigate the buyer's procurement gauntlet from 'you're selected' to
  signature: map the gauntlet early, pre-bake the artifact pack, run
  security, legal, and privacy reviews in parallel on a mutual close plan,
  and negotiate procurement's game without giving away the deal the sales
  team already won. Triggers on 'procurement,' 'security review,' 'security
  questionnaire,' 'vendor review,' 'legal redlines,' 'stuck in legal,' 'DPA,'
  'InfoSec,' 'vendor onboarding,' 'the deal is agreed but not signed,'
  'procurement is squeezing us,' 'close date keeps slipping at contract
  stage,' or any situation where a verbally-won deal enters the buyer's
  buying machinery. BOUNDARY: an rfp-response skill owns the upstream bid
  phase (bid/no-bid, building the response to the evaluator's scorecard);
  this skill begins after selection, when the evaluators hand you to the
  machinery. deal-desk-operations owns your INTERNAL approvals, quoting, and
  concession governance; this skill choreographs the BUYER's process and
  tells deal desk what is coming. deal-qualification-gates predicts this
  phase: a decision-process dimension scored 4+ means the gauntlet below was
  mapped before proposal, which is the whole trick.
status: stable
---

# Procurement Navigation: The Deal After the Deal

The most demoralizing loss in B2B is the deal that was won and then wasn't: champion committed, terms shaken on, and then six weeks of security questionnaires, redlines, and a procurement analyst with a mandate, while the close date rolls forward and the champion's momentum bleeds out. The market data says drag is fatal, not cosmetic: deals that close within about 50 days of TOTAL cycle time win at roughly 47%, versus roughly 20% for deals that stretch past that mark (Ebsta x Pavilion GTM Benchmarks, 2025 edition). The figure measures the whole deal, not the contracting phase alone; the point is that procurement is where the late weeks get added to deals that were on pace, and almost all of that drag is schedulable in advance.

The core rule: **the gauntlet is mapped before the proposal, started in parallel, and run on a mutual plan.** Surprise is the enemy; none of the steps are actually surprising.

## Map the Gauntlet Early

The decision-process questions that qualification should have answered become, at proposal stage, a concrete checklist built WITH the champion:

1. Every step between "yes" and "signed," in their order: security review, privacy/DPA, legal, procurement negotiation, vendor onboarding, signature chain.
2. Per step: who runs it, typical duration, what they need from you, and what has killed vendors there before. Champions answer this question happily; they want the deal to land too.
3. The steps that can run in parallel (almost all of them) versus the true dependencies. Serial-by-default is the buyer's habit, not a law; a champion armed with a parallel plan is your best process negotiator.
4. Calendar traps: fiscal-year close, holiday freezes, the legal team's known backlog, signer vacations. An August signature chain has lost weeks before it starts.

If the champion cannot answer these, the deal-qualification decision-process score just fell, and that is better learned now than at "stuck in legal, week five."

## The Artifact Pack: Pre-Baked, Versioned, Owned

Most procurement delay is you, slowly assembling answers that never change. Maintain a standing pack with an owner and a review date:

- Security: completed standard questionnaires (the common industry formats), certifications and audit reports (up to date and shareable under NDA), architecture and data-flow one-pager, sub-processor list, incident-response summary.
- Legal and privacy: your paper (MSA/DPA templates), your standard positions on the five clauses that always get negotiated (liability caps, indemnity, data terms, termination, SLAs), and the fallback position per clause agreed with counsel IN ADVANCE, so redline rounds take days, not committee cycles.
- Commercial and admin: insurance certificates, tax and banking forms, the vendor-onboarding basics every large buyer requests.

Response time to a security questionnaire is a sales metric during this phase. Same-week answers signal an organization worth buying from; a three-week scramble signals risk to the exact people whose job is smelling it.

## Run It on a Mutual Close Plan

Convert the gauntlet map into a dated, shared plan the buyer co-owns: every step, owner on each side, due date, and the go-live the buyer wants at the top, so every slip is framed in THEIR cost, not your quota. Review it weekly with the champion. Two rules keep it honest:

- A deal in the gauntlet is not Commit-grade until the remaining steps are enumerated with dates and owners. "In legal" is not a status; "redlines returned, our counsel responds Thursday, one open clause" is.
- When a step stalls, escalate through the sponsor with the go-live cost stated, and spend executive-to-executive capital on true blockages only. One well-aimed exec call outperforms four polite check-ins.

## Negotiate Procurement's Game Without Losing Yours

Procurement's mandate is savings and risk reduction; respect the job, do not re-litigate the deal:

- Re-anchor on the business case the champion already sold (this is why the evaluation readout and its numbers exist). Procurement discounts percentages; they respect documented value.
- Every concession is traded, never given: term length, case study rights, expansion options, payment terms, reference calls. A discount given free at this stage reprices this account forever and teaches the buyer's procurement that your first number is decoration (concession governance itself lives in deal-desk-operations).
- Hold the walk-away line set before this phase began, and let procurement win something visible that costs you little; the analyst has a scorecard too.

## Feed the System

Log per deal: gauntlet duration by step, which artifacts were missing, which clauses ate the calendar, where the plan slipped. Three deals in, you have your own procurement benchmark; five deals in, the artifact pack and fallback positions cover 90% of what any buyer will ask, and contracting stops being weather.

## What Good Looks Like

The strongest operators can name, on the day the buyer says yes, every step to signature with an owner and a date, and their security questionnaire turnaround is measured in days. The common failure: treating the verbal yes as the finish line, meeting the gauntlet as a series of surprises, letting the close date roll weekly, and paying a late unearned discount just to end it, the exact sequence that turns a won deal into a 20-percent-win-rate long-cycle statistic. You know it works when contract-stage slippage stops appearing in forecast variance and the champion describes your process, unprompted, as the easiest vendor onboarding they have run.

## Diagnostic Questions

1. For your current late-stage deals: can anyone list the remaining steps to signature with owners and dates? Which ones are guesses?
2. How long did the security review take on your last three enterprise deals, and how much of that was your own response time?
3. Do your standard contract fallback positions exist in writing, pre-agreed with counsel, or does every redline round convene a committee?
4. What did you concede at contract stage last year that was never traded for anything?
5. Which calendar traps (fiscal close, freezes, signer availability) sit inside your current quarter's committed deals, and who has checked?

Provenance: read `references/procurement-provenance.md`.

> Built by [Neon Triforce](https://neontriforce.com)
