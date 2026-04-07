# Workflow Input / Output Contract Template

## Purpose

Describe the workflow in plain language and clarify why the contract exists.

## Output artifact

- name the primary artifact
- link the schema that governs it

## Required inputs

- list the inputs that must exist before the workflow should run
- separate upstream artifacts from raw evidence when relevant

## Optional inputs

- list inputs that improve quality or specificity without changing the workflow's core dependency structure

## Input readiness checks

- define what must be true before execution starts
- call out the minimum evidence or artifact quality bar

## Workflow notes

- describe the intended behavior of the workflow without rewriting the whole job spec
- clarify how the workflow should use evidence, messaging, or downstream dependencies

## Human review gate

- define the review checkpoints that must happen before the artifact is considered reusable

## Failure and fallback behavior

- define what should happen when required inputs are missing or weak
- clarify what can degrade gracefully and what should fail loudly

## Downstream consumers

- list the next workflows or artifacts that should be able to consume the output directly

## Done when

- define what completion means in operational terms
