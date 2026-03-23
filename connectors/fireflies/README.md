# Fireflies Connector

## Purpose

Connect the discovery workflow to Fireflies transcripts.

## Authentication

Set:

- `FIREFLIES_API_KEY`

Do not hardcode API keys in the repo.

## What this connector should support first

1. list transcripts
2. fetch one transcript in detail
3. normalize transcript metadata into the conversation source pack

## First usage

Use:

- [scripts/fetch_fireflies_transcripts.py](/Users/jacklindberg/Documents/Product%20Marketing/scripts/fetch_fireflies_transcripts.py)

Example:

```bash
export FIREFLIES_API_KEY="your-key"
python3 scripts/fetch_fireflies_transcripts.py --limit 5
```

## Notes

- Treat Fireflies as a source system, not as the PMM artifact format.
- The connector's job is retrieval and normalization.
- Parsing and synthesis still happen in the PMM workflows.
