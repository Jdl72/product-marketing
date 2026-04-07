# Client Config Validation Report

## Workspace

- `workspace_name`: `generic-example`
- `workspace_path`: `examples/client-workspace/generic-example`
- `workspace_kind`: `template`
- `overall_result`: `PASS`

## Summary

The template config pack is structurally valid and ready to be copied into a real client workspace.

## Missing files

- none

## File reports

### `client-profile.md`

- `status`: `PASS`
- `path`: `examples/client-workspace/generic-example/config/client-profile.md`
- `reason`: Template scaffold has the required sections and may keep placeholders.
- `placeholder_count`: `9`
- `fallback_behavior`: Continue with generic workflow behavior and mark client framing as unresolved.

### `segment-taxonomy.md`

- `status`: `PASS`
- `path`: `examples/client-workspace/generic-example/config/segment-taxonomy.md`
- `reason`: Template scaffold has the required sections and may keep placeholders.
- `placeholder_count`: `5`
- `fallback_behavior`: Mark segment as `unresolved` and preserve generic schema behavior without inventing client labels.

### `funnel-stages.md`

- `status`: `PASS`
- `path`: `examples/client-workspace/generic-example/config/funnel-stages.md`
- `reason`: Template scaffold has the required sections and may keep placeholders.
- `placeholder_count`: `5`
- `fallback_behavior`: Mark stage as `unresolved` and avoid guessing client stage labels.

### `competitor-map.md`

- `status`: `PASS`
- `path`: `examples/client-workspace/generic-example/config/competitor-map.md`
- `reason`: Template scaffold has the required sections and may keep placeholders.
- `placeholder_count`: `5`
- `fallback_behavior`: Preserve raw competitor mentions and skip canonical normalization.

### `coding-rules.md`

- `status`: `PASS`
- `path`: `examples/client-workspace/generic-example/config/coding-rules.md`
- `reason`: Template scaffold has the required sections and may keep placeholders.
- `placeholder_count`: `6`
- `fallback_behavior`: Use generic schema fields only and keep unresolved mappings explicit.

### `strategic-questions.md`

- `status`: `PASS`
- `path`: `examples/client-workspace/generic-example/config/strategic-questions.md`
- `reason`: Template scaffold has the required sections and may keep placeholders.
- `placeholder_count`: `0`
- `fallback_behavior`: Proceed only from the explicit PMM objective and do not invent executive questions.

### `metrics-scorecard.md`

- `status`: `PASS`
- `path`: `examples/client-workspace/generic-example/config/metrics-scorecard.md`
- `reason`: Template scaffold has the required sections and may keep placeholders.
- `placeholder_count`: `0`
- `fallback_behavior`: Use generic evidence and workflow review instead of fabricated client metrics.

## Review notes

- strongest config file:
- weakest config file:
- blocking config gap:
- next recommended improvement:
