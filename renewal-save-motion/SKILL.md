---
name: renewal-save-motion
aliases: [renewal-save-motion, churn-save]
description: >
  Run the defensive counterpart to expansion: a structured save motion for
  at-risk customers and a renewal runbook that starts at T-120, not the week
  the contract ends. Triggers on 'renewal at risk,' 'customer went quiet,'
  'churn save,' 'save play,' 'they stopped using the product,' 'champion
  left the account,' 'renewal coming up,' 'GRR is slipping,' 'downgrade
  request,' 'cancellation notice,' 'win the renewal,' or any situation where
  a health signal fired and the team's only play is a discount and a prayer.
  Entry condition: a risk flag already exists (from a health scan, usage
  drop, champion departure, or a blocked expansion attempt). BOUNDARY:
  customer-health scanners (e.g. customer-health, account-health-audit)
  DETECT risk across the base; this skill executes the intervention on one
  flagged account, starting where their output ends. expansion-opportunity-
  analysis is the offense on healthy accounts; the two are mutually
  exclusive on the same account at the same time, and its no-activity hard
  gate is precisely the handoff INTO this skill. cs-operations owns the
  full CS org design (segmentation, staffing, QBR cadence); this skill is
  one motion inside that system, not the system.
status: stable
---

# Renewal Save Motion: Defense Is a System, Not a Discount

Median gross revenue retention for private SaaS runs around 90%, with top-quartile companies above 95% (SaaS industry surveys, 2025). The distance between those two numbers is rarely product quality. It is whether the company runs renewals as a managed motion with an early-warning save play, or discovers churn in the cancellation email. Retaining revenue also costs a fraction of re-acquiring it; the 5x-and-up cost gap between acquisition and retention has been replicated across studies for a decade (Bain/HBR lineage, 2014; industry guides still report 5-25x ranges in 2025-2026).

Expansion gets the attention because it is offense. But a dollar of churn cancels a dollar of expansion at par, and the save window closes silently: by the time a customer tells you they are leaving, they finished evaluating alternatives weeks ago.

**Entry condition:** this skill runs on a FLAGGED account. Detection is upstream (health scans, usage monitoring, champion-move detection). If nothing is flagged and no renewal sits inside 120 days, you do not need this skill yet; you need detection.

---

## The Renewal Clock

Every renewal runs the same clock, regardless of health. Healthy accounts move through it in minutes per checkpoint; flagged accounts trigger the save motion.

| Checkpoint | Action |
|---|---|
| T-120 | Renewal owner named. Health verdict pulled (usage trend, support pattern, champion status, sponsor status). Verdict: CLEAN, WATCH, or AT-RISK. |
| T-90 | AT-RISK accounts enter the save motion below. WATCH accounts get a value-recap touch and a re-verdict at T-60. CLEAN accounts get the renewal packet drafted. |
| T-60 | Commercial terms on the table for CLEAN and recovered accounts. No surprises inside 60 days: if the price is changing, the customer heard it by now. |
| T-30 | Signature logistics only. If substantive objections first appear here, the motion failed upstream; log that as the lesson, not "late-stage save." |

The clock exists because renewal risk is visible in behavior (login decay, feature abandonment, sponsor silence) long before it is audible in words. Practice-based rule of thumb, not a study: if you first learn about risk inside 60 days, your detection layer, not this account, is the real problem.

## Risk Triage: Name the Failure Mode First

A save play aimed at the wrong failure mode accelerates the churn. Classify before acting:

1. **Value gap** (they use it and cannot prove it is worth the money): the missing artifact is an impact story in their numbers. Save play: build the value recap FROM their system data, walked through with the economic buyer, not the daily user.
2. **Adoption gap** (they stopped using it, or never really started): the honest question is whether the problem still exists for them. Save play: shrink to the one workflow that hurt when they bought, relaunch that, and only that. A re-onboarding of everything convinces no one.
3. **Champion loss** (your person left, silence followed): treat as a NEW SALE at the same account. Save play: map who inherited the problem, brief them as a stranger who is inheriting a paid solution, never as someone who owes you continuity. Also route the departed champion to your revival lane; one event, two plays.
4. **Sponsor shift** (reorg, new exec, strategy change; your product is now someone else's decision): save play: executive-to-executive re-anchor on the new agenda. A feature demo cannot fix a political change.
5. **Competitive displacement** (an alternative is actively in the building): save play: the switching-cost case plus a roadmap commitment with a date, delivered by someone senior. If you discover this one at T-30, assume you are negotiating an exit, and optimize for a dignified door left open.

## Commercial Levers, In Order

The discount is the last lever, not the first, because a discount buys silence, not adoption, and it reprices every future renewal at this account and every account that hears about it.

1. Scope right-sizing: fewer seats or modules at defensible value beats a discount on unused shelf-space. A smaller true contract retains more revenue over two years than a larger resented one.
2. Term restructure: shorter renewal with success criteria attached, or multi-year with protection, depending on which side is uncertain.
3. Service injection: implementation help, training, an owned success plan. Costs you margin once; a discount costs you margin forever.
4. Pause over cancel where the platform allows it: preserves data, relationship, and the reactivation path.
5. Price concession, last, always exchanged for something real (case study, term length, expansion option, reference), never given for free.

## When the Save Fails

Some accounts should churn: wrong-fit customers bought in an over-eager quarter, companies that pivoted away from the problem. Fighting every churn teaches the team that retention is begging.

- Decide save-versus-release explicitly at triage: fit still right, problem still real, economics still sensible. Two of three or better: fight. Otherwise: release well.
- A released account gets a clean exit, data handover, and a standing re-entry premise ("if [the trigger that broke this] changes, here is the door"). Churned-well accounts are a revival lane later; churned-badly accounts are a review on a site your prospects read.
- Every loss, fought or released, gets an autopsy in the same loss-pattern library your closed-lost motion uses (see closed-lost-revival): failure mode, first detectable signal, days between signal and action. The library is how next quarter's saves start earlier.

## Scorekeeping

- Save rate BY FAILURE MODE, not blended: a 60% save rate on value-gap accounts and 10% on competitive displacement are two different businesses hiding in one metric.
- Signal-to-action lag: days from first risk signal to first human intervention. This is the number the whole motion exists to shrink.
- Concession cost per saved dollar, so finance can see that the service-injection lever beats the discount lever on evidence, not philosophy.
- GRR quarterly against the 90% median / 95% top-quartile line (2025 surveys), segmented the way your board segments it.

Benchmark provenance, vintages, and which rules are practice-based rather than studied: read `references/retention-benchmarks.md`.

## Diagnostic Questions

1. List renewals due in the next 120 days. Who owns each one, by name, today?
2. For your last five churns: on what date was the risk FIRST visible in system data, and on what date did a human first act? The gap is your motion's real latency.
3. What percentage of at-risk saves in the last year used a discount as the first lever, and what did those accounts do at the following renewal?
4. When a champion leaves a customer account, what happens automatically today? Anything?
5. Can your team produce a value recap in the customer's own numbers for your top ten accounts within one day? If not, the value-gap save play has no ammunition.

> Built by [Neon Triforce](https://neontriforce.com)
