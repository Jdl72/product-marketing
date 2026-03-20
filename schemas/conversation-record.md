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

## Evidence fields

- `primary_pains`
- `secondary_pains`
- `desired_outcomes`
- `current_alternatives`
- `objections`
- `buying_triggers`
- `evaluation_criteria`
- `trust_requirements`
- `competitors_mentioned`
- `language_to_use`
- `language_to_avoid`
- `notable_quotes`
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
