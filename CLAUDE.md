# Product Marketing Repo — Claude Instructions

## Default behavior

Always use the skills in this repo before generating PMM output. Do not invent a new workflow each time. The method is in `/skills/` — use it.

## Skill index

| Work | Skill to use |
|---|---|
| Starting any new release or research cycle | `lpa-start-here` |
| Gathering customer conversations from Fireflies | `jobs/gather-customer-conversations.md` |
| Parsing a single conversation into a record | `jobs/parse-single-conversation.md` |
| Synthesizing a set of conversation records | `jobs/synthesize-conversation-set.md` |
| Weekly evidence consolidation | `lpa-weekly-discovery-log` |
| Customer evidence research | `lpa-customer-evidence` |
| Competitive intelligence tracking | `lpa-competitive-intelligence-log` |
| Building positioning | `lpa-positioning-canvas` |
| Segment-specific messaging | `lpa-segment-playbooks` |
| Testing message clarity | `lpa-bar-test` |
| Risk and assumption tracking | `lpa-risk-and-assumption-register` |
| Attack matrix / offense planning | `lpa-attack-matrix` |
| Battle cards | `lpa-battle-cards` |
| ROI assets | `lpa-roi-calculator` |
| Launch routing | `lpa-launch-router` |
| Launch asset planning | `lpa-launch-asset-planner` |
| Stage gate review | `lpa-stage-gate-architecture` |
| Eval proof framework | `lpa-eval-proof-framework` |
| Impact protocol | `lpa-impact-protocol` |

## Discovery pipeline order

Do not invert this sequence:

```
Raw conversations → Source pack → Parsed records → Synthesis → Insight artifacts → Strategy artifacts → Sales/GTM assets
```

Evidence before messaging. Retrieval before writing. Structured outputs over long freeform prose.

## Schema contracts

Artifacts that are passed between stages must conform to the schemas in `/schemas/`. Do not invent new schemas when one already exists.

## Fireflies integration

Fireflies is the primary source for customer and prospect call evidence. The native skill mapping is at:
`/docs/architecture/fireflies-native-skill-mapping.md`

Search grammar: `keyword:"X" scope:sentences from:YYYY-MM-DD to:YYYY-MM-DD limit:50 skip:N`

## Quality checks

Before shipping any positioning or GTM artifact, run the relevant eval rubric from `/evals/`.
