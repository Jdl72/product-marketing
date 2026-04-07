# Battle Card Workflow Contract

## Purpose

Define the minimum contract for producing a battle card that helps sellers compete credibly.

## Output artifact

- `battle-card`
- schema: [battle-card.md](../../schemas/battle-card.md)

## Required inputs

- competitive evidence for the named competitor or alternative
- positioning input that explains our relevant advantage
- proof points and sources that can support objection handling

## Optional inputs

- win/loss analysis
- conversation synthesis with competitive mentions
- segment-specific positioning or proof

## Input readiness checks

- the comparison target is clear
- sources exist for the main competitive claims
- the workflow can describe strengths, weaknesses, trade-offs, and likely objections

## Workflow notes

- preserve trade-off honesty instead of writing one-sided enablement copy
- explain when we win and when we lose
- frame our advantage relative to buyer purchasing criteria, not just features

## Human review gate

- review whether the card is field-usable and source-grounded
- confirm objection handling does not require unsupported claims

## Failure and fallback behavior

- fail if the card has no usable sources
- fail if weaknesses and when-we-lose conditions are omitted
- narrow the scope to a smaller comparison frame rather than bluffing broad competitive certainty

## Downstream consumers

- sales scripts
- solution briefs
- future enablement packs

## Done when

- the card satisfies the schema
- a seller can understand the competitive frame, trade-offs, and proof without inventing missing logic
- sources and confidence are explicit enough for review
