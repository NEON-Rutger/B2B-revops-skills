# Changelog

All notable changes to Neon RevOps are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [v1.0.0], 2026-07-15

### Declared stable
- The library graduates to 1.0.0. The gate: a full adversarial red team of all skills against
  the 2026 market (job-market capability taxonomy, live benchmark verification, platform
  currency, EU regulation), every confirmed finding patched and independently verified, four
  white-space skills added, all benchmarks source-and-vintage encoded, and a neutral-voice pass
  so the skills read as tools rather than marketing.
- All 34 skills set to status: stable in frontmatter (previously a mix of seed/production/active).
- From here, semver applies with post-1.0 semantics: MAJOR for breaking renames or restructures,
  MINOR for new skills or new capability, PATCH for corrections.

---

## [v0.4.2], 2026-07-15

### Changed
- Neutral voice pass: 152 in-content brand mentions across 48 skill files reduced to zero.
  House benchmark labels renamed from brand-prefixed to "(practice-based)"; house thresholds,
  operating defaults and worked-example framing rewritten in neutral practitioner voice.
  What deliberately remains: the one-line "Built by Neon Triforce" byline at the foot of each
  skill and two source-attribution credits. Skills now read as generic tools; the branding
  lives in the bylines and the README.

---

## [v0.4.1], 2026-07-15

### Changed
- De-branding pass: this library is the generic layer, and 20 files carried private or
  Neon-specific residue. Cross-references to private canon skills repointed to their public
  equivalents (icp-builder, deal-velocity-engineer, expansion-revenue-architect,
  revenue-operating-cadence, deal-desk-operations); wiki-link syntax converted to plain skill
  references; retired internal offer names and personal references genericised; internal
  research-sheet citations replaced with their underlying named sources; a private vault path
  removed; the crm-migration-consolidation worked example de-identified to a generic
  billing-platform scenario.

---

## [v0.4.0], 2026-07-15

### Added
- Four new skills from the 2026-07-15 red-team white-space analysis: crm-migration-consolidation
  (CRM merge and post-merger integration with a PE lens: system-of-record per object, identity
  resolution and survivorship, ID crosswalk, ten-step sequencing), pricing-monetisation-ops
  (usage and outcome pricing operations: metering, rating, invoicing, collections, reconciliation,
  contract term tracking and drift detection), deal-desk-operations (approval matrix, discount
  governance, credit and overage economics, desk metrics), gtm-data-architecture (warehouse-native
  GTM for operators: SQL fundamentals, dbt, reverse ETL with reconciliation cadence, composable CDP,
  when not to go warehouse-native). Each ships with a sourced benchmarks reference.

### Changed
- All 30 existing skills patched against adversarially verified red-team findings:
  - Benchmark encoding standard applied throughout: every number carries an inline source and
    vintage or an explicit practice-based label; unverifiable claims removed. 2026 market shifts
    propagated (median win rate 19% vs 29% in 2024, GRR median 84%, coverage as 1/win-rate,
    Magic Number 1.37, Rule of 40 on FCF basis).
  - 2026 platform currency: HubSpot Breeze agents and outcome-based pricing, Data Hub rebrand,
    Salesforce Flow-only automation, Agentforce 360, Data 360, Foundations credit model.
  - AI-native sections added where 2026 practice demands them (AI-assisted forecasting, churn
    prediction and agentic CS tiers, LLM enrichment and waterfall design, predictive routing,
    AI deal scoring).
  - EU compliance guardrails added to data and outbound skills: legitimate interest assessments,
    GDPR Article 14 source trails, Article 21 objection handling, Schrems II supplementary
    safeguards, lawful-basis and vendor-DPA gates, data minimisation notes.
  - Kyle Norton podcast citations resolved to full episode metadata with URLs; MEDDIC attribution
    corrected to John McMahon and Dick Dunkel at PTC; typographic cleanup repo-wide.
  - Missing revops-revenue-planning reference files created (planning assumptions, plan versioning
    governance, reforecasting benchmarks).

---

## [v0.3.0], 2026-07-14

### Added
- New skill: revops-revenue-planning. Annual/quarterly plan construction, top-down vs
  bottoms-up reconciliation, stretch handling, plan versioning (plan of record vs working
  plan), FP&A collaboration charter, reforecast triggers, 12-week planning calendar,
  10-question diagnostic. Includes two generated workbook assets (capacity-model-calculator,
  bottoms-up-planning-sheet; regenerate via scripts/generate_workbooks.py; 16 structure tests).
- New skill: abm-engagement-scoring. Account-level engagement scoring, buying-group/DMU
  coverage tracking, marketing-to-sales handover trigger doctrine, measurement dashboard
  spec, 200-account worked example, sourced ABM benchmarks.
- Benchmark files in both skills passed an adversarial source-verification pass: unverifiable
  claims removed and registered; house operating defaults separated from sourced research.

---

## [v0.2.0], 2026-07-05

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

## [v0.1.0], 2026-04-02

### Added

**RevOps Core (12 skills)**
- `revops-strategy`, revenue operations strategy and pipeline architecture
- `revops-diagnostic`, system diagnostics and constraint identification
- `revops-metrics`, revenue measurement, funnel math, unit economics
- `revops-forecasting`, forecast methodology and pipeline analysis
- `revops-data-governance`, data governance and field management
- `revops-tech-stack`, tech stack architecture and platform evaluation
- `revops-handoffs`, revenue handoff design across the bow-tie model
- `revops-change-management`, change management for RevOps adoption
- `revops-crisis`, emergency response for broken revenue systems
- `revops-org-chart`, RevOps team design and hiring sequencing
- `revops-hubspot`, HubSpot implementation patterns
- `revops-salesforce`, Salesforce implementation patterns

**GTM and Domain (6 skills)**
- `gtm-planning`, GTM motion selection, territory and capacity planning
- `gtm-compensation`, compensation plans, quota setting, OTE structures
- `marketing-operations`, lead scoring, attribution, campaign tracking
- `cs-operations`, customer success operations and renewal management
- `sales-methodology`, SPICED, MEDDIC, Challenger, SPIN, Gap Selling
- `partner-channel-operations`, partner programme design and co-selling

**Pipeline and Data (4 skills)**
- `pipeline-visibility`, pipeline reporting and dashboard design
- `lead-routing`, lead assignment logic and territory design
- `data-enrichment`, enrichment strategy and provider evaluation
- `revenue-operating-cadence`, meeting architecture and board reporting

**ICP, Positioning, and Growth (6 skills)**
- `icp-builder`, ICP development using the GAP method and SPICED framework
- `positioning-messaging-designer`, positioning using Use Case Canvas and Opposites method
- `deal-velocity-engineer`, sales cycle diagnostics and stage exit criteria
- `expansion-revenue-architect`, NRR/GRR systems and whitespace analysis
- `partner-ecosystem-architect`, ecosystem-led growth and nearbound methodology
- `operating-cadence-designer`, operating cadence design with rituals and dashboards

### Notes

- MIT licence
- Skills are standalone markdown files compatible with Claude Code `.claude/skills/` directory
- Each skill chains naturally with related skills (see README for recommended workflows)

---

[v0.2.0]: https://github.com/NEON-Rutger/B2B-revops-skills/releases/tag/v0.2.0
[v0.1.0]: https://github.com/NEON-Rutger/B2B-revops-skills/releases/tag/v0.1.0
