# Conversation Record Schema

## Purpose

Represent one parsed conversation as structured PMM evidence.

## Metadata

- `record_id`
- `source_id`
- `source_type`
- `date`
- `account_or_company`
- `segment`
- `persona_or_role`
- `conversation_context`
- `stakeholder_map`
  Optional. Use when multiple external stakeholders are present and their priorities differ.

## Evidence fields

- `primary_pains`
- `secondary_pains`
- `desired_outcomes`
- `current_alternatives`
- `objections`
- `contract_or_legal_objections`
- `buying_triggers`
- `evaluation_criteria`
- `trust_requirements`
- `competitors_mentioned`
- `language_to_use`
- `language_to_avoid`
- `notable_quotes`
  Preserve speaker attribution and source citation when available. Preferred format:
  `Speaker Name [sentence 123, 14:15-14:24]: "quote"`.
- `term_normalization_notes`
  Capture transcript term corrections or domain-specific normalization, for example `Packview` -> `Pacvue`.
- `summary_of_signal`

## Quality fields

- `evidence_strength`
  strong, moderate, weak
- `confidence`
  high, medium, low
- `missing_context`
- `open_questions`

## Notes

- Keep exact customer language separate from interpretation.
- Do not let one record claim segment-level truth by itself.
- In multi-party calls, preserve role-specific viewpoints instead of flattening them into one buyer voice.
