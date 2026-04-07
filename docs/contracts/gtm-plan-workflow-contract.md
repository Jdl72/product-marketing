# GTM Plan Workflow Contract

## Purpose

Define the minimum contract for turning positioning and buyer evidence into an executable GTM plan.

## Output artifact

- `gtm-plan`
- schema: [gtm-plan.md](../../schemas/gtm-plan.md)

## Required inputs

- a completed `positioning-brief`
- at least one relevant `persona-pack` or equivalent buyer understanding artifact
- explicit launch goal or go-to-market objective

## Optional inputs

- channel integration plan
- demand messaging inputs
- client scorecard metrics
- competitive or win/loss context

## Input readiness checks

- positioning exists and is stable enough to guide execution
- the target segments are defined
- the workflow can name core message, owners, dependencies, and timeline logic

## Workflow notes

- tie channel choices and audience sequence to the upstream positioning logic
- surface sales-enablement and content dependencies explicitly
- keep risks, assumptions, and decision points visible rather than implied

## Human review gate

- review whether the plan is strategically coherent and operationally usable
- confirm measurement, ownership, and dependency logic are all present

## Failure and fallback behavior

- fail if there is no stable positioning input
- fail if the plan cannot assign ownership or timeline logic
- when evidence is partial, preserve the uncertainty in risks and assumptions instead of hiding it

## Downstream consumers

- `content-calendar`
- future launch assets
- sales-enablement plans
- cross-functional action trackers

## Done when

- the plan satisfies the schema
- a team could execute from it without rebuilding the strategy layer
- risks, assumptions, and measurement are clear enough for launch review
