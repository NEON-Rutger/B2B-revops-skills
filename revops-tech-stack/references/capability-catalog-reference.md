# Capability Catalog. Intelligence and Automation Layers

On-demand reference for the revops-tech-stack skill.

These are the per-capability details for the stage-dependent Intelligence Layer and the Automation Layer. The core layering principle lives in SKILL.md; this file holds the capability-by-capability detail.

## The Intelligence Layer (Stage-Dependent)

Add these capabilities as the GTM matures and data volume justifies the investment.

```
CONVERSATION INTELLIGENCE ($10M+ ARR or 10+ reps):
  Capability: Turn sales conversations into coaching insights and
    deal intelligence
  Value: Manager leverage (coach 2x more reps without more meetings),
    competitive intelligence, methodology adherence tracking
  Architecture rule: Must integrate with CRM to tag deals with
    conversation insights. Standalone recording has minimal value.

BUYER INTENT & ENRICHMENT ($15M+ ARR or entering new segments):
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

REVENUE INTELLIGENCE / FORECASTING ($20M+ ARR):
  Capability: AI-assisted forecasting, pipeline analytics, deal
    scoring, trend analysis
  Value: Forecast accuracy improvement, risk identification, pattern
    detection across large deal volumes
  Architecture rule: Requires clean CRM data to work. If stage
    definitions are inconsistent and data is sparse, AI forecasting
    will produce confident-sounding garbage.
```

## The Automation Layer

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
  EU Compliance note: Enriched contact data requires Article 14 GDPR
    notification within one month of collection. Document data source
    per contact. ePrivacy geography: Netherlands permits B2B enrichment
    to corporate addresses; Germany and Austria require prior consent.
    France intermediate. Route enrichment vendors accordingly.
```
