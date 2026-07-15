# Account Engagement Scoring Model

## Building Your Engagement Score

An account engagement score is a composite of first-party signals (your own data) and third-party signals (external intent), weighted by relevance and decayed by recency. The score answers: "How confident am I that this account is in active buying mode right now?"

## Signal Inventory and Baseline Weights

The baseline signal weights below assume a B2B enterprise software buying cycle of 90-180 days, with 5-person buying committees. Adjust for your product, deal size, and buying cycle.

### First-Party Signals (Direct Engagement)

```
SIGNAL TYPE                        BASE WEIGHT  RECENCY DECAY    NOTES
───────────────────────────────────────────────────────────────────────
Website Visit (any page)           1 point      Weekly (50%)      High volume; lightweight
Pricing/ROI page visit             10 points    Monthly (75%)     Strong purchase intent
Demo request form submission       15 points    Persistent        Explicit milestone
Meeting scheduled/attended         20 points    Persistent        Critical confirmation
Case study / whitepaper download   5 points     Weekly (60%)      Consideration signal
Webinar registration               3 points     Persistent        Passive interest
Webinar attendance                 5 points     Weekly (60%)      Passive engagement
Free trial signup                  12 points    Persistent        Product engagement
Free trial login (weekly)          2 points     Weekly (70%)      Continued interest
Email open (not click)             0.5 points   Not counted       Too much noise
Email click (link click)           2 points     Weekly (60%)      Interest signal
Email reply / message sent         10 points    Persistent        Intent confirmation
LinkedIn message reply             3 points     Weekly (60%)      Relationship signal
LinkedIn profile view              1 point      Weekly (40%)      Very passive
Comment on company post            2 points     Weekly (50%)      Engagement
Product review submission          8 points     Persistent        Opinion leadership
ROI calculator usage               7 points     Weekly (65%)      Consideration phase
```

### Third-Party Intent Signals (External Data)

```
SIGNAL TYPE                        BASE WEIGHT  RECENCY DECAY    NOTES
───────────────────────────────────────────────────────────────────────
Bombora/similar co-op intent spike 8 points     Monthly (80%)     Buying signal (Bombora
                                                                  company research activity)
Technographics stack change        5 points     Monthly (85%)     Technical shift detected
(e.g. new tool deployed)
Job posting (hiring tech role)     3 points     Monthly (70%)     Team expansion signal
News mention (funding, M&A)        5 points     Monthly (75%)     Business event
Press release mentioning problem   5 points     Monthly (75%)     Market problem awareness
  (e.g. security breach, outage)
Analyst mention (Gartner, IDC)     2 points     Persistent        Third-party validation
Stock movement / earnings (>10%)   2 points     Monthly (80%)     Financial event
LinkedIn job change (CFO/CIO hired) 4 points    Monthly (70%)     Stakeholder change
```

### Advertising and Campaign Signals

```
SIGNAL TYPE                        BASE WEIGHT  RECENCY DECAY    NOTES
───────────────────────────────────────────────────────────────────────
Ad impression (display, LinkedIn)  0.2 points   Weekly (40%)      Volume noise; minimise
Ad click                           1 point      Weekly (50%)      Mild interest
Landing page visit (post-ad)       2 points     Weekly (60%)      Engaged visitor
Retargeting ad interaction         1 point      Weekly (55%)      Repeated interest
Email campaign click (direct mail) 3 points     Weekly (65%)      Campaign engagement
Webinar ad conversion              5 points     Weekly (65%)      Leads to event
Content gate (form fill)           6 points     Weekly (65%)      Explicit opt-in
Survey response                    4 points     Weekly (70%)      Opinion provided
Event attendance (in-person)       10 points    Persistent        High engagement
Event booth visit                  3 points     Weekly (65%)      Passive event interest
```

## Recency Decay Schedule and Implementation

Signals do not disappear; they decay on a schedule. This prevents old breadcrumb activity from inflating current scores while preserving momentum signals.

### Decay Rules

**Persistent signals** (meetings, demo requests, replies, free trial usage, major events) never decay. They remain active until the account is explicitly recycled back to an earlier stage.

**High-recency signals** (website visits, email clicks, ad engagement) decay weekly at a rate between 40-60%.

**Medium-recency signals** (case study downloads, webinar attendance, news mentions) decay monthly at a rate between 70-85%.

### Decay Formula

```
Score_new_period = Score_previous_period × Decay_factor

Example:
Day 1: Account views pricing page (10 points)
Score on Day 1: 10 points

Day 8 (one week later, monthly 75% decay):
Score on Day 8: 10 × 0.75 = 7.5 points

Day 15 (two weeks later):
Score on Day 15: 7.5 × 0.75 = 5.6 points

Day 90 (thirteen weeks later):
Score on Day 90: ~0.2 points (effectively expired)
```

### Implementation Window

Use a rolling 90-day window for all scores. Signals older than 90 days drop off automatically. This prevents year-old activity from cluttering the score while preserving recent momentum.

## Account Engagement Score Thresholds and Interpretation

After all signals are summed and decay is applied, the total engagement score maps to account stage and readiness:

```
SCORE RANGE        ACCOUNT STAGE      INTERPRETATION & NEXT STEP
─────────────────────────────────────────────────────────────────────────
0-25               Watchlist          Account is on TAM list but shows minimal
                                      engagement. Marketing continues nurture
                                      cadence (monthly newsletter, ads). No sales
                                      outreach yet.

26-50              Aware              Early engagement detected (website visit,
                                      content download, email click). Buying group
                                      is unknown. Continue targeted nurture.
                                      Assign task: identify and reach Economic
                                      Buyer.

51-100             Engaged            Multiple engagement signals or one critical
                                      event (meeting request, demo request).
                                      Buying group may be partially visible.
                                      NOT yet ready for sales. Actions:
                                      (1) If buying group <50%, continue
                                          prospecting for missing roles.
                                      (2) If buying group >=50%, prepare for
                                          handover upon next critical event.
                                      (3) Consider warm AE outreach (not BDR).

101-150            Hot / In-Market    Multiple signals active, OR critical event
                                      occurred. Account is actively researching or
                                      buying. Handover decision based on buying
                                      group coverage:
                                      - If coverage >=50%: HANDOVER to sales
                                        immediately.
                                      - If coverage <50%: Continue buying group
                                        mapping. Reach out to identified contacts
                                        to unlock additional stakeholders.

150+               In-Market / Ready  Account shows multiple critical events
                                      (demo, meeting, proposal request) or very
                                      high engagement. Buying group should be
                                      visible. HANDOVER to sales with high
                                      confidence. AE should have full buying
                                      group map in handover packet.
```

## Stage Multipliers for Prioritisation

When prioritising which accounts to focus on, apply stage multipliers to the raw engagement score. This ensures you allocate resources to the most sales-ready accounts:

```
STAGE              MULTIPLIER   RATIONALE
─────────────────────────────────────────────
Watchlist          × 0.5        Low priority; minimal engagement
Aware              × 0.75       Passive interest; needs nurture
Engaged            × 1.0        Active; requires attention
Hot/In-Market      × 2.0        Sales-ready; highest priority
Handed-to-Sales    × 0.0        Out of marketing measurement
```

**Usage example:**
- Account A: Raw score 85 (Engaged stage) × 1.0 = 85 (priority index)
- Account B: Raw score 110 (Hot stage) × 2.0 = 220 (priority index)
- Account C: Raw score 140 (In-Market stage) × 2.0 = 280 (priority index)

Rank accounts by priority index when assigning nurture resources or deciding which to prioritise for sales outreach support.

## Configuring Engagement Scoring for Your TAM

### Step 1: Validate Your Buying Cycle Length

Your baseline weights assume a 90-180 day buying cycle. If your product has a different cycle, adjust decay rates:

**Shorter cycles (30-60 days, e.g. PLG / SMB tools):**
- Weekly decay rate: 60-70% (signals expire faster)
- Monthly decay rate: 90%+ (preserve only recent activity)
- Critical events trigger handover faster (2-5 days)

**Longer cycles (180-360 days, e.g. enterprise infrastructure):**
- Weekly decay rate: 40-50% (preserve activity longer)
- Monthly decay rate: 70-75% (slower decay)
- Critical events trigger handover slower (14-30 days, allow buying group discovery)

**Very long cycles (360+ days, e.g. mega-deal procurement):**
- Weekly decay rate: 30-40%
- Monthly decay rate: 60-70%
- Consider quarterly refresh of engagement scores instead of weekly

### Step 2: Adjust Weights for Your Deal Type

**High-ticket enterprise (ACV >€500K):**
- Meeting = 25 points (up from 20)
- Demo request = 20 points (up from 15)
- Email reply = 12 points (up from 10)
- Website visit = 0.5 points (down from 1)
- Rationale: High-touch requires explicit stakeholder interactions, not passive browsing

**Mid-market (ACV €50-500K):**
- Use baseline weights as-is
- Demo request = 15-18 points
- Meeting = 18-20 points

**Product-led growth (ACV <€50K):**
- Free trial signup = 15 points (up from 12)
- Free trial login (weekly) = 4 points (up from 2)
- Demo request = 10 points (down; less relevant)
- Website visit = 2 points (up; indicates interest)
- Rationale: Product usage is the primary signal; meetings are secondary

**Vertical / Compliance-heavy (regulated industries):**
- Security/Compliance engagement = 20 points (add new signal)
- Meeting = 25 points (up; longer sales cycle)
- Document review signals (compliance questionnaire, SOC 2 review) = 8 points (add)
- Rationale: Compliance validation is a blocker, not optional

### Step 3: Set Handover Thresholds for Your Team

Base thresholds:
- Handover score gate: >=100 points
- Buying group coverage gate: >=50% of required roles
- Critical event accelerator: Any critical event + Economic Buyer present = handover

**Adjust if:**
- Your sales team is high-volume, BDR-driven: Keep thresholds high (score >=120) to filter for quality
- Your sales team is low-volume, AE-centric: Lower score threshold (>=80) but keep buying group gate strict (>=60%)
- Your product is high-touch: Require both score AND meeting presence (not just score)
- Your product is self-serve: Weight free trial engagement heavily, lower meeting threshold

### Step 4: Validation and Calibration

After 1-2 months of scoring, validate by reverse-engineering from closed-won deals:

**Closed-Won Validation Questions:**
1. What was the average engagement score 60 days before close?
2. What was the average engagement score 30 days before close?
3. Which signal types (demo requests, meetings, etc.) appeared in 80%+ of closed-won accounts?
4. Which signal types appeared in <20% of closed-won accounts? (Remove these from scoring.)
5. What was the average buying group coverage at handover for closed-won deals vs. lost deals?

**Adjust weights upward** for signals that appear in 80%+ of closed-won accounts.
**Adjust weights downward or remove** signals that are noise.
**Adjust thresholds** based on distribution: if 50% of accounts at your handover threshold convert to pipeline, the threshold is right. If <20% convert, raise it. If >80% convert, lower it.

## Implementation: Building Your Scoring System

### Option 1: Manual Monthly Calculation (Spreadsheet)

**Setup (Day 1):**
1. List all 200 (or N) target accounts in Column A
2. Create signal columns for each signal type (website visit, demo request, etc.)
3. Assign base weights as column headers
4. Create a SUM formula to calculate total score per account

**Monthly Update:**
1. Pull engagement data from all sources (GA, CRM, email platform, ad platform, web tracking tool)
2. Populate signal columns with counts or yes/no indicators
3. Apply decay formula to previous month's score
4. Recalculate total score
5. Sort accounts by score; identify movers (up/down >50%)

**Limitation:** Manual, labourious, error-prone at >100 accounts. Suitable for pilots or very small TAMs.

### Option 2: Native Integration (Marketing Automation Platform)

**Setup:**
1. Map each signal type to a CRM contact/account field
2. Build scoring rules in your marketing automation platform (HubSpot, Marketo, Pardot)
3. Set recency decay as automated field refresh (e.g. weekly, monthly)
4. Create score thresholds that trigger tasks or Slack alerts

**Limitation:** Requires paid marketing automation; recency decay logic can be complex to implement.

### Option 3: Third-Party ABM Platform (Recommended for Mature Programmes)

**Option 3a: 6sense, Demandbase, or RollWorks**

These platforms ingest first-party signals (your CRM, website tracking, email, ad platform) and third-party signals (intent data, technographics, news) and calculate engagement scores automatically. By 2026, all major platforms use AI or hybrid ML/AI approaches:

- **6sense:** Predictive buying stage classification with ML-driven anomaly detection in buying group behaviour
- **Demandbase:** Hybrid AI combining engagement signals with firmographic enrichment; automated stakeholder identification via AI
- **RollWorks:** AI-driven account scoring and engagement recommendation engine

Real-time engagement alerts are now standard (fire Slack alerts the moment an account reaches a threshold or critical event triggers). Weekly or monthly batch scoring is increasingly outdated for mature programmes; real-time systems enable faster sales response (within 24 hours of critical event).

**Advantage:** Pre-built buying-stage models, third-party intent integration, automated buying-group detection, AI-driven anomaly detection, real-time alerting.
**Cost:** Typically €50-200K+ annually depending on TAM size.
**Setup time:** 4-8 weeks for integration and configuration.

**Option 3b: Custom Integration (n8n or Zapier)**

Build a workflow that pulls data from all signal sources daily, calculates engagement score using the formula above, and syncs back to your CRM. Use n8n for complex logic, Zapier for simpler integrations.

**Advantage:** Custom logic, low cost (€100-500/month).
**Disadvantage:** Requires technical setup; third-party intent data not included.

## Scoring Model Configuration Worksheet

```
CONFIGURATION ITEM               YOUR VALUE      NOTES
───────────────────────────────────────────────────────────────
Buying Cycle Length              _____ days      30-60 / 90-180 / 180-360 / 360+
Product Category                 __________      SaaS / Infrastructure / Services / PLG
Average Deal Size (ACV)          €xxxxxx
Sales Team Model                 __________      High-touch AE / BDR-driven / Self-serve
Target TAM Size                  _____ accounts

SIGNAL WEIGHT CONFIGURATION
Website visit base weight         _____ points    (Baseline: 1)
Pricing page visit base weight    _____ points    (Baseline: 10)
Demo request base weight          _____ points    (Baseline: 15)
Meeting base weight               _____ points    (Baseline: 20)
Email reply base weight           _____ points    (Baseline: 10)
Free trial signup weight          _____ points    (Baseline: 12)
[Your custom signal]              _____ points

DECAY CONFIGURATION
Website visit weekly decay %      ______%         (Baseline: 50%)
Demo request decay               None / [decay]   (Baseline: None)
Persistent signal decay          None             (No change)
Scoring window                   _____ days      (Baseline: 90)

HANDOVER CONFIGURATION
Handover score threshold          >=_____ points  (Baseline: >=100)
Buying group coverage threshold   >=____%         (Baseline: >=50%)
Critical events list              [custom list]   (See SKILL.md for defaults)

LAUNCH TIMELINE
Baseline scoring setup            [Date]
Pilot accounts (N)                [Date]
Monthly calibration review        [Date]
Full TAM rollout                  [Date]
```

## AI/ML-Driven Engagement Scoring and Automated Buying Group Detection (2026 Adoption)

By 2026, AI and ML approaches are mainstream in ABM platforms. Understanding automation capabilities is important for programme design.

### Predictive Scoring vs. Rules-Based Scoring

**Rules-based scoring** (the manual approach in this guide) uses fixed weights and decay rules. It works well for mature programmes with clear signal patterns.

**ML-driven predictive scoring** learns weights from your closed-won and closed-lost deals. Instead of guessing that a demo request = 15 points, the model observes: "In your business, demo requests from accounts that closed won average 18 engagement signals by close date. Email replies average 3. Pricing page visits average 1.2." It then back-propagates and assigns weights based on actual outcome data.

**6sense (Predictive Buying Stages):** Uses historical buying patterns to classify accounts as Research, Active Evaluation, or Procurement. For each stage, it recommends actions and predicts urgency.

**Demandbase (Hybrid AI):** Combines explicit engagement signals (your first-party data) with implicit signals (firmographic changes, hiring patterns, news) to create engagement confidence scores. Recommends account-level next steps without requiring manual assessment.

### Automated Buying Group Detection

Platforms with AI can detect buying group composition without manual prospecting:

- **Pattern recognition:** When 5 people from Finance and 3 from IT visit your website in a 2-week window, the AI infers they are a buying committee.
- **Recommended next contacts:** "You have identified 2/5 required roles. Our model suggests you reach [name, title] at [account] (predicted 92% likelihood they are involved in buying decisions)."
- **Stakeholder role classification:** AI infers role (Economic Buyer, Technical Buyer, etc.) based on title, department, engagement behaviour, and firmographic fit.

**Confidence levels:** Automated detection is 70-85% accurate depending on data quality. Manual validation remains important for high-stakes handovers.

### When to Use AI/ML vs. Rules-Based Scoring

**Use rules-based (this guide's approach) if:**
- You have <100 accounts (manual process is feasible)
- You have <6 months of closed-deal history (ML model needs training data)
- You need full transparency on scoring logic (rules-based is deterministic; ML is a black box)
- Budget is limited (<€50K/year on platforms)

**Use AI/ML platforms if:**
- You have 200+ accounts and want real-time scoring
- You have 18+ months of closed-deal history (sufficient training data)
- You want predictive insights (which accounts will heat up, which are cooling)
- Your team has bandwidth for platform implementation (4-8 weeks)
- Budget allows €100K-200K annually

### Hybrid Approach (Recommended for Growth)

Start with rules-based scoring to establish discipline and transparency. After 6-12 months, layer in a second-opinion AI model to catch patterns your rules miss. Use both systems in parallel for 30-60 days before fully trusting the AI model.

---

## Troubleshooting Common Scoring Issues

**Issue: All accounts have low scores (0-30).**
- Possible cause: You are not capturing signals (missing GA integration, email tracking off, CRM is empty).
- Fix: Audit signal sources. Confirm data flows to CRM. Add manual entry for known engagement (calls, meetings).

**Issue: Score fluctuates wildly week-to-week.**
- Possible cause: Decay rate is too aggressive, or single high-weight signal (demo request) is dominating.
- Fix: Lower decay rate. Reduce weight on single signals. Add more signal types to smooth variation.

**Issue: High-scoring accounts do not convert to pipeline.**
- Possible cause: Engagement signals do not correlate with buying intent (e.g. researchers downloading content). Buying group coverage is missing.
- Fix: Add buying-group validation as handover gate (do not hand if Economic Buyer is unknown). Reverse-engineer from closed-won deals: which signals appeared before those deals?

**Issue: Salesforce says they never received account data.**
- Possible cause: Integration is broken or not pushing data to CRM.
- Fix: Audit integration logs. Ensure scoring platform is writing to account/contact records. Test one account manually.

---

## Source Attribution

Baseline signal weights and decay methodology adapted from:
- 6sense Predictive Buying Stages Model (2026)
- Demandbase Engagement Minutes Framework (2024)
- Forrester B2B Buying Journey Research (2026)
- Practitioner case studies from client engagements (practice-based) (2025-2026)

Configuration framework based on Kristina Jaramillo's Personal ABM methodology (PersonalABM; host of ABMDoneRight Podcast) and motion-based weighting patterns observed across 50-500 account TAM programmes.
