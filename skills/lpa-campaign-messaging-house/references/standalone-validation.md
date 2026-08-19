# Standalone Campaign Validation

Use this protocol only when the repository's `Bar Test` and `Certification Rubric` skills are unavailable. It does not waive either quality gate.

## 1. Mechanical validation

From the `lpa-campaign-messaging-house` skill directory, run:

```bash
python3 scripts/validate_campaign_messaging_house.py <campaign-house.md>
```

Resolve every error before continuing. A warning may remain only when the artifact stays in Draft mode.

## 2. Message test

Test the three recommended hooks and each pillar's approved phrasing verbatim with 3–5 people who understand the target buyer but did not create the house.

Record:

| Message | Testers | Correct restatement count | Pass rate | Verbatim confusion | Decision |
|---|---:|---:|---:|---|---|
| | | | | | `Pass` / `Revise` |

Require at least 80% correct restatement for every tested message. Revise the ledger first, then regenerate affected derivatives and retest.

## 3. Campaign certification

Score each dimension from 1–5 and cite the house section or claim ID that supports the score:

- Clarity
- Differentiation
- Customer-Centricity
- Proof / Evidence
- Consistency
- Emotional Resonance
- Competitive Awareness
- Actionability
- Channel Fit

Require an average of at least 3.0 with no dimension below 3. `Proof / Evidence` cannot pass if any external derivative cites a non-`Proven` claim.

## 4. Release decision

Return `Release Ready` only when:

- the validator exits successfully;
- every message test passes;
- certification passes;
- the owner and approver sign off on the recorded version.

Otherwise return `Draft — blocked on <failed gate>` and name the next required action.
