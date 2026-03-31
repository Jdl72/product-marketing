# Config-Aware Customer Conversation Runbook

## Purpose

Describe how the core customer-conversation workflow should behave when a client workspace is present.

The method stays generic. The client workspace provides the context needed to scope, tag, and evaluate the evidence responsibly.

## Inputs

Core workflow inputs:

- source systems or transcript files
- PMM objective
- date range
- target conversation type

Client workspace inputs:

- segment taxonomy
- funnel stages
- competitor map
- coding rules
- strategic questions
- scorecard metrics

## Run sequence

### 1. Define the objective

Start with the PMM objective in generic terms.

Examples:

- persona research
- win/loss analysis
- positioning refresh
- sales-enablement proof work

Then check the client workspace for:

- which segments are in scope
- which stages matter
- which leadership questions need answers

### 2. Gather sources

Use the core `Gather Customer Conversations` job.

Client config should only affect:

- which conversations count as relevant
- which stages and source types to prioritize
- which gaps to flag explicitly

Do not alter the source-pack schema for one client.

### 3. Parse conversations

Use the core `conversation-record` schema.

Client config may add interpretation guidance for:

- stage mapping
- segment mapping
- competitor normalization
- buying-trigger tagging
- objection tagging
- proof-type tagging

If a client-specific taxonomy item is missing, keep the generic schema field and mark the client-specific interpretation as unresolved.

### 4. Synthesize the set

Use the core `Synthesize Conversation Set` job.

Client config should shape:

- which groups to synthesize separately
- which strategic questions must be answered
- which recurring patterns matter most
- which metrics or leadership concerns should be addressed

Do not invent confidence based on client urgency or anecdotal salience.

### 5. Route to downstream artifacts

Use the synthesis to feed:

- strategy outputs in the client workspace
- decision and action logs
- future generic artifacts in the core method

Examples:

- positioning brief
- win/loss synthesis
- discovery log
- sales-enablement brief

## Fixed vs configurable behavior

### Fixed in core

- source provenance rules
- quote traceability rules
- confidence discipline
- schema structure
- eval quality bar

### Configurable per client

- stage labels
- segment labels
- competitor taxonomy
- buying triggers
- objection categories
- proof categories
- leadership questions
- scorecard focus

## Failure modes to avoid

- allowing a client taxonomy to replace the generic schema
- using client strategy language as if it were source evidence
- collapsing multiple segments into one synthesis because the client uses a single sales narrative
- hiding contradictory evidence because it conflicts with a preferred positioning direction
- treating missing config as permission to invent new client categories

## Definition of done

The workflow is working correctly when:

- sources are inventoried with provenance
- client config improves scoping and grouping without distorting the evidence
- records remain comparable across clients
- syntheses answer client questions while preserving traceability
- downstream briefs can cite real quotes and source records directly
