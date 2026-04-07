# Product Marketing

This repository is the home for a product marketing agent system built around a source-faithful product marketing method.

## What lives here

- `skills/`
  Portable markdown skills, one per core workflow artifact
- `docs/architecture/`
  System architecture, roadmap, and GitHub work model
- `jobs/`
  Job specs that turn PMM work into buildable workflows
- `connectors/`
  Source-system integrations for evidence gathering
- `scripts/`
  Small utilities for fetching and preparing source material
- `schemas/`
  Output contracts for reusable PMM artifacts
- `examples/`
  Calibration outputs that show what done looks like
- `evals/`
  Quality rubrics and evaluation artifacts
- `.github/ISSUE_TEMPLATE/`
  GitHub issue templates for epics and implementation work

## System goal

Build an AI product marketing system that can:

- understand the market and competitive landscape
- synthesize buyer and user understanding
- generate positioning and GTM strategy
- equip sales with differentiated enablement assets
- support ongoing campaign execution and content operations

## Operating model

The repo is organized into four layers:

1. `Method layer`
   The PMM process and skills
2. `Artifact layer`
   Structured outputs such as personas, positioning briefs, battle cards, GTM plans, and launch docs
3. `System layer`
   Retrieval, orchestration, memory, and agent logic
4. `Evaluation layer`
   Quality checks for process adherence, evidence quality, and output usefulness

## Start here

- [System architecture](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/pmm-agent-system.md)
- [Roadmap](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/pmm-agent-roadmap.md)
- [Discovery system flow](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/discovery-system-flow.md)
- [Core vs client workspaces](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/core-vs-client-workspaces.md)
- [Client workspace contract](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/client-workspace-contract.md)
- [Config-aware conversation runbook](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/config-aware-customer-conversation-runbook.md)
- [Multi-client backlog](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/multi-client-backlog.md)
- [Parse single conversation runbook](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/parse-single-conversation-runbook.md)
- [Discovery term dictionary](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/discovery-term-dictionary.md)
- [Fireflies native skill mapping](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/fireflies-native-skill-mapping.md)
- [GitHub work model](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/github-work-model.md)
- [Conversation synthesis input pack guide](/Users/jacklindberg/Documents/Product%20Marketing/examples/conversations/conversation-synthesis-input-pack.md)
- [Generated conversation synthesis input pack](/Users/jacklindberg/Documents/Product%20Marketing/examples/conversations/conversation-synthesis-input-pack.generated.md)
- [Conversation synthesis example](/Users/jacklindberg/Documents/Product%20Marketing/examples/conversations/conversation-synthesis-example.md)
- [Example client workspace](/Users/jacklindberg/Documents/Product%20Marketing/examples/client-workspace/README.md)
- [Client workspace evaluation example](/Users/jacklindberg/Documents/Product%20Marketing/examples/client-workspace/client-workspace-evaluation-example.md)

## Testing

Run the current script test suite with:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Current coverage includes:

- unit tests for parsing helpers, validation helpers, and Fireflies client behavior
- integration tests for fetch, build, and validate scripts
- an end-to-end test for the parsed-record to synthesis-input workflow
- layered tests for the client-workspace evaluation artifact and script
