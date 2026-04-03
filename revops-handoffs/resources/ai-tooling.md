# AI Tooling for Revenue Handoffs

Production-ready tools for conversation intelligence, enrichment, predictive models, and handoff automation. Recommendations prioritise tools with native HubSpot integration, verifiable adoption (G2 reviews, recognisable customers), and pricing that fits EU B2B scale-ups at €15–150M ARR.

**Research note**: tool recommendations are validated against independent review platforms (G2, Capterra) and real integration documentation. Where a tool lacks independent validation, this is flagged explicitly.

---

## 1. Conversation Intelligence — The Foundation Layer

The handoff document problem is mostly a **CRM data completeness + conversation intelligence** problem, not a separate product category. Get call summaries into HubSpot automatically, enforce SPICED field completion on deal gates, and the handoff largely assembles itself.

### Tier 1: Free / Budget (€0–25/user/month)

#### Fathom — Recommended default for HubSpot-native teams

| Attribute | Detail |
|---|---|
| **What it does** | Records, transcribes, summarises meetings. Auto-syncs to HubSpot. |
| **HubSpot integration** | Native. Auto-syncs summaries, action items, deal insights to Contact, Company, Deal records. HubSpot cards show last 5 meetings with recording link and summary. Edits re-sync instantly. |
| **Pricing** | Free: unlimited recordings + transcripts + AI summaries (solo). Premium: $19–20/user/month. Team: $19/user/month (CRM sync). Business: $25/user/month (CRM field sync, deal views, coaching, AI scorecards). |
| **Templates** | 15+ including BANT, Sandler. Can be customised for SPICED-adjacent workflows. |
| **Key differentiator** | Records natively — no visible bot joining the call. Clients don't see "Fathom Notetaker" in the participant list. Matters for client-facing calls. |
| **Independent validation** | 4.7/5 on G2 (2,000+ reviews). 500,000+ users. HubSpot developer case study confirms native integration quality. CEO Richard White is a known entity (prev. UserVoice). |
| **Limitations** | No mobile app. Free plan transcripts expire after 90 days. CRM sync requires Team plan or above (free plan limited to 3 users per domain). No conversation analytics (talk ratios, etc.) — it's a notetaker, not a coaching platform. |
| **Handoff use** | Call summaries auto-populate HubSpot deal records. Combined with SPICED stage gates, gives CS 80% of the context they need without manual data entry. |

#### Fireflies.ai — Best for conversation analytics on a budget

| Attribute | Detail |
|---|---|
| **What it does** | Records, transcribes, summarises. Adds conversation intelligence (talk-to-listen ratios, topic tracking, sentiment). |
| **HubSpot integration** | Native. Syncs notes, summaries, action items to Contacts, Companies, Deals. Auto-creates contacts for unknown participants. Can map to specific deal pipeline and stage. |
| **Pricing** | Free: 800 min storage, limited AI credits. Pro: $10/user/month (annual). Business: $19/user/month (annual) — needed for HubSpot integration + team analytics. Enterprise: $39/user/month. |
| **Key differentiator** | Conversation intelligence features (speaker analytics, topic detection, sentiment) at a fraction of Gong's price. 100+ language support. Recent Perplexity AI integration for in-meeting web search. |
| **Independent validation** | 4.5/5 on G2 (500+ reviews). 1M+ companies claimed. $1B+ valuation (2025). |
| **Limitations** | Visible bot joins calls (participant list shows "Fireflies.ai Notetaker"). HubSpot integration requires Business plan ($19/user). AI credit system can be confusing — advanced features consume credits that run out. Accuracy dips with strong accents or noisy calls. |
| **Handoff use** | Same as Fathom for basic sync. Better than Fathom if you want analytics on how reps run discovery calls (talk ratio, question frequency) — useful for coaching and quality assurance. |

#### Fathom vs Fireflies — Decision Framework

| Factor | Fathom | Fireflies |
|---|---|---|
| Client-facing calls (no visible bot) | Winner | Bot visible |
| Conversation analytics / coaching | Basic only | Winner |
| HubSpot native integration quality | Excellent (HubSpot case study) | Good (native) |
| Free tier generosity | Winner (unlimited AI summaries) | 800 min storage, limited credits |
| Team pricing for CRM sync | $19–25/user/month | $19/user/month (Business required) |
| Summary speed | ~30 seconds | 5+ minutes reported |
| Multi-language | Good | 100+ languages |

**Recommendation**: Fathom as default for sales-led HubSpot teams (no bot, faster summaries, tighter HubSpot integration). Fireflies if conversation analytics and coaching metrics are a priority.

### Tier 2: Mid-Market (€40–80/user/month)

#### Avoma

| Attribute | Detail |
|---|---|
| **What it does** | Full meeting lifecycle: agenda, recording, transcription, AI summary, CRM sync, coaching, deal intelligence. |
| **Pricing** | Starter: $19/user/month. Plus: $49/user/month. Business: $79/user/month. Enterprise: $129/user/month. |
| **HubSpot integration** | Native. Bi-directional CRM sync. |
| **Independent validation** | 4.6/5 on G2 (1,000+ reviews). |
| **Best for** | Teams that want structured meeting workflows (agenda to recap) across customer-facing functions, not just transcription. |
| **Handoff use** | More structured than Fathom/Fireflies for the handoff use case because it's designed around the full deal lifecycle. Overkill for teams that just need summaries in HubSpot. |

### Tier 3: Enterprise (€150+/user/month)

#### Gong

| Attribute | Detail |
|---|---|
| **What it does** | Full revenue intelligence: conversation intelligence, deal intelligence, forecast AI, coaching, market intelligence. |
| **Pricing** | ~$250/user/month + platform fee. Typically $50–100K/year minimum. |
| **HubSpot integration** | Native. Deep bi-directional sync. |
| **Independent validation** | 4.8/5 on G2 (6,000+ reviews). Category leader. |
| **AI Briefer** | Generates structured deal summaries from conversations, emails, CRM data. Not a standalone product — you're buying the full platform. |
| **When it makes sense** | €75M+ ARR, 50+ reps, need forecast intelligence + coaching platform + conversation analytics as unified system. |
| **When it doesn't** | €15–50M ARR teams where it's over-engineered and over-priced. |

---

## 2. LLM Middleware for Custom Handoff Documents

For teams that want structured handoff documents on deal stage change — without buying a purpose-built tool. This is the highest-leverage, lowest-cost approach for most EU scale-ups.

### Architecture

```
Deal stage change (HubSpot workflow)
  → Automation platform (Make / n8n / Zapier)
    → Pull: deal properties + SPICED fields + call summaries (from Fathom/Fireflies)
      → LLM (Claude or GPT-4) with structured prompt
        → Output: structured handoff document
          → Push back to: HubSpot note on deal / Google Doc / shared workspace
```

### Cost

~€0.10–0.50 per handoff document (LLM API cost). At 20 handoffs/month: €2–10/month — negligible.

### Prompt Template

```
You are generating a customer handoff document from sales to customer success.

CUSTOMER: {company_name}
DEAL VALUE: {arr_delta}
CONTRACT: {contract_start_date} to {contract_end_date}

SPICED QUALIFICATION:
- Situation: {spiced_situation}
- Pain: {spiced_pain}
- Impact: {spiced_impact}
- Critical Event: {spiced_critical_event} — {spiced_critical_event_detail}
- Decision: {spiced_decision_criteria} | Process: {spiced_decision_process}

STAKEHOLDERS: {stakeholders_list}
BUSINESS GOALS: {business_goals}
TECHNICAL REQUIREMENTS: {technical_notes}
COMPETING SOLUTIONS: {competing_solutions}

RECENT CALL SUMMARIES (from Fathom/Fireflies):
{call_summaries}

Generate a structured handoff document with these sections:
1. Customer Overview (2-3 sentences)
2. Pain & Impact (from SPICED, in customer's words)
3. Success Criteria (measurable, specific)
4. Stakeholder Map (role, influence, attitude)
5. Commitments Log (everything we promised, explicit and implicit)
6. Technical Requirements (integrations, migration, compliance)
7. Risk Flags (what could derail onboarding)
8. Recommended Onboarding Path (based on complexity and goals)
```

### Implementation Notes

- **Trigger**: HubSpot workflow on deal stage = Closed Won (after validation passes)
- **Data pull**: HubSpot API for deal/company/contact properties. Call summaries already in HubSpot via Fathom/Fireflies sync.
- **Output**: HubSpot note on deal, or Google Doc linked to deal
- **Quality gate**: CSM reviews and approves before onboarding kickoff
- **n8n advantage for EU**: self-hosted option, data stays in EU (Frankfurt servers), SOC2 compliant

### Build vs Buy

**Build (LLM middleware)** when: budget is tight, you want full control over format, you already have Make/n8n, SPICED data + call summaries from Fathom/Fireflies is sufficient, GDPR control is paramount.

**Buy a purpose-built tool** when: volume exceeds 50+ handoffs/month, you need audit trail out of the box, multiple handoff types need different templates.

**Note on purpose-built handoff tools** (AskElephant, Handoffs.com, etc.): these dominated search results due to SEO/GEO optimisation. They lack meaningful independent review data (minimal G2 presence, no recognisable customer logos). May be fine products, but insufficient evidence to recommend as defaults. Worth monitoring.

---

## 3. Lead Enrichment & Scoring

### Enrichment Tools

| Tool | Capability | Pricing | G2 Rating | HubSpot |
|---|---|---|---|---|
| **HubSpot Breeze Intelligence** | Reverse-IP intent, enrichment from 200M+ profiles, form shortening | Included (credit-based) | Native | Native |
| **Clay** | 150+ data providers, waterfall enrichment, GPT-4 integration | $149–$800/month | 4.9/5 (200+ reviews) | Via Zapier/native |
| **ZoomInfo** | Contact/company data, org charts, technographics | $15–40K/year | 4.4/5 (8,000+ reviews) | Native |

### Intent Data

| Tool | Capability | Pricing | G2 Rating | Notes |
|---|---|---|---|---|
| **6sense** | Account-level intent, buying stage categorisation | Median $55K/year | 4.3/5 (800+ reviews) | EU deployment available. Overkill below €50M ARR. |
| **Bombora** | B2B content consumption signals | $25–100K/year | 4.1/5 (150+ reviews) | Verify EU data residency. |

### Stack by ARR

- **€15–30M ARR**: HubSpot Breeze Intelligence (included) + Clay for custom enrichment
- **€30–75M ARR**: Add 6sense or Bombora if running ABM
- **€75–150M ARR**: Full stack — 6sense + Clay + conversation intelligence

---

## 4. AI SDR / Conversational Qualification

| Tool | Type | G2 Rating | Pricing | Best For |
|---|---|---|---|---|
| **Qualified** | Inbound AI SDR (website) | 4.9/5 (1,000+ reviews) | Enterprise (contact) | High-traffic websites |
| **Salesloft** (incl. Drift) | Orchestration + chatbot | 4.5/5 (4,000+ reviews) | Enterprise | Teams already on Salesloft |
| **HubSpot Breeze Customer Agent** | Website chatbot + qualification | Included (varies by tier) | Part of HubSpot | HubSpot-native teams |

For most EU scale-ups at €15–50M ARR, HubSpot's Breeze Customer Agent is sufficient before investing in Qualified or Salesloft.

---

## 5. Predictive Churn & Expansion

| Tool | Approach | G2 Rating | Pricing |
|---|---|---|---|
| **ChurnZero** | CS workflow + product + support + billing | 4.7/5 (1,200+ reviews) | CS platform pricing |
| **Gainsight** | Multi-signal composite | 4.4/5 (1,500+ reviews) | Enterprise |
| **Pendo** (Predict) | Product usage patterns | 4.4/5 (1,400+ reviews) | Part of Pendo |
| **Vitally** | CS platform with health scoring | 4.5/5 (400+ reviews) | Mid-market pricing |

### Build-Your-Own Option

Push product data to HubSpot company records nightly (activation, seats, WAU/MAU, feature adoption), build composite health score as calculated property, trigger workflows on score changes. Covers ~70% of predictive value without a new platform.

---

## 6. HubSpot-Native AI (Breeze)

**Copilot**: summarise contact/deal records, draft emails, available in CRM + browser extension + mobile.

**Intelligence**: enrich from 200M+ profiles, reverse-IP intent, dynamic form shortening. Handoff use: auto-enrich before routing.

**Agents**: Prospecting Agent (auto-research, score, monitor signals), Customer Agent (24/7 qualification, meeting booking). Handoff use: immediate hand-raiser response.

**AI Lead Scoring** (Marketing Hub Enterprise): evaluates historical contacts, recommends Fit + Engagement criteria, auto-updates.

---

## 7. GDPR & EU Compliance

| Requirement | What to Check |
|---|---|
| **Data residency** | HubSpot offers EU hosting. Verify each tool. |
| **Model training opt-out** | Confirm tools don't train on customer data. Fathom confirms no. Check per tool. |
| **Consent management** | Call recording consent varies by EU country. |
| **Data minimisation** | Only enrich/score with necessary data. |
| **Right to erasure** | All tools must support GDPR deletion. |
| **EU Data Act (2025)** | Switching/interoperability requirements affect SaaS contracts. |

### EU-Safe Stack

| Layer | Recommended | EU Status |
|---|---|---|
| CRM | HubSpot (EU hosting) | Confirmed |
| Conversation intelligence | Fathom or Fireflies | Verify residency per tool |
| Enrichment | Breeze Intelligence (native) | Confirmed |
| Automation | n8n (self-hosted, Frankfurt, SOC2) | Confirmed |
| Intent | 6sense (EU deployment available) | Confirmed |

---

## 8. Recommended Stack by Client ARR

### €15–30M ARR (5–20 reps) — Start here

| Layer | Tool | Cost |
|---|---|---|
| Conversation intelligence | Fathom Team | $19/user/month |
| Enrichment | HubSpot Breeze Intelligence | Included |
| Handoff automation | n8n/Make + Claude API | ~€10–20/month |
| Churn/expansion | HubSpot native (product data push + calculated properties) | Included |
| **Total per rep** | | **~€20–40/month** |

### €30–75M ARR (20–60 reps)

| Layer | Tool | Cost |
|---|---|---|
| Conversation intelligence | Fathom Business or Fireflies Business | $19–25/user/month |
| Enrichment | Clay + Breeze Intelligence | $149–400/month (team) |
| Intent data | 6sense (if ABM-mature) | ~$55K/year |
| Handoff automation | n8n + Claude API | ~€20–50/month |
| CS platform | Vitally or ChurnZero | Mid-market pricing |

### €75–150M ARR (60+ reps)

| Layer | Tool | Cost |
|---|---|---|
| Conversation intelligence | Gong or Avoma | $79–250/user/month |
| Enrichment | Clay + 6sense + ZoomInfo | Enterprise pricing |
| CS platform | Gainsight or ChurnZero | Enterprise pricing |

**Key insight**: at €15–75M ARR, Fathom + Breeze + LLM middleware covers 90% of the handoff automation need for under €40/user/month. Purpose-built handoff tools and enterprise platforms become relevant at scale, not as starting points.
