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
3. Capture:
   - pains
   - desired outcomes
   - current alternatives
   - objections
   - buying triggers
   - trust or evaluation criteria
4. Rate evidence strength conservatively.
5. Do not let one conversation pretend to represent the market.

## Artifact schema

Use:

- [conversation-record.md](/Users/jacklindberg/Documents/Product%20Marketing/schemas/conversation-record.md)

## Human review gate

Review for:

- quote fidelity
- evidence vs interpretation separation
- missing context
- overconfident conclusions

## Evals

Pass if:

- the parse preserves important customer language
- claims are tied to the source
- confidence reflects source quality

Fail if:

- generic summaries replace real signal
- internal assumptions are written as customer facts
- the parse cannot feed downstream PMM artifacts
