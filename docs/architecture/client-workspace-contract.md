# Client Workspace Contract

## Purpose

Define the minimum structure required for a client workspace that consumes the Product Marketing system.

This contract keeps the core repo reusable while giving each client a clear place for configuration, evidence, outputs, and decisions.

## Minimum directory structure

```text
client-workspace/
  config/
  evidence/
  records/
  syntheses/
  briefs/
  decisions/
  campaigns/      # recommended, not required
```

## Required folders

### `config/`

Holds the client-specific configuration pack.

Required files:

- `client-profile.md`
- `segment-taxonomy.md`
- `funnel-stages.md`
- `competitor-map.md`
- `coding-rules.md`
- `strategic-questions.md`
- `metrics-scorecard.md`

### `evidence/`

Holds source inventories and metadata about the raw evidence set.

Examples:

- transcript inventories
- transcript metadata exports
- source coverage notes
- quality notes
- references to raw transcript files or external source IDs

### `records/`

Holds parsed conversation records produced from the core workflow.

Each record should preserve:

- source identifier
- source type
- date
- segment
- quotes
- confidence

### `syntheses/`

Holds grouped syntheses for a stage, segment, theme, or time window.

Examples:

- intro-call synthesis
- late-stage conversion synthesis
- win/loss synthesis
- trust-and-control synthesis

### `briefs/`

Holds client-ready outputs.

Examples:

- leadership memos
- PMM briefs
- sales narrative docs
- positioning outputs

### `campaigns/`

Recommended, not required. Holds Campaign Messaging Houses produced by `lpa-campaign-messaging-house`, one directory per campaign theme.

A messaging house does not belong in `briefs/`. Briefs are client-ready outputs, read once and superseded. A messaging house is a versioned governing document that outlives the assets built from it, and every campaign asset cites the claim IDs it draws on. Storing it beside one-off briefs loses the version history that stops messaging from drifting.

Each campaign directory should hold:

- the house artifact itself, at its current version
- the Campaign Evidence Pack that grounded it
- superseded versions, kept rather than overwritten — the change log in Section 5 references them

Client workspaces that run no multi-asset campaigns can omit this folder. `scripts/evaluate_client_workspace.py` does not check for it.

### `decisions/`

Holds insight-to-action artifacts.

Required files:

- `insight-to-action-tracker.md`
- `open-questions.md`
- `cross-functional-action-log.md`

Recommended:

- `monthly-evidence-review-template.md`
- `decision-log.md`

## Behavior contract

The core repo assumes:

- config files are markdown in v1
- missing client config should fall back to generic schema behavior
- client outputs must preserve quote traceability
- client workspaces may add files, but should not remove the required contract files

## Validation expectations

A valid client workspace:

- has all required folders
- has all required config files
- can point to at least one source inventory in `evidence/`
- stores parsed records separately from syntheses
- keeps leadership-facing briefs separate from raw or intermediate evidence

## Recommended setup flow

1. Create the client workspace from the example template.
2. Fill in the config pack before doing new synthesis work.
3. Build or import the source inventory into `evidence/`.
4. Parse sources into `records/`.
5. Create syntheses in `syntheses/`.
6. Publish client-facing outputs in `briefs/`.
7. Track owners and next steps in `decisions/`.
8. For a multi-asset campaign, build the messaging house in `campaigns/` before any campaign asset gets written.

## Related docs

- [Core vs Client Workspaces](core-vs-client-workspaces.md)
- [Config-Aware Customer Conversation Runbook](config-aware-customer-conversation-runbook.md)
- [Client Workspace Rubric](../../evals/client-workspace-rubric.md)
