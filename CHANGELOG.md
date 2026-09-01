# Changelog

All notable changes to the RevOps Skills Library are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [v1.6.0], 2026-09-01

### Added
- `comp-plan-architecture`: the system around compensation, complementing
  gtm-compensation's plan mechanics. Sequencing law (comp is settled last),
  crediting and attribution rulebook with the three failure modes, comp governance
  (committee, dispute SLA, the five documents), post-merger harmonization with CCOS
  as the reconciliation currency, European legal constraints on changing variable
  pay across nine jurisdictions (NL, DE with confirmed BAG 1 ABR 57/82, FR with
  confirmed Cass. soc. 7 Jan 2026 n° 24-18.742, UK fire-and-rehire Code 2024, IE,
  ES art. 41 ET, IT CCNL layers, SE MBL, DK notice rule), IFRS 15 / ASC 606
  commission capitalization as a design constraint, and SPM tooling selection with
  vendor-advocacy figures labeled as such.
- `saas-pnl-reading`: financial statements for commercial operators. The three
  statements and which one to believe, fast triage, P&L anatomy with the
  classification-flattery table, ARR bridge vs recognized revenue vs billings vs
  cash including cash flow statement structure, EBITDA add-backs and which to
  challenge, board pack red-flag catalogue (presentation, accounting, business,
  governance), and the two-way RevOps-finance translation table. Deliberately
  carries no benchmark norms; defers to revops-metrics.

Both adapted from privately built and fresh-agent-reviewed originals: US spelling,
canon references replaced with in-library siblings, all legal and accounting
findings from the review round already applied.

---

## [v1.5.3], 2026-09-01

### Added
- `positioning-messaging-designer`: Step 0 interview-first gate added before positioning
  canvas work. Founder interview template moves to new reference file
  `references/founder-interview-intake.md` with structured triads (brokenness, why,
  fix) and interchangeability diagnosis. Prevents fiction-based positioning by
  grounding the canvas in founder language.
- `revops-data-governance`: Identity resolution gate (section 4b) added before record
  creation, with four-decision rubric (Link/Create/Review/Reject) and evidence-based
  match scoring. New reference file `references/identity-resolution-rubric.md` carries
  account and contact matching scores and conflict rules. Outbound readiness gate
  (section 4c) with five gates (identity, ownership, reachability, context, fit) and
  worked cleanup sequencing example (identity fixes first, then ownership, then pipeline).
- `deal-velocity-engineer`: Call diagnosis section added for evidence-bound PULL analysis
  (Project, Unavoidable, List of options, Limitations). New reference file
  `references/pull-call-diagnosis.md` carries diagnostic template, worked example,
  and red-flag detection rules. Every claim backed by transcript quote; seller
  performance assessment (testing vs listening); pitch fit validation.

---

## [v1.5.2], 2026-09-01

### Changed
- Listing repositioning across 10 skills (abm-engagement-scoring, cs-operations,
  data-enrichment, deal-desk-operations, deal-velocity-engineer,
  pricing-monetization-ops, revops-data-governance, revops-forecasting,
  revops-handoffs, revops-hubspot): descriptions rewritten pain-first with one
  quotable rule per skill and a compact trigger-phrase tail, replacing the
  keyword-wall openers. Vendor tool names removed from descriptions. Stray
  top-level BOUNDARY frontmatter keys removed (deal-desk-operations,
  pricing-monetization-ops). A What good looks like section added to each of
  the 10 skills. pricing-monetization-ops marketplace category moves from
  Pricing to RevOps.

---

## [v1.5.1], 2026-09-01

### Changed
- `win-loss-program`: third evidence lane added, the customer arena (lean
  klantarena format): 5-8 customers talking, the cross-functional team in the
  listening seats, chronological journey spine, every friction point tagged
  product or process so one session improves the roadmap and the sales motion
  from the same evidence. Analytics tell you what; the arena tells you why.
  Also: the two-quarter self-audit (CRM fields vs interview findings divergence
  table) promoted from the reference into the skill body.
- Cold-review fixes across the v1.5.0 batch: trial benchmark table carries its
  data-quality qualifier inline; the onboarding activation-transfer assumption
  now states its local-validation job in the body; ramp benchmark sentence
  separates the surveyed Bridge Group figure from directional aggregations; the
  procurement cycle-time stat clarified as total deal cycle, not contracting
  phase; practice-based labels added to two rules; win-loss BOUNDARY names
  sales-ramp-enablement as the enablement-output consumer.

---

## [v1.5.0], 2026-09-01

### Added
- `trial-poc-conversion`: evaluations that end in a decision. Motion picker with
  per-motion benchmark ranges, the four-part entry gate (success criteria, then-what,
  committee, clock), activation-first design, midpoint readout, disciplined endings,
  and zombie-trial hygiene. a16z Enterprise Survey (2026) buyer-expectation data;
  trial aggregation ranges flagged as blog-tier with direction-only reliance.
- `win-loss-program`: two evidence lanes over decided deals: transcript/thread mining
  on every decision, buyer interviews on a sample, both outcomes. Neutral-interviewer
  rule, decision-driver taxonomy with weighted multi-cause coding, quarterly
  quote-anchored readout, outputs routed to revival, enablement, battlecards, and
  qualification gates.
- `onboarding-activation`: the signature-to-first-value system. Activation as one
  observable event, the handoff artifact that carries why-they-bought across the
  signature, evidence-gated 30-60-90 arc, three stall signals with named responses,
  graduation with an agreed value baseline feeding qbr-ebr-builder.
- `sales-ramp-enablement`: ramp as an instrumented system. Ramp math into
  capacity/forecast (ramped-equivalents), evidence-gated certification arc with a
  three-outcome gate rule, enablement measured by cohort leading indicators, manager
  cadence minimums. Bridge Group (2023) anchor; unverifiable ramp multipliers
  excluded.
- `procurement-navigation`: from 'you're selected' to signature. Early gauntlet
  mapping with the champion, the standing artifact pack, parallel-by-design mutual
  close plans, Commit-grade status only with enumerated steps, concessions traded
  never given. Ebsta x Pavilion (2025) cycle-length data as the stakes.

### Fixed
- The four v1.2.0/v1.3.0 skills were missing the library byline; added.

---

## [v1.4.4], 2026-09-01

### Fixed
- README was out of sync with the library: the skill count, both category tables, and the
  "how they work together" chains had never been updated for the four skills that shipped
  in v1.2.0 and v1.3.0 (`closed-lost-revival`, `deal-qualification-gates`,
  `renewal-save-motion`, `qbr-ebr-builder`). Corrected skill count 34 → 38, added the
  missing rows with their `Since` versions, and added four chain entries. No skill content
  changed.

---

## [v1.4.3], 2026-08-26

### Changed
- `deal-qualification-gates`: SPICED referred to generically in the skill body and the
  frameworks reference (vendor-name-free public copy).

---

## [v1.4.2], 2026-08-24

### Fixed
- Citation corrections after external review of the ICP scoring update: the in-market
  share stat re-attributed from Gartner to its actual source (the 95:5 rule,
  Ehrenberg-Bass Institute, 2021); the first-vendor-wins figure now cited to the
  6sense Buyer Experience Report (2024); the Gartner AI-project figure restated as
  the prediction it is (February 2025, horizon 2026) in six skills; phantom
  "OpenView 2024/2024-2025" vintages corrected in the expansion and pricing skills
  (OpenView's final edition is 2023; High Alpha continues the series); an
  unverifiable PLG NRR comparison replaced with the underlying judgment; icp-builder's
  platform section de-priced (per-unit agent rates and end-of-support dates removed).

---

## [v1.4.1], 2026-08-21

### Changed
- Library-wide: framework sections now stand on their own. Section headers, inline
  credits, "Source Attribution" tails, and lineage blocks that described where a
  framework or model originated were removed across 37 files; four reference files
  were renamed to describe their content (`enablement-frameworks`,
  `forecast-variance-and-capacity`, `inbound-flip-strategy`,
  `composability-maturity-detail`) with all links updated. Benchmark numbers keep
  their data source and year throughout; named quotations were rewritten as plain
  principles. No framework content was removed or altered in substance.

---

## [v1.4.0], 2026-08-21

### Changed
- `icp-builder`: fit scoring model added as Output 2a (best-customer scorecard with
  multiplied 1-5 ratings, 5-8 discriminating attributes across the three pillars,
  weights out of 100 with per-segment weight sets, tier bands 80/50); tier table now
  carries fit-score bands and feeds from the model, never from feel. New Section 7.5
  TAM List Production: seven-step standing loop (define universe with source-coverage
  rule, enrich including the website-quality signal, score before activation, select
  tiers against capacity, activate known-fit only, validate via cycle times, quarterly
  keep-alive). New validation red flags: CRM-only evidence base as survivorship bias,
  and the score-0-100-or-it's-an-opinion test on CRM operationalization. New
  "What good looks like" section; technographic example made vendor-free; gate
  layer refers to SPICED generically. Skill description and reference index
  updated to match.

---

## [v1.3.0], 2026-08-14

### Added
- `qbr-ebr-builder`: customer-facing business reviews as a value instrument. QBR/EBR
  split by audience, three-panel spine (look back in their numbers / current state
  honestly / look forward jointly owned), segmentation with async-summary long tail,
  attendance drift as a risk signal. Deliberately excludes vendor-marketing QBR
  statistics; practice-based rules labeled as such.

### Changed
- `revops-forecasting`: new "Evidence-Based Forecast Inputs" subsection: four-source
  deal reads (CRM claim, conversation evidence, product usage, signal memory),
  evidence-wins-the-argument rule, bridge to deal-qualification-gates for Commit
  validation and to renewal-save-motion for the renewal slice.
- `closed-lost-revival`: consume-verified-movers rule added for installations that already
  run a standing champion-move monitor.
- `deal-qualification-gates`: added two verified stats from the Ebsta x Pavilion 2025
  dataset (sub-50-day deals win ~47% vs ~20%; early economic-buyer involvement lifts
  win rates ~55%) with an explicit note that this remains the latest full dataset as
  of August 2026.

---

## [v1.2.0], 2026-08-14

### Added
- `closed-lost-revival`: quarterly revival sweep over closed-lost deals, gone-quiet
  proposals, champion job changes, and engaged-then-quiet threads. Three gated lanes,
  a loss-pattern library, campaign compression (5-15 cap), and a human approval
  contract. Fills a marketplace-wide gap: no closed-lost or win-back skill existed.
- `deal-qualification-gates`: evidence-quality scoring (1-5 per qualification
  dimension), per-stage minimum scores, the critical-event forcing question, and
  qualify-or-kill reviews. Extends the gate layer added to icp-builder in the prior
  commit into a full deal-level skill; SPICED default with MEDDICC/BANT mapping in
  references.
- `renewal-save-motion`: the defensive counterpart to expansion. Renewal clock from
  T-120, five-way risk triage, ordered commercial levers (discount last), release-well
  protocol, and save-rate scorekeeping by failure mode. Benchmarks source-and-vintage
  encoded in references.

---

## [v1.1.1], 2026-08-04

### Removed
- Maintenance: consolidated the ICP reference set down to the generic methodology files
  (icp-building-reference, spiced-icp-fit-matrix) and removed internal working files and
  a build log that were never meant to be part of the published library. Example company
  names in the sales-methodology cluster table replaced with archetype descriptions.
  All pointers updated.

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
- De-branding pass: standardized the library as a self-contained generic layer.
  Cross-references now point only to skills that exist in this repo (icp-builder,
  deal-velocity-engineer, expansion-revenue-architect, revenue-operating-cadence,
  deal-desk-operations); wiki-link syntax converted to plain skill references; citations
  normalized to their underlying named sources; the crm-migration-consolidation worked
  example generalized to a generic billing-platform scenario.

---

## [v0.4.0], 2026-07-15

### Added
- Four new skills from the 2026-07-15 red-team white-space analysis: crm-migration-consolidation
  (CRM merge and post-merger integration with a PE lens: system-of-record per object, identity
  resolution and survivorship, ID crosswalk, ten-step sequencing), pricing-monetization-ops
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
    safeguards, lawful-basis and vendor-DPA gates, data minimization notes.
  - Citation metadata completed; typographic cleanup repo-wide.
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
  kotter-adkar-detail, enablement-frameworks, change-scenarios), sales-methodology
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
- `partner-channel-operations`, partner program design and co-selling

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

- MIT license
- Skills are standalone markdown files compatible with Claude Code `.claude/skills/` directory
- Each skill chains naturally with related skills (see README for recommended workflows)

---

[v0.2.0]: https://github.com/NEON-Rutger/B2B-revops-skills/releases/tag/v0.2.0
[v0.1.0]: https://github.com/NEON-Rutger/B2B-revops-skills/releases/tag/v0.1.0
