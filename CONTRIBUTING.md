# Contributing

Contributions are welcome. The bar is intentionally high — these skills are used in live commercial engagements and the quality standard reflects that.

## What makes a good contribution

A skill worth adding must do one thing well and know its limits. Before submitting, ask yourself: does this skill surface constraints the user wouldn't have spotted otherwise, or does it just describe what the user already knows?

## Requirements for every submitted skill

Every pull request must include:

1. **`SKILL.md`** — The skill file itself. Must include:
   - A clear activation trigger (one sentence describing when Claude should load this skill)
   - A BOUNDARY statement that names at least two other skills it intentionally does not overlap with, and why
   - Concrete diagnostic questions or frameworks, not general advice
   - British English throughout (organisation, colour, analyse, behaviour)

2. **`references/` directory** (required if the skill cites external frameworks) — One markdown file per framework or methodology cited, explaining what it is and how the skill uses it. Don't cite MEDDIC or SPICED without explaining how your skill interprets them.

3. **A test prompt** — A one-paragraph scenario that demonstrates the skill working correctly. Include it in the PR description, not in the skill file itself.

## What we won't merge

- Skills that duplicate existing skills without a clear differentiation statement
- Skills that give general advice without a diagnostic or implementation layer
- Skills that require private data, proprietary frameworks, or external paid tools to function
- Skills with Americanised spelling (realise → realize etc.)
- AI tells: em-dashes used more than 4 times per skill, phrases like "game-changer", "dive deep", "leveraging synergies"

## Scope

This repo covers the generic operational layer — frameworks any B2B revenue team can use. It is not the place for:

- Client-specific delivery skills
- Skills requiring Neon Triforce IP or proprietary maturity models
- Experimental or unvalidated frameworks

## Process

1. Open an issue describing the skill before building it — this avoids duplicate effort
2. Fork the repo, create a branch named `skill/[skill-name]`
3. Submit a pull request with the skill file, references (if applicable), and a test prompt in the PR description
4. One maintainer review required before merge

## Questions

Open a [Discussion](https://github.com/NEON-Rutger/B2B-revops-skills/discussions) before opening an issue for exploratory questions. Issues are for confirmed bugs or concrete skill proposals.
