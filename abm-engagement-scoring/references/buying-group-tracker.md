# Buying Group and Decision-Making Unit (DMU) Tracking

## Overview: Why Buying Group Mapping is Non-Negotiable

An engagement score of 150 points from one procurement clerk does not signal market readiness. An engagement score of 75 points spread across the Economic Buyer, Technical Buyer, and End-User Champion does signal readiness.

Buying group mapping transforms engagement scoring from a volume metric into a readiness indicator. Without it, "engagement" is activity. With it, "engagement" is buying momentum.

## Defining Required Roles for Your TAM

Not every contact role is equal. Define which roles MUST be visible to win. Roles vary by product, deal size, and industry.

### Generic Enterprise Software Model (5 Roles)

Use this model if you are selling enterprise software (CRM, ERP, security, collaboration) to large organisations:

```
ROLE                    DEFINITION                          AUTHORITY LEVEL
─────────────────────────────────────────────────────────────────────────────
Economic Buyer          Controls budget and profit-and-loss. ABSOLUTE
                        Final approval authority. Typically   (Veto power)
                        CFO or CIO.

Technical Buyer         Evaluates against technical         HIGH
                        requirements, spec, and procurement  (Veto power on
                        criteria. Often CTO, VP Engineering, tech fit)
                        VP Infrastructure.

End-User Champion       Department leader or power user      MEDIUM
                        who drives adoption and is the       (Influencer)
                        earliest advocate. Often VP Sales,
                        VP Operations, business unit head.

Influencer/Advisor      External voice that shapes opinion.  MEDIUM
                        Analyst, consultant, peer reference, (Influencer)
                        board member. Optional but powerful.

Procurement Lead        Contract negotiation, vendor         MEDIUM
                        management, legal review.            (Speed lever,
                        Necessary but typically not the      not blocker)
                        blocker.
```

### Mid-Market Software Model (3 Roles, Simplified)

For mid-market or smaller deals (€50-200K ACV), reduce scope:

```
ROLE                    PRIORITY
────────────────────────────────
Economic Buyer          REQUIRED
Technical Buyer         REQUIRED (if technical product)
End-User Champion       REQUIRED
```

Procurement Lead may not be formalised; it often is the same person as Economic or Technical Buyer.

### High-Touch / Regulated Industry Model (6+ Roles)

For regulated industries (healthcare, finance, government) or compliance-heavy software, add:

```
ROLE                    DEFINITION
────────────────────────────────────────────────────────────────
Security/Compliance     Signs off on risk, data handling,   (Veto power)
                        and regulatory compliance.

Legal                   Contract and liability review.      (Veto power on
                                                            terms)

Internal Audit          May be involved in vendor audit.    (Influencer)
```

### Product-Led Growth Model (1-2 Roles)

For self-serve or free-tier adoption (Figma, Slack, Notion), buying committee is small:

```
ROLE                    DEFINITION
────────────────────────────────────────────────────────────────
Department Champion     Power user or team lead driving      REQUIRED
                        adoption. Often the first person
                        to trial the product.

Procurement Lead        Only engages after trial success     SECONDARY
                        if contract needed. May not exist.
```

Buying groups are large; decision is often by end-user champion alone. Economic Buyer appears late (contract phase) if at all.

### Custom Model

Define roles specific to your product:
- What job does the buyer hold who can make or block a buying decision?
- How many jobs must be filled for the deal to close?
- What is the minimum set? (If you require 5 roles but only 3 exist in the target company, adjust.)

## Buying Group Coverage Metrics

Track two metrics per account:

### 1. Role Coverage Percentage

```
Role Coverage % = (Roles Identified / Roles Required) × 100

Example (5-role model):
- Identified: Economic Buyer, Technical Buyer, Influencer, Procurement
- Required: Economic Buyer, Technical Buyer, End-User Champion, Influencer, Procurement
- Identified count: 4
- Required count: 5
- Coverage: 4/5 = 80%
```

**Thresholds:**
- 0-25%: Minimal; early stage
- 26-50%: Emerging; gaps remain
- 51-75%: Substantial; one critical role often missing
- 76-100%: Complete; all required roles identified

### 2. Contact Depth Per Role

Do not stop at "role identified." Track how many named individuals hold each role:

```
ROLE                    COUNT IDENTIFIED    TARGET    STATUS
─────────────────────────────────────────────────────────────
Economic Buyer          1                   2         UNDERDONE
Technical Buyer         2                   2         ✓ DONE
End-User Champion       1                   2         UNDERDONE
Influencer              1                   1         ✓ DONE
Procurement             1                   1         ✓ DONE

DEPTH SCORE: 6 / 8 contacts = 75%
```

**Target depths vary by deal size:**
- €50-200K: 1-2 per critical role (Economic, Technical, End-User) suffices
- €200-500K: 2-3 per critical role recommended (reduces single-point-of-failure risk)
- €500K+: 2-3 per critical role plus backup influencers

## Buying Group Tracker Template

Maintain a simple tracker per account:

```
ACCOUNT: Acme Corporation
INDUSTRY: Manufacturing
EMPLOYEE COUNT: 5,000
ICP TIER: Tier 1

BUYING GROUP MAP
────────────────────────────────────────────────────────────────────────────────
ROLE               CONTACT 1               CONTACT 2           ENGAGEMENT SCORE
────────────────────────────────────────────────────────────────────────────────
Economic Buyer     Jane Smith (CFO)        Open                45 (email click)
                   jane@acme.com           

Technical Buyer    Mark Johnson (CTO)      Sarah Lee (VP Eng)   85 (demo request)
                   mark@acme.com           sarah@acme.com      12 (website visit)

End-User Champion  Open                    Open                

Influencer         Dr. Lisa Brown          n/a                   25 (email open)
                   (external advisor)
                   lisa@ext.com

Procurement        Tom Wilson (Vendor)     n/a                   8 (meeting attend)
                   tom@acme.com


COVERAGE SUMMARY
────────────────────────────────────────────────────────────────────────────────
Roles Identified: 3 / 5 = 60% COVERAGE
Missing Critical Roles: End-User Champion (BLOCKER for Tier 1 deals)
Depth (total contacts): 5 contacts across 3 roles

CHAMPION STATUS
────────────────────────────────────────────────────────────────────────────────
Champion Identified: Mark Johnson (CTO, engagement score 85)
Champion Validation:
  - Power / Influence: Yes (controls architecture budget, reports to CEO)
  - Willingness: Yes (invited us to demo, introduced VP Eng)
  - Personal Win: Yes (problem aligns with team's OKR on infrastructure modernisation)


LAST UPDATE: 2026-07-14
NEXT ACTION: Prospect for End-User Champion (VP Operations or VP Manufacturing)
             Email Jane Smith (Economic Buyer) to set discovery call.
```

**Fields explained:**

- **ROLE:** Standard role (from your role model)
- **CONTACT:** Full name, title, email
- **ENGAGEMENT SCORE:** Individual engagement score (sum of signals for that person)
- **Champion:** Y/N + validation notes (see champion validation framework below)
- **Last Touch:** Date and type of last contact or engagement
- **Next Action:** What's the next step to deepen this relationship or fill a gap

## Champion Validation Framework

A champion is not just any engaged stakeholder. A champion has three attributes:

```
ATTRIBUTE 1: POWER / INFLUENCE
──────────────────────────────────────────────────────────────
Indicator         Yes                              No
─────────────────────────────────────────────────────────────
Can mobilise       Controls budget. Can approve      Cannot approve
resources?         within own authority. Can set    anything. Blocked by
                   meetings with peers.             gatekeepers.

Referenced by?     Peers cite them as decision      Peers do not
                   maker or influencer.             mention them.

Can bypass         Can push decisions through       Must follow
gatekeepers?       procurement without              formal process.
                   delays.

VALIDATION TEST: Can this person set up a meeting with the Economic Buyer
                 without your intervention? If yes, they have power.


ATTRIBUTE 2: WILLINGNESS (Internal Selling)
──────────────────────────────────────────────────────────────
Indicator         Yes                              No
─────────────────────────────────────────────────────────────
Sells internally?  Introduces you to other          Keeps
                   stakeholders. Makes case         introductions to
                   in meetings you do not          a minimum. Only
                   attend. Shares outcomes of       engages when you
                   your meeting with peers.        email them.

Proactive?         Follows up with you,            Waits for your
                   asks questions, shares          initiation.
                   ideas for next steps.

Risk appetite?     Willing to pioneer your         Wants proof from
                   solution; does not need         other customers
                   proof first.                    before engaging.

VALIDATION TEST: After your demo/call, does this person email you unsolicited
                 with questions or next-step ideas? If yes, they are willing.


ATTRIBUTE 3: PERSONAL WIN (Incentive Alignment)
──────────────────────────────────────────────────────────────
Indicator         Yes                              No
─────────────────────────────────────────────────────────────
Quantified Goal    Their department OKR or        No clear connection
Tie                personal goal directly         between your solution
                   benefits from your             and their goals.
                   solution.

Measurable         They can point to a specific    Success is vague
Outcome            metric that will improve       or belongs to
                   (e.g. "reduce cycle time       someone else's
                   by 20%" or "eliminate          department.
                   manual reconciliation").

Urgency            Solving this problem is a      No timeline
                   near-term priority for         pressure.
                   them (Q3-Q4 roadmap, not
                   "someday").

VALIDATION TEST: Ask "If this solution solves X, what changes for you personally?"
                 If the answer is clear and connects to their job/goal/incentive,
                 they have a personal win. If the answer is vague or defers to
                 someone else's goal, they do not.
```

### Champion Status Workflow

```
STAGE 1: IDENTIFY POTENTIAL CHAMPIONS
        ↓
        (Apply framework above)
        ↓
STAGE 2: VALIDATE
        • Question 1: "Can you set up a meeting with your CFO?" (Power test)
        • Question 2: "Would you share this with your team?" (Willingness test)
        • Question 3: "How would this help your role/goal?" (Personal Win test)
        ↓
STAGE 3: DESIGNATE AS CHAMPION (if all 3 pass)
        OR CONTINUE NURTURE (if 1-2 pass; retest in 30 days)
        ↓
STAGE 4: ARM THE CHAMPION
        • Provide talking points for internal sell
        • Offer customer reference calls
        • Supply ROI calculator or business case
        ↓
STAGE 5: HANDOFF FEEDBACK
        (When account is handed to sales, provide sales with champion context:
         "Mark is your champion. He wants to reduce manual infrastructure tasks
         by 40%. He can introduce you to Jane (CFO) but you'll need to address
         Sarah (VP Eng) concerns on API compatibility before proposal.")
```

## Buying Group Coverage Gates in Handover

Buying group completeness is a condition for sales handover, not optional. Define explicit gates:

### Handover Gate Framework

**Tier 1 Enterprise Accounts (€500K+ ACV):**
```
HANDOVER REQUIRES:
✓ Engagement Score >=120
✓ Economic Buyer identified (confirmed via email or meeting)
✓ Technical Buyer identified and engaged (visited pricing page OR attended demo)
✓ End-User Champion identified and engaged
✓ 1 Champion validated across at least one role
✓ Buying Group Coverage: >=75%

HANDOVER RECOMMENDED BUT NOT REQUIRED:
• Procurement contact identified
• Influencer/analyst identified
```

**Tier 2 Mid-Market Accounts (€200-500K ACV):**
```
HANDOVER REQUIRES:
✓ Engagement Score >=100
✓ Economic Buyer identified (email or meeting)
✓ Technical Buyer OR End-User Champion identified and engaged
✓ Buying Group Coverage: >=50%

HANDOVER RECOMMENDED:
• Champion validated
• 2+ roles engaged
```

**Tier 3 SMB Accounts (€50-200K ACV):**
```
HANDOVER REQUIRES:
✓ Engagement Score >=80
✓ Primary contact identified (could be Economic + End-User combined)
✓ Buying Group Coverage: >=33% (1 of 3 roles)
✓ Critical event triggered (demo request, meeting, email reply)
```

### Rejection Reason Codes (Sales Feedback Loop)

When sales rejects a handover, they provide a reason code. This feeds back to marketing:

```
REJECTION CODE      MEANING                       MARKETING ACTION
─────────────────────────────────────────────────────────────────────
ICP_UNFIT           Company does not match ICP    Review: why did this
                    (size, industry, geography).  account make the TAM?
                                                  Remove from list.

BUYING_GROUP_GAP    Economic Buyer or tech buyer  Re-engage. Prospect for
                    not identified. Cannot proceed missing role.
                    to conversations.

LOW_INTENT          No recent engagement. Last    Re-nurture. Send new
                    signal >30 days old.          campaign. Check for
                                                  signal capture gaps.

BAD_TIMING          Account is real but not       Keep on nurture list.
                    currently buying. Requeue to  Re-engage in 60 days.
                    next quarter.

DUPLICATE           Account already has open      De-duplicate. Merge
                    opportunity or recent sales   buying group into
                    activity.                     existing opportunity.

WRONG_PERSON        Identified contact is not a   Identify new primary
                    decision-maker or buyer.      contact. Re-engage.

PROSPECT_CONFLICT   Account is already in sales   Take off of marketing
                    pipeline. Already owned by    list; hand to sales
                    AE.                           for management.
```

**Track rejection patterns.** If >50% are rejected for "Low Intent," your engagement score threshold is too low. If >50% are rejected for "Buying Group Gap," you need better prospecting processes before handover.

## Building Your Buying Group Tracker System

### Option 1: Spreadsheet (Manual, Pilot)

**Setup:**
- Column A: Account name
- Columns B-F: Role columns (Economic Buyer, Technical Buyer, etc.)
- Columns G-K: Contact names and emails (per role)
- Column L: Engagement score (formula pulls from engagement-scoring sheet)
- Column M: Coverage % (formula: identified roles / required roles × 100)
- Column N: Champion status
- Column O: Last updated

**Update:** Manual weekly. As you scale beyond 50 accounts, this becomes impractical.

### Option 2: CRM Native (Recommended)

Use your CRM (HubSpot, Salesforce) contact roles and custom fields:

**Setup:**
1. Create contact role types matching your role model (Economic Buyer, Technical Buyer, etc.)
2. Link contacts to account records with role assignments
3. Create custom account fields:
   - `Buying Group Coverage %` (formula: count roles identified / roles required)
   - `Primary Champion` (lookup: contact with champion status = true)
   - `Buying Group Complete` (yes/no field)
4. Create CRM views/reports:
   - All accounts by coverage % (sort ascending)
   - Accounts with coverage <50% (gaps to fill)
   - Accounts with coverage >=75% (ready for handover)

**Advantage:** Real-time, integrated with sales workflow, scalable to 500+ accounts.

### Option 3: ABM Platform Native

Platforms like 6sense, Demandbase, and RollWorks include built-in buying group detection and tracking:

**Features:**
- Automatic identification of decision-makers and influencers via firmographic + engagement data
- Buying group coverage scoring
- Recommended next contacts to engage
- Handover integration with CRM

**Cost:** €50-200K annually depending on TAM size.

## Troubleshooting Common Buying Group Mapping Gaps

**Issue: "We identified the Economic Buyer but they have not engaged."**
- Action: Do not wait. Use the identified Economic Buyer contact to reach other stakeholders ("I spoke with Jane Smith and she mentioned you are handling the technical evaluation..."). This creates an internal referral.

**Issue: "We have one champion but they are low in the org (not Economic Buyer)."**
- Action: Arm this champion to introduce you to the Economic Buyer. Provide them with a one-pager or talking points for internal sell. Ask: "Can you loop in your finance contact?" This converts internal champion into a referral source.

**Issue: "Our buying group is complete but engagement scores are low."**
- Action: You may have mapped the organisational structure but not the active buying process. Escalate engagement by sending a triggering email or content piece to the Economic Buyer directly. "I saw you reviewed our pricing page; happy to answer technical questions; CC'ing Mark (CTO) for his input."

**Issue: "We tried to contact a role but the person refused to engage."**
- Action: They may not be the right person in that role. Try another contact in the same role. Or, they may have delegated. Ask the refusing contact: "Is there someone on your team who is more involved in this evaluation?" You have not found the right Economic Buyer yet.

---

## Source Attribution

Buying group mapping framework adapted from:
- MEDDIC Champion Definition (Atlassian, 2025)
- The Starr Conspiracy B2B Buying Committee Benchmarks (2024)
- Gartner B2B Buying Research (2023-2025)
- Forrester Buying Groups Research (2026)
- Demandbase Multi-Touch Buying Group Attribution (2024)
- Practitioner case studies from ABM engagements (practice-based) (2025-2026)
