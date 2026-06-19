# AI-Assisted Inbound Qualification

On-demand reference for the marketing-operations skill.

When AI is deployed for inbound lead qualification (via Qualified, Agentforce, or custom agents), the lead scoring model needs to adapt:

**AI qualification adds two new dimensions to scoring:**

1. **Behavioural intent signals** — not just "downloaded a whitepaper" but "visited pricing page 3 times in 2 days, opened 4 emails, attended webinar, then hit the contact form." AI can score multi-touch behaviour patterns that humans miss.

2. **Real-time qualification** — AI can run SPICED-style qualification questions via chat before a human gets involved. The lead arrives at the rep pre-qualified with Situation, Pain, and Impact already captured.

**SaaStr result:** 71% of October 2025 closed-won deals came from AI-qualified inbound. Historic baseline was 29-34%. The AI didn't just qualify faster — it qualified BETTER by catching signals humans overlooked.

**Implementation pattern:**
- AI handles first response (speed-to-lead becomes instant)
- AI asks 3-5 qualification questions (mapped to SPICED or BANT)
- AI scores based on responses + behavioural data + firmographic fit
- T1 leads routed to rep immediately with AI-generated brief
- T2 leads entered into AI nurture sequence
- T3 leads deprioritised or recycled

**Lead segmentation for AI qualification** — segment by behaviour, not demographics:
- Website visitors (high-intent pages) → immediate AI engagement
- Content downloaders → educational nurture sequence
- Event registrants → event-specific follow-up sequence
- Returning visitors (previously cold) → re-engagement with context
- Free trial signups → onboarding + qualification hybrid

Source: SaaStr AI Agent Playbook, Part 14; SaaStr inbound case study
