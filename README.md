# RevOps Skills for Claude

28 purpose-built Claude skills for B2B revenue teams. Drop them into your Claude project to get RevOps, GTM, ICP, positioning, deal velocity, partner ecosystem, and operating cadence expertise on demand.

These skills encode the operational layer of a B2B revenue system — the frameworks, benchmarks, diagnostic patterns, and implementation playbooks that revenue operations teams use daily. Each skill is a standalone markdown file that loads methodology into your Claude session, giving you an expert co-pilot for specific RevOps challenges.

## Quick install

```bash
# Clone the repo
git clone https://github.com/NEON-Rutger/neon-revops-skills.git

# Copy individual skills into your Claude project
cp -r neon-revops-skills/revops-strategy/ your-project/.claude/skills/

# Or copy all skills at once
cp -r neon-revops-skills/*/ your-project/.claude/skills/
```

Each skill is a folder containing a `SKILL.md` file (and optionally a `references/` directory with supporting data). Place the folder in your project's `.claude/skills/` directory. Claude discovers and loads skills automatically.

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
| `revops-crisis` | Emergency response when multiple revenue systems break |
| `revops-org-chart` | RevOps team design, role structure, hiring sequencing by stage |
| `revops-hubspot` | HubSpot implementation patterns for RevOps |
| `revops-salesforce` | Salesforce implementation patterns for RevOps |

### GTM and domain (6 skills)

| Skill | What it does |
|---|---|
| `gtm-planning` | GTM motion selection, org design, territory and capacity planning |
| `gtm-compensation` | Compensation plans, quota setting, OTE structures |
| `marketing-operations` | Lead scoring, attribution, campaign tracking, MQL handoff |
| `cs-operations` | Customer success operations, health scoring, renewal management |
| `sales-methodology` | SPICED, MEDDIC, Challenger, SPIN, Gap Selling — multi-framework |
| `partner-channel-operations` | Partner programme design, enablement, co-selling, deal registration |

### Pipeline and data (4 skills)

| Skill | What it does |
|---|---|
| `pipeline-visibility` | Pipeline reporting, dashboard design, hygiene, forecast reporting |
| `lead-routing` | Lead assignment logic, round-robin, territory design, speed-to-lead |
| `data-enrichment` | Enrichment strategy, provider evaluation, integration patterns |
| `revenue-operating-cadence` | Meeting architecture, data pyramid, board reporting |

### ICP, positioning, and growth (6 skills)

| Skill | What it does |
|---|---|
| `icp-builder` | Build and validate ICPs using the GAP method and SPICED framework |
| `positioning-messaging-designer` | Positioning frameworks using Use Case Canvas and Opposites method |
| `deal-velocity-engineer` | Sales cycle diagnostics, stage exit criteria, pipeline deflation |
| `expansion-revenue-architect` | NRR/GRR systems, whitespace analysis, CS-Sales handback |
| `partner-ecosystem-architect` | Ecosystem-led growth, nearbound methodology, partner strategy |
| `operating-cadence-designer` | Operating cadence design — rituals, dashboards, escalation rules |

## How they work together

Skills chain naturally. Common workflows:

- **Diagnostic then fix:** `revops-diagnostic` identifies the constraint, then load the relevant specialist skill
- **ICP to positioning to sales:** `icp-builder` then `positioning-messaging-designer` then `sales-methodology`
- **Deal flow:** `deal-velocity-engineer` then `pipeline-visibility` then `revops-forecasting`
- **Partner:** `partner-ecosystem-architect` then `partner-channel-operations` then `revops-handoffs`
- **Cadence:** `operating-cadence-designer` then `revenue-operating-cadence` then `revops-metrics`

## What's not here

These are the generic operational layer — the frameworks and methodology that any B2B revenue team can use. The full delivery system (proprietary maturity model, diagnostic frameworks, and client-specific delivery skills) is used in private client engagements through [Neon Triforce](https://neontriforce.com).

## Built by

[Rutger Katz](https://www.linkedin.com/in/rutgerkatz/) / [Neon Triforce](https://neontriforce.com) — Revenue operations consulting for B2B SaaS companies scaling from EUR 1M to EUR 150M+ ARR.

## Licence

MIT — see [LICENSE](LICENSE).
