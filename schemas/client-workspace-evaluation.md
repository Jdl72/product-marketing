# Client Workspace Evaluation

## Purpose

Capture whether a client workspace is structurally valid, reusable, and ready to consume the core Product Marketing system without collapsing the core-vs-client boundary.

## Required fields

### `workspace_name`

- human-readable workspace name

### `workspace_path`

- repo-relative or absolute path to the evaluated workspace

### `workspace_kind`

- `template` or `client`

### `overall_result`

- `PASS`, `CONDITIONAL`, or `FAIL`

### `summary`

- short explanation of the evaluation result

### `dimensions`

Each dimension entry must include:

- `dimension_id`
- `label`
- `status`
- `why_it_matters`
- `evidence`
- `next_action`

## Required dimensions

- `contract_completeness`
- `config_pack_readiness`
- `evidence_readiness`
- `decision_layer_readiness`
- `workspace_maturity`

## Status rules

- `PASS`
  The dimension meets the expected quality bar for the current workspace kind.
- `CONDITIONAL`
  The dimension is usable but incomplete and should be improved before broader reuse.
- `FAIL`
  The dimension breaks the workspace contract or blocks reliable downstream use.

## Interpretation guidance

- Template workspaces should be judged on completeness of scaffold, guidance, and handoff clarity.
- Client workspaces should be judged on completeness of config, evidence inventory, and operational readiness.
- The evaluation must not reward client-specific customization inside core jobs, skills, or schemas.

## Review notes

Every completed evaluation should record:

- strongest area
- weakest area
- blocking gap, if any
- recommended next improvement
