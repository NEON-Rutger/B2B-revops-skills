# Expansion Scoring Model & Whitespace Analysis

On-demand reference for the cs-operations skill.

Expansion signals and the CS-to-Sales ownership model live in the skill body. This reference holds the scoring model and whitespace analysis detail used to quantify and prioritise expansion plays.

## Expansion Scoring Model

```
EXPANSION SCORING MODEL:
  Score 0-100 based on:
    Usage growth (30%)         — is usage increasing month-over-month?
    Stakeholder breadth (25%)  — are new people engaging?
    Feature depth (20%)        — are they using advanced features?
    Health trajectory (15%)    — is health score trending up?
    Contract headroom (10%)    — is there room to expand (seats, usage, products)?

EXPANSION OWNERSHIP (by score):
  Score 0-40:   CSM monitors. No active sell.
  Score 41-70:  CSM plants seeds. Shares relevant content. Mentions capabilities.
  Score 71-100: CSM initiates expansion conversation. If deal > threshold → hand to AE.

  Handoff threshold: Varies by org. Typical: expansion > 30% of current ACV → AE involved.
  Below threshold: CSM closes expansion directly (with approval).
```

## Account Scoring for Expansion Readiness

Qualitative readiness triggers that complement the quantitative score:

- Consistent Green health score for 2+ quarters
- Usage of 80%+ of contracted capacity (quantitative trigger)
- Champion has expressed interest in additional use cases
- Stakeholder whitespace: contacts in departments not yet using the product

## Whitespace Analysis

```
WHITESPACE ANALYSIS:
  For each account, map:
    Products purchased vs available    → product whitespace
    Users/seats vs potential           → seat whitespace
    Departments using vs total         → department whitespace
    Features adopted vs available      → feature whitespace
    Stakeholders engaged vs org chart  → relationship whitespace

  Review in QBR. Update quarterly. Use to prioritise expansion plays.
```

**Two dimensions to focus on:**

1. **Stakeholder whitespace:** Which teams or business units could benefit from the product but aren't using it? Map against org chart.
2. **Product whitespace:** Which features or modules is the customer licensed for but not using? Which complementary products are they not yet on?

For full expansion architecture including NRR improvement methodology, see the expansion revenue architect skill. For handoff design and routing logic, see revops-handoffs skill.
