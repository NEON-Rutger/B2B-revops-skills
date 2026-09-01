# Sales compensation administration tooling

## Where spreadsheets break

The genuinely independent evidence is the spreadsheet error research (Panko and the EuSpRIG corpus, studies from the 2000s-2010s; some samples run above 90%): **over 80% of non-trivial spreadsheets contain at least one error**, with material error probability rising sharply above roughly 100 formulas, three tabs, or multiple editors. The research predates modern tooling, but nothing about commission spreadsheets has changed the mechanism it describes: silent formula drift under multiple editors.

Vendor-sourced benchmarks, which should be read as directional advocacy rather than measurement: roughly 23 hours per administrator per month on spreadsheet administration versus 5 to 7 with software; overpayment around 4.2% of payouts on spreadsheets versus 0.5 to 1% with software; around 62% of reps maintaining shadow tracking. Vendor scaling break points are usually given as 1 to 10 payees viable, 25 to 50 strained, 50 to 100 "silently failing", 100+ untenable.

**Three structural arguments hold regardless of whose numbers you believe:**

1. Multiple legacy plan sets, plus transitional dual-territory crediting, plus overlay splits, is precisely the complexity class where spreadsheet linkage fails.
2. Contract-level commission amortization under IFRS 15 requires a per-contract sub-ledger with beginning balance, monthly expense, ending balance and impairment testing on churn. Spreadsheets do this by hand.
3. Where the designer and the administrator are different people, spreadsheets transfer badly. Every undocumented assumption becomes someone else's problem.

## Ask this before recommending any purchase

**What does the existing ERP or revenue recognition module already do?**

Many finance platforms claim configurable ASC 606 and IFRS 15 **revenue recognition** while saying nothing about capitalizing and amortising **contract acquisition costs**. Those are different capabilities. That gap is the thing that decides whether a separate commission sub-ledger is needed, and it is answerable with one email to the vendor.

Also ask how many applications already exist in the CRM estate. Adding a tool to an unrationalised stack is a decision that should be made deliberately, not by default.

## Market shape, 2026

Gartner Peer Insights, Sales Performance Management, as displayed August 2026:

| Vendor | Rating | Reviews |
|---|---|---|
| Everstage | 4.7 | 281 |
| Salesforce SPM | 4.5 | 264 |
| Xactly Incent | 4.4 | 274 |
| CaptivateIQ | 4.6 | 219 |
| Anaplan | 4.3 | 183 |
| Varicent | 4.4 | 104 |
| Performio | 4.4 | 74 |
| ElevateHQ | 4.5 | 38 |
| beqom | 4.5 | 27 |
| Forma.ai | 4.8 | 8 |

QuotaPath, Qobra, Palette and Core Commissions do not appear in that listing.

**Native versus connected.** Only Salesforce Spiff runs on the Salesforce platform itself. CaptivateIQ, Everstage, QuotaPath, Xactly, Varicent, Performio, Forma.ai, Qobra, Palette and Core Commissions all connect by API.

## Indicative pricing

All figures are list or observed-deal data, mostly from vendor blogs and aggregators rather than published price lists. Treat as negotiation anchors, not quotes, and re-verify before using them.

| Vendor | Price signal | Implementation |
|---|---|---|
| QuotaPath | Published: USD 35/user/mo + USD 525/mo platform fee (Growth); USD 50 + USD 800 (Premium) | 45 to 90 days |
| Salesforce Spiff | USD 75/user/mo annually; USD 250/mo per non-Salesforce connector | 4 to 6 weeks Salesforce-only |
| CaptivateIQ | ~USD 55/payee/mo list; median ACV ~USD 35K/yr | USD 10K to 30K, 8 to 12 weeks |
| Everstage | Quote only; median ACV ~USD 41K; USD 30K to 60K/yr at 50 to 100 reps | USD 5K to 15K |
| Xactly Incent | ~USD 40 to 60/user/mo | Reported up to 6 months |
| Varicent | ~USD 56/user/mo | Enterprise scale |
| Performio | Median ACV ~USD 50K; USD 60 to 120/user/mo depending on band | USD 15K to 75K |
| Forma.ai | No public pricing; estimated six figures plus implementation | 8 to 16 weeks |
| Qobra | From ~USD 39/user/mo | Not published |
| ElevateHQ | USD 25 / 30 / 40 per user by tier | Not published |

**Negotiation benchmarks** (Vendr data, likely generalising across the category): competitive context achieves 15 to 30% off initial quotes, multi-year 10 to 25%, end-of-quarter timing a further 5 to 15%, upfront annual payment 3 to 7%.

## Selection criteria for a European multi-entity company

In priority order. The first two are where most evaluations go wrong.

1. **A real contract-cost sub-ledger**, not ASC 606 marketing copy. Ask to see the schedule output: beginning balance, monthly expense, ending balance, impairment trigger. Ask explicitly about **IFRS 15** if that is the reporting framework, since several vendors document ASC 606 only.
2. **Overlay split handling** that mirrors CRM splits without forcing credit totals to 100%. If the tool cannot represent 130% total credit, it cannot represent the plan.
3. **Multi-currency and multi-entity** with auditable FX from a named source at configurable intervals, local currency visible to reps in real time, and consolidated liability reporting with drill-down by entity.
4. **Works council posture.** In Germany, BetrVG s.87(1) no. 6 covers technical systems suitable for monitoring performance, which can make the tool itself co-determined. Ask the vendor whether they have been through a Betriebsrat approval before.
5. **EU data residency and GDPR.** No public vendor comparison addresses this. Put it in the RFP explicitly.

Also relevant in Europe and absent from most comparisons: local social contribution treatment of variable pay, and fully localised UI including date formats and number separators.

## Common complaints, by vendor

Useful for reference calls, because these are the questions that produce honest answers.

- **Salesforce Spiff.** Pleasant for reps, difficult for administrators. Changes require workarounds and touching one area can break another. Reporting often needs export and manual reconciliation. Support response reported as slower since the acquisition. Non-Salesforce CRMs deprioritized and charged per connector. Weak on territory, quota and sales planning.
- **CaptivateIQ.** Onboarding requires more internal lift than promised. Limited out-of-the-box dashboards, with users reverting to spreadsheets. ASC 606 handled via ERP export rather than a native sub-ledger. Scale concerns above 1,000 payees.
- **Everstage.** Sync delays during close periods. Limited report customization. Dependence on support for configuration changes.
- **Xactly.** Legacy platform, enterprise-oriented, long implementations, described as difficult to maintain. Note that Xactly CEA remains among the strongest 606 sub-ledgers, so this is a trade rather than a disqualification.
- **Forma.ai.** Reduced self-service and dependence on the vendor for routine changes. No turnkey 606 module. Quote-only pricing.

## A defensible shortlist shape for 50 to 100 payees in Europe

Rather than a single recommendation, present three options on different theories and let the organization choose the theory:

- **The platform-native option.** Lowest integration effort if the CRM holds all the data, transparent pricing, fastest implementation. Risk sits in administrator experience and roadmap.
- **The mid-market default.** Best independent review volume, explicit contract-cost module, pricing in the mid five figures. Risk sits in verifying IFRS 15 rather than ASC 606.
- **The European option.** EU-domiciled, built for multi-entity and multi-currency, vendor relationship in the same time zone and legal jurisdiction. Risk sits in smaller scale and thinner independent review.

**Rule out** enterprise platforms whose implementation burden is disproportionate at this scale, and managed-service models priced for organizations several times larger.
