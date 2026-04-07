# Content Calendar Workflow Contract

## Purpose

Define the minimum contract for producing a content calendar that stays tied to PMM priorities instead of generic publishing cadence.

## Output artifact

- `content-calendar`
- schema: [content-calendar.md](/tmp/product-marketing-contracts/schemas/content-calendar.md)

## Required inputs

- a `gtm-plan` or other approved PMM source artifact
- explicit campaign goal
- audience definition for the planned content

## Optional inputs

- positioning brief
- demand messaging input
- launch timeline
- content-production constraints from the operating team

## Input readiness checks

- source artifact exists and is stable enough to guide content choices
- campaign goal and audience are explicit
- ownership and distribution assumptions are known

## Workflow notes

- every planned item should trace back to a PMM source artifact
- distinguish message strategy from execution logistics
- avoid filling the calendar with content that has no strategic source

## Human review gate

- review whether entries reflect real PMM priorities and are executable by the team
- confirm source-artifact traceability remains visible

## Failure and fallback behavior

- fail if there is no approved PMM source artifact
- fail if ownership and timing are too vague for execution
- keep the calendar smaller rather than padding it with low-signal items

## Downstream consumers

- editorial planning
- demand-generation execution
- launch communications planning

## Done when

- the calendar satisfies the schema
- each item has a clear campaign goal, source artifact, owner, and CTA
- the calendar can be handed to an execution team without losing PMM traceability
