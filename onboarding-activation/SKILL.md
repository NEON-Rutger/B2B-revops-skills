---
name: onboarding-activation
aliases: [onboarding-activation, time-to-first-value]
description: >
  Design customer onboarding as an activation system: carry the why-they-
  bought evidence across the signature, drive to first realized value on a
  clock, detect stalls while they are cheap, and graduate accounts into the
  steady-state cadence with a value baseline installed. Triggers on 'customer
  onboarding,' 'time to value,' 'time to first value,' 'activation,'
  'implementation drags,' 'customers sign and stall,' 'go-live took months,'
  'adoption never started,' 'onboarding handoff,' 'kickoff call,' or any
  situation where the gap between signed and successful is where accounts
  quietly die. BOUNDARY: trial-poc-conversion ends at the buying decision and
  hands its activation definition forward; this skill starts at signature.
  renewal-save-motion owns intervention on flagged accounts in steady state;
  this skill's stall protocol covers the onboarding window, then hands the
  account over with its baseline. qbr-ebr-builder consumes this skill's
  output directly: the value baseline agreed at graduation is what every
  later business review measures against. cs-operations owns the CS org
  design around all of it.
status: stable
---

# Onboarding to Activation: The Gap Where Accounts Quietly Die

The most dangerous period in a customer's life is the one with the least instrumentation: after the signature, before the first realized value. Sales has moved on, success has a kickoff template, and the buyer's champion is spending political capital on a promise with no proof yet. Churn recorded in month eleven is usually manufactured here, in month one; the renewal defense literature keeps rediscovering that risk is visible in behavior long before it is audible in words, and nowhere is that more true than an onboarding that never activates.

The evaluation data makes the stakes concrete: in trials, activation explains most of the conversion outcome, with activated accounts converting at multiples of un-activated ones (trial-benchmark aggregations, 2025-2026). Post-signature, the same mechanism operates on retention; treating it as transferable is a practice-based judgment this skill makes explicitly, and the first instrumentation job below is to make it a local fact: split your renewal outcomes by activated-versus-not within two quarters, and recalibrate the arc if the split is weak. Median gross revenue retention runs ~90% with top quartile above 95% (industry surveys, 2025); onboarding is the earliest controllable input to which side of that line an account lands on.

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
| Start-up, pre product-market fit | Activation is one customer outcome proving value on their own data (not a go-live date). Define activation manually per segment (e.g., 'The first report that changed a decision' or 'One workflow replaces the old tool'). Run a manual 30-60-90 checklist for your last 3-5 customers: milestone dates, stall signals (blocked access, attendance decay, usage flatline), and activation witnessed. Weekly check-in with the onboarding lead; the question is whether the customer got value, not whether training was delivered. |
| Start-up, product-market fit | Carry evidence forward from qualification (why they bought, success criteria) into kickoff; confirm rather than re-collect. Define activation as one primary event per segment with a 30-60-90 milestone arc: one workflow live by day 30, activation event verified by day 60, expansion and baseline agreed by day 90. Instrument stall detection manually via Slack: name the three stalls (access, attendance, usage) and flag them to the champion when observed. Graduation is explicit: activation verified, baseline documented (their before and after numbers), steady-state cadence owner introduced. |
| Scale-up | Automate activation instrumentation from product telemetry so activation status is dashboard-queryable. CRM tracks handoff artifacts (champion map, success criteria, critical event), onboarding milestones (30-60-90 dates), and stall status (three stall fields). Measure time-to-first-value as a distribution per segment with the tail monitored; accounts outside the normal range get escalation. Graduation: value baseline (before numbers, after numbers, agreed) recorded in every graduated account and fed to renewal team as the baseline for future reviews. |
| Enterprise | Enterprise customers operate multiple business units, geographies, or use cases within a single contract, and onboarding orchestration becomes a multi-stream programme. Define activation per business unit (unit A activates on workflow X; unit B activates on workflow Y; both sit under one contract); track cascading activation dates in the CRM (unit A activation unlocks unit B expansion trigger). Install legal and procurement holds in the onboarding workflow: champion signs-off on activation definition at kickoff, CFO or finance business partner attests the baseline cost-benefit numbers before final graduation. Measure time-to-first-value by business unit and by contract geography; contracts with mixed activation (unit A done, unit B stalled) get escalation separate from full-stall. |

Skip before product-market fit: Stall Detection While It Is Cheap; Diagnostic Questions (sections 2-5).

## Activation Is an Event, Not a Phase

Define activation as the smallest observable event proving the customer experienced the core value on their own data, in their own workflow. Rules:

- **Go-live is not activation.** Configured, trained, and launched are vendor milestones. Activation is a customer outcome: the report that changed a decision, the workflow that replaced the old one, the first week nobody opened the legacy tool.
- One primary activation event per segment or product line, written down, measurable from system data. If it takes a meeting to know whether an account is activated, the definition is wrong.
- Time-to-first-value (signature to activation event) is the program's headline metric, tracked as a distribution, not an average; the tail is where churn lives.

## Carry the Evidence Across the Signature

Most onboarding starts with an amnesia ceremony: a kickoff call asking the customer to re-explain everything they told sales for three months. The handoff artifact fixes this:

1. Why they bought, in their own words: the pain, the quantified impact, the critical event with its date (if qualification gates ran, this is a lookup, not an interview).
2. The success criteria and activation definition, inherited from the evaluation if one ran, authored at kickoff if not.
3. The map of people: champion, economic buyer, the skeptic who almost blocked it, and who is spending political capital on this working.
4. The clock they care about: the critical event that justified buying does not pause because legal signed.

The kickoff then confirms rather than collects, and opens with the one question that resets scope honestly: "what has changed since you signed?"

## The Activation Arc

Structure the onboarding window as milestone gates on a default 30-60-90 arc (compress for simple products; the gates matter, not the dates):

- **First 30: one workflow live.** Shrink to the single workflow that carried the buying case and get it producing on real data. Broad rollouts activate nothing; the everything-onboarding is the adoption-gap save play's origin story.
- **By 60: the activation event, witnessed.** The customer can show the value to their own boss without you in the room. Instrument it; do not survey for it.
- **By 90: expansion of use, baseline agreed.** Second workflow or wider team live, and the value baseline (their before-numbers, their after-numbers, agreed) written down. That baseline is the raw material of every future business review and renewal case.

## Stall Detection While It Is Cheap

Instrument three stall signals from day one, with named responses:

1. **Access stall:** environment, data, or integration blocked for more than a week. Response: escalate to the sponsor with the cost of delay stated against their critical event, not a polite nudge to the blocked admin.
2. **Attendance decay:** kickoff was full, session three is one intern. Response: the champion conversation ("what changed internally?"), because attendance decay in onboarding is the same signal as sponsor drift pre-renewal, just earlier and cheaper.
3. **Usage flatline post-launch:** live but idle for two weeks. Response: shrink further, retrain on the one workflow, and re-anchor on the buying pain; do not add features to an account that has not used the first one.

A stall that survives two responses gets an honest internal verdict, wrong-fit included. Escalating a doomed onboarding into steady state does not save the account; it schedules the churn for a more expensive date.

## Graduation, Not Fade-Out

Onboarding ends with an explicit graduation: activation event verified, baseline documented, steady-state cadence owner introduced, and the first business review scheduled with the baseline as its look-back anchor. Accounts that exit onboarding without a baseline force every future value conversation to start from archaeology.

## What Good Looks Like

The operators who do this well can answer "which accounts signed in the last 90 days and have not activated?" from a dashboard, in seconds, and their kickoff calls open with the customer's own words read back to them. The common failure is a checklist onboarding that completes perfectly (kickoff held, training delivered, go-live confirmed) around an account that never activated, discovered as a surprise at renewal. You know the system works when time-to-first-value has a shrinking median and a monitored tail, and when the renewal team stops asking "what did this customer buy for?" because the answer has been on file since week one.

## Diagnostic Questions

1. What is your activation event, in one sentence, per segment? If the answer is a paragraph of milestones, it is a phase, not an event.
2. What is your median time-to-first-value, and what does the worst decile look like? Who owns that tail today?
3. Open your three most recent kickoffs: did the customer re-explain what they told sales, or did you read it back to them?
4. Which currently-onboarding accounts show access stalls or attendance decay right now, and who is acting on them this week?
5. For accounts that churned in the last year: how many ever activated at all? (This one usually reframes the churn conversation entirely.)

Provenance and practice-based rules: read `references/activation-provenance.md`.

> Built by [Neon Triforce](https://neontriforce.com)
