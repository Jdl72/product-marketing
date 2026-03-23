# Conversation Record Rubric

## Purpose

Evaluate whether a parsed conversation record is good enough for internal PMM use.

Use this rubric after every manual `parse-single-conversation` run.

## Scoring scale

- `1 = poor`
- `3 = acceptable`
- `5 = strong`

## Dimensions

### 1. Source fidelity

Question:

Does the record preserve what the customer actually said without rewriting everything into generic PMM language?

High score:

- exact or near-exact customer wording is preserved where important
- quotes feel anchored to the source

Low score:

- the output sounds smooth but loses the customer voice

### 2. Evidence vs interpretation separation

Question:

Can you tell what came from the source and what was inferred?

High score:

- interpretation is clearly bounded
- unsupported conclusions are avoided

Low score:

- inference is presented as fact

### 3. Completeness

Question:

Does the record capture the major PMM evidence fields that matter for downstream work?

High score:

- pains, outcomes, alternatives, objections, and quotes are all present if the source supports them

Low score:

- major fields are missing without explanation

### 4. Context preservation

Question:

Does the output preserve enough context to make the evidence meaningful?

High score:

- source type, segment, persona, and conversation context are clear

Low score:

- the record could have come from anyone about anything

### 5. Confidence calibration

Question:

Is the stated confidence appropriate for the quality of the source?

High score:

- weak sources are marked weak
- ambiguity is preserved

Low score:

- the record sounds more certain than the evidence justifies

### 6. Downstream usefulness

Question:

Could a PMM use this record in persona, positioning, or synthesis work?

High score:

- the record is structured, specific, and reusable

Low score:

- the output is too vague to feed another workflow

### 7. Stakeholder fidelity

Question:

If multiple external stakeholders are present, does the record preserve where their needs differ?

High score:

- role-specific viewpoints are called out when they matter
- the output does not collapse agency, brand, buyer, and user needs into one voice

Low score:

- the output flattens distinct viewpoints into one generic customer perspective

## Pass / fail rule

Pass if:

- no critical hallucination or source-fidelity problem exists
- average score is at least `3`
- `downstream usefulness` is at least `3`

Fail if:

- the record invents evidence
- key customer language is erased
- confidence is clearly overstated
- multi-party source nuance is erased
- the output cannot support downstream PMM work

## Review notes to capture every time

- strongest part of the parse
- weakest part of the parse
- schema gap exposed
- job-spec clarification needed
- candidate future automated eval
