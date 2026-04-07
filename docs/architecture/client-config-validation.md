# Client Config Validation and Fallback Behavior

## Purpose

Define how the core Product Marketing system should validate client config packs and what fallback behavior is allowed when parts of the config are missing, incomplete, or still template-level.

The goal is to keep the core method reusable without forcing the system to invent client-specific logic.

## Validation model

Validation happens in two layers:

### 1. Structural validation

Checks:

- the required config files exist
- each file uses markdown
- each file contains the required top-level sections for that config type

If structural validation fails, the config pack is not ready for client use.

### 2. Content-readiness validation

Checks:

- the file is populated enough to guide real work
- template placeholders are not mistaken for real configuration
- file content is specific enough to scope evidence and interpretation

Template workspaces may pass as scaffold-ready even when placeholders remain.
Live client workspaces should fail if placeholders still dominate required fields.

## Required config files

- `client-profile.md`
- `segment-taxonomy.md`
- `funnel-stages.md`
- `competitor-map.md`
- `coding-rules.md`
- `strategic-questions.md`
- `metrics-scorecard.md`

## File-specific validation rules

### `client-profile.md`

Must contain:

- `# Client Profile`

Client-ready if:

- client name, category, buyer types, user types, and source systems are populated

Fallback if incomplete:

- the core system may still run generic workflows
- do not infer client category, GTM motion, or buyer model from downstream briefs
- mark client framing as unresolved

### `segment-taxonomy.md`

Must contain:

- `# Segment Taxonomy`
- `## Segments`

Client-ready if:

- at least one real segment ID and segment definition is populated

Fallback if incomplete:

- preserve generic schema behavior
- mark segment as `unresolved`
- do not invent client-specific segment labels

### `funnel-stages.md`

Must contain:

- `# Funnel Stages`
- `## Stage Definitions`

Client-ready if:

- at least one stage definition is populated with inclusion/exclusion logic

Fallback if incomplete:

- preserve generic stage handling
- mark stage as `unresolved`
- do not force transcript evidence into guessed stage labels

### `competitor-map.md`

Must contain:

- `# Competitor Map`
- `## Named Competitors`
- `## Status Quo Alternatives`

Client-ready if:

- at least one named competitor or status quo alternative is populated

Fallback if incomplete:

- preserve raw competitor mentions from evidence
- skip competitor normalization
- do not collapse variants into canonical names without explicit config

### `coding-rules.md`

Must contain:

- `# Coding Rules`
- `## Client Extensions`
- `## Rules`

Client-ready if:

- the client extensions describe at least some stage, segment, objection, trigger, or proof logic

Fallback if incomplete:

- use only generic schema fields
- keep unresolved mappings explicit
- do not create new client categories in core logic

### `strategic-questions.md`

Must contain:

- `# Strategic Questions`

Client-ready if:

- the file contains at least one real strategic question

Fallback if incomplete:

- continue with the explicitly provided PMM objective only
- do not invent executive questions from scattered notes

### `metrics-scorecard.md`

Must contain:

- `# Metrics Scorecard`

Client-ready if:

- the file contains at least one usable metric list or scorecard section

Fallback if incomplete:

- use generic evidence-quality and workflow-health review
- do not fabricate client scorecard metrics from weak signal

## Result states

- `PASS`
  Config is structurally valid and ready for live client use.
- `CONDITIONAL`
  Config is structurally valid as a template scaffold but not fully populated for live client use.
- `FAIL`
  Config is missing required files, required sections, or enough content to guide work safely.

## Behavioral rules

- Missing client config is permission to stay generic, not permission to invent client logic.
- Core jobs, skills, and schemas should degrade toward generic schema behavior, not toward guessed client specificity.
- Fallback behavior must preserve traceability and unresolved states.
- Client workspaces may extend the config pack, but should not remove the required files.

## Recommended automation

Use:

- `python3 scripts/validate_client_config.py <workspace-root>`

This validator should:

- report structural and content-readiness status
- distinguish template-ready from client-ready workspaces
- surface file-specific fallback behavior when gaps are present
