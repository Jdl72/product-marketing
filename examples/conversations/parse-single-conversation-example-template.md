# Parse Single Conversation Example Template

## Raw source metadata

- `source_id`:
- `source_type`:
- `date`:
- `account_or_company`:
- `segment`:
- `persona_or_role`:
- `conversation_context`:
- `stakeholder_map`:

## Raw source summary

Write 2-4 lines describing what this source is and why it was chosen.

## Parsed conversation record

Use the schema in:

- [conversation-record.md](../../schemas/conversation-record.md)

Suggested sections:

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
  Include speaker attribution and source anchors when available.
- `term_normalization_notes`
- `summary_of_signal`
- `evidence_strength`
- `confidence`
- `missing_context`
- `open_questions`

## Review notes

After the manual run, capture:

- what felt easy
- what was ambiguous
- what the schema missed
- what the job spec should clarify
- what should become an eval rule

## Output quality verdict

- `usable as-is`
- `usable with edits`
- `not usable`

Explain why.
