# IFRS 15 and ASC 606 as a comp design constraint

Commission accounting is usually treated as something finance does after the plan is designed. It is not. Several common plan features change the accounting treatment entirely, and the discovery normally happens in an audit.

## Which standard

Say **IFRS 15** for a European group unless there is US reporting somewhere in the structure. The contract-cost principles are substantively aligned (IFRS 15 paragraphs 91 to 94 versus ASC 340-40), so the design guidance is the same either way, but using the right name in the room matters. **Confirm the reporting framework before writing anything for a CFO.**

## Capitalizable versus not

**Capitalizable** as incremental costs of obtaining a contract:

- Sales commissions resulting directly from obtaining a specific contract
- Incremental employee bonuses linked to obtaining an individual contract
- Success fees paid to advisers for securing a deal
- Renewal commissions, over the renewal term

**Not capitalizable:**

- Salaries, which are incurred regardless of contract success
- General advertising
- Proposal and negotiation costs that would be incurred whether or not the contract is won
- **Bonuses tied to a revenue target affected by more than obtaining new contracts.** This is the one that catches most quota-based bonus plans
- Discretionary annual bonuses contingent on overall targets or entity profitability
- SPIFs

## The two traps designers walk into

**1. The continued-employment condition.** A commission contingent on remaining employed through a future date, or on any other service-vesting condition tying the payment to future work rather than to obtaining the contract, is **not a contract acquisition cost at all**. It falls under compensation accounting (IAS 19, or ASC 710 under US GAAP) instead.

This matters because the "must still be employed when the commission is earned" clause is one every employment lawyer will want in the plan. It is good legal protection and it moves the payment out of capitalization. **Flag the tension explicitly at design time rather than letting it surface in an audit.** The decision is a trade between legal protection and accounting treatment, and someone should make it deliberately.

**2. Manager overrides are genuinely contested** among practitioners. Some guidance says overrides are always expensed because they are tied to team performance over a period; other guidance says overrides on individual contracts are capitalizable.

The resolution consistent with PwC's guidance turns on the mechanic:

- An override **computed contract by contract** is incremental and capitalizable.
- An override on **aggregate team attainment** is not.

**This is a plan design decision, not an accounting decision.** The comp designer owns it.

## Amortization

The period must reflect the period over which the asset is consumed, generally the expected customer relationship. Both frameworks allow the period to extend **beyond the initial contract term** where renewal is anticipated, particularly where renewal commissions are lower than acquisition commissions.

Three defensible methods, in descending order of auditor comfort:

1. Cohort retention analysis on actual historical tenure
2. Technology useful life, typically 3 to 7 years for enterprise platforms
3. Contract term plus anticipated renewals, which auditors scrutinise hardest

**The practical expedient is a trap.** The one-year-or-less expedient is unavailable if anticipated renewals push the benefit period beyond twelve months. A SaaS business expecting three or four renewal cycles cannot apply it to new logo deals on 12-month contracts. Regulators have cited registrants for exactly this error.

**Worked example**

```
ARR                     EUR 120,000 over 36 months
Commission rate         10%
Capitalized             EUR 36,000
Expected customer life  60 months
Monthly amortization    EUR 600
Churn at month 24       impair remaining EUR 21,600
Renewal                 capitalized separately, over the renewal term
```

## The design rule

**Build the plan so the capitalizable slice is structurally separable from everything else.**

| Makes compliance harder | Makes compliance easier |
|---|---|
| Tiered and accelerated rates, because one contract spanning multiple tiers raises allocation questions | A distinct, flat-rate, contract-level commission component on new and expansion ACV, separately identified in the plan and in the calculation output |
| Pooled, team or aggregate-attainment components, which break contract-level linkage entirely | Clean separation of new business, expansion and renewal rates, since renewals capitalize over the renewal term only |
| Mid-period plan changes, which force recalculation on the existing capitalized balance | Every other component (quota bonuses, MBOs, team kickers, president's club, SPIFs) grouped into an explicitly non-capitalizable bucket |
| Bundled implementation services mixed with subscription in one commissionable amount | A stable amortization policy per product line, documented once |
| Service-vesting conditions, which reclassify the payment out of contract costs | |
| Multi-payee crediting where the sum exceeds 100%, because each payee's amount must still trace to the contract | |

If the plan is separable, finance produces a per-contract amortization schedule without reverse-engineering the payout logic. If it is not, they build a shadow model, and it will be wrong.

## Why the CFO cares

**1. EBITDA and valuation.** Capitalizing commissions moves cash spend off the current period P&L onto the balance sheet, amortized over years. In a private equity hold heading toward an exit, the treatment of contract acquisition costs directly affects reported EBITDA and therefore the multiple. A plan design that maximizes the non-capitalizable share depresses current-period earnings relative to one that does not.

**2. Multiple legacy policies.** After an acquisition, each legacy entity will have had its own capitalization policy, amortization assumption and evidence set. Harmonizing the **accounting policy** is a separate workstream from harmonizing the **plan**, and the plan design constrains it. Auditors will ask which policy survived and why.

**3. Audit artefacts.** Auditors expect, quarterly:

- A capitalization policy memo stating decision rules, period method and expedient use
- A per-contract amortization schedule with beginning balance, monthly expense and ending balance
- A cohort retention analysis supporting the period assumption
- An impairment review comparing churned customers against carrying balances

**The plan must produce the data those artefacts consume.** That is a design requirement, and it belongs in the calculation specification.

## One thing to keep straight

Compressing sales cycles changes deal volume and payment timing. It does not change amortization logic, because **amortization follows customer life, not sales cycle length.** Do not let anyone conflate the two when a leadership team is targeting shorter cycles.
