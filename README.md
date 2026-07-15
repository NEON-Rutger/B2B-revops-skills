# Neon RevOps, the open-source revenue operations layer for Claude

28 battle-tested Claude skills for B2B revenue teams. Drop them into any Claude project and get expert-level RevOps, GTM, ICP, positioning, deal velocity, and operating cadence thinking on demand.

**Built for:** B2B SaaS companies scaling from €5M to €150M+ ARR, where revenue operations is the constraint and hiring a full RevOps team isn't yet justified.

**What you get:**
- A diagnostics-first framework that finds the real constraint before recommending a fix
- Implementation playbooks for HubSpot, Salesforce, pipeline architecture, and compensation design
- ICP, positioning, and sales methodology skills that chain together into a complete GTM workflow

---

## Quick install

```bash
git clone https://github.com/NEON-Rutger/B2B-revops-skills.git

# Copy individual skills
cp -r B2B-revops-skills/revops-diagnostic/ your-project/.claude/skills/

# Or install everything
cp -r B2B-revops-skills/*/ your-project/.claude/skills/
```

Each skill is a folder containing a `SKILL.md` file (and optionally a `references/` directory). Place the folder in your project's `.claude/skills/` directory. Claude discovers and loads skills automatically when you open the project.

---

## Skills

### RevOps Core (12 skills)

| Skill | What it does |
|---|---|
| `revops-strategy` | Revenue operations strategy, pipeline architecture, strategic advisory |
| `revops-diagnostic` | System diagnostics, constraint identification, root cause analysis |
| `revops-metrics` | Revenue measurement, funnel math, unit economics, benchmarks |
| `revops-forecasting` | Forecast methodology, accuracy measurement, pipeline analysis |
| `revops-data-governance` | Data governance, quality operations, field management |
| `revops-tech-stack` | Tech stack architecture, platform evaluation, capability mapping |
| `revops-handoffs` | Revenue handoff design across the full bow-tie model |
| `revops-change-management` | Change management for revenue operations adoption |
| `revops-crisis` | Emergency response when multiple revenue systems break simultaneously |
| `revops-org-chart` | RevOps team design, role structure, hiring sequencing by stage |
| `revops-hubspot` | HubSpot implementation patterns for RevOps |
| `revops-salesforce` | Salesforce implementation patterns for RevOps |

### GTM and Domain (6 skills)

| Skill | What it does |
|---|---|
| `gtm-planning` | GTM motion selection, org design, territory and capacity planning |
| `gtm-compensation` | Compensation plans, quota setting, OTE structures |
| `marketing-operations` | Lead scoring, attribution, campaign tracking, MQL handoff |
| `cs-operations` | Customer success operations, health scoring, renewal management |
| `sales-methodology` | SPICED, MEDDIC, Challenger, SPIN, Gap Selling, multi-framework |
| `partner-channel-operations` | Partner programme design, enablement, co-selling, deal registration |

### Pipeline and Data (4 skills)

| Skill | What it does |
|---|---|
| `pipeline-visibility` | Pipeline reporting, dashboard design, hygiene, forecast reporting |
| `lead-routing` | Lead assignment logic, round-robin, territory design, speed-to-lead |
| `data-enrichment` | Enrichment strategy, provider evaluation, integration patterns |
| `revenue-operating-cadence` | Meeting architecture, data pyramid, board reporting |

### ICP, Positioning, and Growth (6 skills)

| Skill | What it does |
|---|---|
| `icp-builder` | Build and validate ICPs using the GAP method and SPICED framework |
| `positioning-messaging-designer` | Positioning frameworks using Use Case Canvas and Opposites method |
| `deal-velocity-engineer` | Sales cycle diagnostics, stage exit criteria, pipeline deflation |
| `expansion-revenue-architect` | NRR/GRR systems, whitespace analysis, CS-Sales handback |
| `partner-ecosystem-architect` | Ecosystem-led growth, nearbound methodology, partner strategy |
| `operating-cadence-designer` | Operating cadence design, rituals, dashboards, escalation rules |

---

## How they work together

Skills chain naturally. Start with a diagnostic, then load the specialist.

- **Diagnose then fix:** `revops-diagnostic` finds the constraint → load the relevant specialist skill
- **ICP to pipeline:** `icp-builder` → `positioning-messaging-designer` → `sales-methodology`
- **Deal flow:** `deal-velocity-engineer` → `pipeline-visibility` → `revops-forecasting`
- **Partner motion:** `partner-ecosystem-architect` → `partner-channel-operations` → `revops-handoffs`
- **Operating rhythm:** `operating-cadence-designer` → `revenue-operating-cadence` → `revops-metrics`

---

## What's not here

These are the generic operational layer, the frameworks and methodology that any B2B revenue team can use.

The full delivery system (proprietary maturity model, diagnostic frameworks, and client-specific delivery skills used in live engagements) is used in private client work through [Neon Triforce](https://neontriforce.com). If your team needs implementation support rather than frameworks to self-serve, that's the conversation to have.

## When to hire us

These skills give you the thinking. They won't run a discovery call, facilitate a workshop, or hold your leadership team accountable to a new operating cadence. If you're hitting those limits, or if the diagnostic keeps surfacing the same constraint and nothing changes, [get in touch](https://neontriforce.com).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The bar is intentionally high.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Licence

MIT, see [LICENSE](LICENSE).

---

Built by [Rutger Katz](https://www.linkedin.com/in/rutgerkatz/) / [Neon Triforce](https://neontriforce.com)
