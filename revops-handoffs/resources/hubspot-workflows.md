# HubSpot Workflow Specifications for Revenue Handoffs

Production-ready workflow patterns, pipeline configurations, property catalog, and Breeze AI patterns. All workflows assume HubSpot Professional or Enterprise tier.

---

## 1. MQL Routing Workflow (Contact-Based)

| Component | Details |
|---|---|
| **Trigger** | Lifecycle stage = MQL OR `hs_lead_score` crosses threshold (e.g., 70+) |
| **Hand-raiser override** | If `form_submission_type` = "Demo Request" OR `pricing_page_visit` = Yes in last 24h → skip scoring, route immediately, 5-minute SLA |
| **Actions** | 1. Breeze AI "Summarise Contact" → populate `lead_summary` property |
| | 2. If/then branch by territory: `company_country` or `form_language` for EU routing, `company_size` for segment, `industry` for vertical |
| | 3. Rotate record to owner within matching territory |
| | 4. Create high-priority task: "Follow up on MQL — [contact name]", due 5 minutes |
| | 5. Slack notification with contact details and AI summary |
| | 6. 24h delay → check for logged activity (call, email, meeting — not notes/tasks) |
| | 7. If no activity: escalation task to manager + Slack alert |
| | 8. 48h delay → if still no activity: auto-reassign to next rep in rotation |
| **Properties set** | `mql_date`, `assigned_date`, `territory_assigned` |
| **Notes** | Prevents duplicate enrollment. Account-based override: if company already has owner, route to that owner |

---

## 2. Closed-Won Handoff Workflow (Deal-Based)

| Component | Details |
|---|---|
| **Trigger** | Deal stage = Closed Won |
| **Validation** | Check required handoff fields populated: `spiced_situation`, `spiced_pain`, `spiced_impact`, `business_goals`, `onboarding_poc_email`, `stakeholders_list` |
| **If COMPLETE** | 1. Create ticket in Onboarding Pipeline (copy key properties from deal) |
| | 2. Create renewal deal in Renewal Pipeline (close date = `contract_end_date` − 90 days) |
| | 3. Update company: `customer_status` = Active, `arr_current` += deal amount, lifecycle = Customer |
| | 4. Slack celebration with deal summary |
| | 5. Welcome email from CSM to customer (template with personalisation tokens) |
| | 6. Task for CSM: "Schedule kickoff with [company]", due 48h |
| | 7. If `partner_sourced` = Yes → task for partner manager: "Notify partner of go-live timeline" |
| **If INCOMPLETE** | 1. High-priority task for deal owner listing missing fields |
| | 2. Deal stage does NOT advance (use required fields on stage exit) |
| | 3. Slack notification to sales manager |
| **Notes** | Configure required fields via Settings → Objects → Deals → Pipelines → Conditional stage properties |

---

## 3. Expansion Signal Workflow (Company-Based)

| Component | Details |
|---|---|
| **Trigger** | Company property `expansion_signal` is set to any value |
| **Signal values** | Upsell opportunity / Cross-sell opportunity / Usage limit approaching / New department interest / Customer request |
| **Actions** | 1. Branch by signal → set `expansion_type` (Upsell / Cross-sell warm / Cross-sell new DMU) |
| | 2. Create deal in Expansion Pipeline: name "[Company] — [type] — [date]" |
| | 3. Deal owner: `account_executive` from company (or territory owner for new-DMU) |
| | 4. Copy `arr_current`, `health_score`, `csm_owner` from company |
| | 5. Task for AE: "Review expansion opportunity", due 48h |
| | 6. Task for CSM: "Prepare expansion brief", due 24h |
| | 7. Slack notification to both |
| | 8. Set company `expansion_pipeline_active` = Yes |
| **Auto-trigger variant** | If `seats_used_pct` > 80% OR `new_module_trial` = Yes → auto-set `expansion_signal` |

---

## 4. Renewal Automation Workflow (Deal-Based, Date-Triggered)

| Component | Details |
|---|---|
| **Trigger** | Renewal deal `close_date` is 90 days from now |
| **T-90 actions** | 1. Move deal to "Upcoming Renewal" |
| | 2. Task for CSM: "Prepare renewal proposal", due 7 days |
| | 3. If `health_score` < 50: high-priority task "At-risk renewal review" + Slack to CS manager + tag "At Risk" |
| **T-60 escalation** | If still "Upcoming Renewal": escalation task + internal alert |
| **T-30 escalation** | If not in "Negotiation" or later: executive escalation + auto meeting request |
| **Notes** | Renewal deals auto-created by Closed-Won workflow |

---

## 5. Speed-to-Lead Tracking

HubSpot lacks native speed-to-lead reporting. Workaround:

### Properties

| Property | Type | Purpose |
|---|---|---|
| `first_connection_date` | Date | Set by workflow on first qualifying activity |
| `speed_to_lead_hours` | Calculation | (`first_connection_date` − `createdate`) / 3,600,000 |

### Workflow to Set `first_connection_date`

| Component | Details |
|---|---|
| **Trigger** | Contact has associated activity of type Call, Email (sent), or Meeting |
| **Condition** | `first_connection_date` is unknown (fires once only) |
| **Action** | Set `first_connection_date` = activity date |
| **Notes** | Exclude notes and tasks — they don't represent actual contact |

### Report

Custom report: average `speed_to_lead_hours` by contact owner, lead source, date range. Add to Dashboard 2 (Sales Handoff & Follow-Up).

---

## 6. SLA Escalation Workflow

| Component | Details |
|---|---|
| **Trigger** | `assigned_date` is known AND `first_connection_date` is unknown AND time since `assigned_date` > threshold |
| **Branches** | Hand-raiser: 1 hour. MQL: 4 hours. Partner referral: 24 hours |
| **Actions** | 1. Escalation task for contact owner's manager |
| | 2. Slack: "SLA breach: [name] unworked for [X hours]" |
| | 3. If still unworked after 2× threshold: auto-reassign |
| | 4. Set `sla_breach` = Yes on contact |

---

## 7. Partner Implementation Tracking Workflow

| Component | Details |
|---|---|
| **Trigger** | `partner_sourced` = Yes AND deal stage = Closed Won |
| **Actions** | 1. Set `implementation_status` on deal or create in Partner Implementation Pipeline |
| | 2. Task for partner manager: "Confirm kickoff scheduled", due 3 days |
| | 3. Set `implementation_kickoff_target` = today + 7 business days |
| | 4. 7-day delay → if `implementation_kickoff_date` not set: escalation |
| | 5. On `implementation_status` = Complete: trigger Impl → CS handoff, task for CSM, set `go_live_date` |

---

## 8. Lifecycle Stage Mapping to Bow Tie

| HubSpot Lifecycle Stage | Bow-Tie Position | Notes |
|---|---|---|
| Subscriber | Awareness | Top of funnel |
| Lead | Interest | VM1/VM2 |
| MQL | Handoff trigger | Marketing → Sales transition |
| SQL | Sales-validated | VM3 |
| Opportunity | Deal-associated | VM3/VM4 |
| Customer | Closed Won | VM5+ |
| Evangelist | Advocate | VM7/VM8 |
| Custom: "Onboarding" | Between Customer and Evangelist | Add for right-side visibility |

**Important**: HubSpot never moves lifecycle stages backward automatically. To handle churn or reactivation: workflow must **clear** the property first, then set the new value.

Track "At Risk" as a company-level custom property, not a lifecycle stage — avoids breaking funnel reporting.

---

## 9. Property Catalog

### Deal Properties — New Business Pipeline

| Property | Type | Required At | Purpose |
|---|---|---|---|
| `spiced_situation` | Multi-line text | Discovery Qualified | SPICED framework |
| `spiced_pain` | Multi-line text | Discovery Qualified | SPICED framework |
| `spiced_impact` | Multi-line text | Solution Fit | SPICED framework |
| `spiced_critical_event` | Date | Solution Fit | SPICED framework |
| `spiced_critical_event_detail` | Single-line text | Solution Fit | SPICED framework |
| `spiced_decision_criteria` | Multi-line text | Proposal | SPICED framework |
| `spiced_decision_process` | Multi-line text | Proposal | SPICED framework |
| `handoff_readiness` | Dropdown | Closed Won | Ready / Incomplete / Blocked |
| `onboarding_poc_email` | Email | Closed Won | Customer onboarding contact |
| `business_goals` | Multi-line text | Closed Won | Measurable success criteria |
| `stakeholders_list` | Multi-line text | Closed Won | Champion, buyer, users, detractors |
| `data_migration_required` | Checkbox | Technical Validation | Implementation planning |
| `competing_solutions` | Multi-line text | Discovery Qualified | Competitive context |
| `contract_start_date` | Date | Closed Won | Renewal pipeline automation |
| `contract_end_date` | Date | Closed Won | Renewal pipeline automation |
| `partner_sourced` | Checkbox | — | Triggers partner workflows |
| `partner_company` | Company association | If partner_sourced | Partner identification |

### Deal Properties — Expansion Pipeline

| Property | Type | Values | Purpose |
|---|---|---|---|
| `expansion_type` | Dropdown | Upsell / Cross-sell (warm) / Cross-sell (new DMU) | Drives stages, reporting, forecast |
| `expansion_source` | Dropdown | CS-identified / Customer request / Marketing signal / Usage trigger | Attribution |
| `arr_delta` | Currency | — | Incremental value |
| `cross_sell_intro_source` | Dropdown | Champion referral / Direct outreach / Marketing ABM | Path optimisation |
| `new_dmu_department` | Single-line text | — | BU/department (new-DMU type) |
| `new_dmu_budget_independent` | Checkbox | — | Independent budget? |

Plus: reuse SPICED property group (same fields as new business).

### Deal Properties — Renewal Pipeline

| Property | Type | Values | Purpose |
|---|---|---|---|
| `renewal_risk_level` | Dropdown | Low / Medium / High | At-risk flagging |
| `renewal_proposal_sent_date` | Date | — | Velocity tracking |
| `renewal_outcome` | Dropdown | Renewed / Churned / Downgrade | Outcome categorisation |
| `churn_reason` | Dropdown | Product gap / Price / Champion left / Competitor / Not adopted / Budget cut / Acquired | Churn analysis |

### Company Properties

| Property | Type | Purpose |
|---|---|---|
| `arr_current` | Currency | Total current ARR |
| `customer_status` | Dropdown (Active / Churned / At Risk / Prospect) | Account status |
| `health_score` | Number (0–100) | Composite health |
| `csm_owner` | HubSpot user | CS assignment |
| `account_executive` | HubSpot user | Sales assignment |
| `nps_score` | Number | Latest NPS |
| `last_qbr_date` | Date | QBR cadence tracking |
| `icp_segment` | Dropdown | Segment classification |
| `expansion_signal` | Dropdown | Signal type (triggers workflow) |
| `expansion_pipeline_active` | Checkbox | Active expansion deal? |
| `seats_used_pct` | Number | Product usage (pushed from product) |
| `contract_end_date` | Date | Renewal timing |

### Contact Properties

| Property | Type | Purpose |
|---|---|---|
| `mql_date` | Date | MQL timestamp |
| `assigned_date` | Date | Assignment timestamp |
| `first_connection_date` | Date | First qualifying activity |
| `speed_to_lead_hours` | Calculation | Response time metric |
| `territory_assigned` | Dropdown | Territory routing |
| `lead_summary` | Multi-line text | Breeze AI summary |
| `sla_breach` | Checkbox | SLA compliance tracking |
| `form_submission_type` | Dropdown | Demo Request / Content / Event / etc |

---

## 10. Breeze AI for Handoffs

### Breeze Copilot
- Summarise contact and deal records for handoff context
- Draft emails from meeting notes
- Generate summaries within CRM records, browser extension, mobile

### Breeze Intelligence
- Enrich records from 200M+ company profiles
- Reverse-IP buyer intent scoring
- Dynamic form shortening (reduce fields, enrich in background)

### Breeze Agents
- **Prospecting Agent**: auto-research prospects, score leads, monitor buying signals (funding, leadership changes)
- **Customer Agent**: qualify website visitors 24/7, book meetings with context logged to CRM

### AI Lead Scoring (Marketing Hub Enterprise)
- Evaluates historical contacts
- Recommends Fit and Engagement scoring criteria
- Updates scoring model based on outcomes

### Smart Properties (Data Agent)
- Auto-populate fields using CRM data, web research, call transcripts
- Example: auto-fill `lead_summary` from Breeze + engagement history

---

## 11. Tier Requirements

### Professional (Minimum Viable)

- Multiple pipelines: up to 15
- Workflows: up to 300
- Playbooks: basic
- Breeze Intelligence: credit-based
- Custom reports
- Deal-to-deal associations
- Required fields on stage exit

### Enterprise (Recommended for Scale)

- Playbook property auto-updates
- Custom objects (for partner management, implementation tracking)
- AI Lead Scoring
- Data Agent with smart properties
- Datasets for advanced calculations
- Up to 100 pipelines, 1,000 workflows
- Calculated properties (for speed-to-lead)
