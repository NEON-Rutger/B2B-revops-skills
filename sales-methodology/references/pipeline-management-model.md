# Pipeline Management Operating Model

On-demand reference for the sales-methodology skill.

**Source:** Adapted from Union Square Consulting's Pipeline Management Pyramid. Neon applies this as the operational complement to SPICED — SPICED tells you how to run the conversation; this tells you how to run the pipeline. SPICED qualifies deals; this section operationalizes the full pipeline management model around SPICED — from stage entry criteria to inspection cadence to forecasting.

## Stage Entry/Exit Criteria

Every deal stage needs explicit criteria for what must be true to enter and exit. Without this, stages become meaningless labels and pipeline data reflects rep optimism, not deal reality.

```
STAGE           ENTRY CRITERIA                           EXIT CRITERIA
────────────    ──────────────────────────────────       ──────────────────────────────────
Discovery       - Contact identified as ICP fit          - SPICED S+P scored ≥ 2 each
                - Initial meeting booked/completed       - Pain validated (not assumed)
                - Contact record created in CRM          - Next meeting booked

Qualification   - SPICED S+P+I scored                    - SPICED total ≥ 8/15
                - Decision process understood            - Economic buyer identified
                - Budget range confirmed                 - Timeline established
                - Competition known                      - Champion identified

Solution        - Solution mapped to validated pain      - Solution presented to buyer
Design          - Pricing model selected                 - Objections captured
                - Internal resources confirmed           - Technical validation complete
                - Proposal/SOW drafted                   - Champion coaching delivered

Negotiation     - Proposal delivered to decision-maker   - Terms agreed (verbal)
                - Commercial terms discussed             - Legal/procurement engaged
                - Contract redlines received             - Signature timeline confirmed

Closed Won      - Contract signed                        - Handoff to CS initiated
                - Payment terms confirmed                - Onboarding scheduled
```

An alternative, more granular stage map (MQL through Closed Lost) with the same logic:

```
STAGE               ENTRY CRITERIA                          EXIT CRITERIA (must be true to advance)
─────               ──────────────                          ────────────────────────────────────────
MQL/Prospect        Meets ICP (firmographic + intent fit)   Responded to outreach / booked meeting

Discovery           Meeting booked                          SPICED partially captured: Situation +
                                                            Pain confirmed (minimum viable score ≥ 4)

Qualification       Pain confirmed, S+P+I captured          I+C+E captured; SPICED score ≥ 7;
                                                            Champion identified and engaged

Solution Presented  SPICED complete; solution scoped        Verbal acceptance of solution fit;
                                                            Proposal/pricing shared

Evaluation          Proposal shared                         Legal/procurement engaged or decision
                                                            timeline confirmed within period

Closed Won          Contract signed                         —
Closed Lost         Decision made in favour of competitor   Loss reason documented in CRM
                    or status quo; or deal abandoned
```

## Required CRM Fields by Stage

Every stage should mandate data capture before the deal advances. These are the minimum fields — adapt to your CRM workflow.

```
STAGE               REQUIRED CRM FIELDS
─────               ───────────────────
Discovery           Company size (ARR/headcount), current state, problem trigger
Qualification       Pain category, business impact (quantified if possible), decision process,
                    Champion name + role, critical event / deadline
Solution Presented  Solution scope, commercial model proposed, price range shared
Evaluation          Key stakeholders engaged, procurement/legal status, timeline confirmed
Closed              Win/loss reason, competitor (if applicable), ACV, close date
```

## Stocks & Questions by Stage

"Stocks" = the information inventory that should be captured at each stage. If the stock is empty, the deal shouldn't progress.

```
DISCOVERY STOCKS:                    QUESTIONS TO ASK:
  Situation context                  "How do you handle [X] today?"
  Pain statement (their words)       "What's the main friction?"
  Stakeholder map (initial)          "Who else is involved in this?"
  Current tools/process              "What have you tried before?"

QUALIFICATION STOCKS:                QUESTIONS TO ASK:
  Impact quantified (€/time)         "What would solving this be worth?"
  Critical Event identified          "When does this need to be resolved?"
  Decision process mapped            "Walk me through how you'd make this decision"
  Champion validated                 "Who internally is pushing for this?"
  Budget confirmed                   "Is there budget allocated for this?"

SOLUTION STOCKS:                     QUESTIONS TO ASK:
  Requirements documented            "What does success look like in 90 days?"
  Technical fit validated            "Any integration requirements I should know?"
  Objections surfaced                "What concerns does your team have?"
  Competition comparison             "Who else are you evaluating?"

NEGOTIATION STOCKS:                  QUESTIONS TO ASK:
  Decision criteria ranked           "What matters most in your final decision?"
  Contract redlines listed           "Are there standard procurement terms?"
  Concession limits defined          "What would make this a clear yes?"
  Timeline commitment                "When do you need to go live?"
```

## Disqualification / Deal Kill Criteria (When to Walk Away)

Explicit "close out" rules prevent pipeline pollution and wasted forecast capacity.

**Disqualify immediately if:**
- No identifiable pain connected to your solution after two discovery conversations
- Budget is 0 and there's no route to create budget within 2 quarters
- No executive sponsor or champion willing to engage
- Product fit gap confirmed (customer requirements outside capability)
- Company not in ICP (wrong segment, geography, or GTM motion)

**Put on hold (not disqualify) if:**
- Critical Event is more than 6 months out
- Champion leaves but relationship can be rebuilt
- Budget freeze expected to lift in next quarter

**Full deal kill criteria:**
- SPICED score < 4 after two discovery calls
- No access to economic buyer after qualification stage
- Critical Event keeps moving (no real urgency)
- Champion leaves the organisation
- Deal age > 2x average sales cycle with no stage progression
- Customer requirements outside product capability

**Staleness rule:** Any deal with no stage progression in > 1.5x your average sales cycle triggers a mandatory review. Either advance it or close it out.

## Pipeline Inspection Process

```
WEEKLY DEAL REVIEW (30 min per rep):
  Format: Rep walks through top 5 deals by expected close date
  Questions:
    1. What changed since last week?
    2. What's the next concrete step? (Not "follow up" — specific action)
    3. Is this deal on track for the forecast commit?
    4. What's blocking progress?
    5. Should we involve anyone else? (Champion coaching, exec sponsor)

  Manager actions:
    - Challenge: "What evidence do you have for that?" (test deal quality)
    - Coach: "Here's what I'd try next" (develop capability)
    - Redirect: "This deal is stuck — let's deprioritise or kill it"

MONTHLY PIPELINE COUNCIL (60 min, cross-functional):
  Attendees: Sales leader, Marketing leader, CS leader, RevOps
  Agenda:
    1. Pipeline health: coverage ratio, velocity, stage distribution
    2. Conversion analysis: which stages are leaking?
    3. Source analysis: which channels produce best-quality pipeline?
    4. Forecast review: commit vs actual trend
    5. Actions: what changes this month?

DEAL KILL CRITERIA (when to walk away):
  - SPICED score < 4 after two discovery calls
  - No access to economic buyer after qualification stage
  - Critical Event keeps moving (no real urgency)
  - Champion leaves the organisation
  - Deal age > 2x average sales cycle with no stage progression
  - Customer requirements outside product capability
```

Inspection cadence, framed around deal quality (not just deal volume):

**Weekly (individual rep + manager 1:1):**
- Review SPICED score for each Qualification+ deal
- Call out any deals advancing without meeting exit criteria
- Flag stale deals (no activity in 10+ business days)
- Confirm next best action for every deal in Evaluation

**Monthly (team pipeline review):**
- Review stage conversion rates vs. benchmarks
- Identify systematic gaps (e.g., low Discovery → Qualification conversion = qualification criteria too loose or too tight)
- Review closed-lost reasons and adjust ICP/disqualification criteria if patterns emerge

**Quarterly (revenue planning):**
- Reconcile pipeline coverage ratio vs. quota (minimum 3x for Commit, 4-5x for full quarter target)
- Adjust territory/capacity if pipeline generation is below coverage threshold
- Win/loss analysis: aggregate patterns across wins and losses to update SPICED calibration

## Forecast Categories

```
CATEGORY        DEFINITION                                    CRITERIA
────────        ──────────                                    ────────
Commit          Will close this period. Would bet my job.     - Verbal yes received
                                                              - Contract in legal/procurement
                                                              - Signature expected within period

Best Case       High probability, needs 1-2 things to land.  - Solution presented and accepted
                                                              - Budget confirmed
                                                              - Decision timeline within period
                                                              - No known blockers

Upside          Could close but significant unknowns remain.  - Qualified (SPICED ≥ 8)
                                                              - Champion engaged
                                                              - Timeline plausible but not committed

Pipeline        Active opportunities, too early to forecast.   - In Discovery or early Qualification
                                                              - Building relationship
                                                              - Not yet forecast-ready
```

## Forecasting Methodology

See the revops-forecasting skill for full forecasting depth and methodology. The Forecast Categories above are the sales methodology layer — what reps commit and why. The pipeline management context:
- Commit deals must have all SPICED elements captured and a clear path to signature
- Best Case deals have a qualified champion but one or two open elements (e.g., procurement not yet engaged)
- Upside deals have enough SPICED for a reasonable call but timeline or decision process is unclear
- Pipeline deals are active but too early for the forecast — move to a category only when SPICED score ≥ 6

**Coverage discipline:** If Commit + Best Case < quota, the team doesn't have a forecasting problem — they have a pipeline generation problem. Escalate there, not at forecast accuracy.

For pipeline reporting architecture and dashboard design, see the pipeline-visibility skill.
