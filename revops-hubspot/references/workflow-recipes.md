# HubSpot Workflow Recipes - Ready-to-Implement

Production-ready workflow patterns for B2B SaaS RevOps (€15M-150M ARR, Benelux region).

---

## 1. Lead Lifecycle Automation: Lead → MQL → SQL → Opportunity

### Workflow: Auto-MQL on Lead Score Threshold

**Purpose:** Automatically promote leads to MQL status when they meet fit + engagement thresholds.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact property changed: `hs_lead_score` becomes ≥ 60 |
| **Conditions** | • AND `fit_score` ≥ 60<br>• AND `engagement_score` ≥ 40<br>• AND `lifecycleStage` = "Lead" or "Subscriber" |
| **Actions** | 1. Set property: `lifecycleStage` → "MQL"<br>2. Set property: `lead_status` → "Open"<br>3. Create task: Assign to BDR, due in 2 days<br>4. Send notification: Notify lead owner in Slack<br>5. Enroll in workflow: "MQL to SQL Nurture Sequence" |
| **Notes** | • Threshold aligned with marketing-ops lead-scoring-models.md<br>• Triggers BDR contact within 2 days<br>• Prevents duplicate enrollments with "is not already enrolled" check |

### Workflow: Auto-SQL on First Sales Activity

**Purpose:** Promote MQL to SQL when sales rep engages (call, meeting, email).

| Component | Details |
|-----------|---------|
| **Trigger** | Contact property changed: `last_activity_date` occurs |
| **Conditions** | • AND `lifecycleStage` = "MQL"<br>• AND `lead_status` = "Open" or "Working"<br>• AND `days_inactive` < 2 (recent activity)<br>• AND activity type = Email, Call, or Meeting Log |
| **Actions** | 1. Set property: `lifecycleStage` → "SQL"<br>2. Set property: `lead_status` → "Contacted"<br>3. Increment: `num_contacted_notes`<br>4. Create opportunity (if not exists): Deal amount = €0 (TBD)<br>5. Notify: Slack alert to sales manager<br>6. Add note: "Promoted to SQL - [rep name] engaged on [date]" |
| **Notes** | • Sales qualifies MQL through conversation (MEDDIC/BANT check)<br>• Opportunity created at contact, not yet deal creation<br>• Sales rep populates deal amount, timeline, budget, champion<br>• Prevents spam/accidental promotions with conditions |

### Workflow: Auto-Opportunity Creation on Deal Qualification

**Purpose:** Create formal sales opportunity when SQL is fully qualified.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact property changed: `deal_qualification_method` is set |
| **Conditions** | • AND `lifecycleStage` = "SQL"<br>• AND `budget_confirmed` = true<br>• AND `timeline_confirmed` = true<br>• AND `decision_process_understood` = true<br>• AND NO opportunity already associated |
| **Actions** | 1. Create deal: Associated to contact + company<br>2. Set deal stage: "Qualification"<br>3. Set deal amount: Copy from estimated_annual_value (if exists)<br>4. Assign deal owner: Inherit from contact owner<br>5. Set probability: 20% (for Qualification stage)<br>6. Set closedate: 90 days out (default)<br>7. Create task: Sales rep to schedule discovery call<br>8. Enroll: "Deal Progression Automation" workflow<br>9. Send email: Qualified opportunity notification to AE team |
| **Notes** | • Requires sales rep to confirm MEDDIC elements before trigger<br>• Amount pulled from estimated value, updated later in deal stage<br>• Closedate is estimate; updated as deal progresses<br>• Prevents duplicate opportunities with "no associated deals" check |

---

## 2. Lead Routing Workflows

### Workflow: Territory-Based Routing

**Purpose:** Auto-assign leads to AEs based on company location/industry.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact created or Lead status property changes to "Open" |
| **Conditions** | • `lifecycleStage` = "MQL"<br>• Contact does not have an owner assigned<br>• `company.country` = "Netherlands" OR "Belgium" OR "Germany" |
| **Actions** | **Route by Territory + Company Size:**<br><br>**Netherlands:**<br>1. IF `company.country` = "Netherlands"<br>   - Assign to: AE1 (Primary territory)<br>   - Create task: "Netherlands - First contact in 48 hours"<br><br>**Belgium:**<br>1. IF `company.country` = "Belgium"<br>   - Assign to: AE2 (Primary territory)<br>   - Create task: "Belgium - First contact in 48 hours"<br><br>**Germany:**<br>1. IF `company.country` = "Germany"<br>   - Assign to: AE3 (Primary territory)<br>   - Create task: "Germany - First contact in 48 hours"<br><br>**All Routes:**<br>• Set property: `owner_assigned_date` → Today<br>• Send email: Welcome email to assigned rep<br>• Send notification: Slack to regional manager |
| **Notes** | • Assumes 3 AEs covering Benelux + Germany<br>• Customize territory definitions per org<br>• Prevents double-assignment with "does not have owner" condition<br>• Escalation: If no assignment in 72 hours, notify manager |

### Workflow: Round-Robin Lead Assignment

**Purpose:** Distribute new MQLs equally across available AEs (capacity-based).

| Component | Details |
|-----------|---------|
| **Trigger** | Contact property changed: `lifecycleStage` → "MQL" |
| **Conditions** | • Contact owner = empty (unassigned)<br>• `company.industry` = target industries (SaaS, FinTech, MarTech, etc.)<br>• `arr_eur` between €15M-150M (ICP match) |
| **Actions** | **Round-Robin Assignment:**<br>1. Get list of active AEs: [AE1, AE2, AE3, AE4]<br>2. Count open MQLs for each AE (must be < 20)<br>3. Assign to AE with lowest count<br>4. Set property: `owner` → Assigned AE<br>5. Set property: `owner_assigned_date` → Today<br>6. Create task: "Welcome call - Introduce yourself, 48 hour target"<br>7. Send Slack: Notify AE with MQL card<br>8. Send email: Auto-confirmation to contact (CRM automation)<br><br>**If all AEs at capacity:**<br>• Hold in queue (wait 24 hours)<br>• Retry assignment (workflow logic)<br>• If still no capacity: Notify sales manager |
| **Notes** | • "Open" = currently has <20 active leads<br>• Capacity check prevents overloading<br>• Round-robin rotates per MQL received<br>• Manual override: sales manager can reassign |

### Workflow: Capacity-Based Lead Routing (Alternative)

**Purpose:** Route new MQLs to AEs with lowest pipeline/opportunity count.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact property changed: `lifecycleStage` → "MQL" |
| **Conditions** | • Contact owner = empty<br>• `icp_match_status` = "Perfect Fit" OR "Good Fit"<br>• Company not already in account management |
| **Actions** | **Capacity Check:**<br>1. Calculate for each AE:<br>   - Open opportunities count (dealstage ≠ Closed)<br>   - MQL assignments in last 7 days<br>   - Total pipeline value (EUR)<br>2. Assign to AE with:<br>   - Lowest open opportunity count (target: <15)<br>   - AND lowest pipeline value (enables growth)<br>3. Set property: `owner` → Selected AE<br>4. Create task: Assigned AE → "Reach out within 24 hours"<br>5. Notify: Assigned AE via Slack + email<br>6. Set priority: High (red flag) if AE at max capacity |
| **Notes** | • Prevents BDRs from overloading AEs<br>• Capacity measured by opportunities, not just count<br>• Helps junior AEs build pipeline at sustainable pace<br>• High-value leads routed first |

---

## 3. Deal Stage Automation

### Workflow: Auto-Create Tasks on Deal Stage Change

**Purpose:** Ensure sales team follows process by auto-creating next-step tasks per stage.

| Component | Details |
|-----------|---------|
| **Trigger** | Deal property changed: `dealstage` changes |
| **Conditions** | Trigger on any stage change |
| **Actions** | **Stage: Qualification**<br>• Create task: "Schedule discovery call" (due in 3 days)<br>• Create task: "Document MEDDIC elements" (due in 5 days)<br>• Set property: `next_step` → "Discovery call scheduled"<br>• Expected close: 45-60 days out<br><br>**Stage: Proposal**<br>• Create task: "Send proposal" (due in 1 day)<br>• Create task: "Schedule proposal review" (due in 5 days)<br>• Create task: "Get champion internal approval" (due in 7 days)<br>• Set property: `next_step` → "Awaiting proposal acceptance"<br>• Expected close: 30-45 days out<br><br>**Stage: Contract/Negotiation**<br>• Create task: "Send contract via e-sign" (due in 1 day)<br>• Create task: "Follow up on signature" (due in 5 days)<br>• Create task: "Prepare onboarding" (due in 10 days)<br>• Set property: `next_step` → "Awaiting legal signature"<br>• Expected close: 7-14 days out<br><br>**Stage: Closed Won**<br>• Create task: "CS - Schedule kickoff" (due in 1 day)<br>• Create task: "Create renewal reminder" (recurring, 11 months)<br>• Set property: `lifecycleStage` → "Customer" (on contact)<br>• Send email: Sales + CS team (deal won notification)<br>• Create renewal record (custom workflow or manual)<br><br>**Stage: Closed Lost**<br>• Create task: "Document loss reason" (due in 1 day)<br>• Create task: "Follow up in 6 months" (due in 180 days)<br>• Set property: `lifecycleStage` → "Evangelist" or back to "SQL" (if pursuing)<br>• Send email: Sales leadership (loss analysis) |
| **Notes** | • Tasks auto-assign to deal owner<br>• Keeps deals moving; prevents stalls<br>• Customize task templates per AE preference<br>• Prevent task spam: Check "not already task" condition |

### Workflow: Deal Escalation on Stall

**Purpose:** Alert manager when deal stalls (no activity) for >7 days.

| Component | Details |
|-----------|---------|
| **Trigger** | Workflow timer: Daily check |
| **Conditions** | • Deal stage = "Qualification" OR "Proposal" OR "Contract"<br>• Days inactive > 7<br>• Deal amount ≥ €50k (escalate high-value only)<br>• Deal owner assigned |
| **Actions** | 1. Create task: Deal owner → "Stalled deal - Check in with buyer" (due in 1 day)<br>2. Notify: Sales manager via Slack (escalation)<br>3. Alert email: "Deal [name] inactive 7+ days"<br>4. Add note: "Auto-escalated [date] - No activity since [last_date]"<br>5. Recommendation: Call/email buyer + check if still interested<br>6. If no response in 3 days: Move to "On Hold" pipeline OR close as "No Decision" |
| **Notes** | • Only escalates significant deals (€50k+)<br>• Prevents deals from dying in pipeline<br>• Gives AE 3 days to respond before closure<br>• Customizable: Change threshold for your team |

---

## 4. Re-Engagement Workflows

### Workflow: Stale Lead Re-Engagement

**Purpose:** Re-nurture leads that haven't engaged in 30+ days.

| Component | Details |
|-----------|---------|
| **Trigger** | Workflow timer: Weekly (check every Monday) |
| **Conditions** | • `lifecycleStage` = "MQL" OR "SQL"<br>• `days_inactive` ≥ 30<br>• Last email open > 30 days ago<br>• NOT recently unsubscribed |
| **Actions** | **Automated Re-Engagement Sequence:**<br>1. Send email: "We miss you - Here's what's new" (personalized)<br>2. Wait: 3 days<br>3. If no open: Send follow-up (different subject)<br>4. Wait: 5 days<br>5. If no engagement after 3 emails: Create task<br>   - Task: Sales rep → "Reach out by phone" (due in 2 days)<br>   - Set property: `re_engagement_sequence_enrolled` = true<br><br>**If Engagement Detected:**<br>• Increment: `engagement_score` + 10 points<br>• Recalculate MQL status<br>• If newly qualified: Route to AE (per routing workflow)<br>• Send notification: Marketing team (lead re-activated)<br><br>**If No Engagement After 60 Days:**<br>• Unenroll from nurture sequence<br>• Move to "Nurture" list (lower priority)<br>• Set property: `lifecycleStage` → "Subscriber"<br>• Keep in CRM for future re-targeting |
| **Notes** | • Prevents false negatives (stale doesn't = uninterested)<br>• Sales touch adds human element<br>• Email sequence should be valuable, not salesy<br>• Segment by interest (recent webinar attendee, download recent content, etc.) |

### Workflow: Stalled Deal Recovery

**Purpose:** Re-engage buyers when deal stalls for 14+ days in middle stages.

| Component | Details |
|-----------|---------|
| **Trigger** | Workflow timer: Daily check |
| **Conditions** | • Deal stage = "Qualification" OR "Proposal"<br>• `days_inactive` ≥ 14<br>• Deal amount ≥ €30k<br>• Deal not marked as "On Hold"<br>• Last contact was sales activity (call/meeting/email) |
| **Actions** | **Day 14 (First Alert):**<br>1. Create task: AE → "Reach out to champion" (due in 1 day)<br>2. Send Slack: AE reminder<br>3. Suggest action: "Follow up on proposal" OR "Check on internal approval"<br><br>**Day 21 (Escalation):**<br>1. If no response: Create task<br>   - Task: Sales manager → "Discuss deal strategy" (due in 1 day)<br>2. Notify: Sales director<br>3. Recommendation: Likely stalled, consider "On Hold"<br><br>**Day 30 (Final):**<br>1. If still no activity:<br>   - Move to: `dealstage` = "On Hold" OR close as "No Decision"<br>   - Set property: `stalled_deal_date` = [date]<br>   - Create task: Follow-up in 60 days<br>2. Document: "Buyer not responsive; paused outreach" |
| **Notes** | • Timings: 14, 21, 30 days (customize per company)<br>• Escalation ensures visibility<br>• "On Hold" vs "Closed Lost": Manager judgment call<br>• Can re-open deal if buyer reaches out |

---

## 5. Data Hygiene Workflows

### Workflow: Fill Missing Firmographic Data

**Purpose:** Append missing company/contact data to improve lead quality.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact created |
| **Conditions** | • Email domain exists<br>• Company property = empty OR domain doesn't match email<br>• NOT a bounced/invalid email<br>• `do_not_contact` = false |
| **Actions** | 1. **Lookup & Auto-Populate:**<br>   - Use Clearbit/Apollo/similar integration<br>   - Find company by email domain<br>   - Auto-populate: Company name, industry, size, location<br><br>2. **Enrich Contact:**<br>   - Find contact title, phone, LinkedIn URL<br>   - Auto-populate: Job title, phone number<br><br>3. **Create Contact Association:**<br>   - Link contact to company<br>   - If company doesn't exist in HubSpot: Create it<br><br>4. **Scoring:**<br>   - Calc fit_score based on new data<br>   - If score ≥ 60: Set as lead candidate<br><br>5. **QA:**<br>   - Create task: "Review auto-enriched data" (for BDR)<br>   - Flag high-confidence data vs. lower-confidence<br>   - Manual correction if needed<br>   - Set property: `data_enrichment_date` = Today |
| **Notes** | • Requires third-party enrichment tool integration<br>• Only use high-confidence data (80%+ match)<br>• Flag lower-confidence fields for manual review<br>• Prevents bad data from skewing scoring<br>• Cost: Track enrichment API usage |

### Workflow: Standardize Industry & Company Size

**Purpose:** Ensure consistent data format for reporting accuracy.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact created OR company property changed: `industry` |
| **Conditions** | • `industry` field populated<br>• Value not in standardized list<br>• Example: "SaaS" vs "Software as a Service" vs "saas" |
| **Actions** | 1. **Standardize Values:**<br>   - IF industry CONTAINS "saas" OR "software" (case-insensitive)<br>     - Set to: "SaaS"<br>   - IF industry CONTAINS "finance" OR "banking"<br>     - Set to: "FinTech"<br>   - IF industry CONTAINS "marketing" OR "advertising"<br>     - Set to: "MarTech"<br>   - (etc. for all target verticals)<br><br>2. **Standardize Company Size:**<br>   - IF `numberofemployees` = empty BUT `annualrevenue` populated<br>     - Estimate employees from revenue (use benchmark rules)<br>   - IF multiple size indicators conflict: Flag for manual review<br><br>3. **QA Flag:**<br>   - If automation made change: Create task → "Verify auto-standardized data"<br>   - Note: "Auto-standardized from [original value]"<br>   - Allow sales to override if incorrect |
| **Notes** | • Prevents duplicate/similar values from breaking reports<br>• Use lookup table for standardization rules<br>• Document mappings (SaaS includes "Cloud Software", etc.)<br>• Review quarterly as new variations appear |

### Workflow: Duplicate Detection & Merge

**Purpose:** Identify and merge duplicate contacts/companies.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact created |
| **Conditions** | • Email exists<br>• Company exists (either provided or enriched)<br>• Check: Email OR (First + Last name + Company) already in CRM |
| **Actions** | **If Exact Match Found:**<br>1. Flag: Create task → "Possible duplicate - Review and merge"<br>2. Notify: Data ops team or BDR<br>3. Provide: Link to existing record + comparison<br><br>**If Duplicate Confirmed:**<br>1. Merge: Use HubSpot merge tool<br>   - Primary record: The one with more activity<br>   - Secondary: Archive<br>2. Consolidate: History, notes, deal associations<br>3. Update: All associations to point to primary<br><br>**After Merge:**<br>1. Create task: "Update sales notes with merged record"<br>2. Notify: Sales team (avoid orphaned deals)<br>3. Document: Why merged (duplicate email, etc.) |
| **Notes** | • Run automated duplicate check weekly<br>• Don't auto-merge; always require human confirmation<br>• Risk: Merging loses deal history; use care<br>• Cleanup helps: Accurate reporting, no duplicate follow-ups |

---

## 6. Renewal & Expansion Trigger Workflows

### Workflow: Renewal Reminder (Recurring)

**Purpose:** Alert account managers/CSM before contract renewal with enough lead time.

| Component | Details |
|-----------|---------|
| **Trigger** | Contact property changed: `contract_renewal_month` = next month |
| **Conditions** | • `lifecycleStage` = "Customer"<br>• Contact has associated deal (Closed Won)<br>• Deal age ≥ 1 month (exclude new customers) |
| **Actions** | **60 Days Before Renewal:**<br>1. Create task: CSM → "Initiate renewal conversation" (due in 5 days)<br>2. Create task: AE → "Review renewal terms, prepare quote" (due in 10 days)<br>3. Send email: CSM reminder<br>4. Set property: `renewal_initiated_date` = Today<br><br>**45 Days Before Renewal:**<br>1. If no response: Create follow-up task<br>2. Notify: Sales director (flag for attention)<br><br>**30 Days Before Renewal:**<br>1. Check: Renewal amount set? Quote sent?<br>2. If not: Escalate to manager<br><br>**At Renewal:**<br>1. Create new deal: `dealtype` = "Renewal"<br>2. Copy: Previous deal amount (adjusted for expansion)<br>3. Set closedate: Contract end date<br>4. Assign: To CSM/renewal AE<br><br>**After Renewal:**<br>1. If won: Update contract_renewal_month for next year<br>2. If lost: Set lifecycleStage → "Churned" |
| **Notes** | • Customize timing per company (some prefer 90-day notice)<br>• CSM + AE collaboration needed<br>• Expansion upsell opportunity: Included in renewal conversation<br>• Set up before customer onboarding |

### Workflow: Expansion Opportunity Trigger

**Purpose:** Identify and create expansion opportunities for growing customers.

| Component | Details |
|-----------|---------|
| **Trigger** | Deal property changed: `dealstage` → "Closed Won" |
| **Conditions** | • Deal is new business (not renewal)<br>• Customer was land-and-expand strategy<br>• Deal closed in last 90 days |
| **Actions** | 1. **Post-Sales Handoff:**<br>   - Send email: CSM + Account Manager (closed deal notification)<br>   - Create task: CSM → "Schedule onboarding" (due in 1 day)<br><br>2. **Monitor Usage (automated via integration, or manual):**<br>   - After 30 days: Check product usage metrics<br>   - IF high engagement (80%+ feature adoption): Flag expansion candidate<br>   - Recommend: Add users, upgrade tier, additional modules<br><br>3. **Create Expansion Opportunity:**<br>   - On day 45 post-close:<br>   - Create deal: `dealtype` = "Expansion"<br>   - Deal name: "[Customer] - Expansion: [Module/Tier]"<br>   - Amount: €0 initially (CSM to estimate)<br>   - Stage: "Proposal" (CSM identifies specific product fit)<br>   - Owner: CSM → present to customer → handoff to AE when ready to close<br><br>4. **Expansion Nurture:**<br>   - Create task: CSM → "Discuss expansion opportunity" (due in 60 days)<br>   - Suggest: New user seats, add-on modules, premium tier<br>   - Provide: ROI analysis based on usage |
| **Notes** | • Expansion drives ARR growth post-land<br>• CSM + AE partnership: CSM identifies, AE closes<br>• Usage data integration critical (product analytics)<br>• Set ARR growth targets per renewal + expansion |

---

## Workflow Implementation Checklist

- [ ] Test each workflow in sandbox environment first
- [ ] Define all custom properties needed (reference: property-catalog.md)
- [ ] Train sales + marketing teams on workflow triggers
- [ ] Set up Slack notifications for key handoffs (MQL to AE, deal escalation)
- [ ] Document workflow logic in team playbook
- [ ] Create monthly audit: Check for workflow failures, task completion rates
- [ ] Set success metrics per workflow (e.g., MQL routing time < 24 hours)
- [ ] Review and update quarterly as team processes evolve
- [ ] Archive old/unused workflows to avoid clutter
- [ ] Monitor API/action limits (avoid throttling)

---

## Quick Reference: When to Use Each Workflow

| Workflow | When to Enable | Owner | Key Metric |
|----------|---|---|---|
| Lead Lifecycle Auto-Promotion | Day 1 (foundation) | Marketing Ops | MQL time < 48 hours |
| Territory Routing | Day 1 | Sales Ops | Routing time < 4 hours |
| Deal Stage Tasks | Week 1 | Sales Ops | Task completion 90%+ |
| Stale Lead Re-Engagement | Week 2 | Marketing | Re-engagement rate 20%+ |
| Data Enrichment | Week 3 | Marketing Ops | Data completeness 85%+ |
| Renewal Triggers | Month 3 (post-first-customer) | Revenue Ops | Renewal rate 90%+ |
| Expansion Opportunities | Month 3 (post-first-customer) | RevOps | Expansion rate 30%+ |
