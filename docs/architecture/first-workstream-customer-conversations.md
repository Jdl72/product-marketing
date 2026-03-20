# First Workstream: Customer Conversations

## Why start here

For a solo builder, customer conversations are the highest-leverage starting point because they feed almost every later PMM job:

- personas
- buyer journey
- positioning
- value proposition
- GTM planning
- sales enablement
- ROI framing

If this layer is weak, everything downstream becomes generic.

## First three jobs

### 1. Gather customer conversations

Goal:

Create a clean, parsing-ready source pack.

Primary output:

- `conversation-source-pack`

### 2. Parse a single conversation

Goal:

Turn one source into a structured PMM evidence record.

Primary output:

- `conversation-record`

### 3. Synthesize a conversation set

Goal:

Turn many parsed records into segment-level PMM evidence.

Primary output:

- `conversation-synthesis`

## Recommended solo workflow

1. Pick one PMM objective.
   Example: persona research for one segment.
2. Gather 5-15 relevant raw sources.
3. Build the source pack.
4. Parse 3-5 conversations manually with an LLM and your schema.
5. Review and tighten the parsing instructions.
6. Synthesize the parsed set.
7. Feed the synthesis into one downstream artifact such as persona pack or positioning brief.

## Quality bar for v1

Useful internal workflow means:

- source inventory exists
- parsed records are consistent enough to compare
- synthesis preserves real language and confidence
- one downstream PMM artifact can be created from the evidence

## What not to build first

Do not start with:

- full autonomy
- multi-agent orchestration
- vector databases
- complex UI
- broad campaign generation

Start with:

- stable inputs
- stable outputs
- human review
- repeatable schemas

## Recommended next issue order

For the existing GitHub roadmap, the best immediate sequence is:

1. `#10 Build persona pack workflow and schema`
2. add a new conversation-source schema issue
3. add a new conversation-record schema issue
4. add a new conversation-synthesis workflow issue
5. `#12 Build positioning brief workflow from PMM evidence`

## Connection to current PMM skills

These jobs feed especially well into:

- `Customer Interview`
- `Weekly Discovery Log`
- `Positioning Canvas`
- `PR-FAQ Template`
- `Segment Playbooks`
- `Attack Matrix`
