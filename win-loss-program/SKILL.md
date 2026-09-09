---
name: win-loss-program
aliases: [win-loss-program, win-loss-analysis]
description: >
  Build a standing win-loss program that finds out why deals were actually
  won or lost, from two evidence lanes: mining the transcripts and threads of
  decided deals, and interviewing the buyers themselves after the decision.
  Triggers on 'win-loss,' 'why did we lose,' 'why do we win,' 'loss reasons,'
  'post-mortem this deal,' 'buyer interview,' 'customer arena,' 'group
  customer feedback session,' 'our CRM loss reasons are useless,'
  'competitive losses,' 'what is actually killing our deals,' or any
  situation where decisions about positioning, product, or process are
  being made from rep-reported loss fields. BOUNDARY: objection-mining works
  LIVE deals, extracting objections from in-flight conversations so reps can
  handle them; this skill works DECIDED deals, extracting causes after the
  outcome is known, which is a different evidence standard (no deal left to
  protect). closed-lost-revival consumes this program's loss patterns as its
  library's truth source and runs the re-engagement; battlecard-type skills
  consume the competitive findings; sales-ramp-enablement consumes the
  objection and loss-cause themes as certification curriculum. deal-
  qualification-gates consumes the findings upstream: recurring loss causes
  become new evidence-gate floors.
status: stable
---

# Win-Loss Program: The Truth Source for Everything Downstream

Average B2B win rates sit around 19-21% (Ebsta x Pavilion GTM Benchmarks, 2025 edition, still the latest full dataset). Read as an information problem: roughly four of five worked opportunities end in a decision your company usually never investigates. The loss-reason field in the CRM does not count as investigation. It is filled by the person with the strongest incentive to externalize the cause, seconds after the sting, from a dropdown that forces one cause where there were three. Loss fields cluster on "price" and "timing"; buyer interviews of the same deals routinely surface trust, absent capabilities, a stronger champion on the other side, or a decision that was rigged before the first call. Every downstream system inherits whichever version you record.

A win-loss program replaces attribution folklore with three evidence lanes, run on a standing cadence: mine every decided deal, interview a sample of buyers one on one, and periodically put a group of customers in one room with the whole go-to-market team listening.

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
| Start-up, pre product-market fit | Mine your last 5-10 deals for obvious friction: stalled discovery, price objections repeated across buyers, a decision-maker consistently missing from calls. Run Lane 1 only: pull transcripts and email threads, extract buyer language about the problem, timing, and alternatives. Do not interview or convene a session. The output is a one-page red-flag list, not a taxonomy. The question to answer: if you had 30 customers like your best three, which three decision killers would you fix first? |
| Start-up, product-market fit | You have a proven motion and 10 or more customers won the same way. Run Lane 1 on every decided deal within a week. For strategic wins and losses, add Lane 2 buyer interviews with a neutral interviewer (not the rep). Build a lightweight taxonomy: capability gap, trust/proof problem, price-to-value mismatch, champion strength, competitive move, timing/budget reality, or sales process failure. Tag each deal primary and secondary; track frequency. Hold a monthly sync to route recurring themes to product and enablement. Skip the customer arena until you have three months of patterns and the capacity to convene five customers. |
| Scale-up | Run all three lanes on standing cadence. Lane 1 on every decided deal; Lane 2 on 30-40% of deals (systematic rotating sample); Lane 3 (the customer arena) twice yearly per segment. Code each deal against the full driver taxonomy. Route findings weekly to product, sales, marketing, and CS owners. Hold a quarterly readout by segment, each finding anchored to buyer quotes, ranked by revenue impact. This becomes your single source of truth for positioning, roadmap, and sales-motion changes. |
| Enterprise | Win-loss programmes scale to dozens or hundreds of decided deals per quarter across regions and products, with dedicated interviewers or panels (not always the account owner or rep) trained on neutrality and cross-cultural listening, and Lane 3 expanding to multi-region cohorts or product-specific groups with cross-unit product and sales leadership present. Finance and legal involvement increase (analysing deal structure differences across regions, understanding if contract or procurement processes drove losses), and Governance includes quarterly synthesis sessions with regional sales leaders, product leadership, and finance, routing findings to formal product roadmap and sales-motion change processes. The skill gains weight in: Driver Taxonomy and Synthesis (aggregating and normalising decision drivers across regions and products so regional outliers surface), Buyer Interview Cadence (scaling Lane 2 with trained interviewers across geographies), and Customer Arena Design (multi-region arenas, cross-product cohorts). |

Skip before product-market fit: Lane 2: Buyer Interviews (the sampled, deeper lane); Lane 3: The Customer Arena (the group lane); Synthesis: From Stories to a Decision-Driver Taxonomy; What Good Looks Like; Diagnostic Questions.

## Lane 1: Transcript and Thread Mining (every decided deal)

The cheap lane, and with call recording in place, the one with no excuse. Within a week of any decision, mine the deal's full record: call transcripts, email threads, proposal versions, evaluation notes.

- Extract in the buyer's words: what they said about the problem, alternatives, money, timing, and internal politics. Verbatim quotes with timestamps, never paraphrases; a paraphrase is where wishful thinking re-enters.
- Reconstruct the decision timeline: when did the deal actually die or lock? It is almost never the dated loss event in the CRM; find the call where the energy changed and what preceded it.
- Contrast rep story vs record: write the rep's stated loss reason next to what the record shows. The recurring gap between the two, by rep and by cause, is itself a coaching output.
- Limits, stated honestly: mining only hears what was said TO you. The real reason often lives in the meeting you were not in. That is what Lane 2 is for.

Evidence sources: call transcripts (Fireflies, Gong, Chorus): highest reliability; captures exact SPICED language and depth. (2) Post-decision customer interviews: high reliability for Situation, Pain, Impact validation. (3) CRM history and deal notes: medium reliability; depends on rep discipline and completeness of documentation. (4) Firmographic signals (6sense, Apollo, company headcount change, job changes): medium reliability for Critical Event triggers and market signals. (5) Email and engagement telemetry (open rates, page visits, content clicks): lowest reliability; correlational not causal. For any stage-gate decision that advances or kills a deal, require call transcript or customer interview evidence. CRM notes alone do not clear a gate.

## Lane 2: Buyer Interviews (the sampled, deeper lane)

- **Sampling:** every large or strategic decision, a rotating sample of the rest, and both outcomes. Wins get interviewed too; a program that only studies losses learns half the causal model, and win interviews are where your actual differentiators (versus the ones on your slides) surface.
- **Timing:** 2-6 weeks after the decision (practice-based window). Sooner is raw; later is revisionist.
- **Who asks:** never the account's own rep. A neutral interviewer (founder on strategic deals, RevOps or PMM, or a third party) changes what buyers are willing to say; buyers soften the truth to the person they rejected.
- **Protocol:** 30 minutes, no selling, no defending, no correcting the record. One spine question: "walk me through the decision as it actually happened, from when you first felt the problem." Then follow the story: who was in the room, what almost changed the outcome, what the winning option did that mattered, what you did that annoyed or reassured them. Close with: "what would have had to be true for this to go the other way?"
- **The discipline:** when the buyer says something that stings, the interviewer writes it down and says "that is useful, say more." The program's value is measured by how often the findings are uncomfortable.

## Lane 3: The Customer Arena (the group lane)

The customer arena is a lean service-management format (known in Dutch practice as the klantarena): a moderated session where a group of customers talks about their experience while the company's cross-functional team (product, marketing, sales, customer support) sits in the listening seats. Where Lane 2 reconstructs single decisions, the arena surfaces the pattern layer live, and it answers the question analytics never can. Usage data and funnel metrics tell you WHAT is happening; the arena is where customers tell you WHY, in each other's presence, building on each other's answers in a way one-on-one interviews cannot.

- **Composition:** 5-8 customers per session, mixed deliberately: happy accounts, accounts that almost churned, recent wins, and where you can get them, a lost evaluator or churned customer (one skeptic in the room raises everyone's honesty). Segment-pure per session; a group that shares a context talks specifics.
- **The listening rule:** the company side asks clarifying questions only. No defending, no roadmap promises, no selling. The moment someone from your side explains why the customer's experience was actually fine, the arena is over; it just keeps talking for another hour without telling you anything.
- **The spine:** what are you using it for, why that, where does it grate, what almost made you leave, what would you tell a peer who asked about us. Walk the journey chronologically (first contact, buying process, onboarding, daily use, support) so friction lands on a stage, not in a vague pile.
- **The harvest is double-sided by design:** every friction point gets tagged product or process. "The integration kept breaking" is a product finding; "we never understood the pricing until the third call" is a sales-process finding; "nobody contacted us for four months after go-live" is a post-sale-process finding. Arenas run this way are one of the few instruments that improve the product and the sales motion from the same hour of evidence.
- **Cadence:** one or two per year per segment is enough to matter; the constraint is customer attention, not your calendar. Run one after any strategy-level surprise in the Lane 1/Lane 2 findings; the arena is the fastest way to test whether an interview theme generalizes.
- **The side effect is not a side effect:** customers who spend an afternoon being genuinely listened to, alongside peers, leave more invested than they arrived. Do not abuse this by turning the arena into a marketing event; it works because it is not one.

## Synthesis: From Stories to a Decision-Driver Taxonomy

Individual post-mortems are anecdotes; the program's output is the pattern layer.

1. Code every decided deal against a stable driver taxonomy (product capability, trust and proof, price-to-value, champion strength, competitive move, timing and budget reality, process failure). Multiple drivers per deal, weighted primary/secondary; single-cause coding rebuilds the dropdown problem you are escaping. Arena findings enter the same taxonomy carrying their product-or-process tag, which is what lets one readout speak to the roadmap and the sales motion at once.
2. Quarterly readout, cross-functional by design: sales sees process failures, product sees capability gaps ranked by revenue impact, marketing sees the language buyers actually used, leadership sees the trend lines. One page of findings, each anchored to quotes.
3. Route the outputs to their consumers: loss patterns into the revival library, recurring objections into enablement and proposal pre-handling, competitive findings into battlecards, and systematic causes into qualification gates (a cause that recurs five times is not a loss reason, it is a missing gate).

Worked example: A deal in your pipeline lasted 120 days and closed lost. Lane 1 mining finds the rep recorded 'price not justified,' but the email thread shows the buyer asked 'who else in the region uses this, and what happened to them?' three times unanswered. Lane 2 interview with the buyer confirms: 'We evaluate vendors the way we do hires; references matter, and we saw none.' Primary driver: trust and proof. Secondary: timing (budget cycle moved to Q3). Code it as 1-trust-and-proof, 2-timing-and-budget-reality. Plot both against your taxonomy. If trust surfaces in 40% of losses and only 5% of wins, you have a positioning gap, not a loss-reason problem.

## What Good Looks Like

The strongest programs are boring on cadence and uncomfortable in content: every decided deal mined within a week, interviews running on their sample without a launch decision each time, and a quarterly readout where at least one finding contradicts what the company believes about itself. The common failure is the opposite shape: a burst of post-mortems after a bad quarter, run by the reps on their own deals, producing reasons everyone already agreed with, then silence until the next bad quarter. You know it works when the CRM loss field stops being quoted in decisions because a better source exists, and when a positioning or roadmap choice can cite the interview evidence behind it. And by the second quarter the program audits itself: put the CRM loss fields and the interview findings for the same deals side by side; the divergence table is your local proof that the method surfaces what the fields miss, and if the divergence is small, examine the interviewing before concluding your fields were honest all along.

## Diagnostic Questions

1. Pull your last twenty losses. How many distinct loss reasons does the CRM show, and would anyone bet a euro on them?
2. When did a buyer last tell your company, in their own words and after the decision, why you really lost? Who heard it, and where is it written?
3. Which of your last quarter's losses were interviewed by someone other than the rep who lost them?
4. Name one product, positioning, or process change in the last year that cites decided-deal evidence. If none exists, where do those decisions currently get their facts?
5. Do your win stories and your marketing claims name the same differentiators? If you have never interviewed wins, how would you know?

When not to use this skill: (1) Your last quarter closed fewer than three deals. Use the one-page red-flag list instead (pre-PMF path). (2) You are building objection-handling for in-flight deals. Use objection-mining or deal-qualification-gates instead; this skill works only on decided deals where the decision is final and the buyer's incentive to protect a deal is gone. (3) You are designing your first sales process and have never run a sales motion. Establish the motion first; a win-loss programme answers 'which motion works,' not 'should we have a motion.'

Provenance notes and the practice-based rules list: read `references/win-loss-provenance.md`.

> Built by [Neon Triforce](https://neontriforce.com)
