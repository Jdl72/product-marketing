# Conversation Source Pack Schema

## Purpose

Inventory and normalize the raw customer conversation set before parsing begins.

## Fields

- `source_id`
- `source_system`
  fireflies, local_file, crm, email, support_tool, survey_tool, other
- `external_source_id`
- `source_type`
  interview, sales_call, cs_call, support_ticket, crm_note, email_thread, survey_response, other
- `title`
- `date`
- `account_or_company`
- `segment`
- `persona_or_role`
- `channel`
- `raw_file_path_or_link`
- `source_url`
- `has_transcript`
- `has_summary`
- `language_quality`
  high, medium, low
- `completeness`
  full, partial, fragment
- `confidence`
  high, medium, low
- `notes`

## Pack-level fields

- `objective`
- `time_window`
- `segments_included`
- `source_count`
- `known_gaps`
- `review_status`

## Notes

- Prefer original evidence over secondhand summary.
- Preserve enough metadata to support later filtering and trust decisions.
