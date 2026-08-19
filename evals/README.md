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
- `python3 scripts/evaluate_client_workspace.py examples/client-workspace/generic-example`
  Generates a reusable evaluation artifact from the client workspace contract.
- `python3 skills/lpa-campaign-messaging-house/scripts/validate_campaign_messaging_house.py <artifact>`
  Checks a Campaign Messaging House against its contract: section completeness, claim-status rules, and the bar on `Provisional` or `Unsupported` claims appearing in Section 4 derivatives. Lives beside the skill rather than in `scripts/` because the skill ships as a portable bundle.

## Known rubric gaps

`Campaign Messaging House` has a deterministic validator but no rubric. The validator checks structure and claim-status rules; it cannot judge whether the Dunford Setup earns the Follow-Through, or whether the pillars are the right three. That judgment still needs a human rubric — see the roadmap's next implementation sequence.
