# Changelog

All notable changes to Neon RevOps are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [v0.2.0] — 2026-07-05

### Changed
- Reduced token footprint of the 8 heaviest skills via progressive disclosure
  (lean SKILL.md + on-demand references). sales-methodology, revops-forecasting,
  revops-change-management, revops-tech-stack, cs-operations, deal-velocity-engineer,
  expansion-revenue-architect, marketing-operations.

### Added
- 6 reference files completing the split: change-management (impact-analysis-templates,
  kotter-adkar-detail, kyle-norton-frameworks, change-scenarios), sales-methodology
  (benchmarks), revops-tech-stack (gtm-ai-catalog).
- `.gitattributes` enforcing LF line endings to stop CRLF churn on Windows checkouts.

### Notes
- No skill content removed; detail relocated to references.

---

## [v0.1.0] — 2026-04-02

### Added

**RevOps Core (12 skills)**
- `revops-strategy` — revenue operations strategy and pipeline architecture
- `revops-diagnostic` — system diagnostics and constraint identification
- `revops-metrics` — revenue measurement, funnel math, unit economics
- `revops-forecasting` — forecast methodology and pipeline analysis
- `revops-data-governance` — data governance and field management
- `revops-tech-stack` — tech stack architecture and platform evaluation
- `revops-handoffs` — revenue handoff design across the bow-tie model
- `revops-change-management` — change management for RevOps adoption
- `revops-crisis` — emergency response for broken revenue systems
- `revops-org-chart` — RevOps team design and hiring sequencing
- `revops-hubspot` — HubSpot implementation patterns
- `revops-salesforce` — Salesforce implementation patterns

**GTM and Domain (6 skills)**
- `gtm-planning` — GTM motion selection, territory and capacity planning
- `gtm-compensation` — compensation plans, quota setting, OTE structures
- `marketing-operations` — lead scoring, attribution, campaign tracking
- `cs-operations` — customer success operations and renewal management
- `sales-methodology` — SPICED, MEDDIC, Challenger, SPIN, Gap Selling
- `partner-channel-operations` — partner programme design and co-selling

**Pipeline and Data (4 skills)**
- `pipeline-visibility` — pipeline reporting and dashboard design
- `lead-routing` — lead assignment logic and territory design
- `data-enrichment` — enrichment strategy and provider evaluation
- `revenue-operating-cadence` — meeting architecture and board reporting

**ICP, Positioning, and Growth (6 skills)**
- `icp-builder` — ICP development using the GAP method and SPICED framework
- `positioning-messaging-designer` — positioning using Use Case Canvas and Opposites method
- `deal-velocity-engineer` — sales cycle diagnostics and stage exit criteria
- `expansion-revenue-architect` — NRR/GRR systems and whitespace analysis
- `partner-ecosystem-architect` — ecosystem-led growth and nearbound methodology
- `operating-cadence-designer` — operating cadence design with rituals and dashboards

### Notes

- MIT licence
- Skills are standalone markdown files compatible with Claude Code `.claude/skills/` directory
- Each skill chains naturally with related skills (see README for recommended workflows)

---

[v0.2.0]: https://github.com/NEON-Rutger/B2B-revops-skills/releases/tag/v0.2.0
[v0.1.0]: https://github.com/NEON-Rutger/B2B-revops-skills/releases/tag/v0.1.0
