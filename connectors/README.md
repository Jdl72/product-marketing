# Connectors

This directory holds source-system integrations for PMM evidence gathering.

## Current connectors

- `fireflies/`
  Pull transcripts and transcript metadata from Fireflies for discovery workflows

## Design rule

Connectors only fetch and normalize source material.

They should not:

- synthesize PMM strategy
- generate final artifacts
- replace the job specs or schemas
