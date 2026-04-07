# Persona Pack Workflow Contract

## Purpose

Define the minimum contract for producing a persona pack that can guide positioning, GTM, and enablement work.

## Output artifact

- `persona-pack`
- schema: [persona-pack.md](/tmp/product-marketing-contracts/schemas/persona-pack.md)

## Required inputs

- multiple `conversation-record` artifacts or a relevant `conversation-synthesis`
- evidence that identifies role, context, pains, desired outcomes, and buying behavior
- a declared scope for whether the workflow is building a buyer persona, user persona, or both

## Optional inputs

- segment taxonomy
- funnel-stage definitions
- strategic questions from a client workspace
- win/loss synthesis

## Input readiness checks

- enough evidence exists to distinguish a repeatable persona pattern from a single anecdote
- buyer and user roles are separated where the evidence suggests they differ
- customer language and evaluation criteria can be traced to source evidence

## Workflow notes

- preserve what is observed versus inferred
- keep jobs, pains, outcomes, buying triggers, objections, and language guidance explicit
- do not flatten multiple stakeholder perspectives into one persona without justification

## Human review gate

- review whether the persona sounds like a real market actor rather than a generic profile
- check that evidence basis and confidence are calibrated

## Failure and fallback behavior

- fail if the persona has no evidence basis
- split the output if the evidence actually contains multiple distinct personas
- use narrower scope rather than broad generalization when the signal is thin

## Downstream consumers

- `positioning-brief`
- `gtm-plan`
- `content-calendar`
- future demand messaging and enablement assets

## Done when

- the pack satisfies the schema
- the persona is specific enough for downstream teams to use
- evidence-backed language guidance is preserved for later messaging work
