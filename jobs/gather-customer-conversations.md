# Job Spec: Gather Customer Conversations

## Core job

When I have customer conversations, call notes, transcripts, emails, support threads, and feedback scattered across tools and folders, help me assemble a clean evidence pack that can be parsed reliably.

## Why this job matters

If the evidence pack is weak or messy, every downstream PMM artifact becomes less trustworthy.

## Trigger

Run this job when:

- starting a new PMM workflow
- preparing for persona or positioning work
- preparing for win/loss analysis
- preparing for launch or GTM planning

## Inputs

Potential source types:

- interview transcripts
- sales calls
- customer success calls
- support tickets
- CRM notes
- email threads
- survey responses
- user research notes

## Desired outputs

- `conversation-source-pack`
- `source inventory`
- `source quality notes`
- `parsing-ready file set`

## Universal job map

### 1. Define

Define:

- target segment
- target time window
- conversation types to include
- research question or PMM workflow being supported

### 2. Locate

Locate all relevant sources across drives, notes, CRM exports, and transcript stores.

Supported source systems can include:

- Fireflies
- local transcript exports
- CRM exports
- email exports
- support systems

### 3. Prepare

Normalize the source set:

- remove obvious duplicates
- standardize filenames
- record source metadata
- separate raw source from working notes

### 4. Confirm

Confirm the source set is good enough:

- enough coverage by segment
- enough recent material
- enough direct customer language
- major gaps called out explicitly

### 5. Execute

Assemble the evidence pack and inventory.

### 6. Monitor

Track:

- missing sources
- poor transcript quality
- low-confidence notes
- over-representation of one customer type

### 7. Modify

Refine the source set if key gaps exist.

### 8. Conclude

Freeze the pack for parsing and hand off to the next job.

## Method

1. Define the evidence objective first.
   Example: persona research, positioning refresh, win/loss review.
2. Create a source inventory before summarizing anything.
3. Prefer original transcripts over summaries when both exist.
4. Preserve source provenance for every item.
5. Mark confidence on each source.
6. When using a source system like Fireflies, normalize source metadata before any PMM summarization.

## Artifact schema

Use:

- [conversation-source-pack.md](/Users/jacklindberg/Documents/Product%20Marketing/schemas/conversation-source-pack.md)

## Human review gate

Before moving on, confirm:

- the right sources are included
- the segment/time scope is correct
- the evidence pack is not overly biased or sparse

## Evals

Pass if:

- sources are inventoried with metadata
- duplicates are controlled
- source coverage is adequate for the intended PMM task
- missing evidence is explicitly flagged

Fail if:

- the pack is just a pile of files with no inventory
- source type and segment are unclear
- summaries replace original evidence without traceability
