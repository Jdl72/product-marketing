# Conversation Source Pack Example: Commerce Platform Discovery — March 2026

## Pack-level fields

- `objective`: `identify recurring discovery patterns to drive persona and positioning work for commerce analytics and audience-building segment`
- `time_window`: `2026-01-01 to 2026-03-31`
- `segments_included`:
  - `multi-brand ecommerce operator`
  - `brand plus agency evaluating AMC and DSP partnership`
- `source_count`: `5`
- `known_gaps`:
  - No sources from self-serve customers who did not engage sales
  - No sources from SMB accounts under $1M managed spend
  - Only one churn / lost-deal source included
- `review_status`: `ready for parsing`

---

## Source inventory

### Source 1

- `source_id`: `src-001`
- `source_system`: `fireflies`
- `external_source_id`: `01KM6GSRBZNXNSKQW5BQNDG2M9`
- `source_type`: `sales_call`
- `title`: `Ejam Pricing Follow-Up`
- `date`: `2026-03-20`
- `account_or_company`: `Ejam`
- `segment`: `multi-brand ecommerce operator`
- `persona_or_role`: `operator / buyer evaluating ad-tech and service model`
- `channel`: `video call`
- `raw_file_path_or_link`: `examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md`
- `source_url`: `https://app.fireflies.ai/view/01KM6GSRBZNXNSKQW5BQNDG2M9`
- `has_transcript`: `true`
- `has_summary`: `true`
- `language_quality`: `high`
- `completeness`: `full`
- `confidence`: `high`
- `readiness_status`: `ready for parsing`
- `notes`: `Strong commercial signal. Rich objection and pricing language. Primary voice is Sam Sutcu, single external stakeholder.`

---

### Source 2

- `source_id`: `src-002`
- `source_system`: `fireflies`
- `external_source_id`: `01KMDFR8SB2ZEPT3452AFH85F9`
- `source_type`: `sales_call`
- `title`: `Schleich / Copenhagen Commerce DSP Discovery`
- `date`: `2026-03-23`
- `account_or_company`: `Schleich with Copenhagen Commerce`
- `segment`: `brand plus agency evaluating AMC and DSP partnership`
- `persona_or_role`: `agency lead and brand stakeholder`
- `channel`: `video call`
- `raw_file_path_or_link`: `examples/conversations/parsed-fireflies-schleich-copenhagen-dsp.md`
- `source_url`: `https://app.fireflies.ai/view/01KMDFR8SB2ZEPT3452AFH85F9`
- `has_transcript`: `true`
- `has_summary`: `true`
- `language_quality`: `high`
- `completeness`: `full`
- `confidence`: `high`
- `readiness_status`: `ready for parsing`
- `notes`: `Multi-stakeholder call. Two distinct external voices with different priorities. Strong discovery signal on workflow and partnership design needs.`

---

### Source 3

- `source_id`: `src-003`
- `source_system`: `local_file`
- `external_source_id`: `null`
- `source_type`: `cs_call`
- `title`: `Renewals Check-In — TechBrands Group`
- `date`: `2026-02-14`
- `account_or_company`: `TechBrands Group`
- `segment`: `multi-brand ecommerce operator`
- `persona_or_role`: `account owner / CS contact`
- `channel`: `phone call notes`
- `raw_file_path_or_link`: `sources/raw/techbrands-renewals-feb2026.txt`
- `source_url`: `null`
- `has_transcript`: `false`
- `has_summary`: `true`
- `language_quality`: `low`
- `completeness`: `partial`
- `confidence`: `low`
- `readiness_status`: `needs review`
- `notes`: `Handwritten notes from a phone call, transcribed by the CS rep after the fact. No direct customer language preserved. Summary is generic and likely influenced by internal framing. Do not treat as verbatim evidence. Use only for context signals if included.`

---

### Source 4

- `source_id`: `src-004`
- `source_system`: `crm`
- `external_source_id`: `crm-opp-88124`
- `source_type`: `crm_note`
- `title`: `Pinnacle Media — Post-Demo Notes`
- `date`: `2026-03-05`
- `account_or_company`: `Pinnacle Media`
- `segment`: `multi-brand ecommerce operator`
- `persona_or_role`: `buyer / evaluator`
- `channel`: `CRM`
- `raw_file_path_or_link`: `sources/raw/pinnacle-media-crm-notes-mar2026.txt`
- `source_url`: `null`
- `has_transcript`: `false`
- `has_summary`: `true`
- `language_quality`: `medium`
- `completeness`: `partial`
- `confidence`: `medium`
- `readiness_status`: `needs review`
- `notes`: `CRM note captured by AE immediately after demo. Covers top objections and evaluation questions. No direct quotes, but objections are specific enough to be useful. Partial because the buying committee composition is not recorded and the AE note covers only the final 20 minutes of a 60-minute call.`

---

### Source 5

- `source_id`: `src-005`
- `source_system`: `fireflies`
- `external_source_id`: `01KL9XTRQP4WBZM2K8DJFN7CU1`
- `source_type`: `sales_call`
- `title`: `Meridian Commerce — Duplicate of Discovery Call Recording`
- `date`: `2026-03-10`
- `account_or_company`: `Meridian Commerce`
- `segment`: `multi-brand ecommerce operator`
- `persona_or_role`: `operator / evaluator`
- `channel`: `video call`
- `raw_file_path_or_link`: `sources/raw/meridian-discovery-duplicate.md`
- `source_url`: `https://app.fireflies.ai/view/01KL9XTRQP4WBZM2K8DJFN7CU1`
- `has_transcript`: `true`
- `has_summary`: `true`
- `language_quality`: `high`
- `completeness`: `full`
- `confidence`: `high`
- `readiness_status`: `exclude`
- `notes`: `Duplicate of src-006 (Meridian Commerce discovery call, same date, same participants). Fireflies created a second recording when the call host rejoined after a connection drop. This version covers only the first 12 minutes. Excluded in favor of src-006 which is the complete recording.`

---

## Review notes

- Sources 1 and 2 are the primary parsing targets. Both are `ready for parsing`.
- Sources 3 and 4 are flagged `needs review`. A human reviewer should decide whether to include them in parsing given their partial/low-quality status.
- Source 5 is excluded as a confirmed duplicate. The full version (src-006) is not included in this example pack but would appear in a production pack.
- The most significant known gap is the absence of lost-deal or churned-customer sources. Patterns from this pack will over-represent active evaluators.
