# Product Marketing Repo — Claude Instructions

## Default behavior

Always use the skills in this repo before generating PMM output. Do not invent a new workflow each time. The method is in `/skills/` — use it.

## Two workflows

This repo runs two distinct workflows. Know which one you're in before picking a skill.

1. **Discovery workflow** (`jobs/`) — turns raw customer conversations into evidence. Runs ahead of and alongside the PMM workflow, not inside it.
2. **PMM asset workflow** (`skills/lpa-*`) — the 20-tab launch workbook, sequenced by `lpa-workflow-map`. Turns evidence into positioning, launch, and GTM artifacts.

They connect at two points, both optional accelerants — the PMM workflow never blocks on discovery being run first:

- `Conversation Synthesis` (discovery output) is an optional input to `lpa-customer-interview` and `lpa-weekly-discovery-log` — use it to brief live interviews and enrich the weekly log with call-mined patterns, cited by `convrec-ID` alongside interview IDs.
- `Positioning Brief` (discovery output, gated — see `jobs/synthesize-conversation-set.md`) is an optional input to `lpa-positioning-canvas` — use it as a first-draft accelerant. The workbook's April Dunford sequence and live-interview evidence still govern the final Positioning Canvas; the brief does not skip that work.

`Persona Pack`, `Buyer Journey Map`, `GTM Plan`, and `Win-Loss Synthesis` have schemas and eval rubrics but **no skill produces them yet** — they're roadmap items (see `docs/architecture/discovery-system-flow.md`). Don't treat them as available; don't cite them as a source for a live artifact.

## Discovery workflow — skill index

| Work | Skill to use |
|---|---|
| Gathering customer conversations from Fireflies | `jobs/gather-customer-conversations.md` |
| Parsing a single conversation into a record | `jobs/parse-single-conversation.md` |
| Synthesizing a set of conversation records (and, when the record count and coverage support it, a Positioning Brief) | `jobs/synthesize-conversation-set.md` |

Sequence — do not invert:

```
Raw conversations → Source pack → Parsed records → Synthesis → (gated) Positioning Brief → PMM asset workflow
```

Evidence before messaging. Retrieval before writing. Structured outputs over long freeform prose.

## PMM asset workflow — skill index

Full phase-by-phase sequence, inputs, and handoffs live in `lpa-workflow-map` — treat this table as a lookup, not the source of truth.

| Work | Skill to use |
|---|---|
| Starting any new release or research cycle | `lpa-start-here` |
| Phase and tab sequencing, what feeds what | `lpa-workflow-map` |
| Risk and assumption tracking | `lpa-risk-and-assumption-register` |
| Release priority, launch tier, escalation triggers | `lpa-launch-triage-matrix` |
| Running a live customer interview | `lpa-customer-interview` |
| Defining EV-IDs, golden datasets, pass/fail proof logic | `lpa-eval-framework` |
| Weekly evidence consolidation | `lpa-weekly-discovery-log` |
| Building positioning | `lpa-positioning-canvas` |
| PR-FAQ drafting | `lpa-pr-faq-template` |
| Elevator pitch | `lpa-elevator-pitch` |
| Attack matrix / offense planning | `lpa-attack-matrix` |
| Testing message clarity | `lpa-bar-test` |
| Segment-specific messaging | `lpa-segment-playbooks` |
| Campaign-level master messaging doc (multi-asset campaign, not a single release) | `lpa-campaign-messaging-house` |
| Battle cards | `lpa-battle-cards` |
| ROI assets | `lpa-roi-calculator` |
| Go/no-go stage gate review | `lpa-stage-gate-architecture` |
| Impact protocol | `lpa-impact-protocol` |
| Certification status before release assets ship | `lpa-certification-rubric` |
| Demo script for a certified release | `lpa-demo-script` |
| Release article | `lpa-release-article` |
| Monthly innovation roundup | `lpa-monthly-innovation-roundup` |
| Competitive intelligence tracking (continuous, feeds Attack Matrix / Battle Cards / Positioning Canvas from Phase 2 onward) | `lpa-competitive-intelligence-log` |

## Schema contracts

Artifacts that are passed between stages must conform to the schemas in `/schemas/`. Do not invent new schemas when one already exists. Note: `schemas/persona-pack.md`, `schemas/gtm-plan.md`, and `schemas/positioning-brief.md`'s upstream agents (persona/buyer-journey/win-loss builders) are roadmap schemas — see the roadmap-only note above before treating them as live contracts.

## Fireflies integration

Fireflies is the primary source for customer and prospect call evidence. The native skill mapping is at:
`/docs/architecture/fireflies-native-skill-mapping.md`

Search grammar: `keyword:"X" scope:sentences from:YYYY-MM-DD to:YYYY-MM-DD limit:50 skip:N`

## Quality checks

Before shipping any positioning or GTM artifact, run the relevant eval rubric from `/evals/`.
