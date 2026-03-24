# Runbook: Parse Single Conversation

## Purpose

This is the practical runbook for executing the first useful PMM workflow manually.

It is the bridge between:

- the job spec
- the schema
- the example
- the eval rubric

## Use this when

You have one real customer conversation and want to pressure-test the workflow before building automation.

## Inputs

Required:

- one raw customer conversation source
- source metadata

Optional:

- target segment
- PMM question
- related hypothesis

## Step-by-step

### Step 1: Prepare the source

Capture:

- source type
- date
- account or company
- segment
- role
- conversation context
- stakeholder map if more than one external voice is present
- obvious transcript term corrections that should be normalized

If the source is partial or messy, note that before parsing.

### Step 2: Run the job spec

Use:

- [parse-single-conversation.md](/Users/jacklindberg/Documents/Product%20Marketing/jobs/parse-single-conversation.md)

The goal is not elegant prose.
The goal is a usable `conversation-record`.

### Step 3: Fill the schema

Use:

- [conversation-record.md](/Users/jacklindberg/Documents/Product%20Marketing/schemas/conversation-record.md)

Do not force all fields if the source does not support them.
Instead:

- leave them empty
- mark missing context
- lower confidence

If the source is multi-party:

- preserve role-specific priorities
- note where external stakeholders disagree or emphasize different outcomes

If the transcript has speaker labels:

- preserve speaker attribution on the most important quotes
- do not strip attribution unless the transcript itself is unreliable
- include sentence index or timestamp anchors so a reviewer can find the quote quickly

### Step 4: Save an example

Use:

- [parse-single-conversation-example-template.md](/Users/jacklindberg/Documents/Product%20Marketing/examples/conversations/parse-single-conversation-example-template.md)

This becomes the first example and quality anchor.

### Step 5: Score the output

Use:

- [conversation-record-rubric.md](/Users/jacklindberg/Documents/Product%20Marketing/evals/conversation-record-rubric.md)

Capture:

- strongest part
- weakest part
- what the schema missed
- what should become an automated eval later

### Step 6: Tighten the system

After each manual run, update one or more of:

- job spec
- schema
- example template
- eval rubric

Recent schema gaps exposed by real calls:

- `contract_or_legal_objections`
- `stakeholder_map`
- `term_normalization_notes`
- attributed `notable_quotes`
- sentence-level quote citations

## Definition of done

One run is complete when:

- a `conversation-record` exists
- it has been reviewed with the rubric
- review notes identify concrete schema or method gaps

## Recommended repetition

Run this manually at least three times before automating it.

Why:

- first run exposes obvious schema gaps
- second run tests whether fixes generalized
- third run tells you whether the workflow is stable enough to automate
