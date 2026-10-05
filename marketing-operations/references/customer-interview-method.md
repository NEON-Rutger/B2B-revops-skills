# Customer Interview Method

On-demand reference for the marketing-operations skill. The structured customer interview process that produces the verbatim language, pain priorities and decision criteria that feed lead scoring and campaign targeting. Kept here so this skill runs on its own; the same method also appears in the icp-builder skill, where it feeds ICP and persona building.

## Customer Interview Pipeline

Customer interviews are your **foundational GTM layer**. Here's how to turn them into SPICED ICP + positioning:

### Step 1: Select & Prepare
- Analyze your best customers (use Step 1 above)
- Select 10-20 for interview (start with 5-10 if early stage)
- Create invitation collateral: brief email, calendar hold, incentive (gift card, exec brief)
- Target: 5-20 scheduled interviews on your calendar

### Step 2: Gather Data & Prepare for Interview
- Pull from CRM: deal notes, emails, onboarding trail, customer health score
- Request: RFPs they submitted, procurement notes, contract negotiation emails
- If available: obtain call recordings (sales calls, onboarding, training)
- Load all into an LLM or research doc
- **Create account overview:** 1-page summary of who they are, why they bought, what they're using
- **Create SPICED interview playbook:** 8-10 open-ended questions to guide the conversation

### Step 3: The Interview (8 SPICED Steps)
**Duration:** 30-45 minutes. Record + transcribe.

1. **Open with Safety + Context** (2-3 min)
   - "Thanks for making time. This conversation is confidential."
   - "We're talking with customers to understand how you use [product] and what value you've gotten."
   - "This isn't a sales call; we want to hear what's working and what's not."

2. **Agenda → Check End Time → Confirm Goal** (1 min)
   - State your intent: "We want to capture your story for a case study + internal insights."
   - Confirm their end time: "Do you have until [time]?"

3. **Dive Deep into SITUATION** (5-8 min)
   - "Tell me about your role and what your team does."
   - "What's your organization's growth stage? What's the competitive environment you're in?"
   - "What does your current tech stack look like?"
   - Listen for: company size signals, growth pressure, tech maturity, org structure

4. **Bring Back to the PAIN** (5-8 min)
   - "Before you adopted [product], what was the biggest problem you were facing?"
   - "How was that impacting your business? (speed, cost, compliance, team morale?)"
   - "What had you tried before us?"
   - Listen for: specificity, quantification, emotional weight, previous solutions tried

5. **Get Concrete on IMPLEMENTATION** (5-8 min)
   - "Walk me through how you rolled [product] out. How long did it take?"
   - "Who was the champion? Who else was involved in the decision?"
   - "What surprised you during implementation?"
   - "What would you have done differently?"
   - Listen for: rollout timeline, stakeholder map, friction points, quick wins

6. **Prove the IMPACT** (5-8 min)
   - "What's the concrete value you've gotten? (Cost saved? Time freed? Quality improved?)"
   - "How would you quantify it?"
   - "What would happen if you had to turn it off?"
   - "How's this impacted your career? Your team?"
   - Listen for: quantified ROI, intangible benefits, expansion opportunities

7. **Unpack the CRITICAL EVENT** (3-5 min)
   - "What finally made you decide to move on this? Was there a specific moment or trigger?"
   - "What was the business pressure at that time?"
   - "Who championed the decision internally?"
   - Listen for: trigger type (outage? Board mandate? New hire? Competitive threat?), urgency level

8. **Explore the DECISION** (3-5 min)
   - "Why did you choose us over [competitors / build-in-house]?"
   - "What was the deciding factor?"
   - "What concerns did you have?"
   - Listen for: decision criteria, competitive differentiation, risk reduction

### Step 4: Testimonials
Extract powerful "working with us feels like..." quotes directly in or right after the interview:
- "If you had to describe working with us in one sentence, what would you say?"
- Goal: 1-2 powerful quotes per customer

### Step 5: Quotes & SPICED Extraction
Run the interview transcript through Claude or similar LLM. Use two prompts:

**Prompt 1 (Quotes):**
> "Extract the 5-10 most quotable lines from this customer interview. Focus on lines that illustrate the Situation, Pain, Implementation, Critical Event, or Impact. Format as direct quotes with context."

**Prompt 2 (SPICED Extraction):**
> "Extract and summarize the SPICED framework from this transcript: Situation (their business context when they bought), Pain (specific problem they faced, quantified if possible), Implementation (how they rolled out the solution), Critical Event (what triggered the decision), Decision (why they chose us vs. alternatives). Format as bullet points under each letter."

Use the output for:
- Website testimonials and social proof
- Sales decks and positioning language
- Sharpening your SPICED library with real customer language
- Feeding back into ICP definition and buyer persona refinement

### Step 6: Case Study
If the customer is willing, develop a 1-2 page case study:

**Structure:**
- **Title:** Problem-focused: "How [Company] Reduced [Metric] by X% with [Product]"
- **Introduction:** Who they are, context (industry, scale, role)
- **Challenge:** The SITUATION + PAIN they faced, quantified
- **Solution:** How they implemented your product (their approach)
- **Implementation:** Timeline, stakeholder map, quick wins, learnings
- **Results:** IMPACT, quantified where possible (metrics + testimonial)
- **Quotes:** 2-4 best quotes from interview (threaded through narrative)
- **Closing / Forward Look:** How they're expanding, next priorities, competitive advantage
- **CTA:** "Learn how [product] helped us..." → link to trial / demo / contact

### Step 7: Feed SPICED Back Into ICP & Personas
- Add customer language to your SPICED ICP library
- Update buyer personas with new proof points
- Fill CRM fields: SPICED firmographic, SPICED reason, SPICED champion profile
- Sharpen positioning & messaging based on what resonates

---
