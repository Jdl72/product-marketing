# PMM Agent System

## Vision

Build an AI product marketing system that behaves like a disciplined PMM organization rather than a generic content generator.

The system should:

- retrieve the right evidence before writing strategy
- follow the PMM method instead of inventing a new workflow each time
- produce structured artifacts that a human can review, edit, and ship
- preserve provenance so outputs can be traced back to customer and market evidence

## Primary capability domains

### 1. Market and Competitive Intelligence

Jobs to be done:

- analyze the competitive landscape by segment
- run win/loss analysis
- identify pervasive market problems and unmet needs
- assess distinctive competencies

Primary outputs:

- competitive landscape brief
- win/loss synthesis
- unmet needs map
- distinctive competency memo

### 2. Positioning and Buyer Understanding

Jobs to be done:

- develop buyer and user personas
- map buyer experience
- formulate product positioning
- translate features into outcome-based value propositions

Primary outputs:

- persona pack
- buyer journey map
- positioning brief
- value proposition brief

### 3. GTM and Launch Strategy

Jobs to be done:

- draft GTM plan
- propose outcome-based digital marketing strategy
- develop demand-creation and lead-generation messaging
- integrate new value proposition into existing channels

Primary outputs:

- GTM plan
- channel strategy brief
- demand messaging pack
- channel integration plan

### 4. Sales Enablement and Asset Creation

Jobs to be done:

- educate the sales channel
- develop technical and solution data sheets
- create white papers and ROI assets
- build problem presentations and scripts
- generate pricing materials

Primary outputs:

- battle cards
- solution brief
- technical data sheet
- ROI calculator
- pricing and quoting pack

### 5. Ongoing Campaign Support

Jobs to be done:

- govern messaging for a campaign theme that spans several releases
- support outbound marketing with market/product insights
- maintain a content calendar
- generate recurring content assets

Primary outputs:

- campaign messaging house — **built** (`skills/lpa-campaign-messaging-house`)
- outbound insight brief
- content calendar
- newsletter draft
- press release draft

The campaign messaging house is the first output in this domain with an implementing skill. It matters to the architecture for a reason beyond the artifact itself: it is the first place the system governs work at the campaign layer rather than the release layer, and the first to carry a claim ledger — every claim with an ID, a proof source, and a status, where `Provisional` and `Unsupported` claims are barred from external derivatives. That ledger is the traceability principle below, enforced mechanically rather than by review.

## System layers

### Method layer

Contains the PMM process as reusable skills and workflow definitions.

Current home:

- `skills/`

### Artifact layer

Contains the structured outputs produced by the system.

Recommended home:

- `schemas/`
- `examples/`

### System layer

Contains orchestration and retrieval logic.

Recommended home:

- `agents/`
- `pipelines/`
- `connectors/`

### Evaluation layer

Contains quality checks, review criteria, and regression tests.

Recommended home:

- `evals/`

## Core vs client workspace model

The Product Marketing repo is the reusable PMM system of method.

Client-specific work should live in separate client workspaces that consume the repo workflows, schemas, and evals.

Core owns:

- reusable method
- reusable artifact contracts
- reusable retrieval and validation helpers
- reusable quality bar

Client workspaces own:

- client taxonomy
- source inventories
- coded records and syntheses
- client-facing briefs
- decision and action logs

See:

- [Core vs Client Workspaces](core-vs-client-workspaces.md)
- [Client Workspace Contract](client-workspace-contract.md)

## Target system architecture

### A. Evidence ingestion

Inputs:

- customer interviews
- sales call transcripts
- CRM notes
- competitive research
- product docs
- launch materials
- win/loss notes
- website and campaign materials

System responsibilities:

- normalize source metadata
- chunk and index evidence
- tag by segment, persona, competitor, stage, and confidence

### B. Research and synthesis agents

Responsibilities:

- competitive intelligence synthesis
- win/loss analysis
- unmet needs synthesis
- persona extraction
- buyer journey synthesis

These should produce structured drafts, not final messaging.

### C. Strategy agents

Responsibilities:

- positioning generation
- value proposition generation
- GTM planning
- launch planning
- pricing and packaging support

These should consume validated evidence and output reviewable artifacts.

### D. Asset generation agents

Responsibilities:

- battle cards
- sales scripts
- data sheets
- white papers
- ROI materials
- newsletters and press releases

These should be downstream of strategy, not parallel to it.

### E. Orchestrator

Responsibilities:

- decide which workflow to run
- retrieve the minimum necessary evidence
- route between skills
- enforce dependencies
- carry artifact state forward
- detect missing evidence rather than bluffing

## Design principles

- Retrieval before writing
- Evidence before messaging
- Structured outputs over long freeform prose
- One artifact at a time
- Human review at major locks and launches
- Traceability from output back to source evidence
- Conservative claims unless proof exists

## Minimum viable build order

1. Method OS
   Turn PMM method into reliable reusable skills and schemas
2. Human-in-the-loop PMM workspace
   Run workflows manually with LLMs using repo artifacts
3. Retrieval and evidence layer
   Add transcript, doc, and competitive evidence ingestion
4. PMM orchestrator
   Add workflow routing and stateful execution
5. Continuous PMM operations
   Add recurring monitoring and campaign support workflows
