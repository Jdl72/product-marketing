# Core vs Client Workspaces

## Purpose

Define the boundary between the reusable Product Marketing system and client-specific implementations.

The goal is to keep the repo reusable across consulting clients while still allowing deep, evidence-rich work for a specific company such as [client].

## Design rule

Standardize the method. Configure the client layer.

The core repo should answer:

- how PMM work gets done
- which artifacts exist
- how evidence is gathered and validated
- what quality bar each artifact must meet

The client workspace should answer:

- which segments matter
- which funnel stages matter
- which sources count as relevant
- which competitors and alternatives matter
- which leadership questions the work should answer

## Keep in core

Keep these reusable and client-agnostic:

- jobs
- skills
- schemas
- evals
- connectors
- validation helpers
- issue templates
- generic workflow runbooks
- examples that demonstrate method, not client strategy

Core workflows must remain usable without any one client attached.

## Keep in client workspaces

Keep these outside the core repo:

- segment taxonomy
- funnel stage definitions
- persona labels used by that client
- product and module taxonomy
- competitor map and normalization rules
- buying-trigger taxonomy
- objection taxonomy
- proof-type taxonomy
- strategic questions
- scorecard metrics
- source inventories
- parsed records
- syntheses
- client-facing briefs and decks
- decision logs and action trackers

## What not to encode in core

Do not promote client-specific language into default system behavior.

Examples:

- [client]-specific terms such as `DSP`, `AMC`, or `Walmart`
- client-specific funnel stages such as `intro`, `trial`, or `touchbase`
- client-specific KPI sets
- client-specific leadership narratives
- client-specific quote libraries or conclusions

Client-specific terms may appear in examples, but they must be marked as examples rather than defaults.

## Why this split matters

Without the split:

- the repo drifts into a single-client consulting folder
- future clients require editing core logic
- evidence standards become tangled with one company's vocabulary
- client IP pollutes the reusable method

With the split:

- the repo stays portable
- each client gets a clear implementation contract
- evidence remains traceable within client workspaces
- the consultant builds a reusable operating system instead of one-off deliverables

## Connection to the system

The Product Marketing repo is the system of method.

Client workspaces are external consumers that:

1. supply client-specific configuration
2. store client evidence and outputs
3. reuse the repo workflows and schemas

## Related docs

- [Client Workspace Contract](client-workspace-contract.md)
- [Config-Aware Customer Conversation Runbook](config-aware-customer-conversation-runbook.md)
