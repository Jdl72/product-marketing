# Discovery System Flow

## Purpose

This document is the roadmap artifact for the discovery-first PMM system.

It defines the recommended structure of:

- discovery-focused agents
- reusable skills
- core evidence artifacts
- downstream dependencies

## Why discovery comes first

The quality of later PMM outputs depends on the quality of discovery.

If the customer evidence layer is weak:

- personas become generic
- positioning becomes speculative
- GTM plans become ungrounded
- sales assets become shallow
- campaign support drifts into content generation without strategy

Because of that, the system should be built from the discovery layer upward.

## Architecture principle

Build:

`raw conversations -> normalized evidence -> parsed records -> synthesis -> insight artifacts -> strategy artifacts -> downstream assets`

Do not invert this order.

## System view

```mermaid
flowchart TD
    A["Raw Customer Inputs"] --> A1["Interview transcripts"]
    A --> A2["Sales call notes"]
    A --> A3["Customer success calls"]
    A --> A4["Support tickets and emails"]
    A --> A5["CRM notes and win-loss notes"]
    A --> A6["Survey responses and forms"]

    A1 --> B["Discovery Orchestrator"]
    A2 --> B
    A3 --> B
    A4 --> B
    A5 --> B
    A6 --> B

    B --> C1["Skill: Gather Customer Conversations"]
    C1 --> C2["Artifact: Conversation Source Pack"]

    C2 --> D1["Agent: Source Normalizer"]
    D1 --> D2["Skill: Parse Single Conversation"]
    D2 --> D3["Artifact: Conversation Record"]

    D3 --> E1["Agent: Conversation Synthesizer"]
    E1 --> E2["Skill: Synthesize Conversation Set"]
    E2 --> E3["Artifact: Conversation Synthesis"]

    E3 --> F1["Agent: Persona Builder"]
    E3 --> F2["Agent: Buyer Journey Mapper"]
    E3 --> F3["Agent: Positioning Input Builder"]
    E3 --> F4["Agent: Win-Loss Analyzer"]
    E3 --> F5["Agent: Objection and Alternative Mapper"]

    F1 --> G1["Artifact: Persona Pack"]
    F2 --> G2["Artifact: Buyer Journey Map"]
    F3 --> G3["Artifact: Positioning Brief Input"]
    F4 --> G4["Artifact: Win-Loss Synthesis"]
    F5 --> G5["Artifact: Objection and Alternative Map"]

    G1 --> H["Downstream PMM System"]
    G2 --> H
    G3 --> H
    G4 --> H
    G5 --> H

    H --> H1["Positioning"]
    H --> H2["Value Proposition"]
    H --> H3["GTM Plan"]
    H --> H4["Sales Enablement"]
    H --> H5["Campaign Support"]
```

## Simple mental model

```mermaid
flowchart LR
    A["Raw conversations"] --> B["Source pack"]
    B --> C["Parsed conversation records"]
    C --> D["Synthesis layer"]
    D --> E["Insight artifacts"]
    E --> F["Strategy artifacts"]
    F --> G["Sales and GTM assets"]
```

## Agent and skill boundaries

### Skills

Skills should hold the stable method.

Recommended discovery-first skills:

- `Gather Customer Conversations`
- `Parse Single Conversation`
- `Synthesize Conversation Set`
- `Customer Interview`
- `Weekly Discovery Log`

### Agents

Agents should execute and orchestrate.

Recommended discovery-first agents:

- `Discovery Orchestrator`
  decides what to run next and tracks workflow state
- `Source Normalizer`
  prepares raw inputs for parsing
- `Conversation Synthesizer`
  aggregates parsed records into evidence patterns
- `Persona Builder`
  turns synthesis into persona-ready output
- `Win-Loss Analyzer`
  extracts loss drivers, win drivers, and objections

## Core artifacts

These are the required evidence artifacts for discovery-first PMM work:

- `Conversation Source Pack`
- `Conversation Record`
- `Conversation Synthesis`
- `Persona Pack`
- `Buyer Journey Map`
- `Positioning Brief Input`

## Recommended build order

### Phase 1: Evidence foundation

Build first:

1. `Gather Customer Conversations`
2. `Parse Single Conversation`
3. `Synthesize Conversation Set`

Definition of done:

- raw sources are inventoried
- parsed records are consistent
- synthesis can support one downstream PMM artifact

### Phase 2: Insight layer

Build next:

4. `Persona Pack`
5. `Buyer Journey Map`
6. `Win-Loss Synthesis`
7. `Objection and Alternative Map`

Definition of done:

- the system can produce structured buyer understanding from conversation evidence

### Phase 3: Strategy layer

Build next:

8. `Positioning Brief`
9. `Value Proposition Brief`
10. `GTM Plan`

Definition of done:

- strategy outputs are grounded in evidence rather than invented from scratch

### Phase 4: Downstream asset layer

Build after discovery and strategy are stable:

11. `Battle Cards`
12. `Sales Scripts`
13. `ROI Assets`
14. `Demand Messaging`
15. `Campaign Support`

## Solo-builder recommendation

For one person, do not start with a full multi-agent system.

Start with:

- one lightweight orchestrator
- three discovery-first skills
- three stable schemas
- human review on every output

That means:

- agent complexity stays low
- output quality stays inspectable
- later automation has a clean evidence foundation

## Roadmap decision rule

If a proposed PMM workflow cannot clearly say:

- what discovery evidence it needs
- what evidence artifact it consumes
- what structured artifact it produces

then it should not be built yet.

## Repo connections

This roadmap artifact connects to:

- [First Workstream: Customer Conversations](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/first-workstream-customer-conversations.md)
- [PMM Agent System](/Users/jacklindberg/Documents/Product%20Marketing/docs/architecture/pmm-agent-system.md)
- [Jobs README](/Users/jacklindberg/Documents/Product%20Marketing/jobs/README.md)
