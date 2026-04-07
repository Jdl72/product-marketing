# Positioning Brief Workflow Contract

## Purpose

Define the minimum contract for producing a reusable positioning brief from grounded PMM evidence.

## Output artifact

- `positioning-brief`
- schema: [positioning-brief.md](../../schemas/positioning-brief.md)

## Required inputs

- one or more `conversation-synthesis` artifacts relevant to the target segment
- evidence or synthesis covering the buyer problem and status quo alternatives
- explicit target segment and target persona

## Optional inputs

- competitive landscape brief
- win/loss synthesis
- distinctive competency memo
- strategic questions from a client config pack

## Input readiness checks

- the target segment is known
- the workflow has enough evidence to describe a real buyer problem
- proof points can be tied to evidence or marked as assumptions

## Workflow notes

- derive the differentiated promise from evidence rather than inventing slogan language
- keep status quo alternatives explicit
- separate proof-backed claims from open assumptions

## Human review gate

- review whether the audience, problem, promise, and proof hang together
- confirm the brief does not overstate certainty or collapse multiple audiences into one story

## Failure and fallback behavior

- fail if there is no usable evidence basis for the target segment
- degrade gracefully when proof is partial by marking assumptions instead of inventing certainty
- do not publish a differentiated promise without some evidence basis

## Downstream consumers

- `gtm-plan`
- `content-calendar`
- `battle-card`
- future sales-enablement assets

## Done when

- the brief satisfies the schema
- the differentiated promise is evidence-backed or explicitly caveated
- downstream GTM work can consume it without re-deriving the audience and problem framing
