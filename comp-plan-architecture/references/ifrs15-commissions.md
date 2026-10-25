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
- SPIFs and other incentives whose payout depends on anything beyond obtaining contracts. A SPIF paid per contract obtained can be incremental, so check the mechanic rather than the label

## The two traps designers walk into

**1. The continued-employment condition.** A commission contingent on a **substantive** future service condition, one that ties the payment to future work rather than to obtaining the contract, can fall outside contract acquisition costs and under compensation accounting instead (IAS 19, or ASC 710 under US GAAP). The test is whether the service condition is substantive: a condition that only requires employment on the payment date is generally treated differently from a vesting period that runs well past the contract. That judgment sits with the auditor, so confirm the treatment before the clause is drafted.

This matters because the "must still be employed when the commission is earned" clause is one every employment lawyer will want in the plan. It is good legal protection, and depending on how long the condition runs it can move the payment out of capitalization. **Flag the tension explicitly at design time rather than letting it surface in an audit.** The decision is a trade between legal protection and accounting treatment, and someone should make it deliberately.

**2. Manager overrides are genuinely contested** among practitioners. Some guidance says overrides are always expensed because they are tied to team performance over a period; other guidance says overrides on individual contracts are capitalizable.

The test that the published guidance in circulation (PwC among others) converges on is whether the payout depends on nothing but obtaining contracts:

- An override **computed contract by contract** on the reports' contracts is incremental and capitalizable.
- An override on **aggregate team attainment** can still be incremental where attainment consists only of contracts obtained, and stops being incremental once profitability, individual performance reviews or other non-contract factors enter the formula. Cite the specific publication your auditor accepts before relying on either reading.

**This is a plan design decision, not an accounting decision.** The comp designer owns it.

## Amortization

The period must reflect the period over which the asset is consumed, generally the expected customer relationship. Both frameworks allow the period to extend **beyond the initial contract term** where renewal is anticipated, particularly where renewal commissions are lower than acquisition commissions.

Three defensible methods, in descending order of auditor comfort:

1. Cohort retention analysis on actual historical tenure
2. Technology useful life, typically 3 to 7 years for enterprise platforms (practice range; defend it with your own product lifecycle data)
3. Contract term plus anticipated renewals, which auditors scrutinize hardest

**The practical expedient is a trap.** The one-year-or-less expedient is unavailable if anticipated renewals push the benefit period beyond twelve months. A SaaS business expecting three or four renewal cycles cannot apply it to new logo deals on 12-month contracts. This is an error that draws regulator and auditor scrutiny; verify the expedient's availability with the auditor before applying it.

**Worked example**

```
ARR                     EUR 120,000 over 36 months
Commission rate         10%
Capitalized             EUR 36,000
Expected customer life  60 months (assumes one 24-month renewal, derived from
                        cohort retention; state this assumption in the policy memo)
Monthly amortization    EUR 600
Churn at month 24       impair remaining EUR 21,600
Renewal                 capitalized separately, over the renewal term
```

## The design rule

**Build the plan so the capitalizable slice is structurally separable from everything else.**

| Makes compliance harder | Makes compliance easier |
|---|---|
| Tiered and accelerated rates, because one contract spanning multiple tiers raises allocation questions | A distinct, flat-rate, contract-level commission component on new and expansion ACV, separately identified in the plan and in the calculation output |
| Pooled, team or aggregate-attainment components, which weaken contract-level linkage and need an explicit auditor position | Clean separation of new business, expansion and renewal rates, since renewals capitalize over the renewal term only |
| Mid-period plan changes, which force recalculation on the existing capitalized balance | Every other component (quota bonuses, MBOs, team kickers, president's club, SPIFs) grouped into one bucket whose treatment is settled once with the auditor, usually non-capitalizable |
| Bundled implementation services mixed with subscription in one commissionable amount | A stable amortization policy per product line, documented once |
| Service-vesting conditions, which reclassify the payment out of contract costs | |
| Multi-payee crediting where the sum exceeds 100%, because each payee's amount must still trace to the contract | |

If the plan is separable, finance produces a per-contract amortization schedule without reverse-engineering the payout logic. If it is not, they build a shadow model, and it will be wrong.

## Why the CFO cares

**1. EBITDA and valuation.** Capitalizing commissions moves cash spend off the current period P&L onto the balance sheet, amortized over years. In a private equity hold heading toward an exit, the treatment of contract acquisition costs directly affects reported EBITDA and therefore the multiple. A plan design that maximizes the non-capitalizable share depresses current-period earnings relative to one that does not.

**2. Multiple legacy policies.** After an acquisition, each legacy entity will have had its own capitalization policy, amortization assumption and evidence set. Harmonizing the **accounting policy** is a separate workstream from harmonizing the **plan**, and the plan design constrains it. Auditors will ask which policy survived and why.

**3. Audit artifacts.** Auditors expect, quarterly:

- A capitalization policy memo stating decision rules, period method and expedient use
- A per-contract amortization schedule with beginning balance, monthly expense and ending balance
- A cohort retention analysis supporting the period assumption
- An impairment review comparing churned customers against carrying balances

**The plan must produce the data those artifacts consume.** That is a design requirement, and it belongs in the calculation specification.

## One thing to keep straight

Compressing sales cycles changes deal volume and payment timing. It does not change amortization logic, because **amortization follows customer life, not sales cycle length.** Do not let anyone conflate the two when a leadership team is targeting shorter cycles.
