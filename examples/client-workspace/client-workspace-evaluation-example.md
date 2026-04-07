# Client Workspace Evaluation

## Workspace

- `workspace_name`: `generic-example`
- `workspace_path`: `examples/client-workspace/generic-example`
- `workspace_kind`: `template`
- `overall_result`: `PASS`

## Summary

The workspace satisfies the current contract and is ready for its intended use stage.

## Dimensions

### `contract_completeness` — Contract Completeness

- `status`: `PASS`
- `why_it_matters`: The workspace must satisfy the core directory and file contract before downstream workflows can rely on it.
- `evidence`:
  - missing_dirs=none
  - missing_config_files=none
  - missing_decision_files=none
- `next_action`: Keep the contract stable as the workspace grows.

### `config_pack_readiness` — Config Pack Readiness

- `status`: `PASS`
- `why_it_matters`: Client config should guide workflow behavior without forcing edits to core jobs, skills, or schemas.
- `evidence`:
  - empty_config_files=none
  - workspace_kind=template
- `next_action`: Use the config pack as the source of client-specific vocabulary and rules.

### `evidence_readiness` — Evidence Readiness

- `status`: `PASS`
- `why_it_matters`: A client workspace needs a defined home for provenance so downstream strategy and briefs stay traceable.
- `evidence`:
  - has_evidence_readme=True
  - has_source_inventory=False
- `next_action`: Keep evidence inventories current as new source material is added.

### `decision_layer_readiness` — Decision Layer Readiness

- `status`: `PASS`
- `why_it_matters`: The workspace should provide a stable handoff from evidence and synthesis into action and open questions.
- `evidence`:
  - empty_decision_files=none
  - decision_file_count=3
- `next_action`: Use the tracker files as the durable handoff into decision-making.

### `workspace_maturity` — Workspace Maturity

- `status`: `PASS`
- `why_it_matters`: The evaluation should distinguish a valid scaffold from a workspace that is ready for sustained client use.
- `evidence`:
  - records_files=none
  - syntheses_files=none
  - brief_files=none
- `next_action`: The workspace has enough structure and signal to support recurring use at its current stage.

## Review notes

- strongest dimension:
- weakest dimension:
- blocking gap:
- recommended next improvement:
