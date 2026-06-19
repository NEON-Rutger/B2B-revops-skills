# AI Rollout: Five-Phase Playbook

On-demand reference for the revops-change-management skill.

This is your operational blueprint. Use it to sequence your AI adoption.

**Phase structure: Discover → Pilot → Scale → Embed → Govern**

Each phase has gates (go/no-go decisions), specific activities, and success metrics.

## Phase 1: Discover (Weeks 1–3)

**Goal:** Identify which processes, decisions, and teams benefit most from AI. Build business case.

**Activities:**
- Audit current processes: where's manual work, where do humans add low value, where's error-prone work?
- Prioritize by impact and ease (impact/effort matrix)
- Identify high-risk processes first (compliance-sensitive, data-heavy, error-prone)
- Build financial case: time savings, quality improvements, cost avoidance
- Check regulatory landscape (Works council notification if EU-based)

**Duration:** 2–3 weeks

**Success metrics:**
- 3–5 priority processes identified
- Business case quantified (conservative estimate OK here)
- Regulatory blockers identified (early)
- Executive alignment on first pilot

**Gate:** Proceed to Pilot when executive sponsor approves business case and pilot scope.

---

## Phase 2: Pilot (Weeks 4–8)

**Goal:** Test one AI application in a controlled environment with a small, engaged team. Prove concept. Learn what doesn't work.

**Two-week sprint structure (repeat as needed within pilot phase):**

```
SPRINT TEMPLATE: Scope → Baseline → Build → Run → Evaluate → Document

Week 1: Scope & Baseline
Day 1-2: Scope
  - Define the specific decision/task: "Qualification scoring for inbound leads"
  - Define AI tool: vendor, model, integration point
  - Define success: "AI scores match human qualification 80%+ of the time"
  - Define constraints: data available, team capacity, regulatory requirements

Day 3-4: Baseline
  - Measure current state: How long does qualification take? Accuracy? Who decides?
  - Document decision logic: What criteria does a human use to qualify?
  - Establish comparison: Can we run manual and AI in parallel for a week?

Week 2: Build & Run
Day 5-7: Build
  - Configure tool: connect data, set parameters, define rules
  - QA: test on historical data, validate outputs match expectations
  - Safety check: confirm no data leakage, no PII exposure, no bias amplification

Day 8-10: Run
  - Live pilot: 100–200 records through AI + human decision
  - Log: inputs, AI output, human decision, time taken
  - Weekly standups: team feedback, quick fixes to parameters
  - Incident log: any errors, any weird outputs, any governance issues

Week 3: Evaluate & Document
Day 11-12: Evaluate
  - Compare: AI vs human accuracy, speed, consistency
  - Sentiment: team feedback, adoption friction, confidence in tool
  - Financial: hours saved, quality improvements, cost-per-decision

Day 13-14: Document
  - Pilot report: what worked, what didn't, learnings
  - Process map: AI's new place in the workflow
  - Team playbook: how to use tool for next phase
  - Recommendation: scale, refine, or kill
```

**Pilot metrics (measure all):**
- **Accuracy:** AI decision vs. ground truth (human expert review). Target: 75%+ agreement.
- **Consistency:** Same input yields same output. Target: 95%+ (identify edge cases).
- **Speed:** Time per decision (AI vs. human). Target: 60%+ faster.
- **Adoption:** Team using tool without prompting. Target: 80%+ of available opportunities used.
- **Confidence:** Team trusts AI outputs (survey 1–5). Target: 3.5+.

**Kill criteria (when to stop an initiative):**
- Accuracy <65% (tool not reliable enough)
- Adoption <40% after 2 weeks (team doesn't want it)
- Data quality issues discovered (garbage in, garbage out)
- Governance blockers identified (regulatory issue, data sensitivity)
- Cost-per-use higher than manual process
- Team confidence score <2.5 (distrust too high)

**Gate:** Proceed to Scale when:
- Accuracy ≥75% OR team confident in outputs + clear remediation plan
- Adoption ≥60%
- No unresolved governance issues
- Financial case holds (ROI neutral or positive within 6 months)

---

## Phase 3: Scale (Weeks 9–16)

**Goal:** Expand from one team to 3–4 teams. Roll out with clear playbooks. Build confidence.

**Activities:**
- Expand to adjacent teams (similar roles, similar processes)
- Recruit change champions from pilot team (they become trainers)
- Weekly operational cadence: usage standup, issue triage, quick wins celebration
- Build skill: structured training, hands-on practice, certification (optional but effective)
- Gather feedback: monthly pulse survey, open suggestion channel

**Duration:** 6–8 weeks

**Success metrics:**
- 3–4 teams active, 60%+ usage rate
- Accuracy sustained (75%+) or improving
- Incident rate <1 per 100 active users
- Team confidence increasing (sentiment survey)
- Time savings realized and quantified

**Gate:** Proceed to Embed when:
- 60%+ of expanded user base actively using tool
- Business case metrics met (time saved, quality improved)
- No major governance incidents
- Process standardization documented

---

## Phase 4: Embed (Weeks 17–26)

**Goal:** Make AI usage standard operating procedure. Integrate into workflows, performance metrics, hiring.

**Activities:**
- Integrate AI into formal workflows: job descriptions updated, training mandatory, metrics tracked
- Add to onboarding: new hires trained on AI tools day 1
- Performance management: AI productivity (time saved, quality) becomes KPI
- Feedback loops: monthly review of outputs, retraining as needed
- Build organizational muscle memory: "this is how we work now"

**Duration:** 8–10 weeks

**Success metrics:**
- 80%+ usage rate sustained
- New hires up to speed within 2 weeks
- Accuracy stable or improving
- Productivity metrics show sustained gains
- Shadow AI usage declining (people using approved tools)

**Gate:** Move to Govern when:
- AI-enabled workflow is default, not optional
- Team competency normalized
- Business value clearly realized
- Regulatory compliance proven over time

---

## Phase 5: Govern (Ongoing, starting week 26+)

**Goal:** Ensure sustained use, manage risk, optimize continuously.

**Ongoing activities:**
- Monthly metrics review: usage, accuracy, incidents, cost-per-use
- Quarterly business review: is AI still delivering ROI? Should we expand?
- Continuous retraining: skill decay monitoring, refresher cadence
- Incident management: protocol for errors, data breaches, user issues
- Tool refresh: evaluate new models, update parameters, retire if outdated
- Works council reporting (EU): quarterly updates on usage, incidents, any changes

**Metrics (track forever):**
- Active user rate, engagement rate, output acceptance rate
- Incident rate, data governance compliance, audit pass rate
- Time saved per user, quality improvements (reduced rework)
- ROI (realized + trending + capability)

---

## Weekly Cadence During Implementation

Once you're in Pilot, Scale, or Embed, this is your rhythm:

```
WEEKLY STANDUP (30 min, Tuesdays 9am)
Attendees: Project lead, tool owner, team representatives, change champion

Agenda:
1. Usage: Are people using it? Adoption rate vs. target?
2. Issues: Any errors, data problems, user confusion?
3. Quick wins: What's working well? Celebrate it.
4. Blockers: What's slowing adoption? What needs fixing?
5. Forecast: What's coming next week?

Decision rights:
- Quick fix (parameter tweak, training gap): PM decides, implements by Thursday
- Larger issue (tool limitation, design change): escalate to steering, decide within 1 week
- Kill decision: steering committee vote (Weeks 1–4 of pilot)

OUTPUT:
- 1-pager: adoption %, issues, next week's focus
- Shared with sponsors, works council (EU), exec team
```

---

This framework takes 6–9 months from Discover to full Embed. That's realistic. GenAI adoption is not a 6-week sprint. It's a quarterly narrative.

Your biggest risk isn't the technology. It's abandoning the change process too early when adoption looks slow (weeks 4–6 is always slow), or trying to move faster than your organization can absorb.

Move at the speed of trust-building, not the speed of the technology.
