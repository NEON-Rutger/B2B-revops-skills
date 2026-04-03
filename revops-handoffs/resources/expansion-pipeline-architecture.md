# Expansion Pipeline Architecture

Three-type expansion model, new-DMU cross-sell handling, ownership thresholds, HubSpot association model, SPICED requirements, and reporting payoff.

---

## 1. Why Expansion Needs Its Own Pipeline

Every expansion motion (upsell, cross-sell, add-on) needs its own deal record in a separate pipeline because:

- Each has its own sales cycle, close date, ACV delta, and conversion rate
- Mixing into new-business pipeline poisons both datasets
- Can't read new-logo win rate or expansion velocity cleanly
- In WbD terms: expansion is CR7 (Recurring Impact → Maximum Impact) and Δt7 (Time to Expand) — you need clean objects to measure both

---

## 2. Three-Pipeline Architecture

### Pipeline 1 — New Business (left side of bow tie)

Standard acquisition stages with SPICED gates:

| Stage | Probability | Gate |
|---|---|---|
| Discovery Qualified | 10% | SPICED situation and pain documented |
| Solution Fit Confirmed | 30% | Impact and critical event documented |
| Technical Validation | 50% | Technical requirements validated |
| Proposal / Commercial | 70% | Decision criteria and process documented |
| Verbal Commit | 90% | Champion confirms |
| Contract Sent | 95% | Legal/procurement in motion |
| Closed Won | 100% | Signed |
| Closed Lost | 0% | Lost reason required |

### Pipeline 2 — Expansion (right side of bow tie)

Shorter stages — trust exists. But with type-conditional rigour:

| Stage | Probability | Gate |
|---|---|---|
| Expansion Identified | 10% | Signal documented, CSM confirms timing |
| Discovery Qualified* | 20% | *Only for "Cross-sell (new DMU)" type — full SPICED required |
| Solution Fit* | 40% | *Only for "Cross-sell (new DMU)" type |
| Needs Assessment | 30%/60%** | Discovery done, SPICED updated for new pain |
| Proposal Sent | 60%/70%** | Commercial terms shared |
| Negotiation | 80% | Decision-maker engaged |
| Closed Won / Lost | 100/0% | Signed |

*Conditional stages: required when `expansion_type` = "Cross-sell (new DMU)". Upsells and warm cross-sells skip these.

**Probability adjusts: upsells enter Needs Assessment at higher effective probability than new-DMU cross-sells. Use `expansion_type` filter in forecasting.

### Pipeline 3 — Renewals (retention)

Auto-created by workflow on original Closed Won. Close date = contract end − 90 days.

| Stage | Gate |
|---|---|
| Active Contract | 6–12 months out |
| Upcoming Renewal | <90 days, CSM preparing |
| Renewal Proposal Sent | Terms shared |
| Negotiation | Discussion active |
| Renewed | Signed for next term |
| Churned | Lost + churn reason required |
| Downgrade | Renewed at lower value + reason |

---

## 3. The Three Expansion Types

This is the most important design decision. Not all expansion is the same motion.

### Type 1: Upsell (More of Same)

**DMU**: Same champion, same budget holder, same decision process.
**Examples**: More seats, higher tier, additional capacity, premium features.
**Sales cycle**: Short. Often a conversation, not a negotiation.
**Pipeline path**: Identified → Proposal → Won (skip Needs Assessment if simple).
**SPICED**: Refresh only — the original pain still applies, just more of it.
**Win rate benchmark**: 50%+.
**Velocity benchmark**: Days to weeks.

### Type 2: Cross-Sell (Warm)

**DMU**: Partial overlap — existing champion introduces new stakeholder, but there's a new budget or decision process.
**Examples**: New product module for existing team, adjacent use case championed by same person but involving new approvers.
**Sales cycle**: Moderate. Discovery needed on the new pain, but existing relationships accelerate.
**Pipeline path**: Identified → Needs Assessment → Proposal → Negotiation → Won.
**SPICED**: Partial refresh — Situation similar, Pain and Impact are new, Decision process may differ.
**Win rate benchmark**: 30–40%.
**Velocity benchmark**: Weeks to low months.

### Type 3: Cross-Sell (New DMU)

**DMU**: Completely new buying group, new budget holder, new champion, new decision criteria. The existing customer's BU-A team may not even be involved.
**Examples**: Different department adopting the product, new business unit, different geography within the same company.
**Sales cycle**: Full. This is a new-logo sale inside a known company. Trust is with the account, not the buying group.
**Pipeline path**: Identified → Discovery Qualified → Solution Fit → Proposal → Negotiation → Won.
**SPICED**: Full and new. Different Situation (department context), different Pain (they may not know BU-A uses the product), different Impact, different Critical Event, different Decision process.
**Win rate benchmark**: 20–30%.
**Velocity benchmark**: Months — comparable to new business.

### The Litmus Test

**"Would losing the existing contract in BU-A affect the likelihood of closing in BU-B?"**

- If yes → it's expansion (cross-sell warm or new DMU), keep in expansion pipeline
- If no → it's a new logo that shares a company name. Route to new-business pipeline with "customer referral" source tag

### Why This Distinction Matters

Without it:
- Win rates look artificially low (new-DMU deals drag down the expansion average)
- Velocity looks artificially slow (months-long cycles mixed with week-long upsells)
- Forecast is wrong (CRO can't weight different motions)
- CS performance is misjudged ("CS isn't generating good opportunities" when really the deals are fine for what they are)

With it:
- Clean benchmarks per motion
- Accurate forecast weighting
- CS gets proper credit
- Right process applied to right deal
- Routing can differ by type (new DMU may need different rep)

---

## 4. New-DMU Cross-Sell: What Changes

### Stakeholder Map Starts Over

The existing company record has contacts from BU-A. The new-DMU deal needs its own contacts:
- New champion
- New economic buyer
- New end users
- Possibly new procurement/legal contacts

In HubSpot: the expansion deal associates to **different contacts** than the original deal, even though both sit under the same company. Deal-to-contact associations are per-deal, not per-company.

### SPICED Is Mandatory and Full

Not a refresh — a **new SPICED**:

| Component | Original Deal | New-DMU Cross-Sell |
|---|---|---|
| Situation | BU-A's context | BU-B's context (may be completely different) |
| Pain | BU-A's pain | BU-B's pain (they may not know BU-A uses the product) |
| Impact | BU-A's impact metrics | BU-B's impact metrics |
| Critical Event | BU-A's timeline | BU-B's timeline (different budget cycle, project deadlines) |
| Decision | BU-A's process | BU-B's process (different approvers, procurement rules) |

Gate: deal should not advance past first stage without complete SPICED.

### Introduction Path Matters

Three paths with different conversion profiles:

| Path | Mechanism | Expected Conversion | Speed |
|---|---|---|---|
| Champion referral | BU-A champion introduces to BU-B stakeholder | Highest | Fastest |
| AE/CSM direct outreach | Using account knowledge and access | Moderate | Moderate |
| Marketing ABM play | LinkedIn + email into new department | Lower (but scalable) | Slowest |

Track in `cross_sell_intro_source` property to optimise over time.

### Ownership May Differ

If BU-B falls in a different:
- **Vertical** → may need a different AE with domain expertise
- **Geography** → may need local-language rep
- **Segment** → may need different sales motion (enterprise vs mid-market)

The expansion deal AE should be determined by who owns the **new** buying group's segment, not automatically inherited from the company's existing account owner. Build this into routing logic.

### Timeline Is Independent

BU-B has its own:
- Budget cycle
- Project deadlines
- Procurement requirements
- Implementation timeline

Don't assume BU-A's contract dates or renewal cycle apply.

---

## 5. HubSpot Association Model

### Deal-to-Company

All deals (new business, expansion, renewal) associate to the same Company record. This gives you a single view of all commercial relationships with the customer.

### Deal-to-Contact

Each deal associates to the contacts relevant to **that** deal:
- New-business deal → BU-A contacts (original champion, buyer, users)
- Upsell deal → same BU-A contacts (or subset)
- Warm cross-sell → mix of BU-A and new contacts
- New-DMU cross-sell → **different** contacts (BU-B champion, buyer, users)

### Deal-to-Deal

Use **deal-to-deal association** (Professional+) to link:
- Expansion deal → original new-business deal (lineage)
- Renewal deal → original new-business deal
- Multiple expansion deals → same original deal

This enables:
- Δt7 measurement: time from original Closed Won to first expansion
- Full customer revenue lineage on a single view
- Cohort analysis: which original deals generate the most expansion?

### Company Properties

Aggregate fields on the Company record:
- `arr_current` — total current ARR (sum of active deals)
- `customer_status` — Active / Churned / At Risk
- `expansion_pipeline_active` — Yes/No
- `total_expansion_deals` — count
- `first_expansion_date` — for Δt7 calculation

---

## 6. Expansion Deal Properties

### Required on All Expansion Deals

| Property | Type | Values | Purpose |
|---|---|---|---|
| `expansion_type` | Dropdown | Upsell / Cross-sell (warm) / Cross-sell (new DMU) | Drives stage requirements, reporting, forecast weighting |
| `expansion_source` | Dropdown | CS-identified / Customer request / Marketing signal / Usage trigger | Attribution for expansion pipeline |
| `arr_delta` | Currency | — | Incremental value (not total contract) |
| `associated_original_deal` | Deal association | Link to original deal | Lineage, Δt7 |
| `csm_owner` | HubSpot user | Copied from company | Keeps CS visible even when AE runs commercial |

### Additional for Cross-Sells

| Property | Type | Values | Purpose |
|---|---|---|---|
| `cross_sell_intro_source` | Dropdown | Champion referral / Direct outreach / Marketing ABM | Path optimisation |
| `new_dmu_department` | Text | — | Which department/BU (for new-DMU type) |
| `new_dmu_budget_independent` | Checkbox | — | Whether BU-B has independent budget |

### SPICED Properties (Same as New Business)

Reuse the SPICED property group: `spiced_situation`, `spiced_pain`, `spiced_impact`, `spiced_critical_event`, `spiced_critical_event_detail`, `spiced_decision_criteria`, `spiced_decision_process`.

For upsells: SPICED refresh (existing fields updated).
For warm cross-sell: partial new SPICED (some fields new, some refreshed).
For new-DMU cross-sell: all fields must be new — gate advancement on completeness.

---

## 7. Automation: Signal → Deal Creation

CSMs should **not** create expansion deals manually. They flag signals; the system creates deals.

### Workflow: CS-Identified Signal

1. CSM sets `expansion_signal` property on Company record
   - Values: Upsell opportunity / Cross-sell opportunity / Usage limit approaching / New department interest / Customer request
2. Workflow branches by signal type:
   - "Usage limit approaching" / "Customer request" / "Upsell opportunity" → `expansion_type` = Upsell
   - "Cross-sell opportunity" → `expansion_type` = Cross-sell (warm)
   - "New department interest" → `expansion_type` = Cross-sell (new DMU)
3. Create deal in Expansion Pipeline
   - Name: "[Company] — [expansion_type] — [date]"
   - Owner: `account_executive` from company (or territory owner for new-DMU)
   - Copy: `arr_current`, `health_score`, `csm_owner` from company
4. Create task for AE: "Review expansion opportunity", due 48h
5. Create task for CSM: "Prepare expansion brief", due 24h
6. Slack notification to both
7. Set company `expansion_pipeline_active` = Yes

### Workflow: Auto-Detected Usage Signal

Trigger: product data pushed to HubSpot:
- `seats_used_pct` > 80%
- `new_module_trial` = Yes
- `feature_limit_hit` = Yes

Action: auto-set `expansion_signal` → triggers CS-identified workflow above.

---

## 8. Reporting Payoff

With clean pipelines, type tagging, and associations, you can answer:

| Question | How | Expected Insight |
|---|---|---|
| Win rate by expansion type? | Filter expansion pipeline by `expansion_type` | Upsell ~50%+, warm cross-sell ~30%, new-DMU ~20% |
| Velocity by type? | Average days in pipeline by `expansion_type` | New-DMU is 2–3× longer than upsell |
| Expansion pipeline by source? | Group by `expansion_source` | Is CS generating enough, or marketing doing heavy lifting? |
| Best intro path for cross-sells? | Group by `cross_sell_intro_source` | Champion referral converts highest |
| Time to first expansion (Δt7)? | `first_expansion_date` − original `closed_won_date` | By segment, by product, by implementation path |
| NRR decomposition? | GRR (renewal pipeline) + expansion rate − churn | Component-level view of retention health |
| Forecast accuracy by type? | Predicted vs actual close by `expansion_type` | Weight new-DMU at lower probability |
| Which original deals generate most expansion? | Deal-to-deal association + `arr_delta` | Cohort/segment analysis |

---

## 9. Ownership Model Decision Framework

### By ACV Threshold

| Expansion ACV | Commercial Owner | CS Role | Sales Involvement |
|---|---|---|---|
| < €10K | CSM | Owns end-to-end | None (unless escalated) |
| €10K–50K | AM or AE | Provides context, stays in meetings | Runs commercial with CS support |
| > €50K | AE (full cycle) | Introduces, advisory | Full sales process |

### By Complexity

Even below €10K, if the expansion involves:
- New procurement process → involve AE
- Multi-stakeholder sign-off → involve AE
- Competitive evaluation → involve AE
- Contract renegotiation → involve AE

### By Type Override

New-DMU cross-sells may warrant AE involvement regardless of ACV because:
- Discovery depth is higher
- New stakeholder relationships need building
- Competitive dynamics may differ from original sale

### Governance Requirements

Define thresholds explicitly in writing. Review quarterly. The most common failure: ambiguity where nobody closes because everyone assumes someone else will.

Record ownership decisions in governance ledger with effective date and owner.
