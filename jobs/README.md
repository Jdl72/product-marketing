# Jobs

This directory turns high-level PMM jobs into buildable, reusable job specs.

Each job spec should define:

- `job`
  The core functional thing the user is trying to get done
- `trigger`
  When the job should run
- `inputs`
  What evidence or files are required
- `method`
  The process to follow
- `artifacts`
  What should be produced
- `review gates`
  Where a human should approve or correct
- `evals`
  What pass/fail means

Schema-backed workflows that are not yet full job specs should still declare their reusable boundaries in:

- [workflow contracts](/tmp/product-marketing-contracts/docs/contracts/README.md)

## Current first-workstream

The first jobs in this repo focus on customer conversations and feedback:

1. `gather-customer-conversations`
2. `parse-single-conversation`
3. `synthesize-conversation-set`

These three jobs create the evidence foundation for personas, positioning, GTM, and sales enablement.
