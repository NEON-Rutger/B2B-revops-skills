# HubSpot Property Catalog - RevOps Reference

Complete property inventory for B2B SaaS revenue operations (€15M-150M ARR).

---

## Contact Properties

### Lifecycle & Qualification

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `lifecycleStage` | Enumeration | Subscriber, Lead, MQL, SQL, Opportunity, Customer, Evangelist, Other | Lead creation | All pipeline reports |
| `lead_status` | Enumeration | Open, Working, Unqualified, Contacted, Attempted Contact, Bad Timing | MQL → SQL | Sales engagement reports |
| `hs_lead_status_reason` | Enumeration | Not a fit, Wrong person, Company policies restrict, Not enough budget, Bad timing, Budget already allocated, Competitor, Stalled deal | Unqualified | Deal loss analysis |
| `num_contacted_lead_notes` | Number | — | — | Sales engagement tracking |
| `num_contacted_notes` | Number | — | — | Engagement metrics |

### Scoring & Engagement

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `hs_lead_score` | Number | 0-100 | Lead creation | Lead scoring dashboard |
| `engagement_score` | Number | 0-120 | MQL qualification | Marketing automation reports |
| `fit_score` | Number | 0-80 | MQL qualification | Lead scoring dashboard |
| `hs_analytics_num_page_views` | Number | — | — | Engagement metrics |
| `hs_analytics_num_visits` | Number | — | — | Engagement metrics |
| `email_open_rate` | Number | 0-100% | — | Email performance reports |
| `last_activity_date` | Date | — | — | Activity aging reports |
| `days_inactive` | Number | — | — | Re-engagement triggers |

### Source & Attribution

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `hs_analytics_first_touch_converting_campaign` | Text | — | Lead creation | Attribution reports |
| `hs_analytics_last_touch_converting_campaign` | Text | — | MQL creation | Attribution reports |
| `hs_analytics_first_url` | Text | — | Lead creation | Channel performance |
| `utm_source` | Text | linkedin_paid, google_paid, email, content, event, etc. | Lead creation | Channel breakdown |
| `utm_medium` | Text | paid_social, email, content, webinar, event, etc. | Lead creation | Attribution model |
| `utm_campaign` | Text | — | Lead creation | Campaign performance |
| `utm_content` | Text | — | Lead creation | A/B testing insights |
| `original_source` | Enumeration | Direct, Organic Search, Paid Search, Paid Social, Organic Social, Email, Event, Partner, Other | Lead creation | Channel reporting |
| `original_source_timestamp` | Date | — | Lead creation | Source aging analysis |

### Firmographic & Qualification

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `jobtitle` | Text | — | Contact creation | Buyer persona tracking |
| `hs_lead_grade` | Enumeration | A, B, C, D, F | MQL creation | Lead ranking |
| `industry` | Enumeration | SaaS, FinTech, MarTech, HR Tech, Sales Tech, etc. | Contact creation | Industry segment reports |
| `intent_signals` | Enumeration (multi) | Pricing page visits, Demo requests, Competitor mention, Alternative searches, Proposal viewed | — | Intent scoring |
| `buying_cycle_stage` | Enumeration | Awareness, Consideration, Decision, Negotiation | — | Pipeline progression |
| `decision_maker_flag` | Checkbox | true/false | Contact creation | Decision-maker routing |
| `title_seniority_level` | Enumeration | C-Suite, VP, Director, Manager, Individual Contributor, Other | Contact creation | Routing & priority |

### Engagement Tracking

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `num_emails_received` | Number | — | — | Email engagement |
| `num_emails_opened` | Number | — | — | Email engagement |
| `num_emails_clicked` | Number | — | — | Email engagement |
| `hs_email_open` | Date | — | — | Last engagement tracking |
| `hs_email_click` | Date | — | — | Last engagement tracking |
| `webinar_attendance` | Enumeration (multi) | Q1 2026 Forecasting Webinar, Q2 2026 RevOps Trends, etc. | — | Event participation |
| `content_downloads` | Enumeration (multi) | 2026 State of RevOps, Sales Playbook, etc. | — | Content engagement |
| `demo_watched` | Checkbox | true/false | — | Product engagement |
| `product_tour_completed` | Checkbox | true/false | — | Product engagement |
| `time_since_last_touch` | Number | Days | — | Activity aging |

### Contact Preferences & Compliance

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `hs_lead_status_date` | Date | — | — | Lifecycle timing |
| `hs_email_bounce` | Enumeration | Not bounced, Bounced, Deferred, Complaint | — | Data quality |
| `hs_email_unsubscribed` | Checkbox | true/false | — | Compliance tracking |
| `do_not_call` | Checkbox | true/false | — | Compliance tracking |
| `hs_language` | Enumeration | English, Dutch, German, French | — | Campaign preferences |
| `hs_sales_email_click` | Checkbox | true/false | — | Sales engagement metrics |

---

## Company Properties

### Firmographics (ICP Matching)

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `name` | Text | — | Company creation | All reports |
| `industry` | Enumeration | SaaS, FinTech, MarTech, HR Tech, Sales Tech, etc. | Company creation | Industry segment reports |
| `numberofemployees` | Number | — | Company creation | Company size bucketing |
| `annualrevenue` | Number | EUR (0-500M) | Company creation | ARR segmentation |
| `arr_eur` | Number | 0-500M | Company creation | Deal sizing, ICP fit |
| `funding_stage` | Enumeration | Pre-seed, Seed, Series A, B, C, D+, Growth, Public | — | Investor profile reports |
| `country` | Enumeration | Netherlands, Belgium, Germany, France, UK, etc. | Company creation | Geo segment reports |
| `technology_stack` | Enumeration (multi) | AWS, Azure, GCP, Salesforce, HubSpot, etc. | — | Technology intelligence |
| `primary_product` | Text | — | Company creation | Product/solution fit |

### Company Segmentation & Scoring

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `company_segment` | Enumeration | Enterprise, Mid-Market, SMB, Startup | Company creation | Segment reporting |
| `hs_company_id` | Text | Auto-populated | Company creation | System tracking |
| `target_fit_score` | Number | 0-100 | Company creation | ICP scoring |
| `icp_match_status` | Enumeration | Perfect Fit, Good Fit, Partial Fit, Not a Fit | Company creation | ICP reporting |
| `hs_ideal_customer_profile` | Checkbox | true/false | Company creation | ICP filtering |
| `competitor_flag` | Checkbox | true/false | Company creation | Competitive exclusion |
| `partner_flag` | Checkbox | true/false | Company creation | Partner identification |

### Company Health & Engagement

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `company_engagement_score` | Number | 0-100 | — | Engagement dashboards |
| `health_score` | Number | 0-100 | Customer stage | Customer health reports |
| `days_since_last_activity_company_level` | Number | — | — | Activity aging |
| `num_associated_contacts` | Number | Auto-calculated | — | Contact coverage reports |
| `num_associated_deals` | Number | Auto-calculated | — | Pipeline density |
| `num_open_deals` | Number | Auto-calculated | — | Opportunity tracking |
| `num_won_deals` | Number | Auto-calculated | — | Customer status |
| `total_revenue_eur_closed_won` | Number | EUR | Customer stage | Lifetime value |
| `upcoming_renewal_date` | Date | — | Customer stage | Renewal forecasting |
| `account_owner_assigned_date` | Date | — | Customer stage | Account assignment timing |

### Company Commercial Profile

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `deal_size_avg_eur` | Number | EUR | — | Pipeline forecasting |
| `deal_size_max_eur` | Number | EUR | — | Upsell potential |
| `deal_size_min_eur` | Number | EUR | — | Land strategy |
| `sales_cycle_days_avg` | Number | Days | — | Forecasting accuracy |
| `contract_renewal_month` | Enumeration | January, February, March, etc. | Customer stage | Renewal planning |
| `expansion_potential_eur` | Number | EUR | Customer stage | Expansion planning |
| `churn_risk_flag` | Checkbox | true/false | Customer stage | Risk management |
| `churn_reason` | Enumeration | Product mismatch, Better alternative, Cost, No longer needed | Churned | Loss analysis |

---

## Deal Properties

### Deal Basics & Pipeline

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `dealname` | Text | — | Deal creation | All reports |
| `dealstage` | Enumeration | Negotiation, Prospect, Qualification, Proposal, Contract, Closed Won, Closed Lost | Deal creation | Pipeline stage reports |
| `pipeline` | Enumeration | Outbound, Inbound, Channel, Expansion | Deal creation | Pipeline source tracking |
| `dealtype` | Enumeration | New Business, Expansion, Renewal | Deal creation | Revenue type reporting |
| `amount` | Number | EUR | Deal creation | Revenue forecasting |
| `amount_eur` | Number | EUR | Deal creation | Reporting consistency |
| `closedate` | Date | — | Deal creation | Forecast accuracy |
| `closed_date_actual` | Date | — | Deal close | Close date tracking |

### Deal Methodology & Qualification

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `deal_qualification_method` | Enumeration | MEDDIC, BANT, SPIN, Intro call pending, Not yet qualified | Prospect stage | Deal quality tracking |
| `pain_identified` | Checkbox | true/false | Qualification stage | Sales methodology |
| `budget_confirmed` | Checkbox | true/false | Proposal stage | Risk assessment |
| `timeline_confirmed` | Checkbox | true/false | Proposal stage | Forecast accuracy |
| `decision_process_understood` | Checkbox | true/false | Qualification stage | Sales readiness |
| `stakeholders_identified` | Number | Count of stakeholders | Qualification stage | Buying committee size |
| `champion_identified` | Checkbox | true/false | Qualification stage | Success indicator |
| `competition_identified` | Enumeration (multi) | Competitor A, Competitor B, Do Nothing, etc. | Qualification stage | Competitive analysis |

### Forecasting & Commercial Terms

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `probability_percentage` | Number | 0-100% | Deal creation | Pipeline forecast |
| `win_probability_predicted` | Number | 0-100% | — | AI-powered forecast |
| `deal_visibility` | Enumeration | Committed, Best Case, Pipeline | Deal stage | Forecast accuracy |
| `forecast_category` | Enumeration | Pipeline, Best Case, Committed | — | Forecast reporting |
| `contract_term_months` | Number | 1-60 | Proposal stage | ARR calculation |
| `contract_value_annual_eur` | Number | EUR | Proposal stage | Annual contract value |
| `list_price_eur` | Number | EUR | Proposal stage | Discount tracking |
| `discount_percentage` | Number | 0-100% | Proposal stage | Pricing analytics |
| `discount_eur` | Number | EUR | Proposal stage | Discount reporting |
| `recurring_vs_onetime` | Enumeration | Recurring, One-time, Hybrid | Proposal stage | Revenue type |

### Deal Dynamics & Engagement

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `days_in_stage` | Number | Auto-calculated | — | Sales cycle tracking |
| `days_to_close` | Number | Auto-calculated | — | Forecast accuracy |
| `num_associated_contacts` | Number | Auto-calculated | — | Buying committee tracking |
| `last_activity_date` | Date | Auto-calculated | — | Deal momentum |
| `days_inactive` | Number | Auto-calculated | — | Stalled deal detection |
| `sales_activity_count_last_30_days` | Number | Auto-calculated | — | Engagement tracking |
| `num_meetings_last_30_days` | Number | Auto-calculated | — | Sales activity |
| `next_step` | Text | — | All active stages | Deal progression |
| `next_step_date` | Date | — | All active stages | Activity planning |
| `owner_assigned_date` | Date | — | Deal creation | Ownership tracking |

### Reason for Loss (Closed Lost Only)

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `reason_for_loss` | Enumeration | Competitor, Price, Product gaps, Timing, Budget, Wrong fit, No decision, Other | Closed Lost | Loss analysis |
| `loss_analysis_notes` | Text | — | Closed Lost | Sales coaching |
| `customer_acquired_by_competitor` | Checkbox | true/false | Closed Lost | Competitive intelligence |
| `lost_to_do_nothing` | Checkbox | true/false | Closed Lost | Market analysis |

### Attribution & Source

| Property Name (snake_case) | Type | Options/Values | Required at Stage | Reports |
|---------------------------|------|-----------------|-------------------|---------|
| `first_touch_campaign` | Text | — | Deal creation | Attribution reporting |
| `last_touch_campaign` | Text | — | Deal close | Attribution reporting |
| `campaign_associated` | Enumeration (multi) | Campaign IDs | — | Multi-touch attribution |
| `marketing_attributed_revenue_eur` | Number | EUR | Deal close | Marketing ROI |
| `deal_source` | Enumeration | Inbound, Outbound, Partner, Customer Referral, Event | Deal creation | Sales productivity |

---

## Custom Object Considerations

### When to Create Custom Objects

| Scenario | Custom Object Name | Rationale |
|----------|-------------------|-----------|
| Multiple decision-makers per deal | `decision_committee` | Track each stakeholder influence |
| Formal proposal process | `proposal` | Link multiple versions to deal |
| Event attendance tracking | `event_attendance` | Track multi-person company participation |
| Contract line items | `contract_item` | Detailed pricing by product/module |
| Customer success metrics | `cs_health_check` | Track health outside of contact/company |

---

## Property Naming Standards

| Convention | Example | Usage |
|-----------|---------|-------|
| **snake_case** | `arr_eur`, `contract_value_annual_eur` | All custom properties |
| **Currency suffix** | `_eur`, `_amount_eur` | Always specify currency in name |
| **Boolean format** | `{noun}_flag`, `{action}_status` | Checkbox properties |
| **Enumeration** | `{noun}`, `{action}_status` | Single/multi-select properties |
| **Count/metric** | `num_{noun}`, `total_{noun}` | Number properties for aggregation |

---

## Property Audit Checklist

- [ ] All properties have descriptions in HubSpot
- [ ] Currency fields include "EUR" in property name or label
- [ ] Required fields marked as required at appropriate deal stage
- [ ] No more than 50 custom properties per object (performance)
- [ ] Duplicate properties consolidated (e.g., amount vs. amount_eur)
- [ ] List properties kept to <100 options for performance
- [ ] Multi-select properties used only when truly needed
- [ ] Regular audit quarterly to remove unused properties
- [ ] Sales team trained on all properties they use
- [ ] Documentation kept in team wiki or Confluence

---

## Sample Property Set by Revenue Stage

### Minimum Required (Early-Stage RevOps)

**Contacts:** `lifecycleStage`, `email`, `phone`, `jobtitle`, `company`, `engagement_score`

**Companies:** `name`, `industry`, `annualrevenue`, `country`, `company_segment`

**Deals:** `dealname`, `dealstage`, `amount`, `closedate`, `dealtype`

### Recommended (Scaling Stage - €15M-50M ARR)

Add: `hs_lead_score`, `lead_status`, `hs_analytics_first_touch_converting_campaign`, `hs_analytics_last_touch_converting_campaign`, `health_score`, `days_in_stage`, `probability_percentage`, `reason_for_loss`

### Advanced (Mature RevOps - €50M-150M+ ARR)

Add all above plus: `fit_score`, `hs_lead_grade`, `intent_signals`, `buying_cycle_stage`, `contract_term_months`, `discount_percentage`, `win_probability_predicted`, `churn_risk_flag`, `expansion_potential_eur`, and custom objects.
