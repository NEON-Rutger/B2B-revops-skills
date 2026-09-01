# ARR, revenue, billings and cash

The single most common confusion for a commercial leader reading a P&L, and understanding it well is disproportionately credibility-building because most commercial people never close the gap.

## ARR is not revenue

| | ARR | Recognized revenue |
|---|---|---|
| Direction | Forward-looking snapshot at a point in time | Backward-looking, earned over the period |
| Basis | Contracted annual value | Service actually delivered |
| Audited | No | Yes |
| Governed by | Company definition | IFRS 15 or ASC 606 |

They differ because of timing, mid-period starts, services revenue, one-off items, and multi-year structures.

**The consequence people miss:** new ARR signed in the last month of a quarter contributes almost nothing to that quarter's revenue. A quarter with outstanding bookings and disappointing revenue is normal, not contradictory. Conversely, a quarter with strong revenue and weak bookings is a warning that looks like success.

## The ARR bridge

The RevOps-native view, and the thing to bring to a CFO unprompted.

```
Opening ARR
  + New logo ARR
  + Expansion ARR
  - Contraction ARR (downgrades)
  - Churned ARR
= Closing ARR
```

**If a company reports ARR growth without publishing the bridge, ask for it.** Growth from new logos, growth from expansion, and growth that only looks good because churn was unusually low are three different businesses with three different risks. A group presenting a single growth percentage is either not measuring the bridge or not liking what it shows.

Extensions worth requesting once the basic bridge exists: the bridge split by product line, by segment, and by legacy entity in an acquired group. Aggregate ARR growth routinely conceals one product line collapsing while another grows.

## Billings, deferred revenue and RPO

**Billings** = revenue + change in deferred revenue. Approximates what was invoiced in the period, and is closer to cash than revenue is.

**Deferred revenue** is a liability: cash collected for service not yet delivered. Rising deferred revenue usually means healthy annual-upfront billing. Falling deferred revenue while revenue holds up often means a shift to monthly or quarterly billing, which is a cash story rather than a demand story.

**RPO (remaining performance obligations)** is total contracted revenue not yet recognized, including amounts not yet billed. **cRPO** is the portion expected within twelve months. RPO captures multi-year commitments that both ARR and deferred revenue miss, which makes it the better number in an enterprise business with long contracts.

**Why a commercial leader should care:** a shift from annual-upfront to monthly billing can crater operating cash flow while every commercial metric looks unchanged. If finance is suddenly anxious and sales is confident, this is often the reason. It is also frequently a concession sales made without knowing its cost.

## Why a profitable SaaS company burns cash

Work through the mechanics rather than asserting the conclusion. There are five, and usually more than one is running at once.

**1. Sales and marketing is spent now, revenue arrives over years.** A customer acquired in January costs the full acquisition cost immediately and returns it over the payback period. Growth therefore consumes cash by design, and faster growth consumes more.

**2. Commissions are paid on signature, revenue is recognized monthly.** The cash goes out in one month against revenue earned over twelve or thirty-six.

**3. Billing terms.** Monthly billing collects cash over twelve months for revenue recognized over the same twelve, giving no working capital benefit. Annual upfront collects it all on day one. Same revenue, entirely different cash profile.

**4. Rising DSO.** Revenue is recognized on invoice; cash arrives when the customer pays. A slipping collections process shows up in cash long before it shows up in the P&L, and it is frequently caused by commercial decisions: bad payment terms conceded in negotiation, disputed invoices from scope disagreements, or invoicing that waits on a milestone nobody chased.

**5. Capitalization.** Capitalized R&D and capitalized commissions raise reported profit without changing the cash that left the building.

**The reverse case, which surprises people more:** a company with heavy annual-upfront billing and a growing deferred revenue balance can generate cash while reporting losses. That is not a trick. It is a working capital position, and it reverses the moment growth slows.

## The reconciliation to run

When revenue and cash tell different stories, this sequence usually finds it:

1. Compute billings (revenue + change in deferred revenue). Compare growth in billings to growth in revenue.
2. If billings growth lags revenue growth, look at billing terms mix.
3. Check DSO trend over eight quarters.
4. Check the capitalized balances, both R&D and contract costs, and whether either grew faster than revenue.
5. Check whether any large customer moved from annual to monthly, or vice versa.

## The cash flow statement's structure, briefly

Three sections, and knowing which one a number lives in answers most questions about it:

- **Operating:** cash the business itself generated or consumed. Under the usual indirect method it starts from profit, adds back non-cash charges (depreciation, amortization, share-based comp), then adjusts for working-capital movements: deferred revenue rising is a cash source (customers prepaid), receivables rising is a cash sink (revenue booked, cash not collected). This reconciliation line by line IS the bridge between the P&L story and the cash story.
- **Investing:** capex and, importantly for SaaS, capitalized development. Costs capitalized out of the P&L reappear here, which is why aggressive capitalization flatters operating cash flow as well as EBITDA: the spend did not disappear, it moved sections.
- **Financing:** debt drawn or repaid, equity raised, in PE contexts the interest and sweep mechanics.

The single most useful habit: read operating cash flow next to EBITDA for the same period. A persistent, growing gap between them has a reason, and the reason is always in working capital or capitalization, both of which are interrogable with the questions in this file.

## Definitions to pin down before quoting any of these

Every one of these is company-defined and moves between organizations. Ask, do not assume.

- Does ARR include services? Most exclude, some include.
- Does ARR include contracted but not yet live customers?
- Is expansion measured net of contraction, or separately?
- Is churn measured on customers or on revenue?
- Is a downgrade contraction, or partial churn?
- Is a customer who churns and returns within a period counted twice?
- Are multi-year contracts held at year-one value or averaged?

**In a merged group, assume each legacy entity defined these differently until proven otherwise.** Reconciling ARR definitions across entities is often the first real deliverable a revenue operations function produces, and it is usually more valuable than any dashboard.
