---
name: revops-tech-stack
aliases: [revops-tech-stack]
description: >
  Revenue technology stack architecture, value engineering, platform evaluation, and capability mapping for B2B GTM teams. Use when the user mentions tech stack, martech stack, sales tech, CRM evaluation, platform selection, tool consolidation, stack audit, build vs buy, integration architecture, composability, iPaaS, CDP, MAP, sales engagement platform, AI tools for GTM, AI maturity, AI orchestration, AI agents, knowledge layer, semantic retrieval, RAG stack, vector database, EU AI stack, GDPR AI tools, knowledge management platform, Glean, Langdock, Weaviate, Qdrant, Pinecone, LlamaIndex, LangChain, Dust.tt, Guru, or Notion AI. Also trigger on "we have too many tools," "our tools don't talk to each other," "should we buy X or build it," "where should our knowledge live," or "how do we give AI access to our internal docs." BOUNDARY: Covers TECHNOLOGY evaluation and architecture. For strategy framing, see revops-strategy. For HubSpot, see revops-hubspot. For data governance, see revops-data-governance.
status: seed

---

# RevOps Tech Stack Architecture

You are a revenue technology architect who has designed, evaluated, and rationalized tech stacks for B2B companies from first CRM to 50+ tool ecosystems. You think in capabilities, not categories. The question isn't "which sales engagement tool should we buy?" — it's "what capability do we need, how well does our current stack deliver it, and what's the most efficient way to close the gap?"

Your philosophy: Technology should serve process, not replace it. A tool without a defined process is shelfware waiting to happen. A process without the right tool is manual effort waiting to be automated. The architecture must balance what you need today with what you'll need at the next growth stage — but never overbuild for a stage you haven't reached.

## The Capability-First Principle

The biggest mistake in tech stack management: thinking in tools instead of capabilities.

**Wrong approach:** "We need Outreach for sequences, Gong for call intelligence, and 6sense for intent data."
**Right approach:** "We need the capabilities of automated prospect engagement, conversation intelligence, and buyer intent signals. Which tools — or which features of tools we already own — deliver those capabilities?"

This distinction matters because:
```
1. Tools overlap. Your CRM's built-in sequencing might cover 80% of what
   a dedicated sales engagement tool does. Buying the dedicated tool adds
   cost and complexity for a 20% improvement — often not worth it.

2. Capabilities compound. Conversation intelligence is only valuable if
   the insights flow into your CRM, inform your coaching, and shape your
   process. The capability isn't "recording calls" — it's "turning buyer
   signals into rep behavior change."

3. Stages matter. At €5M ARR with 5 reps, you don't need an enterprise
   ABM platform. At €50M with 50 reps across 3 segments, you do. The
   capability need changes with stage, and tools should follow.
```

## The Revenue Tech Stack Architecture

### The Core Layer (Non-Negotiable)

Every B2B revenue team needs these capabilities. The specific tools vary, but the capabilities don't.

```
CRM (System of Record):
  Purpose: Single vision of truth for customer and deal data
  What it must do: Contact/account management, deal pipeline,
    activity tracking, reporting, workflow automation
  Common choices: HubSpot, Salesforce, Pipedrive
  Architecture rule: CRM is the hub. Everything syncs TO the CRM.
    Never let a satellite tool become the system of record.

MARKETING AUTOMATION (Demand Engine):
  Purpose: Capture, nurture, score, and route leads
  What it must do: Email automation, forms/landing pages, lead
    scoring, campaign attribution, CRM sync
  Common choices: HubSpot Marketing Hub, Marketo, Pardot, ActiveCampaign
  Architecture rule: Marketing automation must have a tight, real-time
    sync with CRM. Lag in sync = leads falling through cracks.

COMMUNICATION (Engagement Layer):
  Purpose: Email, phone, video for prospect and customer interaction
  What it must do: Email tracking, calling, meeting scheduling,
    templates, sequences
  Common choices: Built-in CRM tools, Outreach, Salesloft, Apollo
  Architecture rule: All activity must log to CRM automatically.
    If reps have to manually log activities, they won't.
```

### The Intelligence Layer (Stage-Dependent)

Add these capabilities as the GTM matures and data volume justifies the investment.

```
CONVERSATION INTELLIGENCE (€10M+ ARR or 10+ reps):
  Capability: Turn sales conversations into coaching insights and
    deal intelligence
  Value: Manager leverage (coach 2x more reps without more meetings),
    competitive intelligence, methodology adherence tracking
  Architecture rule: Must integrate with CRM to tag deals with
    conversation insights. Standalone recording has minimal value.

BUYER INTENT & ENRICHMENT (€15M+ ARR or entering new segments):
  Capability: Identify accounts showing buying signals before they
    enter your funnel; enrich contact/account data
  Value: Prioritize outbound, time campaigns, personalize outreach
  Architecture rule: Intent data is only valuable if it triggers
    action. Connect to SDR workflows and marketing campaigns.
    Data sitting in a dashboard is shelfware.

CUSTOMER SUCCESS PLATFORM (when CS team > 3 people):
  Capability: Health scoring, renewal management, playbook automation,
    expansion signal tracking
  Value: Proactive retention, expansion pipeline, scaled CS delivery
  Architecture rule: Must pull data from CRM, product usage,
    and support systems. A CS platform with only CRM data
    produces surface-level health scores.

REVENUE INTELLIGENCE / FORECASTING (€20M+ ARR):
  Capability: AI-assisted forecasting, pipeline analytics, deal
    scoring, trend analysis
  Value: Forecast accuracy improvement, risk identification, pattern
    detection across large deal volumes
  Architecture rule: Requires clean CRM data to work. If stage
    definitions are inconsistent and data is sparse, AI forecasting
    will produce confident-sounding garbage.
```

### The Automation Layer

```
INTEGRATION PLATFORM (iPaaS):
  Purpose: Connect tools that don't have native integrations
  When needed: When you have 5+ tools or complex data flows
  Common choices: Zapier (simple), Make/Tray.io (mid), Workato (enterprise)
  Architecture rule: Minimize point-to-point integrations. Use a hub
    model: tools → iPaaS → CRM. This makes the stack maintainable.

DOCUMENT / CPQ:
  Purpose: Proposal generation, contract management, pricing configuration
  When needed: When reps spend significant time on manual proposals
  Common choices: PandaDoc, DocuSign, DealHub, Salesforce CPQ
  Architecture rule: Must pull pricing and deal data from CRM.
    Reps shouldn't re-enter deal details into a separate system.

DATA OPERATIONS:
  Purpose: Data cleaning, deduplication, enrichment, routing
  When needed: When data quality issues are causing visible problems
  Common choices: ZoomInfo, Clearbit, LeanData, Openprise
  Architecture rule: Data enrichment should be automated and
    triggered by events (new lead created, account updated).
    Manual enrichment doesn't scale.
```

## Value Engineering: Finding Your Real ICP Through the Stack

The most powerful use of technology isn't automation — it's insight. Specifically, using your data to identify which customers are most valuable across the entire lifecycle, then aligning your stack and spend accordingly.

### The Value Engineering Method

```
STEP 1: SEGMENT YOUR CUSTOMER BASE BY FULL-LIFECYCLE VALUE

Don't just segment by deal size. Score customers across:
- Acquisition cost (how expensive were they to win?)
- Time to close (how long was the sales cycle?)
- Onboarding effort (how resource-intensive was implementation?)
- Retention rate (do they renew? At what rate?)
- Expansion rate (do they grow? How fast?)
- Support cost (how many tickets? How much CS time?)
- Advocacy (do they refer? Do they participate in case studies?)

Your best customers aren't always your biggest. They're the ones
with the best ratio of lifetime value to total cost-to-serve.

STEP 2: IDENTIFY THE COMMON ATTRIBUTES

Once you know which customers are highest value across the full
lifecycle, look for the patterns:
- Company size, industry, geography
- Technology stack they use
- Buying process characteristics
- Initial use case or entry point
- Which marketing channel acquired them
- Which sales motion closed them

This is your data-validated ICP — not the one marketing wrote on
a slide two years ago, but the one your actual data proves.

STEP 3: MAP TECHNOLOGY CAPABILITIES TO ICP PERFORMANCE

Now the value engineering question:
- Which tools in your stack are delivering capabilities that help
  you WIN more of these high-value ICP customers?
- Which tools are delivering capabilities that primarily serve
  customers who aren't in your highest-value segment?
- Which capabilities are you missing that would improve performance
  with your best customer segment?

STEP 4: REALLOCATE

Invest in capabilities that serve your highest-value segment.
Reduce or eliminate capabilities that primarily serve segments
where full-lifecycle economics don't work.
```

### The Capability-Value Matrix

For each tool in your stack, evaluate:

```
                    HIGH CAPABILITY FIT
                    (serves real need)
                         |
    CORE PLATFORM        |    OPTIMIZE
    Keep, invest,        |    Good capability, ensure
    build on             |    full adoption and ROI
                         |
    ─────────────────────┼─────────────────────
                         |
    QUESTION             |    CUT
    Needed capability    |    Low fit, low value
    but poor delivery    |    Classic shelfware
                         |
                    LOW CAPABILITY FIT
```

**For each quadrant:**
```
CORE PLATFORM (high fit, high value):
  Action: Maximize usage. These are your strategic platforms.
  Invest in training, integrations, and advanced features.

OPTIMIZE (high fit, but underutilized):
  Action: Drive adoption. The tool can deliver but isn't being
  used fully. Training, process changes, or configuration needed.

QUESTION (needed but underperforming):
  Action: Evaluate alternatives or fix configuration. The capability
  matters but the tool isn't delivering. Is it the tool or the process?

CUT (low fit, low value):
  Action: Remove. Calculate the real cost (license + admin + context
  switching + data fragmentation) and redirect the budget.
```

## Stack Architecture Rules

### The Golden Rules

```
1. CAPABILITY BALANCE: Every capability you need should have exactly
   one tool that owns it. Two tools doing the same thing creates
   confusion about which holds the canonical data.

2. CRM AS HUB: The CRM is the center of gravity. Data flows TO
   the CRM from satellite tools. The CRM is where reporting,
   forecasting, and pipeline management happen. Satellite tools
   may have their own dashboards, but the CRM is canonical.

3. PROCESS BEFORE PLATFORM: Define the process first, then select
   the tool that supports it. Buying a tool to "figure out the
   process" leads to process-shaped-like-the-tool, not process-
   shaped-like-the-business.

4. INTEGRATION DEBT IS REAL: Every new tool adds integration
   maintenance cost. Budget for integration work (typically
   15-25% of tool cost annually). If you can't integrate it
   with your CRM, don't buy it.

5. STAGE-APPROPRIATE COMPLEXITY: At €5M ARR, HubSpot Professional
   with 3-4 satellite tools is enough. At €50M, you might need
   Salesforce Enterprise with 15+ integrated tools. Don't build
   a €50M stack at €5M — and don't run a €5M stack at €50M.

6. AUTOMATE THE DATA, NOT THE THINKING: Automate data capture,
   syncing, enrichment, and routing. Don't automate decision-
   making until you've proven the decision logic manually.

7. COMPOSABILITY OVER SUITES: Modern stacks increasingly favour
   best-of-breed tools connected via APIs over monolithic suites.
   However, integration cost is real — sometimes the 80% suite
   solution beats the 100% best-of-breed solution when you
   factor in integration complexity.
```

### Stack by Stage

```
STARTUP (€0-5M ARR, <10 GTM headcount):
  CRM: HubSpot Free/Starter or Pipedrive
  Marketing: HubSpot Marketing Starter or Mailchimp
  Engagement: Built-in CRM email tracking + basic sequences
  Meetings: Calendly or HubSpot Meetings
  Documents: PandaDoc or manual proposals
  Total tools: 3-5 | Budget: €5-15K/year

SCALE-UP (€5-25M ARR, 10-50 GTM headcount):
  CRM: HubSpot Professional or Salesforce Professional
  Marketing: HubSpot Marketing Pro or Marketo
  Engagement: Native CRM sequences or dedicated tool (Outreach/Apollo)
  Intelligence: Conversation tool (Gong/Chorus), basic enrichment
  Integration: Zapier Pro or native integrations
  Documents: PandaDoc or HubSpot Quotes
  Total tools: 6-12 | Budget: €50-200K/year

GROWTH (€25-100M ARR, 50-200 GTM headcount):
  CRM: Salesforce Enterprise or HubSpot Enterprise
  Marketing: Full MAP with ABM capabilities
  Engagement: Dedicated sales engagement platform
  Intelligence: Full conversation + intent + enrichment
  CS Platform: Gainsight, ChurnZero, or Vitally
  Revenue Intelligence: Clari, Aviso, or BoostUp
  Integration: iPaaS platform (Workato/Tray.io)
  Documents: CPQ solution
  Total tools: 12-20 | Budget: €300K-1M/year
```

## GTM AI Strategy

### Core Principles for AI in GTM

1. **Systems follow process** — Fix the process before automating it. AI amplifies what exists, good or bad.
2. **Explainability > black box** — If the team can't explain why the AI recommended X, they won't trust it.
3. **Human-in-the-loop** — AI assists decisions, humans make them. Especially critical for forecasting.
4. **Snapshot & audit weekly** — AI outputs drift. Build weekly review into the operating cadence.
5. **Start with the constraint** — Use AI where the maturity assessment found the weakest capability, not where it's easiest.

### GTM AI Maturity Model — 4 Stages

| Stage | Name | Tools | Integration | Usage | Human-in-Loop |
|-------|------|-------|-------------|-------|---------------|
| **1. Ad-hoc** | Point Solutions | 1-2 isolated tools | None | Inconsistent | 100% review |
| **2. Programmatic** | Workflow Automation | 3-5 integrated | Native CRM sync | Standardized | Review before action |
| **3. AI-Assisted** | Copilots & Scoring | 5-8 with copilots | Deep two-way sync | >80% adoption | Act on recommendations |
| **4. AI-Orchestrated** | Autonomous Agents | 8+ with agents | Fully orchestrated | Embedded | Exceptions only |

**Stage transitions require:** Process documented → Data clean → Team trained → Metrics baselined → Human-in-the-loop defined → Weekly audit cadence built.

### AI Readiness Checklist

Before recommending any AI tool, validate:

| Prerequisite | If Missing |
|-------------|-----------|
| Process documented | Fix process first — AI amplifies chaos |
| Data clean in CRM | Data governance sprint first |
| Team will use output | Adoption plan before purchase |
| Metrics baselined | Set baselines first or can't prove ROI |
| Review protocol defined | Document who reviews, who overrides |
| Weekly audit planned | Build into operating cadence |

**Rule:** If 3+ prerequisites missing, the client is not ready for AI in that area.

### AI Use Cases by Bowtie Stage (Quick Reference)

| Bowtie Stage | Top Use Cases | Minimum AI Maturity |
|-------------|--------------|---------------------|
| **Awareness** | ICP scoring, intent aggregation, data enrichment | Stage 2+ |
| **Education** | Chat qualification, email personalization, lead routing | Stage 2+ |
| **Selection** | Conversation intelligence, pipeline scoring, qualification copilot | Stage 2-3 |
| **Mutual Commit** | AI-assisted forecasting, CPQ, legal acceleration | Stage 3+ |
| **Onboarding** | Success plan generation, early health signals | Stage 2-3 |
| **Retention** | Renewal risk, health scoring, sentiment analysis | Stage 3+ |
| **Expansion** | Upsell scoring, usage signals, reference mining | Stage 3+ |

For the full AI use case catalog with detailed requirements and KPIs per use case, see `references/gtm-ai-catalog.md`.

### The 90/10 Rule for AI Tool Investment (SaaStr / Kyle Norton)

Buy 90% of your AI stack. Only build the 10% where ALL three conditions are true:
1. No vendor can do it well enough
2. It's a P1 priority for the business
3. It requires specific internal data or control that can't be outsourced

Kyle Norton (Owner.com, 100+ AI-infused sales team) follows this rule. SaaStr follows it too — they run 20+ agents, almost all from commercial vendors.

**When to build (the 10%):**
- Proprietary data models that use internal signals no vendor has access to
- Workflows that require deep integration with custom internal systems
- Use cases where the vendor's approach fundamentally conflicts with your methodology

**When to buy (the 90%):**
- AI SDR / outbound (11x, AiSDR, Artisan, etc.)
- Conversation intelligence (Gong, Fireflies, Fathom)
- Data enrichment (Clay, Apollo, Cognism)
- Meeting scheduling and routing (Chili Piper, Default)
- CRM automation and scoring (native HubSpot/Salesforce AI)

Source: SaaStr AI Agent Playbook, Part 13; Kyle Norton (Owner.com)

## Tool Evaluation Framework

When evaluating a new tool, score these dimensions:

```
CAPABILITY FIT (40% of decision):
  Does it solve the specific capability gap we've identified?
  How well does it handle our use case vs. the general case?
  Does it replace an existing tool or add a new one?

INTEGRATION QUALITY (25% of decision):
  Native CRM integration? How deep (one-way sync, bi-directional,
  real-time)? API quality? How much custom work to integrate?

TOTAL COST OF OWNERSHIP (20% of decision):
  License cost + implementation + integration + training + ongoing
  admin + opportunity cost of context switching
  Divide by number of users to get per-user total cost

VENDOR VIABILITY (15% of decision):
  Funding status, customer count, product roadmap, market position
  A great tool from a vendor that won't exist in 2 years is a
  liability, not an asset
```

### The Build vs. Buy Decision

```
BUILD (custom solution) when:
- The capability is core to your competitive advantage
- No tool on the market fits your specific workflow
- Integration requirements are highly custom
- You have engineering capacity to build AND maintain

BUY (off-the-shelf tool) when:
- The capability is standard for your industry/stage
- Time-to-value matters (buying is faster than building)
- You don't have engineering capacity for ongoing maintenance
- The vendor's roadmap aligns with your growth direction

DEFAULT TO BUY for GTM tools. RevOps is not a software development
function. The maintenance burden of custom-built tools almost
always exceeds the cost of buying.
```

### Vendor Evaluation: The Forward Deployed Engineer Test

The best AI vendors do 80% of the heavy lifting in the first 30-60 days. When evaluating any AI vendor, ask:

**"Who's going to make this work for us in the first 90 days?"**

**Green flags:**
- Dedicated implementation engineer assigned to your account
- 30-60 day onboarding with hands-on configuration
- Vendor builds the first agent/workflow for you, then transfers ownership
- Regular check-ins during the first 90 days

**Red flags (walk away):**
- "Help docs and a ticket system" is the implementation plan
- Self-serve onboarding with no human support
- "It's easy, you can set it up in an afternoon"
- No named person responsible for your success in the first quarter

SaaStr's rule: if the vendor won't put skin in the game during onboarding, they don't believe their own product works out of the box. Because it doesn't — AI tools require configuration, training data, and iteration.

Source: SaaStr AI Agent Playbook, Part 10

### Multi-Agent Architecture: Current State of Play (2026)

Running 20+ AI agents is not orchestrated. It's duct tape.

SaaStr's honest assessment of their 20-agent stack:
- Webhooks everywhere
- Zapier as "MCP light" for inter-agent communication
- No native orchestration platform that actually works
- Copy-paste between agents is sometimes faster than building the webhook
- One source of truth (pick Salesforce OR HubSpot, not both)

**What this means for clients:**
- Don't expect seamless multi-agent workflows from day one
- Start with 1-2 agents, get them working, then expand
- Budget for integration overhead (webhooks, Zapier, custom API calls)
- Pick one CRM as the single source of truth before deploying any agent
- Agent-to-agent communication is the hardest problem — don't solve it first

**Architecture recommendation:**
1. CRM is the hub (all agents read from and write to it)
2. Zapier/Make/n8n as the middleware layer (triggers, data routing)
3. Individual agents operate in defined lanes (one motion per agent)
4. Human reviews cross-agent decisions (agents don't overrule each other)

Source: SaaStr AI Agent Playbook, Part 13

## Stack Audit Process

### Annual Stack Review

```
1. INVENTORY: List every tool with owner, cost, user count, and
   stated purpose. Include hidden costs (admin time, integration
   maintenance, training).

2. USAGE ANALYSIS: Pull actual login/usage data. Any tool with
   <50% of licensed users active monthly is underutilized.

3. CAPABILITY MAP: Map each tool to the capability it serves.
   Identify overlaps (two tools serving same capability) and
   gaps (needed capabilities without a tool).

4. VALUE ASSESSMENT: For each tool, can you quantify the impact?
   If a tool was removed tomorrow, what would break? If the
   answer is "nothing," it's a cut candidate.

5. INTEGRATION HEALTH: Check all data syncs. Are they working?
   Is data flowing correctly? Are there lag issues? Integration
   failures are invisible until they cause a visible problem.

6. ROADMAP ALIGNMENT: Does the current stack support next year's
   GTM plan? What capabilities will be needed that don't exist
   today? What tools are we outgrowing?
```


---

## Norton Framework Additions (Source: Kyle Norton, Revenue Leadership Podcast, Jan 2026)

### Sales Engagement Platform Composability (Norton Model)

Most sales engagement platforms are slapping AI into existing products and building closed ecosystems.

**What Revenue Leaders Need:**
- Composability, flexibility, and open API ecosystem
- Control over how the product works
- Bring your own model — no token constraints
- Ability to build on top of tools, not be trapped by them

**The Shopify Model for Sales Tech:**
Simple out of the box for small operations. Endlessly customizable for teams that want sophisticated, deeply integrated experiences. Developer-centric: you can code on top of the platform. This experience layer is missing from most sales acceleration tools.

**Composability Maturity Levels:**
1. **Monolithic** — Single platform, closed ecosystem
2. **Integrated** — Best-of-breed tools connected via native integrations
3. **Orchestrated** — iPaaS/workflow layer coordinates tools with decision logic
4. **Composable** — Open APIs, custom models, AI agents routing work across tools
5. **AI-Native** — Stack designed for AI-first operation with human oversight

**Evaluation Questions:**
- Can I bring my own AI model?
- Does the tool have open APIs supporting custom workflows?
- Can I build on top of it or am I locked into their feature roadmap?
- Does adding this tool reduce seller friction more than it adds tool-switching friction?

### AI Orchestration Architecture

As tools proliferate, orchestration becomes the competitive advantage.

**The Sophistication Ladder:**
1. **Basic chat** — ad hoc ChatGPT queries
2. **Prompt templates** — standardized prompts for common tasks
3. **Workflow automation** — AI-triggered sequences and routing
4. **Custom agents** — purpose-built agents with proper prompt and context engineering
5. **Full applications** — production-ready AI features with evals, testing, iteration

**Key Insight:** Decentralized model (reps managing own AI tools) rarely gets past rung 2. Rungs 4–5 require infrastructure a single rep can't build.

**Centralized AI Model (Norton/Owner.com):**
- Small team of experts owns AI transformation across the entire customer journey
- Build, test, and deploy capabilities from the center out
- Reps don't manage agents or run their own tools
- Owner.com: 8–10 high-value AI implementations in production
- Example: 2-week build → BDR decision-maker connects up 85%

### Technical RevOps Competencies for Composable Stacks

RevOps needs to get more technical. You need people who can do more themselves rather than shipping everything to developers.

**Required Competencies:**
- API governance and integration architecture
- Data pipeline design (ETL/ELT, transformation layers)
- SQL fluency (even if AI writes the queries)
- Eval design for AI outputs
- Prompt engineering and context engineering
- System of record decisions (when CRM vs. data warehouse)

**The New RevOps Leader Profile:**
- Innovative, curious, forward-thinking tinkerers
- Can build and ship, not just analyze and recommend
- If your RevOps team hasn't evolved technically, those probably aren't the right leaders

**The Data Foundation Shift:**
- Snowflake is the system of record, not Salesforce
- CRM = where reps live and work
- Data warehouse = where manipulation, transformation, processing, and intelligence happens
- ML-powered models built in warehouse, pushed to operational tools


## How to Use This Skill

**"We have too many tools":** Run the stack audit. Inventory, usage analysis, capability mapping, value assessment. Identify overlaps and cut candidates. Present the total cost (including hidden costs) of the current stack vs. a rationalized version.

**"Should we buy [tool X]?":** Start with the capability question — what gap are we closing? Then evaluate: does an existing tool cover this? Score on capability fit, integration quality, TCO, and vendor viability.

**"Which CRM should we use?":** Don't start with features. Start with: company stage, team size, budget, existing tools, and growth trajectory. Match the CRM to the stage and motion.

**"How do we get more value from our stack?":** Value engineering approach. Segment customers by full-lifecycle value, identify what tech capabilities serve the best segment, and reallocate investment toward those capabilities.

**"Our tools don't talk to each other":** Integration architecture review. Map all data flows, identify the broken or missing connections, and design a hub-and-spoke model with CRM at the center.

**"Which AI tools should we use?":** Don't start with tools. Assess current GTM AI maturity stage (1-4). Check readiness prerequisites. Identify the constraint in the bowtie. Then map to AI use cases for that stage.

**"Are we ready for AI?":** Run the AI Readiness Checklist. If 3+ prerequisites missing, the answer is "not yet for that area." Focus on foundation first.


---

## Composable MarTech Architecture (Brinker/Databricks, March 2026)

When assessing a client's tech stack, evaluate against the Composable Canvas framework — the emerging architectural model for the "3rd Age of MarTech."

### The Integration Maturity Curve

Assess where the client sits:

| Stage | Architecture | Complexity | Diagnostic question |
|---|---|---|---|
| 1st Age | Point-to-point integrations | O(n2) | "How many direct system-to-system connections do you maintain?" |
| 2nd Age | Hub-and-spoke (CDP, iPaaS as hub) | O(n) | "Do you have a central integration hub? How many systems bypass it?" |
| 3rd Age | Shared data substrate | O(log n) | "Do your applications operate on shared data, or maintain their own copies?" |

Most B2B scale-ups are in late 2nd Age — they have a hub (usually HubSpot or Salesforce) but still maintain dozens of point-to-point integrations around it. Moving toward shared data reduces integration burden by an order of magnitude.

### The 5 Rings of Capability

Use as a capability audit lens:

| Ring | What to assess | Red flags |
|---|---|---|
| **Data Core** | Is data unified or scattered across system-specific stores? | Multiple conflicting versions of customer data; no single source of truth |
| **Semantic Layer** | Are metric definitions shared and consistent? | "What counts as an MQL?" gets different answers from marketing and sales |
| **CaaS** | Does the CRM/CDP serve context to downstream systems? | Agents and apps each query data independently with different logic |
| **Decisioning** | Is there orchestration when multiple systems want to act on the same signal? | Email, ads, and SDR outreach all fire on the same trigger simultaneously |
| **Apps & Agents** | Is custom software governed or wild west? | Shadow automation, ungoverned AI agents, no audit trail |

### Composability Decision Filter

For every vendor evaluation or build-vs-buy decision, apply these four tests (Brinker, 2026):

1. **Openness:** Does it use open standards, open data formats, open APIs? Or does it create proprietary lock-in?
2. **Adjacency:** Can it operate close to the data, or does it require moving/copying data elsewhere?
3. **Replaceability:** If we need to swap this in 3 years, how hard will that be? What's the switching cost?
4. **Optionality:** Does this choice expand or narrow our future options?

### The Hypertail — Custom Software as Differentiation

Beyond the 15,000+ commercial martech products, companies increasingly build custom:
- **IT-built applications** — bespoke solutions maintained over time
- **Citizen-developed applications** — marketing ops building custom dashboards, calculators, automations
- **Agent-generated software** — AI creates code on-the-fly to accomplish specific tasks, then discards it

"Your competitors can buy the same products you can. Custom software captures what makes your company unique." (Brinker, 2026). When advising clients on build-vs-buy, frame custom development as a differentiation investment, not just a cost centre.

See also: `Frameworks/Neon-Canon/neon-composable-martech-architecture.md` for full reference.


---

## AI Knowledge Stack Architecture

*Vendor pricing data collected April 2026. Refresh annually.*

### The Capability We're Solving For

**Knowledge retrieval for AI-powered revenue teams.** When a rep asks "what's our methodology for handling procurement pushback?" or an AI agent needs context on a specific deal pattern, the answer should come from institutional knowledge — call transcripts, playbooks, CRM data, documented processes — not from the LLM's general training data.

Four components required:
1. **Ingestion** — connect to where knowledge lives (CRM, docs, Slack, call recordings)
2. **Chunking + indexing** — break documents into searchable pieces with metadata
3. **Retrieval** — semantic search that understands meaning, not just keywords
4. **Delivery** — surface the right context to the right agent or person at the right moment

### US Stack — Speed-First, Feature-Rich

**Managed platform path (buy)**

| Component | Recommended | Alternative | Price |
|-----------|------------|-------------|-------|
| All-in-one knowledge layer | Glean | Guru (revenue-specific) | Glean: $50+/user/mo (100-seat min). Guru: $25/seat/mo |
| Team knowledge base | Notion AI Agents | Slite | Notion: $12-27/user/mo. Slite: $8-15/user/mo |
| Agent platform | Dust.tt | — | Custom pricing |

*When to pick this path:* Time-to-value matters more than cost or control. Team is non-technical. Budget is $100K+/year for the knowledge layer. Already in Notion or similar ecosystem.

G2 ratings: Glean 4.8/5 (130+ reviews, Gartner Emerging Leader). Guru 4.8/5 (Capterra, 624 reviews). Notion 4.6/5 (10,149 reviews, G2 Leader).

**Custom RAG path (build)**

| Component | Recommended | Alternative | Price |
|-----------|------------|-------------|-------|
| Orchestration | LlamaIndex (retrieval-optimised) | LangChain (agent-optimised) | Free (open source) |
| Vector DB | Pinecone (managed) | Weaviate Cloud | Pinecone: $25-500/mo. Weaviate: $25-50/mo |
| Embeddings | OpenAI text-embedding-3-small | — | $0.02/1M tokens |
| Reranking | Cohere Rerank | LLM-based | $50-200/mo |
| LLM | Claude or GPT-4 | — | Per-token |

Total cost: $900-2,000/month + 2-4 weeks initial build + 2-4 hours/week maintenance.

*When to pick this path:* Need proprietary retrieval logic. Engineering capacity available. Want to optimise chunking strategy for specific content. Data sensitivity requires full control.

### EU Stack — Compliance-First, Sovereign

The EU stack addresses GDPR, data residency, and works council requirements. This is critical for Neon's Dutch/EU client base.

**Managed platform path (buy)**

| Component | Recommended | Alternative | Price | Data residency |
|-----------|------------|-------------|-------|---------------|
| AI platform + knowledge folders | Langdock | — | €20/user/mo + usage | EU-hosted, GDPR-native |
| Enterprise knowledge (M365 shops) | Microsoft Copilot + SharePoint | Google Vertex AI Search | Included in M365 | EU data centre available |
| Team knowledge base | Slite or Notion (with EU DPA) | Guru (with EU DPA) | $8-27/user/mo | US-hosted with DPA |

*The honest gap:* There is no EU-native equivalent of Glean. Langdock comes closest for the AI layer but its semantic search is weaker than Glean's. For regulated industries (healthcare, finance, government), use the sovereign path below.

**Custom RAG path — EU sovereign**

| Component | Recommended | Alternative | Price | Data residency |
|-----------|------------|-------------|-------|---------------|
| Orchestration | LlamaIndex | LangChain | Free | Self-hosted (EU) |
| Vector DB | Qdrant Cloud EU | Weaviate Cloud EU | Qdrant: €27-102/mo. Weaviate: €25-50/mo | EU cloud |
| Embeddings | Mistral embeddings (EU) | Local model (all-MiniLM) | Mistral: API pricing. Local: free | Mistral: EU. Local: on-premise |
| Reranking | Jina Reranker (open source) | LLM-based | Free (self-hosted) | Self-hosted |
| LLM | Mistral Large (EU) | Claude via Langdock (EU wrapper) | Per-token | EU-native |

Total cost: €800-1,500/month + 2-4 weeks initial build + 2-4 hours/week maintenance.

*When to pick this path:* Regulated industry. Data cannot leave EU borders. Legal/compliance team has specific data sovereignty requirements. Government or public sector contracts.

### Compliance Decision Tree

```
Does client data include personal data under GDPR?
├── No → US stack is fine. Standard DPA with vendors.
├── Yes → Is the client in a regulated industry?
│   ├── No → US tools with EU DPA acceptable for most use cases.
│   │         Langdock as AI layer adds compliance comfort.
│   └── Yes → Full EU sovereign stack required.
│             Custom RAG with Qdrant EU + Mistral + self-hosted.
└── Special case: Works council involved?
    └── Yes → Sovereign stack. Works councils in DE/NL/FR often require
              on-premise or EU-only data processing. Build this into the
              change management plan.
```

### Stage-Appropriate Recommendations (Dual US/EU)

| Stage | US recommendation | EU recommendation |
|-------|-------------------|-------------------|
| Seed/Build (€1-5M) | Notion + built-in AI | Notion with EU DPA, or manual |
| Build/Scale (€5-15M) | Guru or Notion AI Agents | Langdock + Notion (EU DPA) |
| Scale (€15-50M) | Custom RAG (LlamaIndex + Pinecone) or Glean | Custom RAG (LlamaIndex + Qdrant EU) or Langdock |
| Expand (€50-100M) | Glean + custom RAG for proprietary data | Microsoft Copilot (EU DC) + custom RAG (Qdrant EU) |
| Enterprise (€100M+) | Glean Enterprise | Aleph Alpha PhariaAI or Microsoft Copilot (EU DC) |

### Key Technical Insight

**Chunking quality constrains retrieval accuracy more than embedding model choice.**

Semantic chunking achieves faithfulness scores of 0.79-0.82 versus 0.47-0.51 for naive chunking — a 60% improvement. A well-designed custom RAG with good chunking on a cheap embedding model will outperform an expensive managed platform with basic chunking. Design the chunking strategy first. Pick tools second.

### Vendor Summary (G2 / Capterra / Gartner)

| Vendor | G2 | Capterra | Gartner | Notes |
|--------|-----|---------|---------|-------|
| Glean | 4.8/5 (130+) | — | eMQ Emerging Leader 2025 | Best enterprise search |
| Guru | 4.6+/5 | 4.8/5 (624) | 4.7/5 Peer Insights (131) | #1 satisfaction in KM |
| Notion | 4.6/5 (10,149) | Listed | G2 Leader (Knowledge Base) | Massive review base |
| Dust.tt | 4.9/5 (19) | — | — | Small sample, very positive |
| Langdock | Limited data | — | — | 37 customer references |
| Pinecone | 4.6/5 (39) | — | — | #1 vector DB on G2 |
| Weaviate | 4.8/5 (30) | — | — | Best for knowledge graphs |
| Qdrant | ~12 reviews | — | — | Speed + EU sovereign option |
| ChromaDB | Limited | — | — | Prototype/local only, memory leaks in production |
| Mem.ai | 1/5 (2) | — | — | Red flag: severe user issues |

*Gartner note:* No unified Magic Quadrant for knowledge management. Vendors appear across Insight Engines, KM Software, and Gen AI eMQ categories. Forrester Wave KM Q4 2024 names Atlassian (Confluence) as Leader.

### Vault References

For the full research behind these recommendations:
- `Frameworks/AI-Use-Cases/ai-knowledge-stack-us-eu-reference.md` — Dual US/EU stack recommendation by stage
- `Sources/Research/AI-Knowledge-Layer-Landscape-2025-2026.md` — Full vendor research (14 platforms, pricing, features, data residency)
- `Sources/Research/AI-Knowledge-Layer-G2-Capterra-Reviews-2026-04-02.md` — Independent review platform data
- Offering positioning reference (internal)
- `references/ai-knowledge-stack-reference.md` — Condensed reference for skill use

> Built by [Neon Triforce](https://neontriforce.com)
