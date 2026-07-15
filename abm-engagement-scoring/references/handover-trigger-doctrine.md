# Marketing-to-Sales Handover Trigger Doctrine

## Core Principle: Handover Discipline Enables Accountability

A handover is the moment marketing passes an account to sales with three pieces of information: (1) "This account is engaged," (2) "Here are the people we have identified," (3) "Here is what we recommend as the first step." Sales then decides whether to pursue. The quality of the handover packet and the clarity of handover criteria determine whether marketing gets credit for the pipeline it influences or disappears into noise.

Handover discipline also protects sales. Poor handovers (low engagement, incomplete buying group, stale signals) waste AE time on accounts that are not ready. Good handovers (hot engagement, identified economic buyer and champion, recent critical event) accelerate pipeline.

## Handover Qualification Criteria

An account is ready for handover when THREE conditions align:

```
CONDITION 1: ENGAGEMENT SCORE >=100
└─ Account shows active buying signals
   Multiple sources or critical event detected
   Exception: Lower threshold (>=80) if critical event + Economic Buyer present

CONDITION 2: BUYING GROUP COVERAGE >=50%
└─ At least half of required roles identified
   OR Economic Buyer explicitly engaged (email reply, meeting accepted, proposal request)
   Exception: Can handover with <50% IF critical event (demo, RFP) + Economic Buyer confirmed

CONDITION 3: ACCOUNT HAS NOT BEEN HANDED BEFORE
└─ First handoff only. If sales rejected previously, requirement is stricter.
   (See "Persistent Rejection" section below.)
```

**All three must be true to trigger handover.** Handover occurs when all three gates are OPEN. If any gate is closed, account remains in marketing nurture.

## Critical Events (Handover Accelerators)

A critical event can accelerate handover even if engagement score is borderline (70-100), provided buying group requirements are partially met.

### Critical Event Definitions

```
CRITICAL EVENT                      BUYING GROUP GATE          TIME TO HANDOVER
──────────────────────────────────────────────────────────────────────────────
1. DEMO REQUEST
   (Contact submits demo form)      Economic Buyer should be    24 hours
                                    identifiable OR present
                                    in the request

2. MEETING SCHEDULED
   (Calendar invite from            N/A                         Immediate
    prospect for discovery call)    (Trigger assumes they sent
                                     it for a reason)

3. PROPOSAL REQUEST
   (Prospect explicitly asks        N/A (explicit ask)          Immediate
    for pricing or proposal)

4. RFP ISSUED
   (Formal request for proposal)    N/A (formal process)        Immediate

5. PRODUCT TRIAL ACTIVATION
   (User signs up for free trial    At least 1 identified       Follow within 7 days
    and completes first action:     contact should be the       (not immediate;
    creates account, invites users, champion or power user      allow trial to show
    runs first report)              for this signal)            value)

6. THIRD-PARTY INTENT SPIKE
   (News mention, analyst review,   2+ roles showing active     48 hours
    job posting for related role,   engagement OR recent
    competitive mention on social)  signal >5 days old

7. BUYING SIGNAL CLUSTERING
   (Demo request + meeting request  No buying group gate;       24-48 hours
    within 2 weeks from different   account clearly moving
    contacts)
```

**Critical events are binary.** They either happened or did not. Track them in CRM as explicit milestone dates. When a critical event occurs, alert sales within the time window above.

## Handover Packet Specification

When an account meets handover criteria, marketing prepares a formal handover packet. This packet is sales' brief on the account.

### Section 1: Executive Summary (1 paragraph)

```
[Company Name] is actively researching [solution category] with [engagement summary].
Our recommended next step is [specific action]. This account is ready for AE conversation.
```

**Example:**
"Acme Corp is actively evaluating infrastructure automation solutions. We have identified
three key stakeholders: CFO (budget owner), CTO (technical decision-maker), and VP Ops
(end-user champion). Recent signals include a demo request and pricing page review. CTO
Mark Johnson has engaged twice. Recommend AE reach out to Jane Smith (CFO) with a
business case focused on operational efficiency. We have a warm intro via Mark."

### Section 2: Company Profile (Essential Facts)

```
Company Name:          Acme Corporation
Industry:              Manufacturing
Geography:             Netherlands (Amsterdam HQ)
Employee Count:        2,500
Estimated Revenue:     €150M+
Founded:               2008
Recent News:           Launched new product line Q2 2026

ICP Fit Score:         Tier 1 (Perfect fit)
TAM Segment:           Mid-Market Enterprise
Customer Status:       Non-customer (new account)
Sales Territory:       [AE name or territory code]
```

### Section 3: Engagement Context (How We Know They Are Active)

```
Engagement Score:      125 points (HOT)
Last 30 days:
  • 3 website visits (pricing page, ROI calculator, case study)
  • 1 demo request (Mark Johnson, CTO, July 12)
  • 2 email clicks (product feature announcement, webinar invite)
  • 1 document download (case study on automation)

Recency:               Last signal July 14 (48 hours old)
Trend:                 Rising (engaged steadily over 4 weeks, no drops)
Acceleration:          Demo request triggered 48h ago; signals clustering
```

### Section 4: Buying Group Map (Decision-Makers and Influencers)

```
ROLE               NAME                TITLE              ENGAGEMENT SCORE  CHAMPION?
──────────────────────────────────────────────────────────────────────────────────
Economic Buyer     Jane Smith          CFO                45                 No
                   jane@acme.com       (Finance)          (one email click)

Technical Buyer    Mark Johnson        CTO                85                 YES
                   mark@acme.com       (Infrastructure)   (demo request +
                                                          2 visits + reply)

End-User Champion  Open                n/a                  n/a                  n/a
                   

Influencer         Tom Brown           VP Operations      30                 No
                   tom@acme.com        (User adoption)    (one click)

Procurement        Open                n/a                  n/a                  n/a


BUYING GROUP COVERAGE: 3 / 5 roles = 60%
CHAMPION IDENTIFIED: Mark Johnson (CTO)
  - Has power (controls infra budget, reports to CEO)
  - Willingness: Yes (invited us to demo, replied to email)
  - Personal Win: Yes (goal is to reduce manual infrastructure tasks)
```

### Section 5: Recommended First Steps (What Sales Should Do)

```
NEXT STEP 1 (IMMEDIATE):
└─ Mark Johnson (CTO) has accepted our demo for July 18.
   Recommend: AE attends demo to scope technical requirements
   and ask Mark to introduce you to Jane Smith (CFO).

NEXT STEP 2 (WITHIN 5 DAYS):
└─ Schedule discovery call with Jane Smith (CFO).
   Scope: Operational efficiency gains + budget timeline.
   Ask: "Has Mark updated you on the demo findings?"

NEXT STEP 3 (WITHIN 10 DAYS):
└─ Identify End-User Champion (Operations or Finance team).
   Ask Jane or Mark for intro to department head who manages workflow.
   Send warm introduction, not cold call.

KEY TALKING POINTS (for AE):
• Automation reduces manual reconciliation by 40% (relevant to ops)
• Integrates with existing stack (manufacturing + ERP)
• Average ROI payback: 18 months (relevant to CFO)
• Peer customer in same industry: [Customer reference]
```

### Section 6: Marketing Activity History (Context for AE)

```
ACTIVITIES RUN TO THIS ACCOUNT:
• June 15: Added to "Infrastructure Automation" email nurture sequence
• June 22: LinkedIn ad served (case study: 10x cost reduction)
• June 28: Email sent: "Q3 automation roadmap" (opened, clicked)
• July 8: Invited to webinar (registered, attended)
• July 12: Demo request via website form
• July 14: Case study + ROI calculator sent via email

CONTENT CONSUMED:
• Pricing page (2x visits)
• ROI calculator (completed, result shown 15% savings)
• Case study: Manufacturing + Automation (downloaded)
• Webinar recording: Q3 Product Roadmap (watched 28 min / 45 min)

RESPONSES TO MARKETING:
• 2 email opens (link clicks)
• 1 demo request
• 1 document download
• No responses to LinkedIn outreach yet
```

### Section 7: Known Objections or Constraints (Help Sales Prepare)

```
KNOWN CONSIDERATIONS:
• Budget: On track; they have Q3 discretionary budget for infrastructure
• Timeline: Evaluating for Q4 implementation (90-120 day cycle)
• Competitive: Mentioned competitor in webinar chat (noted 2 companies in eval)
• Technical: Concerned about integration with legacy ERP system (raised in demo req)
• Regulatory: Manufacturing facilities in EU; GDPR + data residency requirements

PROACTIVE TALKING POINTS FOR AE:
• "Most of our clients integrate with your ERP version within 2 weeks"
• "GDPR compliance is built in; all data stays in EU"
• "We typically see 8-12 week implementation for your company size"
```

### Section 8: CRM Readiness Checklist

```
☑ Account record created in Salesforce
☑ Contact records created (Mark Johnson, Jane Smith, Tom Brown)
☑ Contact roles assigned (CTO, CFO, VP Operations)
☑ Account tagged with: "ABM", "Tier 1", "Active Buying"
☑ Opportunity structure: (recommend creating now if in-market)
  ☐ Opportunity record created? _____ (AE to create after first call)
☑ Activity history visible (email/call/meeting dates in CRM)
☑ Previous interactions logged (any prior sales touches? No n/a clean account)
☑ EU compliance check (if account in EU): No Article 21 right-to-object recorded
  (Verify: Contact has not exercised unconditional right to object to direct
   marketing. If yes on record, do NOT hand to sales; remove from outreach list.)
```

**DPIA Note (for large-scale engagement profiling and buying group mapping):** Under EU AI Act and GDPR Article 35, large-scale automated profiling of buying group members (especially when using automated role detection or stakeholder mapping) may trigger Data Protection Impact Assessment (DPIA) requirements. The DPIA is prudent but not automatically mandatory under current guidance (EDPB; as of June 2026). If your handover packet or engagement system performs algorithmic classification of contacts by role or buying intent, document the processing and maintain evidence of fairness testing.

### Section 9: Handover Metadata

```
Handover Date:         July 15, 2026
Handover Prepared By:  Sarah (Marketing)
Sales Assigned To:     Mike Chen (AE, Netherlands territory)
Expected Response By:  July 17, 2026 (SLA: 48h)
Handover Confidence:   HIGH (hot engagement + identified champion + recent critical event)

Conditions Met:
  ✓ Engagement Score 125 (>=100 threshold)
  ✓ Buying Group Coverage 60% (>=50% threshold)
  ✓ Critical event triggered (demo request)
  ✓ Account has NOT been handed before
```

## Handover SLA and Sales Acceptance Workflow

### Handover SLA (Service Level Agreement)

**Marketing SLA to Sales:**
- Handover packet delivered by end of business day
- All data current as of that morning

**Sales SLA to Marketing:**
- Sales reviews and responds within 48 hours
- Response includes: ACCEPT or REJECT
- If REJECT, sales provides reason code (see rejection codes below)

### Sales Acceptance Workflow

When sales receives a handover:

```
STEP 1: SALES REVIEWS HANDOVER PACKET (within 24 hours)
        ↓
STEP 2: DECIDE: ACCEPT or REJECT?
        ↓
        ACCEPT PATH                     REJECT PATH
        ↓                               ↓
STEP 3: Create opportunity             Provide rejection reason code
        Assign AE                       (see table below)
        Log in CRM
        ↓
STEP 4: AE reaches out within 3 days   Marketing analyses feedback
        (typically within 48h)          Re-engages account or updates
        ↓                               criteria
STEP 5: Log first AE activity
        (call / meeting / email)
        Mark as "in sales process"
```

### Sales Rejection Reason Codes

When sales rejects a handover, they select a reason code. This feedback loops back to marketing and informs process adjustment.

```
CODE          REASON                         MARKETING ACTION
──────────────────────────────────────────────────────────────────────────────
ICP_UNFIT     Company does not match ICP.    Remove from TAM list immediately.
              Size, industry, geography,     Audit how they got added.
              or use case mismatch.

BG_GAP        Critical buying group role     Prospect for missing role.
              missing (esp. economic buyer   Re-engage if found.
              if they are not responding).

LOW_INTENT    No recent engagement. Signals  Re-nurture or recycle to next
              are stale (>30 days old).      quarter. Check for signal
              Timing is off.                 capture issues.

BAD_TIMING    Account is real but not        Park in nurture. Requeue for
              buying now. Evaluating for     Q4 or next year.
              next year or other timeline.

DUPLICATE     Account already has open       Remove from ABM list. Merge
              opportunity or sales activity. buying group into existing
                                             opportunity in sales system.

WRONG_PERSON  Primary contact identified is  Find new champion. Prospect for
              not a real decision-maker.     different contact. Re-engage.
              No authority to move forward.

PROSPECT_      Account already owned by       Remove from marketing list.
CONFLICT       sales. AE has active eval.    Note: no double-work.
                                             Inform sales of new buying
                                             group members identified.
```

**Track rejection patterns quarterly:**
- If >50% rejected for "Low Intent": your engagement score threshold is too low
- If >50% rejected for "BG Gap": your prospecting/identification process is weak
- If >50% rejected for "ICP Unfit": your TAM definition needs revision
- Healthy rejection rate: 40-60% (some accounts need more nurture, some are poor fits)

## Persistent Rejection and Re-Qualification

If an account has been handed to sales and rejected twice, that account requires explicit re-qualification before a third handover.

### Persistent Rejection Workflow

```
ATTEMPT 1: Hand to sales
           ↓
           ACCEPT → Into sales pipeline
           REJECT → Feedback collected, re-engage per reason code
           ↓
ATTEMPT 2: (After 60 days of continued engagement)
           Re-assess engagement score and buying group
           Hand to sales again
           ↓
           ACCEPT → Into sales pipeline
           REJECT → STOP. Do not hand again.
           ↓
ATTEMPT 3: (ONLY with explicit conditions)
           Can hand again if:
           - Engagement score has risen >50 points since last rejection
           - A new champion has been identified
           - A critical event has occurred
           - Buying group coverage has improved >25%
           - Sales confirms they will actively pursue (not auto-reject)
           ↓
           Hand with explicit caveat: "We heard feedback. Here's what changed."
```

### Re-Qualification Criteria (Before Attempt 3)

```
METRIC                              BEFORE REJECTION    AFTER RE-ENGAGEMENT    CHANGE
──────────────────────────────────────────────────────────────────────────────────────
Engagement Score                    95                  150                    +58%
Buying Group Coverage               55%                 75%                    +20%
Champion Status                     None identified     Mark Johnson (CTO)     NEW
Critical Events                     1 (demo req)        3 (demo + meeting +    +2
                                                        proposal req)
Last Signal Date                    45 days old         2 days old             Recent
```

If re-qualified account meets >3 of the above changes, handover is warranted.

## Special Cases and Exceptions

### Exception 1: Multiple Contacts from Same Account

If two different people from the same account meet handover criteria independently, treat as ONE account handover, not two.

**Action:**
1. Merge buying group info into one handover packet
2. Highlight that multiple people are engaged (positive signal)
3. Hand as single account to one AE
4. Recommend AE loop both contacts into first conversation

### Exception 2: Account Already in Sales Pipeline

If sales already has an open opportunity at the account, do NOT hand separately.

**Action:**
1. Identify the existing opportunity owner (AE name)
2. Send handover packet directly to that AE (not to sales manager)
3. Packet includes: "New buying group members identified: [names]. Recommend you loop them in."
4. Log in CRM as "buying group expansion" or "multi-threading support"
5. Do NOT create a competing opportunity

### Exception 3: Account with Declined Champion

If the identified champion explicitly declines to help or leaves the company, do NOT hand immediately.

**Action:**
1. Re-assess account without that champion
2. If engagement score drops >50 points, recycle to nurture
3. If score remains healthy via other contacts, identify new champion before handing
4. Add to handover packet: "Prior champion [name] is no longer at company. New champion prospect: [name]. May need AE to validate."

### Exception 4: Super-Hot Account (Score >200)

If an account reaches 200+ engagement points with multiple critical events clustered, handover immediately regardless of normal gates.

**Action:**
1. Escalate to Sales Director (do not wait for manager review)
2. Provide raw handover packet (even if buying group incomplete)
3. Recommend AE calls immediately (same day)
4. Packet note: "This account is in-market NOW. Buying group not yet complete; recommend AE drives buying committee discovery."

---

## Handover Measurement and Feedback Loop

### Metrics to Track (Post-Handover)

```
METRIC                             CALCULATION                HEALTHY BENCHMARK
──────────────────────────────────────────────────────────────────────────────
Handover Acceptance Rate           Accounts accepted by sales   60-75%
                                   / accounts handed

Handover-to-Opportunity            (Opportunities created from  60-80% (within
Conversion Rate                    handed accounts) / (accounts 90 days)
                                   handed)

Time to Opportunity                Days from handover to        <30 days
                                   opportunity creation
                                   (median)

Opportunity-to-Close Rate          (Closed-won from handed)     20-40% (depends
(ABM Attribution)                  / (opportunities from        on stage at
                                   handed accounts)             handover)

Win Rate (ABM-influenced)          Closed-won from ABM          15-30% (typically
                                   accounts / pipeline from     higher than
                                   ABM accounts                 non-ABM)

Average Deal Size (ABM)            Revenue from ABM-sourced    Compare to
                                   closed-won accounts         non-ABM baseline

Handover Quality Score             (Acceptance rate × Opp       >65 indicates
                                   conversion) / 100            good discipline
```

### Monthly Handover Report

```
METRIC                              JULY    Q2 AVG   TREND
────────────────────────────────────────────────────────────
Accounts handed                     18      15       ↑
Accounts accepted by sales          16      12       ↑
Acceptance rate                     89%     80%      ↑
Accounts creating opportunities     12      9        ↑
Opp conversion rate                 75%     75%      =
Avg time to opp                     18d     22d      ↑ (faster)
Accounts closing won (YTD)          2       n/a        (trailing)
ABM-sourced pipeline (YTD)          €2.4M   n/a        
```

### Feedback Loop Cadence

**Monthly (Marketing Ops + Sales Leadership):**
- Review handover acceptance rates
- Analyse rejection reason codes
- Adjust threshold if needed

**Quarterly (Executive):
- ABM-sourced pipeline and revenue
- Handover quality trends
- ABM efficiency metrics vs. other go-to-market motions

---

## Source Attribution

Handover doctrine framework adapted from:
- 6sense Account Qualification and Handover Model (2026)
- Demandbase Account Progression Framework (2024)
- Kristina Jaramillo Personal ABM Handoff Methodology (PersonalABM; 2024-2025)
- Sales Enablement Society: Marketing-to-Sales Handoff Best Practices (2025)
- Practitioner case studies from Neon Triforce ABM implementations (2025-2026)
