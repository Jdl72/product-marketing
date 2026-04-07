# Client Workspace Rubric

## Purpose

Evaluate whether a client workspace is ready to consume the core Product Marketing system without breaking the reusable method layer.

Use this rubric when:

- reviewing a new generic template workspace
- reviewing a live client workspace such as [client]
- deciding whether a workspace is ready for broader workflow use

## Result scale

- `PASS`
  The workspace satisfies the contract and is ready for the intended use level.
- `CONDITIONAL`
  The workspace is structurally usable but still has meaningful gaps.
- `FAIL`
  The workspace is missing core contract elements or is not safe to rely on.

## Dimensions

### 1. Contract Completeness

Question:

Does the workspace satisfy the minimum directory and file contract?

Pass:

- all required directories exist
- all required config files exist
- all required decision files exist

Conditional:

- the structure is mostly present but some files are placeholders that need follow-through

Fail:

- any required directory is missing
- any required config or decision file is missing

### 2. Config Pack Readiness

Question:

Is the client configuration pack complete enough to scope work without editing core logic?

Pass:

- every required config file is present and non-empty
- the config pack can guide segmentation, stage mapping, competition, coding, and strategic framing

Conditional:

- the files exist but important sections are still placeholders

Fail:

- configuration is missing or empty enough that the core workflow would have to invent client logic

### 3. Evidence Readiness

Question:

Does the workspace define where evidence lives and how it can be traced?

Pass for templates:

- the workspace explains where evidence inventories belong

Pass for live clients:

- at least one evidence inventory or equivalent source-tracking file exists

Conditional:

- evidence guidance exists but no concrete inventory is present for a live client workspace

Fail:

- there is no defined evidence layer or no place to track provenance

### 4. Decision Layer Readiness

Question:

Can evidence move into decisions and action without inventing new structure?

Pass:

- the insight tracker, open questions log, and cross-functional action log all exist and are readable

Conditional:

- the structures exist but are still minimally populated

Fail:

- downstream action artifacts are missing

### 5. Workspace Maturity

Question:

Is the workspace appropriate for its intended current stage?

Pass for templates:

- it is clearly usable as a starting point for a new client

Pass for live clients:

- it has config, evidence tracking, and at least one concrete sign of live implementation such as an inventory, tracker entries, or client-specific decision content

Conditional:

- the scaffold is valid but still early in real operational use

Fail:

- the workspace exists only nominally and is not actually usable

## Pass / fail rule

Pass if:

- no dimension is `FAIL`
- the workspace preserves the core-vs-client boundary
- the workspace is usable for its declared stage

Conditional if:

- no dimension fails
- one or more dimensions still need meaningful follow-up before scaling use

Fail if:

- any required contract element is missing
- client logic would have to leak into core method assets to make the workspace usable
- evidence provenance has no defined home

## Review notes to capture every time

- strongest dimension
- weakest dimension
- whether the workspace is template-ready or client-ready
- next recommended improvement
