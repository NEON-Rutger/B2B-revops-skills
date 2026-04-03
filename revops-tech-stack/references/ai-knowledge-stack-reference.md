# AI Knowledge Stack — Quick Reference
*Last updated: April 2026. Pricing and ratings current as of this date.*

## What the knowledge layer does

Gives AI agents and reps access to institutional knowledge (call transcripts, playbooks, CRM data, documented processes) rather than generic LLM output. Four components: ingestion → chunking + indexing → retrieval → delivery.

---

## US Stack

### Buy path
| Use case | Tool | Price |
|----------|------|-------|
| Enterprise knowledge search | Glean (best-in-class) | $50+/user/mo, 100-seat min |
| Revenue team KM | Guru | $25/seat/mo |
| Team knowledge base | Notion AI Agents | $12-27/user/mo |
| Agent platform | Dust.tt | Custom |

### Build path (custom RAG)
| Component | Tool | Price |
|-----------|------|-------|
| Orchestration | LlamaIndex (retrieval) or LangChain (agents) | Free |
| Vector DB | Pinecone | $25-500/mo |
| Embeddings | OpenAI text-embedding-3-small | $0.02/1M tokens |
| Reranking | Cohere Rerank | $50-200/mo |
Total: $900-2,000/mo + 2-4 week build

---

## EU Stack (GDPR-first)

### Buy path
| Use case | Tool | Data residency |
|----------|------|---------------|
| AI platform + knowledge | Langdock | EU-hosted, GDPR-native |
| M365 shops | Microsoft Copilot + SharePoint | EU DC available |
| Team KB with DPA | Slite or Notion + EU DPA | US-hosted, DPA covered |

### Build path (EU sovereign)
| Component | Tool | Data residency |
|-----------|------|---------------|
| Orchestration | LlamaIndex | Self-hosted EU |
| Vector DB | Qdrant Cloud EU | EU cloud |
| Embeddings | Mistral (EU) or local all-MiniLM | EU-native or on-premise |
| LLM | Mistral Large or Claude via Langdock | EU |
Total: €800-1,500/mo + 2-4 week build

---

## Decision tree

```
GDPR personal data involved?
├── No → US stack fine
├── Yes + unregulated → US tools with EU DPA (or Langdock)
└── Yes + regulated OR works council → EU sovereign stack
```

---

## Stage guide

| ARR | US | EU |
|-----|----|----|
| €1-5M | Notion AI | Notion + EU DPA |
| €5-15M | Guru or Notion AI Agents | Langdock |
| €15-50M | Glean or custom RAG (Pinecone) | Custom RAG (Qdrant EU) |
| €50-100M | Glean + custom RAG | Copilot EU + custom RAG |
| €100M+ | Glean Enterprise | Aleph Alpha or Copilot EU |

---

## Top vendor ratings (G2 / Capterra)

| Vendor | Rating | Reviews | Note |
|--------|--------|---------|------|
| Glean | 4.8/5 | 130+ | Gartner eMQ Emerging Leader |
| Guru | 4.8/5 | 624 (Capterra) | #1 KM satisfaction |
| Dust.tt | 4.9/5 | 19 | Small sample, very positive |
| Pinecone | 4.6/5 | 39 | #1 vector DB on G2 |
| Weaviate | 4.8/5 | 30 | Best knowledge graphs |
| Qdrant | ~12 reviews | — | EU sovereign option |
| ChromaDB | Limited | — | Prototype only, not production |
| Mem.ai | 1/5 | 2 | Avoid |

---

## Critical insight

**Chunking quality > embedding model choice.** Semantic chunking: 0.79-0.82 faithfulness. Naive chunking: 0.47-0.51. A 60% improvement. Design chunking first, pick tools second.

---

## Full vault docs

- Full AI knowledge stack guide (US/EU reference)
- 14-platform landscape analysis (2025-2026)
- G2/Capterra review data (April 2026)
