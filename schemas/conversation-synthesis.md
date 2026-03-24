# Conversation Synthesis Schema

## Purpose

Aggregate multiple conversation records into segment-level PMM evidence.

## Scope

- `synthesis_id`
- `objective`
- `segment`
- `persona_scope`
- `time_window`
- `record_count`

## Core outputs

- `top_recurring_pains`
- `desired_outcomes`
- `current_alternatives`
- `buying_triggers`
- `evaluation_criteria`
- `objections`
- `trust_requirements`
- `competitors_and_substitutes`
- `language_to_use`
- `language_to_avoid`
- `representative_quotes`
  Preserve speaker attribution and record-level citations. Preferred format:
  `Speaker Name [record convrec-..., sentence 123, 14:15-14:24]: "quote"`.

## Analysis fields

- `strongly_supported_patterns`
  Each pattern should cite the supporting records.
- `emerging_patterns`
  Each pattern should cite the supporting records and indicate limited support.
- `contradictory_signals`
  Each contradiction should name the records or stakeholders in tension.
- `strategic_implications`
- `recommended_downstream_artifacts`

## Quality fields

- `coverage_notes`
- `bias_risks`
- `confidence`

## Notes

- Preserve contradictions when they are real.
- Mark where evidence is strong enough to guide strategy versus only suggestive.
- Do not make synthesis claims without record-level support.
