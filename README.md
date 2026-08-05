# RevOps Skills Library for Claude

**Current release: v1.0.0 (2026-07-15), 34 skills, all stable.** See the [CHANGELOG](CHANGELOG.md) for what changed in each release.

34 battle-tested Claude skills for B2B revenue teams. Drop them into any Claude project and get expert-level RevOps, GTM, ICP, positioning, deal velocity, and operating cadence thinking on demand.

**Built for:** B2B SaaS companies in the growth phase where revenue operations is the constraint and hiring a full RevOps team isn't yet justified.

**What you get:**
- A diagnostics-first framework that finds the real constraint before recommending a fix
- Implementation playbooks for HubSpot, Salesforce, pipeline architecture, and compensation design
- ICP, positioning, and sales methodology skills that chain together into a complete GTM workflow
- Every benchmark carries a named source and vintage, so you know which numbers are 2026 reality and which are pre-2024 folklore

---

## Quick install

```bash
git clone https://github.com/revops-skills/claude-revops-library.git

# Copy individual skills
cp -r claude-revops-library/revops-diagnostic/ your-project/.claude/skills/

# Or install everything
cp -r claude-revops-library/*/ your-project/.claude/skills/
```

Each skill is a folder containing a `SKILL.md` file (and optionally a `references/` directory). Place the folder in your project's `.claude/skills/` directory. Claude discovers and loads skills automatically when you open the project.

---

## Skills

### RevOps Core (14 skills)

| Skill | What it does | Since |
|---|---|---|
| `revops-strategy` | Revenue operations strategy, pipeline architecture, strategic advisory | v0.1.0 |
| `revops-diagnostic` | System diagnostics, constraint identification, root cause analysis | v0.1.0 |
| `revops-metrics` | Revenue measurement, funnel math, unit economics, benchmarks | v0.1.0 |
| `revops-forecasting` | Forecast methodology, accuracy measurement, pipeline analysis | v0.1.0 |
| `revops-revenue-planning` | Annual and quarterly plan construction, top-down vs bottoms-up reconciliation, reforecasting | v0.3.0 |
| `revops-data-governance` | Data governance, quality operations, field management | v0.1.0 |
| `revops-tech-stack` | Tech stack architecture, platform evaluation, capability mapping | v0.1.0 |
| `revops-handoffs` | Revenue handoff design across the full bow-tie model | v0.1.0 |
| `revops-change-management` | Change management for revenue operations adoption | v0.1.0 |
| `revops-crisis` | Emergency response when multiple revenue systems break simultaneously | v0.1.0 |
| `revops-org-chart` | RevOps team design, role structure, hiring sequencing by stage | v0.1.0 |
| `revops-hubspot` | HubSpot implementation patterns for RevOps | v0.1.0 |
| `revops-salesforce` | Salesforce implementation patterns for RevOps | v0.1.0 |
| `crm-migration-consolidation` | CRM migration and post-merger instance consolidation: system of record, identity resolution, cutover | v0.4.0 |

### GTM and Domain (7 skills)

| Skill | What it does | Since |
|---|---|---|
| `gtm-planning` | GTM motion selection, org design, territory and capacity planning | v0.1.0 |
| `gtm-compensation` | Compensation plans, quota setting, OTE structures | v0.1.0 |
| `marketing-operations` | Lead scoring, attribution, campaign tracking, MQL handoff | v0.1.0 |
| `cs-operations` | Customer success operations, health scoring, renewal management | v0.1.0 |
| `sales-methodology` | SPICED, MEDDIC, Challenger, SPIN, Gap Selling, multi-framework | v0.1.0 |
| `partner-channel-operations` | Partner program design, enablement, co-selling, deal registration | v0.1.0 |
| `abm-engagement-scoring` | Account-level engagement scoring, buying-group coverage, handover trigger doctrine | v0.3.0 |

### Pipeline and Data (5 skills)

| Skill | What it does | Since |
|---|---|---|
| `pipeline-visibility` | Pipeline reporting, dashboard design, hygiene, forecast reporting | v0.1.0 |
| `lead-routing` | Lead assignment logic, round-robin, territory design, speed-to-lead | v0.1.0 |
| `data-enrichment` | Enrichment strategy, provider evaluation, integration patterns | v0.1.0 |
| `revenue-operating-cadence` | Meeting architecture, data pyramid, board reporting | v0.1.0 |
| `gtm-data-architecture` | Warehouse-native GTM for operators: SQL fundamentals, dbt, reverse ETL, composable CDP | v0.4.0 |

### Pricing and Deal Operations (2 skills)

| Skill | What it does | Since |
|---|---|---|
| `pricing-monetization-ops` | Usage and outcome pricing operations: metering, rating, invoicing, reconciliation, contract drift | v0.4.0 |
| `deal-desk-operations` | Deal desk design: approval matrix, discount governance, credit and overage economics | v0.4.0 |

### ICP, Positioning, and Growth (6 skills)

| Skill | What it does | Since |
|---|---|---|
| `icp-builder` | Build and validate ICPs using the GAP method and SPICED framework | v0.1.0 |
| `positioning-messaging-designer` | Positioning frameworks using Use Case Canvas and Opposites method | v0.1.0 |
| `deal-velocity-engineer` | Sales cycle diagnostics, stage exit criteria, pipeline deflation | v0.1.0 |
| `expansion-revenue-architect` | NRR/GRR systems, whitespace analysis, CS-Sales handback | v0.1.0 |
| `partner-ecosystem-architect` | Ecosystem-led growth, nearbound methodology, partner strategy | v0.1.0 |
| `operating-cadence-designer` | Operating cadence design, rituals, dashboards, escalation rules | v0.1.0 |

---

## How they work together

Skills chain naturally. Start with a diagnostic, then load the specialist.

- **Diagnose then fix:** `revops-diagnostic` finds the constraint → load the relevant specialist skill
- **ICP to pipeline:** `icp-builder` → `positioning-messaging-designer` → `sales-methodology`
- **Deal flow:** `deal-velocity-engineer` → `pipeline-visibility` → `revops-forecasting`
- **Partner motion:** `partner-ecosystem-architect` → `partner-channel-operations` → `revops-handoffs`
- **Operating rhythm:** `operating-cadence-designer` → `revenue-operating-cadence` → `revops-metrics`
- **Data foundation:** `gtm-data-architecture` → `revops-data-governance` → `pipeline-visibility`
- **Monetization:** `pricing-monetization-ops` → `deal-desk-operations` → `gtm-compensation`
- **Post-merger:** `crm-migration-consolidation` → `revops-data-governance` → `revops-hubspot` or `revops-salesforce`

---

## Versioning

The library uses semantic versioning, tracked in [CHANGELOG.md](CHANGELOG.md):

- **MINOR (v1.x.0):** new skills, or substantive new capability inside existing skills (new frameworks, new sections, benchmark refreshes that change recommendations).
- **PATCH (v1.x.y):** corrections, sourcing fixes, typography, small clarifications. No new capability.
- **MAJOR (v2.0.0):** renames, folder restructures, or removals that break an existing install.

Release discipline: every release updates the CHANGELOG, the version line at the top of this README, the skill count, and the Since column for any new skill. Benchmarks inside skills carry their own source and vintage inline (for example "(Benchmarkit, 2026)"), so a skill's numbers are auditable independently of the library version.

---

## What's not here

These are the generic operational layer: the frameworks and methodology that any B2B revenue team can use independently.

These skills provide frameworks for self-serve implementation. They won't run a discovery call, facilitate a workshop, or hold your leadership team accountable to a new operating cadence. If you need implementation support beyond self-service skills, consider engaging a revenue operations consultant.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The bar is intentionally high.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT, see [LICENSE](LICENSE).

---

Built by [Rutger Katz](https://www.linkedin.com/in/rutgerkatz/) / [Neon Triforce](https://neontriforce.com)
