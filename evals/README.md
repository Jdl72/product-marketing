# Evals

This directory holds quality checks for PMM workflows.

At this stage, start with human-readable rubrics before building full automation.

## Evaluation layers

### 1. Evidence quality

Is the source reliable and interpretable enough to use?

### 2. Output quality

Is the artifact useful, grounded, and structurally complete?

### 3. Method adherence

Did the workflow follow the intended process?

## Recommended first eval

Start with:

- `conversation-record-rubric.md`
- `client-workspace-rubric.md`
- `conversation-synthesis-rubric.md`
- `positioning-brief-rubric.md`
- `persona-pack-rubric.md`
- `gtm-plan-rubric.md`
- `battle-card-rubric.md`
- `content-calendar-rubric.md`

These give the repo a baseline evaluation layer across the current schema-backed conversation, strategy, enablement, and campaign artifacts.

## Current automated checks

- `python3 scripts/validate_conversation_synthesis.py examples/conversations/conversation-synthesis-example.md`
  Confirms that key synthesis pattern sections cite supporting record ids.
- `python3 scripts/validate_workflow_contracts.py`
  Confirms schema-backed workflow contracts include required sections, schema links, and explicit failure behavior.
- `python3 scripts/validate_client_config.py examples/client-workspace/generic-example`
  Confirms the template client workspace keeps the required config structure and exposes fallback-ready placeholders.
- `python3 scripts/evaluate_client_workspace.py examples/client-workspace/generic-example`
  Generates a reusable evaluation artifact from the client workspace contract.
