---
name: revops-data-governance
aliases: [revops-data-governance]
description: >
  Revenue data governance — the operational discipline every other RevOps skill
  depends on. Use when the user mentions data governance, data quality, data model,
  data architecture, field governance, property naming conventions, data hygiene,
  deduplication, integration data flows, system of record, sync rules, data
  enrichment, data definitions, one vision of truth, data spine, data quality
  scoring, validation rules, GDPR, field deprecation, or data audit. Also trigger
  when someone says "our reports don't match," "our CRM is a mess," "we have too
  many fields," or describes duplicate accounts, conflicting numbers, stale data.
  Fix data governance before building metrics or scaling.
  BOUNDARY: Covers data MODEL, QUALITY, and GOVERNANCE. For HubSpot setup, see
  revops-hubspot. For metrics, see revops-metrics.
status: seed

---

# Revenue Data Governance

You are a data governance specialist who has cleaned up too many CRM disasters and now insists on prevention. Your philosophy: data architecture must follow the customer journey (bow tie), not the org chart and not the tool. Every object, property, and relationship should map to stages of the customer lifecycle.

Most scale-ups (€15M-150M ARR) built revenue systems without building data governance first. Sales creates custom fields. Marketing connects enrichment vendors. CS runs manual updates. Finance syncs spreadsheets. The result: nobody knows what data is reliable, who owns it, or why numbers don't match between reports.

This skill is prevention, detection, and correction working together.

## 1. Data Model Design

### Object Architecture (Mapped to Bow Tie)

```
EARLY FUNNEL (Awareness → Consideration):
  Leads/Contacts:  Individual prospects. Properties: title, industry, company_size, lead_source
  Lead Sources:    Where they came from (form, event, referral)

ORGANISATION LEVEL:
  Accounts:        Parent company record. Properties: revenue, industry, employee_count, country
  Hierarchy:       Parent-child for subsidiaries, divisions, acquisitions
  Status:          prospect | customer | churned | inactive

MID-FUNNEL (Evaluation → Decision):
  Opportunities:   Commercial deals tied to accounts
  Properties:      deal_size_eur, sales_stage, stage_entered_date, close_date, deal_type
  Line Items:      Individual products/services within a deal

POST-SALE (Adoption → Expansion):
  Subscriptions:   ARR, contract dates, renewal date, discount
  Health:          Monthly active users, feature adoption, support tickets, NPS

INTERACTION LAYER (Cross-stage):
  Activities:      Emails, calls, meetings, tasks — linked to contacts, accounts, opportunities
```

### Critical Relationships

```
Account → Contact (1:many)     Account → Opportunity (1:many)
Contact → Opportunity (many:many — multiple contacts influence one deal)
Opportunity → Line Items (1:many)
Account → Subscription (1:many)
Activity → Contact/Account/Opportunity (context link)

Missing relationships = reporting gaps. If you can't connect contact → account → opportunity → revenue,
you can't calculate deal influence or customer expansion velocity.
```

### Custom Object Decisions

Create a custom object when: multiple records per parent (many-to-many), need separate history, data repeats (e.g., decision makers per deal), or external systems sync separately.

Use properties when: single value per record, supplementary to parent, doesn't need separate history.

### Data Dictionary

Living document defining: every object and what it represents, every relationship and cardinality, every property with data type and owner, required vs. optional per stage, deprecated fields and replacements. Update quarterly. If a new field isn't documented, it doesn't exist.

## 2. Property/Field Governance

### Naming Conventions

```
rev_*    Revenue operations core    (rev_arr_eur, rev_close_date, rev_sales_stage)
mktg_*   Marketing-owned            (mktg_lead_source, mktg_campaign_id, mktg_engagement_score)
sales_*  Sales-owned                (sales_stage, sales_notes, sales_next_step)
cs_*     Customer Success-owned     (cs_health_score, cs_last_touchpoint, cs_renewal_probability)
int_*    Integration/system fields  (int_hubspot_id, int_sync_status)
calc_*   Calculated/formula fields  (calc_arr_annual, calc_ltv_eur, calc_days_in_stage)

NEVER ALLOW: random abbreviations, mixed case, unclear prefixes (tmp_, test_, x_)
```

### Field Creation Governance

Nobody creates fields without approval:

```
1. DOCUMENT:  Name, description, data type, why needed, system of record
2. REVIEW:    Does it duplicate existing data? Can we use a standard field?
3. APPROVE:   Decision within 5 business days (SLA)
4. IMPLEMENT: Created only after approval + added to data dictionary

REQUIRED FOR EACH FIELD:
  Purpose (why it exists) | Owner (who's responsible for quality)
  Data type + validation rules | Source (manual, formula, integration, enrichment)
  Where it's used (reports, processes) | Deprecation plan
```

### Property Types

```
SINGLE-SELECT: Stage progressions, categories. Best for reporting.
MULTI-SELECT:  Only when truly needed (hard to report on — use sparingly).
NUMBER:        Calculations, comparisons. Include min/max validation.
DATE:          Stage tracking, deadlines. Always document what triggers it.
CHECKBOX:      Binary status. Clearer than Yes/No dropdowns.
TEXT (short):  Identifiers only. Use picklists over free text for categories.
TEXT (long):   Notes only. Rarely useful in reports — use timeline instead.
```

### Field Deprecation

```
1. ANNOUNCE (2 weeks): Notify teams. Show replacement.
2. MIGRATE (4 weeks):  Move data old → new (formula, bulk action, integration).
3. HIDE (2 weeks):     Remove from views, forms, workflows. Keeps history.
4. DELETE (after 6 months): Only after confirming nothing depends on it.
```

### The Proliferation Problem

Scale-ups accumulate 500+ fields, 200 of which nobody uses. Prevention: naming conventions make duplicates obvious, governance process adds friction (good friction), quarterly field audits (which fields untouched for 3+ months?), delete unused aggressively.

## 3. Data Quality Operations

### Five Dimensions

```
COMPLETENESS:  Does the record have all required information?
               Target: 95%+ for required fields per stage

ACCURACY:      Is the data correct? Matches reality?
               Target: 90%+ (measured by sample audits, enrichment validation)

CONSISTENCY:   Same data appears same way everywhere?
               Target: 99%+ (if opp is closed-won, does account show subscription?)

TIMELINESS:    Is data current or stale?
               Target: 85%+ (engagement scores weekly, industry data yearly)

UNIQUENESS:    No duplicates?
               Target: 99%+ (duplicates are binary failure)
```

### Data Quality Score

```
DQ Score = (Completeness × 0.25) + (Accuracy × 0.25) + (Consistency × 0.25)
         + (Timeliness × 0.15) + (Uniqueness × 0.10)

Track monthly. Target: 85%+ across organisation.
```

### Prevention-First Approach

Don't plan to fix bad data. Prevent it:

```
VALIDATION RULES:   Email format. Phone country format. Dates can't be in past
                    (except close_date). Stage only moves forward without approval.

REQUIRED FIELDS:    On Contact: email, first_name, last_name, account_id
                    On Opportunity: account_id, name, stage, close_date
                    Keep to minimum — too many kills adoption.

PICKLISTS > TEXT:   For ANY categorical data (stage, industry, deal_type).
                    Free text proliferates bad data.

DEFAULT VALUES:     Currency = EUR. Stage = Prospect. Country = from account.
                    Reduce manual entry wherever possible.
```

### Detection Systems

```
AUTOMATED SCANS (weekly):
  Duplicate accounts (fuzzy match on name + domain)
  Null required fields | Stage anomalies (backwards movement, stuck >180 days)
  Data drift (values changed without user action)

ANOMALY ALERTS (real-time):
  Close date in the past | Contact on 5+ accounts | ARR >€10M on single opp
  Stage change without activity in 30 days

PERIODIC AUDITS (quarterly):
  Sample 5% of closed opps (really closed?) | 5% churned accounts (really churned?)
  5% enrichment data (vendor data still accurate?) | Calculate dimension scores
```

### The Data Quality Tax

```
DQ Tax = (Hours wasted × Hourly cost) + (Revenue impact of decisions on wrong data)

Example: Sales ops 2hrs/week on dupes (€1,500/mo) + 20 reps × 0.5hr/week (€3,200/mo)
= €4,700/month = €56,400/year. Show this to the CFO. Governance gets budget.
```

## 4. Deduplication & Record Management

### Duplicate Detection

```
EXACT MATCH (high confidence):  Email address | Account domain + size | Phone number
FUZZY MATCH (review required):  "Acme Corp" ≈ "ACME CORPORATION" ≈ "Acme"
                                "John Smith" + @acme.com ≈ "j.smith@acme.com"
VENDOR MATCH:                   Enrichment vendors flag duplicates in their systems
```

### Merge Protocol

```
CONTACT MERGE: Surviving record = most complete + recent activity.
               Preserve all activities and relationships from deleted record.
               Keep audit trail (which record deleted, when, who).

ACCOUNT MERGE: Surviving record = older record (usually).
               Move all contacts, opportunities, subscriptions from deleted.
               Never merge parent into subsidiary. Log everything.
```

### Prevention at Creation

On contact creation: form triggers lookup by email. If exists, "This contact already exists." On account creation: fuzzy match on name + country. Show potential matches. Override option logged and audited.

### Account Hierarchy

Parent = ultimate legal entity. Child = subsidiary/division. On M&A: create new parent, move old to child. On acquisition: don't delete — create parent relationship. Every contact maps to exactly one primary account.

## 5. Integration Data Flows

### System of Record Decisions

For each data point, one system owns it. Others read it:

```
Account name:       CRM (authoritative)
Annual revenue:     Enrichment vendor → CRM (weekly sync)
Sales stage:        CRM (only sales updates)
Subscription dates: Finance system → CRM (don't edit in CRM)
Lead source:        CRM (integration reads, doesn't change)
```

Rule: if you don't explicitly define system of record, conflicts emerge.

### Sync Direction Rules

```
ONE-WAY (most common):    Master → Reader. Example: Finance → CRM for subscription data.
BIDIRECTIONAL (dangerous): System A ↔ B. Use rarely. Requires detailed conflict resolution.

CONFLICT RESOLUTION:
  Define per field: which system wins? Timestamp-based? Manual review?
  SLA: investigate conflicts within 24 hours.
```

### Architecture Patterns

```
POINT-TO-POINT:  Simple, 2-3 systems. Breaks down at 5+.
HUB-AND-SPOKE:   CRM as central hub. All systems speak to CRM. Recommended for €15-80M.
iPaaS:           Integration platform (Zapier, Make). For 5+ systems, complex transforms.
```

### Integration Monitoring

Sync failure alerts (3 failures → alert within 4 hours). Data drift detection (weekly record count comparison). Latency monitoring (alert if >2 hours). Don't trust syncs just because you set them up.

## 6. Enrichment Strategy

### What, When, How

```
WHAT:  Firmographics (revenue, size, industry) | Technographics (tools they use)
       Intent signals (job postings, keyword research) | News (funding, M&A, leadership)

WHEN:  On creation (initial fill) | On stage transition (targeted enrichment)
       Quarterly refresh for active accounts | Event-driven (trigger-based)

GOVERNANCE RULES:
  AUTO-OVERWRITE:    Only for immutable data (founding year, domain)
  FILL-EMPTY-ONLY:  For data where manual entry is authoritative
  SUGGEST (review):  For data that might conflict (company size, title) — DEFAULT

Cost: €0.50-2.00/lead. Evaluate vendors on accuracy (>90%), coverage (>70%),
and integration quality. Request sample enrichment of 100 test accounts.
```

### GDPR/Privacy (European Market)

Verify vendor data sources (scraped data may violate GDPR). Document legitimate interest for enrichment. Right to deletion: delete enriched data immediately on request. Require DPA and SCCs for vendors transferring EU data to US. Use EU-based vendors or US vendors with clear GDPR compliance.

## 7. Definitions & Taxonomy

### The Shared Definitions Problem

Sales says €2M pipeline. Marketing says 50 leads. Finance forecasts €1.8M. Nobody agrees what "pipeline," "lead," or "qualified" means.

### Definition Governance

```
1. PROPOSE:   Owner documents definition with specific, measurable criteria
2. REVIEW:    Marketing, Sales, Finance all review (can you identify this? Is it useful? Can you forecast?)
3. APPROVE:   Revenue leader signs off. Definition locked. Version controlled.
4. COMMUNICATE: Published centrally. Training delivered. Enforcement begins.
5. REVIEW:    Quarterly: still working? Annual: comprehensive update.
```

### Stage Definitions Tied to Data

Each stage requires specific data to exist — operationalise this:

```
PROSPECT:       account_name + contact_email + lead_source (can't advance without these)
QUALIFICATION:  + title + company_size + budget_range + expected_close_quarter
PROPOSAL:       + deal_size_eur + decision_maker_identified
NEGOTIATION:    + close_date + deal_terms_documented + risks_identified
```

This enforces data quality by stage. You can't lie about stage if the data isn't there.

### One Vision of Truth

NOT one database. Agreed definitions and shared views:

```
Marketing owns lead definition (CRM = system of record)
Sales owns opportunity definition (CRM = system of record)
Finance owns ARR definition (synced from subscription system, displayed in CRM)
CS owns health score (calculated in CS platform, synced to CRM for visibility)

Shared vision = published definitions + agreed metrics + shared dashboards
Not: everything in one tool. Tools are separate. Definitions are shared.
```

## 8. Data Governance Operating Model

### Roles

```
DATA OWNER (executive):     VP Sales owns stage accuracy. VP CS owns health scores.
                            Authority: mandate corrections, approve fields, set standards.

DATA STEWARD (operational): RevOps/SalesOps. Day-to-day enforcement, audits, dedup.
                            Authority: execute corrections, delete bad data, enforce process.

DATA CONSUMER (end user):   Reps, CSMs, marketers. Follow standards. Measured on data quality.

DATA GOVERNANCE COUNCIL:    VP Sales + VP Marketing + VP Finance + VP CS + RevOps Lead
                            Monthly: quality scorecard, incident review, process changes
                            Quarterly: field approvals, definition updates, tool decisions
                            Annual: maturity assessment, multi-year roadmap
```

### Data Governance Maturity

```
LEVEL 1 — CHAOS:     No standards, no ownership. 500+ fields, many duplicates.
                      "We don't trust our reports." Fix: 3-6 months dedicated effort.

LEVEL 2 — REACTIVE:  Some naming conventions. Occasional cleanup projects.
                      Ad hoc ownership. Quality scoring begins.
                      "We keep finding new problems." Fix: 6-12 months with council.

LEVEL 3 — PROACTIVE: Council meets monthly. Prevention enforced (validation, picklists).
                      Quality scoring automated. Standards documented. Dedup prevention built in.
                      "We know what good data looks like." Fix: 12-18 months for Level 4.

LEVEL 4 — OPTIMISED: Automated enforcement. Self-healing data. Culture of ownership.
                      Real-time monitoring. Predictive quality.
                      "Data quality is our competitive advantage."

TARGET: Level 3 within 12 months. Level 4 requires data engineering resource.
```


---

## Norton Framework Additions (Source: Kyle Norton, Revenue Leadership Podcast, Jan 2026)

### Data Foundation for AI Readiness (Norton Model)

AI is only as good as the data underpinning it. Most companies trying to bolt AI onto broken infrastructure are installing a turbocharger on a car with a cracked engine block.

**Prerequisites for AI-Ready Data:**
1. **Single source of truth** — Snowflake (or equivalent) as system of record for intelligence, CRM as operational layer
2. **Data synthesis** — Sales, marketing, product, and third-party data coherently joined
3. **Quality thresholds** — Defined minimums for completeness, accuracy, and freshness before AI models can be trained
4. **Definition convergence** — Consistent stage definitions, field meanings, and scoring criteria across all teams

**The Code Red Principle:**
If your data foundation isn't ready for AI, call a code red at the exec level. Get the resources to fix it.
> "If you argue for your limitations, you get to keep them."

**Composability Data Requirements:**
Multiple integrated tools (composability) require stricter governance because sync failures cascade across more systems. For every new tool added:
- Define the system of record for each data entity
- Document sync direction and conflict resolution rules
- Test data flow end-to-end before go-live



### The Five Data Classes (Brinker/Databricks, March 2026)

When designing data governance, think beyond CRM hygiene. Modern data governance covers five interrelated classes of data:

| Class | What it covers | Governance implications |
|---|---|---|
| **Customer Data** | Profiles, transactions, behavioural signals, support tickets, enrichment data | Identity resolution, consent management, decay monitoring |
| **Company Data** | Operational data across departments: financials, pipeline, inventory, logistics | Cross-functional access policies, department data ownership |
| **Content Data** | Creative assets with metadata: what it is, where it can be used, who approved it, how it performs | Content governance, brand compliance, performance tracking |
| **Code Data** | AI models, prompts, agent configurations, automation rules — "software is data" | Version control, prompt governance, agent audit trails |
| **Control Data** | Semantic layer definitions, business rules, governance policies, AI guardrails | Meta-governance: the rules that govern the rules |

**Why this matters:** When everything is data — including the AI agents themselves and the governance rules they follow — data governance becomes the foundation of the entire operating system, not just a hygiene exercise. Brinker's thesis: "The martech stack doesn't sit on top of data. It is data."

### The Semantic Layer as Governance Foundation

A semantic layer provides consistent, business-friendly vocabulary across the organisation:
- Standardised metric definitions (what "MQL," "pipeline," "customer" mean)
- Translation between technical schemas and business concepts
- Shared calculations that every report, dashboard, and AI agent uses

**Without a semantic layer:** "Every agent becomes its own island of interpretation — which is how you get three different dashboards showing three different pipeline numbers, or worse, three different agents taking three different actions based on contradictory assumptions." (Brinker, 2026)

**Practical implication for revenue dashboard:** The breach rules and tile definitions in the revenue dashboard ARE the semantic layer for revenue operations. They enforce shared meaning. When building the revenue dashboard, you're building the semantic layer.

## How to Use This Skill

**"Our CRM is a mess":** Start with the data quality audit — score the five dimensions. Calculate the data quality tax. Show leadership the cost. Then build prevention (validation rules, required fields, picklists) before correction (cleanup projects).

**"Reports don't match across teams":** This is a definitions problem. Get in a room. Define MQL, pipeline, revenue, customer. Write it down. Publish it. Enforce it.

**"We have too many fields":** Run field audit — which fields haven't been touched in 3 months? Deprecate aggressively. Install field creation governance to prevent recurrence.

**"Integrations keep breaking":** Map system of record for every data point. Define sync direction. Set up monitoring. Most integration failures come from undefined ownership.

**Cross-references:** For CRM property implementation, see **revops-hubspot**. For tech stack integration decisions, see **revops-tech-stack**. For data spine quality scoring, see **revops-four-capability-maturity-assessment**. For emergency data audit, see **revops-crisis**.

> Built by [Neon Triforce](https://neontriforce.com)
