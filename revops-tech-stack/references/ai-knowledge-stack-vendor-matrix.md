# AI Knowledge Stack. Vendor and Pricing Matrix (US / EU)

On-demand reference for the revops-tech-stack skill.

*Vendor pricing data collected April 2026. Platform ratings as of July 2026. Quarterly refresh required for SaaS pricing changes.*

The fuller vendor research behind the AI Knowledge Stack: US and EU stack options (buy vs. build), compliance decision tree, stage-appropriate dual recommendations, the key technical insight on chunking, and the vendor review summary. The capability-we're-solving-for framing and pointers live in SKILL.md. (This is distinct from `ai-knowledge-stack-reference.md`, the condensed reference.)

## US Stack. Speed-First, Feature-Rich

**Managed platform path (buy)**

| Component | Recommended | Alternative | Price |
|-----------|------------|-------------|-------|
| All-in-one knowledge layer | Glean | Guru (revenue-specific) | Glean: $50+/user/mo (100-seat min). Guru: $25/seat/mo |
| Team knowledge base | Notion AI Agents | Slite | Notion: $12-27/user/mo. Slite: $8-15/user/mo |
| Agent platform | Dust.tt | N/A | Custom pricing |

*When to pick this path:* Time-to-value matters more than cost or control. Team is non-technical. Budget is $100K+/year for the knowledge layer. Already in Notion or similar ecosystem.

G2 ratings (July 2026): Glean 4.7/5 (162 reviews, Gartner Emerging Leader). Guru 4.8/5 G2 and 4.7/5 Gartner Peer Insights (Capterra 639 reviews). Notion 4.6/5 (10,149 reviews, G2 Leader).

**Custom RAG path (build)**

| Component | Recommended | Alternative | Price |
|-----------|------------|-------------|-------|
| Orchestration | LlamaIndex (retrieval-optimised) | LangChain (agent-optimised) | Free (open source) |
| Vector DB | Pinecone (managed) | Weaviate Cloud | Pinecone: $25-500/mo. Weaviate: $25-50/mo |
| Embeddings | OpenAI text-embedding-3-small | N/A | $0.02/1M tokens |
| Reranking | Cohere Rerank | LLM-based | $50-200/mo |
| LLM | Claude or GPT-4 | N/A | Per-token |

Total cost: $900-2,000/month + 2-4 weeks initial build + 2-4 hours/week maintenance.

*When to pick this path:* Need proprietary retrieval logic. Engineering capacity available. Want to optimise chunking strategy for specific content. Data sensitivity requires full control.

## EU Stack. Compliance-First, Sovereign

The EU stack addresses GDPR, data residency, and works council requirements. This is critical for Dutch and EU teams.

**Managed platform path (buy)**

| Component | Recommended | Alternative | Price | Data residency |
|-----------|------------|-------------|-------|---------------|
| AI platform + knowledge folders | Langdock | N/A | €20/user/mo + usage | EU-hosted, GDPR-native |
| Enterprise knowledge (M365 shops) | Microsoft Copilot + SharePoint | Google Vertex AI Search | Included in M365 | EU data centre available |
| Team knowledge base | Slite or Notion (with EU DPA) | Guru (with EU DPA) | $8-27/user/mo | US-hosted with DPA |

*The honest gap:* There is no EU-native equivalent of Glean. Langdock comes closest for the AI layer but its semantic search is weaker than Glean's. For regulated industries (healthcare, finance, government), use the sovereign path below.

**Custom RAG path. EU sovereign**

| Component | Recommended | Alternative | Price | Data residency |
|-----------|------------|-------------|-------|---------------|
| Orchestration | LlamaIndex | LangChain | Free | Self-hosted (EU) |
| Vector DB | Qdrant Cloud EU | Weaviate Cloud EU | Qdrant: €27-102/mo. Weaviate: €25-50/mo | EU cloud |
| Embeddings | Mistral embeddings (EU) | Local model (all-MiniLM) | Mistral: API pricing. Local: free | Mistral: EU. Local: on-premise |
| Reranking | Jina Reranker (open source) | LLM-based | Free (self-hosted) | Self-hosted |
| LLM | Mistral Large (EU) | Claude via Langdock (EU wrapper) | Per-token | EU-native |

Total cost: €800-1,500/month + 2-4 weeks initial build + 2-4 hours/week maintenance.

*When to pick this path:* Regulated industry. Data cannot leave EU borders. Legal/compliance team has specific data sovereignty requirements. Government or public sector contracts.

## Compliance Decision Tree

```
Does client data include personal data under GDPR?
├── No → US stack is fine. Standard DPA with vendors.
├── Yes → Is the client in a regulated industry?
│   ├── No → US tools with EU DPA acceptable for most use cases.
│   │         Langdock as AI layer adds compliance comfort.
│   │         Note: Schrems II requires supplementary safeguards and
│   │         transfer-risk assessment for all US-hosted processing.
│   └── Yes → Full EU sovereign stack required.
│             Custom RAG with Qdrant EU + Mistral + self-hosted.
└── Special case: Works council involved?
    └── Yes → Sovereign stack. Works councils in DE/NL/FR often require
              on-premise or EU-only data processing. Build this into the
              change management plan. Supplement with transfer safeguards
              (encryption, contractual restrictions, audit rights).
```

## Stage-Appropriate Recommendations (Dual US/EU)

| Stage | US recommendation | EU recommendation |
|-------|-------------------|-------------------|
| Seed/Build (€1-5M) | Notion + built-in AI | Notion with EU DPA, or manual |
| Build/Scale (€5-15M) | Guru or Notion AI Agents | Langdock + Notion (EU DPA) |
| Scale (€15-50M) | Custom RAG (LlamaIndex + Pinecone) or Glean | Custom RAG (LlamaIndex + Qdrant EU) or Langdock |
| Expand (€50-100M) | Glean + custom RAG for proprietary data | Microsoft Copilot (EU DC) + custom RAG (Qdrant EU) |
| Enterprise (€100M+) | Glean Enterprise | Aleph Alpha PhariaAI or Microsoft Copilot (EU DC) |

## Key Technical Insight

**Chunking quality constrains retrieval accuracy more than embedding model choice.**

Semantic chunking outperforms naive chunking significantly (practice-based). A well-designed custom RAG with good chunking on a cheap embedding model will outperform an expensive managed platform with basic chunking. Design the chunking strategy first. Pick tools second.

## Vendor Summary (G2 / Capterra / Gartner, as of July 2026)

| Vendor | G2 | Capterra | Gartner | Notes |
|--------|-----|---------|---------|-------|
| Glean | 4.7/5 (162, July 2026) | N/A | eMQ Emerging Leader 2025 | Best enterprise search |
| Guru | 4.8/5 (G2, July 2026) | 4.8/5 (639, July 2026) | 4.7/5 Peer Insights (July 2026) | #1 satisfaction in KM |
| Notion | 4.6/5 (10,149) | Listed | G2 Leader (Knowledge Base) | Massive review base |
| Dust.tt | 4.9/5 (19) | N/A | N/A | Small sample, very positive |
| Langdock | Limited data | N/A | N/A | 37 customer references |
| Pinecone | 4.6/5 (39) | N/A | N/A | #1 vector DB on G2 |
| Weaviate | 4.8/5 (30) | N/A | N/A | Best for knowledge graphs |
| Qdrant | ~12 reviews | N/A | N/A | Speed + EU sovereign option |
| ChromaDB | Limited | N/A | N/A | Prototype/local only, memory leaks in production |
| Mem.ai | 1/5 (2) | N/A | N/A | Red flag: severe user issues |

*Gartner note:* No unified Magic Quadrant for knowledge management. Vendors appear across Insight Engines, KM Software, and Gen AI eMQ categories. Forrester Wave KM Q4 2024 names Atlassian (Confluence) as Leader.

## Vault References

For the full research behind these recommendations:
- `Frameworks/AI-Use-Cases/ai-knowledge-stack-us-eu-reference.md`. Dual US/EU stack recommendation by stage
- `Sources/Research/AI-Knowledge-Layer-Landscape-2025-2026.md`. Full vendor research (14 platforms, pricing, features, data residency)
- `Sources/Research/AI-Knowledge-Layer-G2-Capterra-Reviews-2026-04-02.md`. Independent review platform data
- Offering positioning reference (internal)
- `references/ai-knowledge-stack-reference.md`. Condensed reference for skill use
