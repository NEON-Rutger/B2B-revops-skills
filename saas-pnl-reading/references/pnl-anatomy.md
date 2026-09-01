# The SaaS P&L, line by line

## The structure

```
Revenue
  Subscription revenue
  Services / implementation revenue
  Maintenance / support revenue
= Total revenue

Cost of revenue (COGS)
  Hosting and infrastructure
  Customer support
  Customer success            (sometimes)
  Services delivery salaries
  Third-party license costs
  Amortization of capitalized software  (sometimes)
= Gross profit

Operating expenses
  Sales and marketing (S&M)
  Research and development (R&D)
  General and administrative (G&A)
= Operating profit / EBIT

  + Depreciation and amortization
= EBITDA

  + Adjustments / add-backs
= Adjusted EBITDA
```

## The classification choices, and what each one flatters

This is the part a non-finance reader misses, and it is where most of the interpretive work lives. None of these are wrong. All of them change the story.

| Choice | Effect if done one way | Effect if done the other | The question |
|---|---|---|---|
| **Customer success in COGS or S&M** | In COGS: depresses gross margin, flatters S&M efficiency and CAC | In S&M: flatters gross margin, worsens apparent S&M efficiency and CAC | Which is it, and has it changed between the periods being compared? |
| **Capitalized R&D** | Capitalized: raises current EBITDA, creates an intangible asset amortized over years | Expensed: lower current EBITDA, no asset | How much was capitalized this year, over what period, and has the rate changed? |
| **Capitalized commissions** | Capitalized: moves sales cash spend off the current P&L | Expensed: full cost hits the period the deal was signed | What is the capitalized contract cost balance, and what amortization period supports it? Note this one is less of a free choice than the rest of the table: both IFRS 15 and ASC 606 REQUIRE capitalizing incremental costs of obtaining a contract where recovery is expected; the genuine policy choice is the practical expedient (expense when the amortization period would be a year or less). A company simply expensing multi-year commissions is off-standard, not conservative. Mechanics in comp-plan-architecture's IFRS 15 reference |
| **Hosting costs** | In COGS: correct, and gross margin reflects real delivery cost | Drifting into R&D: gross margin looks better than it is | Are all infrastructure costs in COGS? |
| **Implementation staff** | In COGS: services margin is visible | In S&M or R&D: services losses are hidden | Where do delivery salaries sit? |

**The single highest-yield question in this table:** a company that suddenly starts capitalizing more R&D or more commissions has improved EBITDA without improving anything. A changed capitalization rate with no accompanying explanation is worth more scrutiny than almost anything else on the page.

## Gross margin, by stream

Blended gross margin is nearly useless in a multi-stream SaaS business. Always split it.

**Subscription gross margin** is the real quality signal. It reflects hosting efficiency and support load per customer. It is the number that tells you whether the product scales.

**Services gross margin** is usually thin or negative, and that can be deliberate: services sold near cost to secure a subscription. It becomes a problem when services grow faster than subscription, because blended margin falls while the business appears to be growing well.

**Maintenance and support** on legacy perpetual licenses is typically very high margin. In a merged or acquired group it can be quietly carrying the entire P&L while everyone discusses subscription growth. Worth isolating explicitly.

**The question that reveals the most:** what is subscription gross margin alone, excluding services, over the last eight quarters? If it is falling, one of three things is happening: hosting is inefficient, support load per customer is rising, or discounting is eroding realized price. Each has a different owner.

## The operating expense lines

**Sales and marketing.** Contains quota-carrying salaries and variable, marketing program spend, sales leadership, and often sales operations and enablement. The line that most affects it commercially is quota attainment, because variable compensation flexes with it.

Watch for: S&M growing faster than revenue for more than two consecutive periods without a stated investment thesis. And check whether CS sits here or in COGS before comparing S&M efficiency to any benchmark.

**Research and development.** Product, engineering, design. Reduced by whatever is capitalized. In an acquisitive group carrying multiple product lines, R&D is structurally higher than a single-product peer, and comparing to a single-product benchmark is misleading.

**General and administrative.** Finance, legal, HR, executive, facilities, insurance, professional fees. Transaction costs and integration costs often land here before being added back.

Watch for: G&A that does not scale down as a percentage of revenue over time. In a PE-owned group, monitoring fees and sponsor costs may sit here and may be added back later.

## Reading the P&L against itself

Four ratios do most of the work, and all four should be read as trends rather than points.

| Ratio | What it tells you | What distorts it |
|---|---|---|
| Subscription gross margin | Whether the product scales | CS classification, hosting classification, capitalized software amortization |
| S&M as % of revenue | Cost of growth | Whether CS sits in S&M; whether commissions are capitalized |
| R&D as % of revenue | Investment in product | Capitalization rate; number of product lines carried |
| Revenue per employee | Operating leverage overall | Contractor versus employee mix; recent acquisitions |

## Period comparison discipline

Before comparing any two periods:

1. Confirm no classification changed between them.
2. Confirm no acquisition landed mid-period, and if one did, ask for both the reported and organic view.
3. Confirm the capitalization rate is unchanged.
4. Confirm currency treatment is unchanged, and ask for constant-currency where entities span currencies.
5. Check whether the prior period was restated. Restatements are rarely announced loudly.

## What a non-finance reader should be able to say after reading a P&L

- Which revenue stream is growing and which is carrying the margin.
- Whether subscription margin is improving or eroding, and the likely cause.
- Whether reported profit was helped by a capitalization choice.
- Which operating line grew fastest relative to revenue, and whether anyone has explained why.
- What is missing from the presentation.
