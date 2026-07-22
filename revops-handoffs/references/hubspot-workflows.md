# HubSpot Handoff Workflows

On-demand reference for the revops-handoffs skill. Read before giving HubSpot-specific handoff implementation advice. For broader HubSpot architecture beyond handoffs, also consult the revops-hubspot skill.

HubSpot can enforce every handoff in the bow tie, but only if the pipelines, properties, and workflows are built deliberately. Below is the handoff-specific configuration.

## 1. Pipeline architecture

Three pipelines, each with a distinct job:

- **New Business.** Standard acquisition stages through Closed Won.
- **Expansion.** Driven by an `expansion_type` property (upsell, cross-sell-warm, cross-sell-new-dmu) that governs which stages are conditionally required. See the expansion-pipeline-architecture reference for the stage logic.
- **Renewals.** Auto-created on Closed Won, dated to the contract term, and surfaced at T-90.

## 2. Property catalog

The handoff-critical custom properties HubSpot does not give you out of the box:

| Property | Object | Purpose |
|---|---|---|
| `first_connection_date` | Contact | Timestamp of first genuine sales touch, for speed-to-lead measurement |
| `speed_to_lead_hours` | Contact | Calculated from lead creation to `first_connection_date` |
| `expansion_type` | Deal | Drives conditional stages in the Expansion pipeline |
| `handoff_completeness_score` | Deal | Gate value checked before Closed Won can be set |
| `context_packet_url` | Deal | Link to the SPICED handoff document |
| `lead_tier` | Contact | Hand-raiser, MQL, or PQL, for routing |

HubSpot has no native speed-to-lead measurement, so the `first_connection_date` plus calculated `speed_to_lead_hours` pair is the workaround that makes the Marketing to Sales SLA reportable.

## 3. Core workflows

**MQL routing.** Trigger on MQL threshold reached. Actions: auto-enrich, set `lead_tier`, route by territory or account owner (account-based override always wins over rotation), post a Slack notification, start a 5-minute SLA timer, and auto-escalate or reassign at 24 hours if unworked.

**Closed-Won handoff.** Trigger on deal stage equals Closed Won. Gate: block or flag if `handoff_completeness_score` is below threshold or `context_packet_url` is empty. Actions on pass: create the onboarding ticket, create the associated Renewal deal dated to the term, notify the implementation or CS owner.

**Expansion signal.** Trigger on a company or usage property crossing a threshold (seat utilization, feature adoption, headcount growth). Actions: auto-create an Expansion deal, set `expansion_type`, associate it to the original deal, assign per the ownership thresholds, and notify the CSM and AE.

**Renewal automation.** Date-triggered at T-90 on the Renewal deal. Actions: assign owner, attach the customer-specific ROI or QBR material, start the renewal ABM sequence.

## 4. Breeze AI patterns

Where HubSpot Breeze earns its place in handoffs:

- **Deal and lead summaries** on the Marketing to Sales handoff, so the receiving rep opens a briefed record rather than raw fields.
- **Native intent scoring** feeding `lead_tier` and routing priority.
- **Context-packet drafting** at Closed Won, assembling deal history, stakeholders, and commitments into the handoff document for human review.

Treat Breeze output as a first draft that a human confirms, never as an unreviewed source of truth on commitments made during the sale.

## 5. Tier requirements

- **Deal-to-deal associations** (needed for the expansion lineage and time-to-expansion measurement) require **Professional** or above.
- **Calculated properties** (`speed_to_lead_hours`) require **Professional** or above.
- **Advanced workflow branching and escalation** are smoothest on **Professional / Enterprise**.
- On **Starter**, approximate with simpler date-stamp properties and manual review, and recognize that your SLA enforcement will be partial.

## How to use this reference

Match the workflow to the presenting problem: unworked leads points to MQL routing plus the 24-hour escalation, "CS never knows what sales promised" points to the Closed-Won completeness gate plus context-packet property, and "nobody owns expansion" points to the expansion-signal workflow plus the ownership thresholds encoded in the routing.

Confirm your HubSpot tier before implementing any workflow that requires Professional or above.
