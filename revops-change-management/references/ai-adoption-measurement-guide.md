# AI Adoption Measurement Guide

On-demand reference for the revops-change-management skill.

Usage metrics (% adoption, login frequency) lie. They tell you how often people click the tool, not whether the tool is actually changing work.

**Four dimensions of AI adoption (measure all four):**

| Dimension | What it measures | Key metrics |
|---|---|---|
| **Engagement** | Frequency and consistency of use | Daily/weekly active users %, sessions per user, feature adoption rate |
| **Behaviour** | How teams are actually interacting with outputs | Output acceptance rate, refinement/iteration rate, handoff patterns |
| **Capability** | Confidence and skill in using the tool effectively | Proficiency self-assessment, error reduction rate, time-to-competence |
| **Governance** | Oversight effectiveness and risk control | Incident reports, data handling compliance, audit pass rate |

**Complete measurement formula:**
Quantitative telemetry (tool logs, usage data) + qualitative insights (user interviews, team sentiment) = complete picture of adoption health.

**AI adoption KPI set (RevOps specific):**

```
Engagement tier:
- Active AI Users %: (unique users/total eligible) × 100. Target: 70%+ by month 6.
- AI Tool Engagement Rate: (weekly active sessions / total users) × 100. Target: 60%+ sustained.

Behaviour tier:
- Output Acceptance Rate: (outputs used as-is or refined / total outputs generated) × 100. Target: 65%+.
- Time Saved per Function: hours/week recovered from task automation. Target: 5 to 8 hrs/FTE/week.

Capability tier:
- Proficiency Score: (skill self-assessment + error rate reduction) / 2. Target: 3.5+/5 by month 4.
- Time-to-Value per Role: weeks to first meaningful productivity gain. Target: 3 to 4 weeks.

Governance tier:
- Incident Rate: (data breaches, compliance violations) per 1,000 active users. Target: <1 per month.
- Audit Pass Rate: % of samples meeting governance standards. Target: 98%+.
```

**ROI measurement (3-tier model):**

1. **Realized ROI** (months 1 to 3): Direct time savings and automation. Dollar value of hours freed. Easy to quantify. Usually overstated.

2. **Trending ROI** (months 3 to 9): Quality improvements (better proposals, higher qualification accuracy), faster decision cycles, reduced rework. Harder to quantify; requires baseline comparison.

3. **Capability ROI** (months 6 to 18): Organizational learning, capability uplift, competitive advantage from AI fluency. Hardest to measure; most valuable long-term. Frame as "organizational option value" (you've built a team that can scale AI further).

**Realistic expectations:**
- Expect 3 to 6 month ROI horizon, not 6 weeks
- First 6 weeks will show time investment (learning curve)
- Weeks 6 to 12 show usage and early efficiency gains
- Months 3 to 6 show behaviour change and quality improvements
- Month 6+ shows organizational capability gains
