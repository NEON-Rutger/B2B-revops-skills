---
name: qbr-ebr-builder
aliases: [qbr-ebr-builder, business-review-builder]
description: >
  Design and build customer business reviews that buyers actually attend:
  QBR (operational cadence) and EBR (executive cadence), with the value
  recap in the customer's own numbers as the load-bearing artifact.
  Triggers on 'QBR,' 'EBR,' 'business review,' 'executive business review,'
  'quarterly review deck,' 'prove value to the customer,' 'renewal
  conversation prep,' 'customer stopped attending reviews,' 'our QBRs are a
  feature parade,' 'success plan review,' or any situation where post-sale
  value needs to be demonstrated to the people who pay, not just the people
  who use. BOUNDARY: account-health-audit and customer-health scanners
  produce the internal diagnostic BEFORE the review; this skill builds the
  customer-facing instrument itself and starts from their output.
  renewal-save-motion owns the intervention when a review surfaces risk;
  expansion-revenue-architect and expansion-opportunity-analysis own the
  motion when it surfaces headroom; this skill hands off to both and runs
  neither. revenue-operating-cadence owns INTERNAL meeting architecture;
  a business review is a customer-facing meeting and follows different
  rules: their agenda, their numbers, their next quarter.
status: stable
---

# QBR / EBR Builder: Reviews Buyers Attend

Most business reviews die the same death: a slideware feature parade delivered to the daily users while the economic buyer, the person who will decide the renewal, has stopped attending. Then renewal season arrives and the value case gets built in a panic, from scratch, for an audience that has not heard it all year.

A business review exists to do one job: keep the people who PAY convinced of value, in their numbers, on a rhythm, so the renewal is a formality and the expansion conversation has a natural venue. Median gross revenue retention for private SaaS sits around 90% with top quartile above 95% (industry surveys, 2025); the review cadence is one of the few controllable instruments that moves an account from the first group's trajectory to the second's.

**Entry condition:** an internal health read already exists (from an account health audit or health scan). A review built without one is theater; you are presenting to the customer what you have not verified yourself.

---

## QBR vs EBR: Two Instruments, Not One

The single blended "QBR" is where most programs go wrong. Separate the two:

| | QBR (operational) | EBR (executive) |
|---|---|---|
| Audience | Daily users, program owner | Economic buyer, executive sponsor |
| Rhythm | Quarterly (or async for small accounts) | 1-2 per year, anchored 90-120 days before renewal |
| Question it answers | Is the thing working and used well? | Was this worth the money, and what should it do next? |
| Content center | Adoption, blockers, roadmap of USE | Value recap in their numbers, strategic alignment, roadmap of OUTCOMES |
| Failure mode | Feature parade | Skipping it because "the users are happy" |

The EBR anchored ahead of renewal matters because by the time a renewal conversation starts, an unengaged economic buyer has already formed their view from hallway signal. The EBR is where you form it instead.

## Segmentation: Who Gets What

Review effort is a budget; spend it where revenue concentrates.

- **Top tier (largest ARR, expansion headroom, strategic logos):** quarterly QBR + 1-2 EBRs per year, live.
- **Middle tier:** semi-annual QBR, EBR only when a trigger fires (renewal inside 120 days, risk flag, expansion signal, sponsor change).
- **Long tail:** no live reviews. A quarterly async value summary (one page, auto-assembled from usage and outcome data, human-reviewed) replaces the meeting. A calendar full of small-account QBRs is how CS teams burn out while GRR falls anyway.

An AI-agent note that changes the old math: assembling the review pack used to be the expensive part, which justified skipping reviews for smaller accounts. When an agent assembles the data pack from usage, CRM, and conversation history, the constraint moves to CUSTOMER attention, not your capacity. Spend the freed capacity on better meetings for the top tier, not more meetings everywhere.

## The Review Architecture: Three Panels

Every review, QBR or EBR, runs the same three-panel spine. Depth differs by audience.

**Panel 1: Look back, in their numbers.** The value recap is the load-bearing artifact of the entire review. Rules:
- Built from THEIR system data and THEIR baseline, agreed at onboarding or the previous review. If no baseline exists, the first review's job is to install one.
- Outcomes, not activity: "reduced X by Y since March" beats "487 workflows run" in every room that matters.
- Quantify honestly, including what did NOT improve. One acknowledged miss buys credibility for every claimed win; a review with no misses reads as marketing.
- If the value recap cannot be built, that is a finding, not an inconvenience: either instrumentation is missing (fix that) or value is absent (route to the save motion now, not at renewal).

**Panel 2: Current state, honestly.** Adoption depth against plan, open issues with owners and dates, health verdict shared plainly. Do not launder the internal health read into a greener customer-facing version; sophisticated buyers keep their own scorecard, and the gap between yours and theirs is trust lost.

**Panel 3: Look forward, jointly owned.** Next quarter's success plan with the customer's name on half the actions: goals, owners, dates, and the one metric the next review will be judged on. A review that ends without the customer owning actions was a presentation. This panel is also where expansion surfaces naturally: unmet goals plus adjacent problems, raised as THEIR roadmap, not your quota.

## Stakeholder Rules

- The economic buyer attends the EBR, or the EBR moves. Running it without them is rehearsal, not review. Getting them there is the sponsor's job, agreed as part of the success plan, not a calendar surprise.
- Map attendance drift as a signal: a sponsor who attended two reviews and skips the third just told you something the health score has not caught yet. Feed it to the risk triage.
- New stakeholder in the room (reorg, new exec): the review restarts at their zero, with a compressed look-back. Assume inherited context of nothing; see the champion-loss pattern in renewal-save-motion.

## Outputs and Routing

A review is upstream instrumentation for the rest of the post-sale system. Every review produces:

1. An updated success plan (Panel 3), dated and shared.
2. A refreshed baseline for the next value recap.
3. Routed flags: risk signals to the save motion, expansion signals to the expansion motion, product blockers to product with a feedback loop the customer can see.
4. A one-paragraph internal verdict on the account: trajectory, sponsor state, one thing to fix before next review.

## Anti-Patterns

- **The feature parade:** roadmap-heavy decks answer a question nobody asked. Roadmap earns 10 minutes of Panel 3, framed by their goals.
- **The NPS theater:** a survey score is not a value recap. Scores decorate; outcomes convince.
- **The annual ambush:** the first value conversation happening at renewal is the most expensive scheduling failure in CS. The EBR 90-120 days ahead exists to make renewal week boring.
- **The unchanged deck:** if the review could be last quarter's deck with new dates, cancel it and send the async summary; you are spending customer attention with no news.
- **The solo review:** vendor presents, customer receives. Jointly built agendas (send Panel 1 in advance, ask what they want contested) double as engagement signal: an account that will not co-build an agenda is telling you where you stand.

## Diagnostic Questions

1. For your top ten accounts: when did the economic buyer last hear the value case, from you, in their numbers? Not the users, the buyer.
2. Can you produce a value recap with an agreed baseline for your largest renewal due in the next two quarters, today, without a data archaeology project?
3. What percentage of your last quarter's reviews ended with customer-owned actions that got done?
4. Which accounts had sponsors stop attending reviews in the last year, and what happened at their renewals? (This one usually settles the argument for the program.)
5. How many hours does one review pack take to assemble, and is that number the reason your long tail gets no reviews at all?

## Benchmarks and Provenance

GRR median ~90% / top quartile 95%+ (industry surveys, 2025; provenance detail shared with renewal-save-motion's `references/retention-benchmarks.md`). The 90-120 day EBR-before-renewal anchor, the three-panel spine, and the segmentation tiers are practice-based operating rules, labeled as such; validate against your own renewal cohort once two quarters of review discipline exist. Full notes: `references/business-review-practices.md`.
