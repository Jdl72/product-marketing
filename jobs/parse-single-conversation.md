# Job Spec: Parse Single Conversation

## Core job

When I have one customer conversation or feedback artifact, help me turn it into a structured PMM evidence record without losing the customer’s words or over-interpreting the source.

## Trigger

Run this job for:

- one transcript
- one sales call
- one interview note set
- one support thread
- one email exchange

## Inputs

- one raw conversation source
- source metadata if available
- optional hypothesis or research focus

## Desired outputs

- `conversation-record`
- pain points
- desired outcomes
- alternatives
- objections
- customer language
- evidence quality rating

## Universal job map

### 1. Define

Define what kind of source this is and what PMM question it may inform.

### 2. Locate

Locate:

- raw text
- speaker roles
- account or segment info
- date and context

### 3. Prepare

Prepare the source by:

- cleaning obvious formatting noise
- separating interviewer/internal notes from customer language
- marking low-confidence sections
- identifying whether one or multiple external stakeholders are present; if multiple, list each stakeholder by name and role before parsing begins
- identifying obvious transcript term errors that should be normalized; record each normalization in `term_normalization_notes` with the original form and the corrected form

### 4. Confirm

Confirm there is enough signal to parse:

- identifiable customer statements
- enough context to interpret the conversation

### 5. Execute

Extract structured PMM evidence.

### 6. Monitor

Watch for:

- hallucinated interpretation
- over-compression
- weak or missing customer quotes
- confusion between seller language and customer language

### 7. Modify

Revise the parse if it is too generic or too interpretive.

### 8. Conclude

Save the conversation record and route it to synthesis.

## Method

1. Preserve the source type and context.
2. Separate exact language from inferred meaning.
3. Attribute quotes to speakers whenever the source supports it.
4. Include sentence-level or timestamp-level citation anchors on notable quotes whenever the source supports it.
5. Normalize domain-specific terms conservatively and record each normalization.
6. Capture:
   - pains
   - desired outcomes
   - current alternatives
   - objections
   - contract or legal objections when present
   - buying triggers
   - trust or evaluation criteria
   - stakeholder-specific priorities when the source includes multiple external voices
7. Rate evidence strength conservatively.
8. Do not let one conversation pretend to represent the market.

## Artifact schema

Use:

- [conversation-record.md](/Users/jacklindberg/Documents/Product%20Marketing/schemas/conversation-record.md)

## Human review gate

Review for each of the following. All items are active checks — not optional:

- **Quote fidelity:** Quoted language matches the source verbatim. No paraphrasing inside quotation marks.
- **Speaker attribution:** Every quoted statement identifies the speaker by name when the source supports it. Unattributed quotes are only acceptable when the transcript genuinely cannot identify the speaker.
- **Transcript citation anchors:** Every notable quote includes a sentence number or timestamp anchor when the source supports it (e.g., `[sentence 231, 14:15-14:24]`).
- **Evidence vs interpretation separation:** Customer language is preserved in dedicated fields (e.g., `notable_quotes`, `language_to_use`). Interpretations go in summary and evidence fields. The two are not mixed.
- **Stakeholder mapping:** If multiple external stakeholders were present, the record includes a `stakeholder_map` that names each stakeholder and their role. Distinct priorities are preserved in the relevant evidence fields rather than flattened.
- **Term normalization:** Every transcript term that was corrected or normalized is recorded in `term_normalization_notes` with the original form and the corrected form. Normalization is conservative — only clear and well-supported corrections are applied.
- **Overconfident conclusions:** Confidence ratings and evidence strength reflect the actual source quality, not wishful thinking.
- **Missing context:** Known gaps and open questions are recorded so downstream synthesis does not treat the record as complete.

## Evals

Pass if:

- the parse preserves important customer language
- claims are tied to the source
- confidence reflects source quality

Fail if:

- generic summaries replace real signal
- internal assumptions are written as customer facts
- distinct stakeholder needs are collapsed without noting the difference
- quoted language loses speaker attribution when the transcript supports it
- the parse cannot feed downstream PMM artifacts
