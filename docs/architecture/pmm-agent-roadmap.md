# PMM Agent Roadmap

## Current status

The repo has already completed the early setup work that this roadmap originally described:

- reusable schemas exist for the current core artifact set
- the conversation workflow has an end-to-end example and automated tests
- GitHub epic and child-issue structure is in place
- multi-client hardening docs and example workspace scaffolding now exist

That means the roadmap should no longer treat issue setup and first examples as the immediate next work. The next practical gap is widening evaluation coverage across the major schema-backed outputs so the repo has a more complete quality layer.

## Milestones

### M1. Method OS

Goal:

Turn the PMM method into reusable, GitHub-native assets.

Scope:

- one skill per workflow artifact
- output schemas for key artifacts
- example inputs and outputs
- issue model for epics and child work

Definition of done:

- method artifacts can be run manually in Claude or GPT
- outputs are consistent enough for review
- each skill has a clear upstream/downstream contract

### M2. Human-in-the-loop PMM Workspace

Goal:

Make the repo useful before full agent orchestration exists.

Scope:

- workflow docs
- issue templates
- artifact templates
- evaluation rubrics

Definition of done:

- a human can run a complete PMM workflow using repo assets
- outputs can be stored and reviewed in GitHub

### M3. Evidence Layer

Goal:

Add structured retrieval over PMM source material.

Scope:

- transcript ingestion
- competitive research ingestion
- CRM and note ingestion
- evidence tagging and indexing

Definition of done:

- the system can retrieve relevant evidence for each major PMM workflow

### M4. Strategy Orchestrator

Goal:

Build the first orchestrator agent for PMM workflows.

Scope:

- workflow routing
- artifact dependency checks
- evidence retrieval calls
- state handoff between workflows

Definition of done:

- the system can run a multi-step PMM workflow with human checkpoints

### M5. Asset and Campaign Operations

Goal:

Extend the system from strategy into recurring execution support.

Scope:

- sales asset generation
- content calendar support
- newsletter and press release drafting
- ongoing competitive and campaign support

Definition of done:

- the system supports both launch-time and ongoing PMM work

## Epic map

### Epic 1. Market and Competitive Intelligence

Child work:

- competitive landscape analysis
- win/loss analysis
- unmet needs synthesis
- distinctive competencies analysis

### Epic 2. Positioning and Buyer Understanding

Child work:

- persona generation
- buyer journey mapping
- positioning statement workflow
- value proposition workflow

### Epic 3. GTM and Launch Strategy

Child work:

- GTM planning
- digital marketing strategy support
- demand messaging
- promotional channel integration

### Epic 4. Sales Enablement and Asset Creation

Child work:

- competitive enablement
- data sheets
- white papers and ROI assets
- sales scripts and problem presentations
- pricing materials

### Epic 5. Ongoing Campaign Support

Child work:

- outbound insight support
- content calendar
- recurring content asset generation

## Recommended next implementation sequence

Completed foundations:

1. Create schemas for the most reusable artifacts
2. Add examples for one end-to-end PMM workflow
3. Open GitHub epic issues
4. Open child issues under each epic

Current next task:

5. Add evaluation criteria for each major output type

After that:

6. Expand workflow input/output contracts across the schema-backed artifacts
7. Add config validation and fallback behavior for client workspaces
8. Extend evidence-layer retrieval beyond the current conversation workflow
