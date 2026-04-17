# WbD Data Model Scaffold

*Reference file for revops-metrics, neon-obeya-builder, neon-expansion-revenue-architect, cs-operations, neon-benchmark-reference, revops-handoffs.*

---

## Section 1: V/CR/Δt per Bowtie Stage

Every bowtie stage maps to three measurement dimensions: **Volume Metric (VM)**, **Conversion Rate (CR)**, and **Velocity (Δt)**. Neon metric names are primary; WbD notation in parentheses.

### Inside Sales Motion (MQL → SQL → SAL path)

| Stage | Volume Metric (VM) | Conversion Rate (CR) | Velocity (Δt) |
|---|---|---|---|
| Awareness | Total Addressable Reach / MQLs (VM1) | Visitor → MQL % (CR1) | Days from first touch to MQL (Δt1) |
| Education | MQLs (VM2) | MQL → SQL % (CR2) | Days MQL → SQL handover / p95 (Δt2) |
| Selection | SQLs / Opportunities (VM3) | SQL → Opp % (CR3) | Days SQL → Opp creation (Δt3) |
| Commit | Opportunities (VM4) | Opp → Won % (CR4) | Sales cycle length / days Opp → Close (Δt4) |
| Onboarding | New Customers (VM5) | Activation Rate % at 30d (CR5) | Days to first value / TTV (Δt5) |
| Adoption | Active Customers (VM6) | Usage Threshold % (CR6) | Time to recurring usage milestone (Δt6) |
| Expansion | Expansion-Eligible Accounts (VM7–9) | Renewal %, Expansion Rate %, Upsell Win % (CR6–CR8) | Days from signal to expansion close (Δt7–8) |

### Enterprise Motion (MQA → Opportunity → Qualified Opp path)

| Stage | Volume Metric | Conversion Rate | Velocity |
|---|---|---|---|
| Awareness | Marketing Qualified Accounts (MQA) | Accounts touched → MQA % | Days first intent signal → outreach |
| Education | MQAs in nurture | MQA → Meeting Booked % | Days MQA → first discovery meeting |
| Selection | Active Opportunities | Opp → Qualified Opp % | Days to complete SPICED qualification |
| Commit | Qualified Opps | Qualified Opp → Won % | Days qualified → contract signed |
| Onboarding–Expansion | Same as Inside Sales above | Same structure | Same structure |

### PLG Motion (Hand-raise → PQL → PQA path)

| Stage | Volume Metric | Conversion Rate | Velocity |
|---|---|---|---|
| Awareness | Free / Trial Sign-ups | Visitor → Sign-up % | Days first touch → sign-up |
| Education | Active Trial Users | Trial → Hand-raise % | Days trial start → hand-raise signal |
| Selection | Product Qualified Leads (PQL) | PQL → PQA (Sales-Accepted) % | Days PQL → first sales contact |
| Commit | PQAs | PQA → Paid % | Days PQA → first payment |
| Onboarding–Expansion | Same as Inside Sales | NRR / Seat Expansion | Time from free → paid milestone |

**Usage notes:** In mixed motions (e.g. PLG + Enterprise overlay), run separate V/CR/Δt tracks per motion. Do not blend — blended metrics hide the structural problem in one track.

---

## Section 2: Expansion Type Matrix

Expansion type is defined by two axes: **same vs new impact** (what the customer wants to achieve) and **same vs new decider** (who makes the purchase decision).

| | **Same Decider** | **New Decider** |
|---|---|---|
| **Same Impact** | **Renew** | **Resell** |
| **New Impact** | **Upsell** | **Cross-sell** |

### Definitions

**Renew** — Same customer, same use case, same buyer. Lowest risk expansion type. Success signal: time-to-renewal conversation (earlier = healthier).

**Upsell** — Same customer, new use case (or expanded seats/volume), same buyer. Triggered by usage threshold or expansion signal in Tile 5. Owner: CS-to-Sales handoff on a defined trigger.

**Cross-sell** — New use case AND new buyer within the same account. Requires a new SPICED qualification cycle. Treat as a new enterprise opportunity.

**Resell** — Same use case, but the champion has departed and a new buyer must re-justify the investment. **Highest-risk expansion type and most overlooked.** The product continues working; the commercial relationship restarts from scratch. Champion departure is the trigger signal — log it the day you learn of it. Without proactive resell management, Resell silently becomes churn within 90 days of the new buyer taking the role.

**Implication for CS motion:** Build a champion departure playbook into the CS workflow. Trigger: contact role change detected (HubSpot workflow, LinkedIn Sales Nav alert, or manual log). Action: schedule introduction call with new contact within 14 days.

---

## Section 3: Churn Classification

Two fundamentally different churn types require different interventions. Conflating them produces the wrong fix.

### Onboarding Churn (Buyer's Remorse)

**When it happens:** Within 0–90 days of contract start.
**Root cause:** The customer bought a promise the product has not yet delivered. Expectation mismatch, slow time-to-first-impact, or poor handoff from sales.
**What it is NOT:** Product failure or competitive displacement.
**Fix:** Repair the sales-to-CS handoff (does CS receive SPICED context at handoff?), compress time-to-first-value, and set correct expectations during the sales cycle.

**Diagnostic question:** "Did the customer reach Activation within 30 days?" No → onboarding churn risk. Check Δt5.

### Usage Churn (Lack of Impact)

**When it happens:** 90+ days in. Often surfaces at renewal.
**Root cause:** The customer is not achieving the impact they expected. Could be adoption failure (customer didn't use the product correctly), fit failure (product doesn't solve their actual pain), or impact failure (product solves the stated pain but not the business outcome).
**What it is NOT:** Buyer's remorse.
**Fix:** Fix adoption motion (onboarding content, CSM-led usage reviews, proactive check-ins), validate the Impact Journey stage (see cs-operations), and tighten health scoring to catch customers stuck at Stage 1–3.

**Diagnostic question:** "Is the customer actively using the product AND achieving measurable outcomes?" No to either → usage churn risk. Check CR6 and Δt6.

**Why this distinction matters:** Throwing CSM resources at onboarding churn doesn't fix a broken sales handoff. Adding onboarding steps doesn't fix usage churn from a poor ICP fit. The fix must match the type.

---

## Section 4: Benchmarking Methods

Three cuts, each more surgical than the last. Use them in this order.

### Method 1: Industry Benchmarks (Broad Cut)

**What:** Published medians across a broad SaaS population (e.g. OpenView SaaS Benchmarks, Bessemer Cloud Index, SaaStock data).
**When:** Direction-setting only. "Are we in the right ballpark?" Use to identify major deviations (>2× off benchmark). Do not use for target-setting.
**Limitation:** Blends all GTM motions, ARR stages, and verticals. A PLG company at €5M ARR will look broken against an enterprise benchmark at €100M ARR. Always segment before comparing.

### Method 2: Peer Comparison (Selective Cut)

**What:** Benchmarks from companies with the same GTM motion, ARR range, and ACV profile. Requires normalised data — same definitions for MQL, SQL, Opp, etc.
**When:** After you have industry direction. Use to set realistic targets. "What does good look like for a company like us?"
**Limitation:** Requires data you often don't have from peers. Proxy: use investor portfolio benchmarks or neon-benchmark-reference with correct filters (ARR stage + GTM motion).

### Method 3: Trendline Analysis (Surgical Cut)

**What:** 12-month LTM (last twelve months) analysis of your own V/CR/Δt metrics. Are conversion rates improving, stable, or degrading? What changed when?
**When:** For target-setting, coaching, and countermeasure validation. "Are we getting better?" This is the most actionable method — you control the inputs.
**Tool:** Control charts (P-charts for conversion rates, X-MR charts for velocity). A metric in statistical control is predictable; a metric with special cause signals requires root cause.

### Performance Matrices

Combining two KPIs into a 2×2 creates actionable quadrants. Examples:

- **Pipeline coverage × Win rate:** Low coverage + high win rate → demand gen problem. High coverage + low win rate → qualification or deal execution problem.
- **NRR × GRR:** High NRR + low GRR → expansion masking churn (fragile). High GRR + low NRR → sticky but not growing (missed expansion signals).
- **CAC payback × NRR:** Long payback + high NRR → investment case is ok but cash-intensive. Short payback + low NRR → efficient acquisition but retention leak destroys LTV.

---

*Source: WbD Data Model and Revenue Architecture frameworks. Use in conjunction with neon-benchmark-reference for stage-appropriate targets.*
