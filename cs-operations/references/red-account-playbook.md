# Red Account Playbook

On-demand reference for the cs-operations skill.

Signals aren't enough. Define the playbook triggers — what happens automatically when a customer turns Red.

## Immediate Actions (within 24 hours of Red flag)

1. CSM notifies CS Lead
2. CS Lead reviews health breakdown — which dimension is driving Red? (Usage? Engagement? NPS? Adoption?)
3. CS Lead and AE jointly decide: rescue mode or renewal risk conversation

## Rescue Mode (if > 90 days until renewal)

- Executive outreach: CS Lead or Head of CS calls the economic buyer directly
- Root cause session: structured call to understand what went wrong
- Recovery plan: documented list of 3-5 actions with owners and deadlines
- Weekly check-in until back to Yellow

## Renewal Risk Mode (if < 90 days until renewal)

- Activate the renewal process immediately — do not wait for the standard T-90 trigger
- Consider commercial options: downgrade path, implementation support extension, POC of new features

## Customer Health Monitoring Cadence

Health scoring defines the score. The cadence defines what you do with it.

```
FREQUENCY       ACTIVITY                                    OWNER
─────────       ────────                                    ─────
Weekly          Review accounts with score drop > 10pts     CSM (automated alert)
                Flag any Green → Yellow or Yellow → Red     CSM + CS Lead
Monthly         Full health score review for all accounts   CSM per account
                Escalation: any Red account reviewed with   CS Lead + AE
                CS Lead and AE
                Update health scores based on new data       CSM
Quarterly       Portfolio health review (CS team)           CS Lead
                QBR preparation for T1 accounts             CSM
                Red account recovery planning               CS Lead + AE
```

A health score without a review cadence is a dashboard no one acts on. The cadence is the operating system; the score is the signal.
