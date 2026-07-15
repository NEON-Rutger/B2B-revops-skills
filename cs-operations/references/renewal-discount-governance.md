# Renewal Discount Governance

On-demand reference for the cs-operations skill.

## The Discount Sunset Problem

The #1 cause of contentious renewals: the initial deal had a discount that was never documented to expire. At renewal, the customer's anchor is what they paid, not what the product is worth. Every CSM dreads the conversation: "Why is my renewal 25% higher?"

This is a governance failure, not a customer problem. The fix is structural.

**Prevention (at deal close):**

- Every discounted deal must have a `Discount_Expiry_Date` in CRM
- T-120 renewal workflow must flag expiring discounts automatically
- CSM must prepare value justification BEFORE the renewal conversation, not after the customer complains

## Renewal Pricing Conversation Framework

**Step 1: Lead with value, not price (T-90).** Before any pricing conversation, deliver a value realisation report: usage data, business outcomes achieved, ROI vs. original business case. The customer needs to see the value before they see the price.

**Step 2: Frame the step-up (T-60).** "Your initial agreement included a first-year pricing benefit as part of [commitment/early adoption]. The renewal reflects the full value of the platform, which has [added X features / expanded Y capabilities / supported Z% more users than originally scoped]."

**Step 3: Offer graduated step-up if needed (T-30).** If the customer pushes back hard: 50% of the price increase in Year 1, full price Year 2. This is a save play, not a negotiation tactic. Use only when the alternative is churn.

## Save Plays with Pricing Components

| Scenario | Save play | Pricing element | Approval |
|----------|-----------|----------------|----------|
| Discount expiring, customer at risk | Graduated step-up (50% Yr 1, full Yr 2) | Time-limited bridge | Sales Mgr |
| Usage dropped, customer underutilising | Scope reduction to lower tier | Retain at lower ARR; plan re-expansion | CSM |
| Feature gap blocking renewal | 90-day trial of higher tier at current price | Expansion play as save | CSM + Sales Mgr |
| GPO member threatening churn | Validate GPO terms. Confirm volume commitment. | Per GPO framework | Deal Desk |
| Budget genuinely cut | Split billing or deferred payment | Cash flow accommodation, not discount | Finance |

**Key rule:** Save plays with pricing components must be tracked separately from standard renewals. Tag with reason code. Track: what % of save-play renewals expand back to full price within 12 months? This tells you whether the save was effective or just delayed churn.

## GPO Renewal Coordination

For accounts under GPO/consortium agreements:

- **T-120:** Check GPO master record for current tier and volume status
- **T-90:** Validate actual volume against committed volume
- **T-60:** If volume below commitment, prepare tier adjustment conversation with GPO account owner
- **T-30:** Renewal terms must align with GPO agreement. No ad-hoc deviations without Deal Desk

For the full GPO handling framework (admin fees, volume tiers, negotiation rules), see pricing-strategy skill.
