# Conversation Synthesis Input Pack

This file is generated from parsed conversation records and serves as a synthesis-ready handoff artifact.

To regenerate it, run:

```bash
python3 scripts/build_conversation_synthesis_input.py \
  examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md \
  examples/conversations/parsed-fireflies-schleich-copenhagen-dsp.md \
  --objective "identify reusable discovery patterns for downstream persona and positioning work" \
  --segment "commerce operators evaluating analytics, audience, and managed-service platforms" \
  --persona-scope "operator / agency lead / brand stakeholder involved in evaluation and rollout decisions" \
  --time-window "2026-03-20 to 2026-03-23" \
  --output examples/conversations/conversation-synthesis-input-pack.generated.md
```
