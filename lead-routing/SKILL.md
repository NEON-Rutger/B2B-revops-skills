---
name: lead-routing
aliases: [lead-routing]
description: >
  Lead routing strategy, assignment logic, round-robin patterns, territory
  design, speed-to-lead SLA frameworks, and routing automation for B2B
  revenue teams. Use when the user mentions lead routing, lead assignment,
  round-robin, territory assignment, lead distribution, speed-to-lead,
  lead SLA, lead queue, routing rules, routing logic, account-based routing,
  geographic routing, skills-based routing, load balancing, lead handoff,
  inbound lead routing, outbound lead routing, routing tools (LeanData,
  Chili Piper, Default), or lead cherry-picking. Also trigger on 'leads
  aren't getting to the right rep,' 'our routing is broken,' 'leads sit in
  a queue,' 'reps cherry-pick,' 'speed-to-lead is too slow,' or 'we need
  to redesign territories.' BOUNDARY: Covers routing STRATEGY and LOGIC
  (CRM-agnostic). For CRM-specific implementation, see revops-hubspot or
  revops-salesforce. For enrichment that feeds routing, see data-enrichment.
  For lead scoring, see marketing-operations.
status: seed

---

# Lead Routing for B2B Revenue Operations

Lead routing determines which rep gets which lead, how fast, and with what context. It's where marketing's work either converts to pipeline or dies in a queue.

## Why Routing Matters

**Speed kills (in a good way)**:
### Speed-to-Lead Impact (Research-Backed)

| Finding | Source |
|---------|--------|
| Responding within 1 minute: 391% conversion boost | Velocify |
| Responding within 5 minutes: 21× more likely to qualify vs 30 min | Dr. James Oldroyd, MIT Sloan, 2007 (15,000+ leads) |
| <5 min response: 32% close rate, 2.6× higher than 24+ hours | LeanData, 2025 |
| 10-minute hand-raiser SLA: 40% increase in lead-to-opportunity conversion | Justin Norris, RevOps FM, 2025 |
| Instant booking: 66.7% conversion vs ~30% industry average | Chili Piper, 2025 (4M form submissions) |
| Average B2B response time: 42 hours; 23% never respond | HBR, 2011 (2,241 companies) |

> *Conversion impact decays rapidly after the first 5 minutes but exact decay curves vary by industry, lead source, and deal size. The research consensus: respond to hand-raisers within 5-10 minutes; the difference between 10 minutes and 30 minutes matters more than the difference between 1 hour and 4 hours.*
Every minute between form submission and rep response reduces conversion probability. Speed-to-lead is the most under-optimised metric in most B2B organisations.

---

## Routing Architecture

### The Routing Decision Tree

Every routing system answers five questions in order:

```
1. Is this a known account? (Account matching)
   → Yes: Route to Account Owner (ABM path)
   → No: Continue

2. Does this lead match our ICP? (Scoring/qualification)
   → Below threshold: Route to nurture / marketing automation
   → Above threshold: Continue to sales routing

3. Which territory does this belong to? (Territory assignment)
   → Evaluate geography, industry, company size, product interest
   → Assign territory

4. Which rep within the territory? (Assignment logic)
   → Round-robin, weighted, skills-based, or load-balanced
   → Assign owner

5. Is the assigned rep available? (Availability check)
   → Yes: Assign and notify
   → No: Route to backup or queue with SLA escalation
```

### Routing Models

| Model | How It Works | Best For | Watch Out For |
|-------|-------------|----------|---------------|
| **Geographic** | Route by region/country/city | Field sales with territories | Unbalanced territories |
| **Named Account** | Route to account owner | ABM, enterprise sales | New accounts fall through |
| **Round-Robin** | Rotate evenly across reps | Inside sales, equal territories | Doesn't account for capacity |
| **Weighted Round-Robin** | Rotate with weighting (e.g., senior rep gets 2x) | Mixed-tenure teams | Complex to maintain |
| **Skills-Based** | Route by product knowledge, language, vertical expertise | Multi-product, multi-lingual | Bottlenecks on specialists |
| **Load-Balanced** | Route based on current capacity | High-volume teams | Requires real-time capacity data |
| **Hybrid** | Territory first → round-robin within territory | Most B2B SaaS teams | More routing rules to maintain |

---

## Round-Robin Design

### Basic Round-Robin

Rotate leads evenly across a pool of reps:

```
Counter = 0
Reps = [Alice, Bob, Carol, David]

Lead 1 → Reps[0 % 4] = Alice   (counter → 1)
Lead 2 → Reps[1 % 4] = Bob     (counter → 2)
Lead 3 → Reps[2 % 4] = Carol   (counter → 3)
Lead 4 → Reps[3 % 4] = David   (counter → 4)
Lead 5 → Reps[4 % 4] = Alice   (counter → 5)
```

### Weighted Round-Robin

Assign weights to reps (e.g., senior rep handles more, ramping rep handles fewer):

> *Illustrative example. Configure weights based on rep capacity, ramp status, and current quota attainment.*

| Rep | Weight | Share |
|-----|--------|-------|
| Alice (senior) | 3 | 37.5% |
| Bob (mid) | 2 | 25% |
| Carol (mid) | 2 | 25% |
| David (ramping) | 1 | 12.5% |

Implementation: Expand the rotation list proportionally:
`[Alice, Alice, Alice, Bob, Bob, Carol, Carol, David]`

### Round-Robin with Availability

Add availability checks before assignment:

```
Get next rep from rotation
  → Check: Is rep on OOO / vacation?
    → Yes: Skip, advance counter
  → Check: Has rep exceeded daily lead cap?
    → Yes: Skip, advance counter
  → Check: Is current time within rep's working hours?
    → Yes: Assign
    → No: Assign to queue, schedule assignment for next business hour
```

### Common Round-Robin Problems

| Problem | Symptom | Fix |
|---------|---------|-----|
| **Cherry-picking** | Reps grab "good" leads, leave others | Route directly to owner, not to shared queue |
| **Queue rot** | Leads sit in queue untouched | SLA timer + auto-reassignment |
| **Uneven distribution** | One rep gets more leads | Audit counter logic; check for timezone/filter issues |
| **New rep flooding** | Ramping rep gets same volume as veteran | Use weighted round-robin during ramp |
| **Timezone gaps** | Leads arrive outside business hours with no owner | Time-aware routing or follow-the-sun model |

---

## Territory Design

### Territory Variables

| Variable | Examples | Complexity |
|----------|---------|-----------|
| **Geography** | Country, region, city, postcode | Low |
| **Industry/Vertical** | SaaS, Healthcare, Financial Services | Low-Medium |
| **Company Size** | SMB (<100), Mid-Market (100-1,000), Enterprise (1,000+) | Low |
| **Product/Solution** | Product A vs Product B; platform vs point solution | Medium |
| **Named Accounts** | Strategic accounts assigned to specific reps | Medium |
| **Hybrid** | Geography × Size × Industry | High |

### Territory Balance Metrics

Check quarterly:
- **Pipeline per territory**: Should be ±10-15% of median across territories (Fullcast territory planning research, 2024-2025)
- **Lead volume per territory**: Even distribution within same segment
- **Win rate per territory**: Significant variance suggests territory design issue, not rep issue
- **Quota-to-pipeline ratio**: Each territory should have 3-4x pipeline coverage

### Territory Assignment Methods

**Static assignment** (spreadsheet-managed):
- Pros: Simple, transparent
- Cons: Doesn't scale; manual updates; no automatic reassignment
- Best for: <10 reps, simple territories

**Rule-based assignment** (CRM automation):
- Pros: Automatic; consistent; auditable
- Cons: Rules can conflict; maintenance overhead
- Best for: 10-50 reps, moderate complexity

**Enterprise Territory Management** (Salesforce ETM or equivalent):
- Pros: Hierarchical; multi-territory assignment; forecasting integration
- Cons: Complex setup; expensive
- Best for: >50 reps, overlays, complex hierarchies

---

## Speed-to-Lead SLA Framework

### SLA Tiers

| Lead Tier | Definition | SLA (First Touch) | Escalation |
|-----------|-----------|-------------------|------------|
| **Tier 1 (Hot)** | High ICP fit + high engagement score; demo/pricing request | 5 minutes | 15 min: alert manager; 30 min: reassign |
| **Tier 2 (Warm)** | Good ICP fit + moderate engagement; content download | 1 hour | 2 hours: alert manager; 4 hours: reassign |
| **Tier 3 (Nurture)** | Low fit or low engagement | 24 hours | 48 hours: return to marketing; alert ops |
n> *T1 (5-minute) threshold is research-backed: MIT (21× at 5 min), Justin Norris (10 min → 40% conversion lift), Chili Piper (instant booking → 66.7% conversion). T2 (1-hour) is backed by LeanData's MQL SLA recommendation. T3 (24-hour) represents common practitioner convention for lower-intent leads. All tiers should be calibrated to your team capacity and lead volume.*

### SLA Tracking Fields

| Field | Type | Purpose |
|-------|------|---------|
| Routed_At | DateTime | When lead was assigned to an owner |
| First_Touched_At | DateTime | When owner first logged activity |
| SLA_Minutes | Formula (First_Touched - Routed) | Time to first engagement |
| SLA_Status | Formula (Met/Warning/Breached) | Real-time SLA compliance |
| SLA_Tier | Picklist (Tier 1/2/3) | Which SLA applies |

### Escalation Workflow

```
Lead Assigned (Routed_At populated)

Timer 1: SLA_Tier threshold reached, no activity logged
  → Alert rep (Slack/email): "Lead SLA at risk"

Timer 2: SLA_Tier threshold × 2, still no activity
  → Alert manager: "Lead SLA breached"
  → Create task for manager review

Timer 3: SLA_Tier threshold × 4, still no activity
  → Reassign to backup rep or queue
  → Alert RevOps: "Lead reassigned due to SLA breach"
  → Log SLA_Breached = true for reporting
```

---

## Account-Based Routing (ABM)

When the lead matches an existing account:

```
New Lead arrives
  → Match to existing Account (by email domain, company name, or enrichment)
  → Match found?
    → Yes, Account has an Owner:
        → Route to Account Owner (preserves relationship)
        → If Owner is SDR: Route to assigned AE instead
        → Notify Account Owner: "New contact from your account"
    → Yes, Account exists but no Owner:
        → Route via standard territory logic
        → Assign Account Owner simultaneously
    → No match:
        → Standard routing (territory + round-robin)
```

### ABM Routing Considerations

- **Multi-threading signal**: New contact from existing account = potential expansion signal → route to Account Owner AND alert CS
- **Competitor accounts**: Route differently (or exclude from routing entirely)
- **Customer accounts**: New contact from existing customer → route to CSM, not sales
- **Churned accounts**: Former customer re-engaging → high priority; route to win-back specialist or original AE

---

## Routing Tool Landscape

### Dedicated Routing Tools

| Tool | Strength | Best For |
|------|----------|----------|
| **LeanData** | Most mature SFDC routing; visual flow builder | Salesforce-first orgs with complex routing |
| **Chili Piper** | Real-time booking + routing; instant scheduling | Teams wanting form → meeting in one step |
| **Default** | Modern routing + enrichment + scheduling combined | Mid-market teams wanting all-in-one |
| **RevenueHero** | Affordable alternative to Chili Piper | Budget-conscious teams |

### Build vs Buy Decision

```
<500 leads/month + simple territories?
  → Build with native CRM automation (free)

500-5,000 leads/month + moderate complexity?
  → Evaluate dedicated routing tool
  → Build if team has strong CRM admin

>5,000 leads/month OR complex territories?
  → Dedicated routing tool (LeanData, Chili Piper, Default)
  → ROI = speed-to-lead improvement × conversion lift × deal value
```

---

## Routing Audit Checklist

Run quarterly:

1. **Coverage**: Are there any routing rules that produce no owner? (leads falling through cracks)
2. **Balance**: Is lead distribution even across reps in same segment? (±10% variance acceptable)
3. **Speed**: What's median speed-to-lead? What's 90th percentile? (target: <5 min median for Tier 1)
4. **SLA compliance**: % of leads touched within SLA? (target: >90%)
5. **Reassignment rate**: How often are leads reassigned? (>15% suggests routing logic issues)
6. **Conversion by route**: Do different routing paths convert differently? (identify broken paths)
7. **Queue health**: How many leads are sitting in queues right now? How long? (target: 0 leads >1 hour)
8. **Availability coverage**: Are there time periods with no available reps? (follow-the-sun gaps)

---

## Cross-References

- For CRM-specific routing implementation → see **revops-hubspot** or **revops-salesforce**
- For enrichment that feeds routing decisions → see **data-enrichment**
- For lead scoring and MQL definitions → see **marketing-operations**
- For handoff design (what happens after routing) → see **revops-handoffs**
- For territory design within GTM planning → see **gtm-planning**


---

## References

- Dr. James Oldroyd, MIT Sloan (2007). 15,000+ leads, 6 companies. 5-minute response: 21× more likely to qualify.
- Velocify. 1-minute response: 391% conversion boost.
- HBR (2011). "The Short Life of Online Sales Leads." 2,241 companies. Average response: 42 hours. 23% never responded.
- Justin Norris, RevOps FM (2025). "A Complete Guide to Speed-to-Lead." 10-min hand-raiser SLA → 40% lead-to-opportunity conversion lift.
- LeanData (2025). Lead Processing Time + Representative Response Time framework. <5 min = 32% close rate, 2.6× higher than 24+ hours.
- Chili Piper (2025). 2025 Benchmark Report: ~4M form submissions. Instant booking: 66.7% conversion vs ~30% industry average.
- Fullcast (2024-2025). Territory planning research: ±10-15% variance tolerance for balanced territories.
- LeanData. Round-robin routing datasheet; account-based routing documentation.
- Chili Piper. Lead-to-account matching; meeting routing documentation.

> Built by [Neon Triforce](https://neontriforce.com)
