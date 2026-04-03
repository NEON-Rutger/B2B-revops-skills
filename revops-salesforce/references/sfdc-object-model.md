# Salesforce Object Model Reference

## Core Object Relationships

```
Account (company)
├── Contact (people at the company, many-to-one)
├── Opportunity (deals, many-to-one)
│   ├── OpportunityContactRole (links contacts to deals)
│   ├── OpportunityLineItem (products on the deal)
│   └── OpportunityTeamMember (sales team on the deal)
├── Case (support tickets)
└── Activity (tasks, events, emails logged)

Lead (separate object — unqualified prospects)
└── Conversion → creates Account + Contact + Opportunity
```

## Lead vs Contact-First Workflow

| Approach | When to use | Trade-offs |
|----------|------------|------------|
| **Lead-first** | High-volume inbound (>500/month), marketing-heavy | Requires conversion process; attribution breaks if not managed; duplicates common |
| **Contact/Account-first** | ABM, enterprise sales, <200 target accounts | Skips conversion; cleaner data model; harder to isolate unqualified prospects |
| **Hybrid** | Most B2B SaaS teams | Leads for unknown prospects, direct Contact creation for named accounts |

**Decision framework**: If >500 inbound leads/month and need to qualify before routing, use Lead-first. If running ABM with <200 target accounts, go Contact/Account-first.

## Record Types

Record Types allow different page layouts, picklist values, and process definitions per use case on the same object.

**Common patterns**:
- **Opportunity**: New Business vs Renewal vs Expansion (different stages, fields, processes)
- **Account**: Customer vs Prospect vs Partner (different layouts, required fields)
- **Lead**: Inbound vs Outbound vs Partner-referred (different scoring and routing)

**When to use Record Types vs Custom Objects**: Record Types when data model is the same but process differs. Custom Objects when data model is fundamentally different.

## Custom Objects and Relationships

| Relationship Type | Use When | Limits |
|-------------------|----------|--------|
| **Lookup** | Optional relationship, record can exist independently | 40 per object |
| **Master-Detail** | Child can't exist without parent; cascading delete; roll-up summaries | 2 per object |
| **Many-to-Many** | Junction object with two master-detail relationships | Requires custom junction object |

**Practical limits**:
- 800 custom fields per object (operate at 70-80% for agility)
- 40 relationships (lookup + master-detail combined) per object
- 3 levels of master-detail depth maximum
- 25 roll-up summary fields per object

## Common Custom Objects for B2B RevOps

| Object | Purpose | Key Fields |
|--------|---------|------------|
| **Subscription__c** | Track recurring revenue separately from Opportunity | ARR, MRR, Start Date, End Date, Renewal Date, Status |
| **Handoff_Record__c** | Capture context during team transitions | From_Owner, To_Owner, Context, Handoff_Date, SLA_Status |
| **Health_Score__c** | CS health tracking over time | Account (lookup), Score, Date, Dimensions (JSON or child records) |
| **Territory_Assignment__c** | Manual territory tracking (if not using ETM) | Account (lookup), Territory, Rep, Start_Date |
| **Forecast_Snapshot__c** | Historical forecast tracking | Period, Rep, Commit, Best_Case, Pipeline, Actual |

## Field Governance

### Naming Convention

Standard: `[Category]_[Name]__c`

| Category | Examples |
|----------|---------|
| ICP_ | ICP_Fit_Score__c, ICP_Tier__c |
| Rev_ | Rev_ARR__c, Rev_NRR__c, Rev_Expansion__c |
| Ops_ | Ops_Routed_At__c, Ops_SLA_Status__c |
| Enrich_ | Enrich_Source__c, Enrich_Date__c, Enrich_Status__c |
| Score_ | Score_Lead__c, Score_Fit__c, Score_Engagement__c |

### Required Fields by Stage

| Object/Stage | Required Fields |
|-------------|----------------|
| Lead (creation) | Email, Company, Lead Source |
| Lead (MQL) | Company + Email domain (validated) |
| Opportunity (creation) | Account, Amount (estimate OK), Close Date, Stage |
| Opportunity (Qualification) | At least 1 Contact Role, qualification notes |
| Opportunity (Proposal) | Amount (firm), Products/Line Items |
| Opportunity (Closed Lost) | Loss_Reason__c, Competitor__c (if competitive loss) |

## Duplicate Management

**Matching Rules** (max 5 active per object):
- Lead: Email domain + Company Name (fuzzy, 85% threshold)
- Contact: Email (exact) OR First Name + Last Name + Account (fuzzy)
- Account: Website domain (exact) OR Company Name (fuzzy, 85%)

**Duplicate Rules**:
- Alert (show warning, allow save): Default for most cases
- Block (prevent save): Only for hard duplicates (exact email match on Contact)

## Account Hierarchy

For enterprise accounts with subsidiaries:
- Use ParentAccount field for corporate hierarchy
- Roll-up reports aggregate child account data
- Territory assignment can cascade from parent
- Consider: should Opportunities live on parent or child Account? (Usually child, with parent reporting via hierarchy)
