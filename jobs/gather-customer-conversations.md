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

**Flagging rules — apply to every source before inventory is finalized:**

- **Duplicate:** Two or more sources cover the same conversation or the same customer feedback event. Mark each duplicate as `status: exclude — duplicate of [source_id]`. Keep the higher-quality version and discard the rest.
- **Partial source:** The transcript or notes are incomplete — e.g., recording cut off early, only one side of an email thread is captured, or the summary omits the product discussion. Mark as `completeness: partial` and `status: needs review`. Do not silently include partial sources as if they were complete.
- **Low-quality source:** The transcript has heavy noise, the language quality is too degraded to trust, or the source is so sparse that meaningful customer language cannot be extracted. Mark as `language_quality: low` and `status: needs review` or `status: exclude`. Note the specific quality problem in the `notes` field.

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

- [conversation-source-pack.md](../schemas/conversation-source-pack.md)

## Readiness status

Every source in the inventory must have one of three statuses before the pack is frozen:

- **`ready for parsing`** — complete source, acceptable quality, correct segment, no unresolved duplicate flag
- **`needs review`** — partial source, low quality, unclear segment fit, or a quality concern that requires human judgment before parsing proceeds
- **`exclude`** — confirmed duplicate, out-of-scope segment, or quality too degraded to produce reliable PMM evidence

Sources with status `needs review` or `exclude` must not be routed to the parsing job without an explicit human decision recorded in the pack.

## Human review gate

Before moving on, confirm all of the following. Each item is a hard gate — the pack does not advance until it passes.

**Source quality gate:**
- Every source has a `readiness_status` of `ready for parsing`, `needs review`, or `exclude`.
- No source with `status: needs review` or `status: exclude` is silently included in the parsing queue.
- Duplicate sources are marked and the reason for exclusion is recorded.
- Partial and low-quality sources are explicitly flagged, not silently carried forward.

**Segment fit gate:**
- Every included source maps to the target segment.
- Sources from adjacent or unclear segments are either excluded or flagged with a note explaining why they are included.

**Coverage adequacy gate:**
- The pack has enough sources to support the intended PMM task (e.g., at least three distinct customer voices for persona work; more for positioning).
- `known_gaps` is filled in, even if the answer is "none identified."
- The distribution across segments, roles, and source types is not obviously lopsided.

**Pack-level pass condition:**
All three gates above must be met and `review_status` must be set to `ready for parsing` before handing the pack to the next job.

## Evals

Pass if:

- sources are inventoried with metadata
- every source has a `readiness_status` of `ready for parsing`, `needs review`, or `exclude`
- duplicates are explicitly flagged and excluded, not silently included
- partial sources are marked `completeness: partial` and given a `needs review` or `exclude` status
- low-quality sources are marked `language_quality: low` with a note explaining the quality problem
- source coverage is adequate for the intended PMM task
- missing evidence is explicitly called out in `known_gaps`
- the pack-level `review_status` is set to `ready for parsing` only after all three review gates pass

Fail if:

- the pack is just a pile of files with no inventory
- source type and segment are unclear
- summaries replace original evidence without traceability
- duplicate or low-quality sources are included without a flag
- `review_status` is set to `ready for parsing` but partial or low-quality sources are still in the parsing queue without a note
