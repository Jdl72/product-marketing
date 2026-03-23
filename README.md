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
- [GitHub work model](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/github-work-model.md)
