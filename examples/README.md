# Examples

This directory holds worked examples for PMM workflows.

Examples are important because they define what "done" looks like before automation exists.

Use examples to:

- calibrate output quality
- refine schemas
- write eval rubrics
- regression test future workflow changes

## Recommended structure

- `conversations/`
  Raw and parsed conversation examples
- `personas/`
  Persona outputs grounded in real evidence
- `positioning/`
  Positioning outputs grounded in conversation synthesis

## Current starting point

The first examples should focus on:

1. one raw customer conversation
2. one parsed `conversation-record`
3. one small `conversation-synthesis`

Current concrete examples:

- [Parsed conversation: Ejam Pricing Follow-Up](conversations/parsed-fireflies-ejam-pricing-follow-up.md)
- [Parsed conversation: Schleich / Copenhagen DSP Conversation](conversations/parsed-fireflies-schleich-copenhagen-dsp.md)
- [Conversation synthesis input pack guide](conversations/conversation-synthesis-input-pack.md)
- [Generated conversation synthesis input pack](conversations/conversation-synthesis-input-pack.generated.md)
- [Conversation synthesis example](conversations/conversation-synthesis-example.md)
