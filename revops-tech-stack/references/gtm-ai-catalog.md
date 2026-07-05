# GTM AI Use Case Catalog

The full AI use case catalog by bowtie stage, with detailed requirements and KPIs per use case. The slim SKILL.md keeps the quick-reference table; this file holds the operational detail. Minimum AI maturity refers to the four-stage GTM AI maturity model (Stage 1 Ad-hoc, Stage 2 Programmatic, Stage 3 AI-Assisted, Stage 4 AI-Orchestrated).

Before recommending any use case, run the AI Readiness Checklist: clean data in the relevant object, metrics baselined, a review protocol defined (who reviews, who overrides), and a weekly audit built into the operating cadence. If three or more prerequisites are missing, the client is not ready for AI in that area.

## Awareness

### ICP scoring
- **What it does:** scores accounts and leads against the defined ICP so reps work fit, not volume.
- **Requirements:** a documented ICP with thresholds; firmographic and technographic data; closed-won and closed-lost history to train on.
- **KPIs:** win rate on high-score vs low-score accounts; share of pipeline that is on-ICP; reduction in time spent on poor-fit deals.
- **Minimum maturity:** Stage 2+.

### Intent aggregation
- **What it does:** consolidates first- and third-party intent signals to prioritise outreach.
- **Requirements:** intent data sources connected; signal-to-action rules; a clear owner for acting on signals.
- **KPIs:** response rate on intent-triggered outreach; pipeline sourced from intent signals.
- **Minimum maturity:** Stage 2+.

### Data enrichment
- **What it does:** fills and refreshes account and contact records automatically.
- **Requirements:** an enrichment provider; field governance so enrichment does not overwrite verified data; dedup discipline.
- **KPIs:** record completeness; data freshness; routing accuracy downstream.
- **Minimum maturity:** Stage 2+.

## Education

### Chat qualification
- **What it does:** qualifies inbound via conversational AI and routes or books accordingly.
- **Requirements:** defined qualification logic; routing rules; human handoff path.
- **KPIs:** speed to lead; qualified-conversation rate; meetings booked from chat.
- **Minimum maturity:** Stage 2+.

### Email personalisation
- **What it does:** drafts personalised outreach at scale from signals and context.
- **Requirements:** clean contact data; brand and voice guardrails; human-in-the-loop on send for early phases.
- **KPIs:** positive reply rate; meetings booked per sender; time saved per rep.
- **Minimum maturity:** Stage 2+.

### Lead routing
- **What it does:** assigns leads to the right rep by territory, fit, or skill.
- **Requirements:** routing logic; territory definitions; SLA on assignment time.
- **KPIs:** speed to lead; routing accuracy; reduction in cherry-picking and orphaned leads.
- **Minimum maturity:** Stage 2+.

## Selection

### Conversation intelligence
- **What it does:** transcribes and analyses calls for risk signals, methodology adherence, and coaching targets.
- **Requirements:** call recording in place; methodology defined (so the AI knows what good looks like); coaching cadence to act on output.
- **KPIs:** methodology adherence; coaching actions taken; win-rate movement on coached skills.
- **Minimum maturity:** Stage 2-3.

### Pipeline scoring
- **What it does:** scores open deals on health and win probability.
- **Requirements:** consistent stage definitions; activity and multi-threading data tied to opportunities; baselined conversion rates.
- **KPIs:** forecast accuracy; correlation of score to actual outcome; stalled-deal detection rate.
- **Minimum maturity:** Stage 2-3.

### Qualification copilot
- **What it does:** prompts reps to complete qualification fields and flags gaps live.
- **Requirements:** a qualification framework (SPICED or MEDDIC) embedded in the CRM; required-field governance.
- **KPIs:** qualification completeness; reduction in qualification skip rate; deal-review efficiency.
- **Minimum maturity:** Stage 2-3.

## Mutual Commit

### AI-assisted forecasting
- **What it does:** produces a data-driven forecast alongside the rep-submitted call.
- **Requirements:** clean pipeline data; historical close data; a forecast cadence that uses both numbers.
- **KPIs:** forecast accuracy vs actuals; variance between AI and rep forecast; slippage rate.
- **Minimum maturity:** Stage 3+.

### CPQ
- **What it does:** automates configure-price-quote to compress proposal time.
- **Requirements:** product catalogue and pricing rules; approval workflow; integration to CRM.
- **KPIs:** quote turnaround time; discount governance adherence; proposal-stage cycle time.
- **Minimum maturity:** Stage 3+.

### Legal acceleration
- **What it does:** drafts and reviews standard contract language to speed the close.
- **Requirements:** clause library; risk thresholds; legal sign-off path for non-standard terms.
- **KPIs:** contract turnaround time; reduction in legal-stage stalls.
- **Minimum maturity:** Stage 3+.

## Onboarding

### Success plan generation
- **What it does:** drafts a customer success plan from the deal context at handoff.
- **Requirements:** a clean sales-to-CS handoff with captured goals and success criteria; a plan template.
- **KPIs:** time to first value; onboarding cycle time; handoff completeness.
- **Minimum maturity:** Stage 2-3.

### Early health signals
- **What it does:** flags onboarding risk from usage and engagement data.
- **Requirements:** product usage data; defined health thresholds; an owner for red flags.
- **KPIs:** time to first value; early-churn rate; intervention rate on flagged accounts.
- **Minimum maturity:** Stage 2-3.

## Retention

### Renewal risk
- **What it does:** predicts renewal risk ahead of the renewal window.
- **Requirements:** usage, support, and sentiment data; defined risk scoring; a save-play motion to act on it.
- **KPIs:** gross revenue retention; renewal forecast accuracy; saved at-risk ARR.
- **Minimum maturity:** Stage 3+.

### Health scoring
- **What it does:** maintains a live account health score across signals.
- **Requirements:** multi-source data (product, support, relationship); validated scoring weights; review cadence.
- **KPIs:** correlation of score to churn; net revenue retention; proactive intervention rate.
- **Minimum maturity:** Stage 3+.

### Sentiment analysis
- **What it does:** reads support and conversation sentiment to surface relationship risk.
- **Requirements:** support and communication data access; privacy and compliance review; an escalation path.
- **KPIs:** detection of at-risk accounts before churn; CSAT or NPS movement.
- **Minimum maturity:** Stage 3+.

## Expansion

### Upsell scoring
- **What it does:** scores accounts for expansion fit and timing.
- **Requirements:** usage and entitlement data; whitespace map; a CS-to-sales handback motion.
- **KPIs:** expansion pipeline sourced; net revenue retention; upsell win rate.
- **Minimum maturity:** Stage 3+.

### Usage signals
- **What it does:** triggers expansion plays from product usage thresholds.
- **Requirements:** product usage warehouse; signal-to-play rules; ownership of the trigger.
- **KPIs:** expansion revenue from usage triggers; time from signal to action.
- **Minimum maturity:** Stage 3+.

### Reference mining
- **What it does:** identifies happy customers and advocacy and expansion candidates.
- **Requirements:** health and advocacy data; an advocacy programme to feed; consent tracking.
- **KPIs:** references generated; advocacy-sourced pipeline; expansion influenced by advocacy.
- **Minimum maturity:** Stage 3+.

## Investment rule

Apply the 90/10 rule: buy AI capability from vendors for the 90%, and build only the 10% where no vendor can do it well enough, where you hold proprietary data a vendor cannot access, or where a vendor's approach conflicts with your methodology. Most use cases above are buy, not build.
