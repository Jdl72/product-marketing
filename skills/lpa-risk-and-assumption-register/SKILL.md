---
name: lpa-risk-and-assumption-register
description: Create the Risk & Assumption Register as defined in the Lindberg launch workbook. Use when converting launch uncertainty into specific risk, assumption, and hypothesis IDs with severity, root cause, customer segment, and test plans.
---

# Risk & Assumption Register

Portable markdown module for workbook artifact `1.2 Risk & Assumption Register`.

## Purpose

Build the register in the workbook's logic, combining product discovery assumptions with FMEA-style risk thinking.

## Section order

1. `IDENTIFICATION`
2. `DESCRIPTION & CONTEXT`
3. `CONTROLS`
4. `RISK SCORING (FMEA)`
5. `MITIGATION & VALIDATION`
6. `REGISTER SUMMARY`

## Non-negotiables

- Convert vague concerns into explicit failure modes.
- Write root cause, not just symptom.
- Score `SEV`, `OCC`, and `DET` on a 1–10 scale.
- Re-score after mitigation to track whether risk actually reduced.
- Test high-priority items first in downstream evidence work.

## FMEA Scoring Formula

```
RPN = SEV × OCC × DET
```

Score each factor on a 1–10 scale. RPN auto-calculates.

- **SEV (Severity):** How bad is the impact if the failure occurs? 1 = negligible, 10 = catastrophic.
- **OCC (Occurrence):** How likely is the failure to occur? 1 = remote, 10 = almost certain.
- **DET (Detectability):** How detectable is the failure before it reaches the customer? 1 = certain to detect, 10 = undetectable.

## Priority Thresholds

| Priority | RPN Range | Required Action |
|---|---|---|
| CRITICAL | RPN ≥ 200 | Must mitigate before proceeding |
| HIGH | RPN 100–199 | Mitigate or accept with leadership sign-off |
| MEDIUM | RPN 40–99 | Monitor with test plan |
| LOW | RPN < 40 | Log and accept |

## Required Fields

### Identification
- `ID` — R (Risk), A (Assumption), or H (Hypothesis) prefix + number
- `Type` — Risk / Assumption / Hypothesis
- `Risk Category` — AI & Autonomy / Operational / Desirability & Value / Market & Competitive / other workbook category
- `Date Added`

### Description & Context
- `Statement / Failure Mode`
- `Potential Effect / Impact`
- `Root Cause / Underlying Reason`
- `Customer Segment`

### Controls
- `Current Controls / Monitors`
- `Test Method / Experiment` — how to test or probe this risk
- `Evidence Required` — what specific evidence would validate or falsify it

### Risk Scoring (FMEA)
- `Severity (SEV)` — 1–10
- `Occurrence (OCC)` — 1–10
- `Detectability (DET)` — 1–10
- `RPN` — SEV × OCC × DET (auto-calculated)
- `Priority` — CRITICAL / HIGH / MEDIUM / LOW (derived from RPN threshold)

### Ownership & Status
- `Owner`
- `Due Date`
- `Validation Status` — Open / Testing / Validated / Falsified / Mitigated / Accepted / Escalated
- `Notes`

### Post-Mitigation Scores
- `Post-Mitigation SEV`
- `Post-Mitigation OCC`
- `Post-Mitigation RPN` — Post-Mitigation SEV × Post-Mitigation OCC × DET

## Validation Status Vocabulary

| Status | Meaning |
|---|---|
| Open | Identified, not yet being tested |
| Testing | Active experiment or validation in progress |
| Validated | Assumption confirmed true |
| Falsified | Assumption confirmed false — update plan accordingly |
| Mitigated | Risk reduced through design or process change |
| Accepted | Risk acknowledged and accepted without mitigation |
| Escalated | Raised to leadership for sign-off or resolution |

## Post-Mitigation Re-Scoring Instruction

After mitigation, re-score `SEV` and `OCC` only. `DET` stays the same — it reflects the detection capability of the current system, not the mitigation action. `Post-Mitigation RPN` re-calculates as Post-Mitigation SEV × Post-Mitigation OCC × DET. Compare against original RPN to confirm the risk actually reduced.

## Instructions

1. Convert each issue into a specific failure mode or testable belief.
2. Assign an `R`, `A`, or `H` style identifier if one does not exist.
3. Use the workbook categories when possible: AI & Autonomy, Operational, Desirability / Value, Market / Competitive, and related launch categories.
4. Write the root cause, not just the symptom.
5. Separate `Test Method / Experiment` from `Evidence Required` — these are distinct fields.
6. Capture current controls honestly, including `none` when no monitor exists.
7. Set `Priority` from the RPN threshold table, not by judgment alone.
8. After mitigation, re-score SEV and OCC and update Post-Mitigation RPN.

## Output

Return:

- `Register Entries`
- `Top Priority Risks`
- `Hypotheses to Validate in Customer Interview`
- `Risks that must reach Stage Gate review`
- `Register Summary`
- `Next Required Artifact`

## Register Summary

Include a summary block at the end of every completed register. The summary contains:

**Counts by type:**
- Risk: [n]
- Assumption: [n]
- Hypothesis: [n]

**Counts by priority:**
- CRITICAL: [n]
- HIGH: [n]
- MEDIUM: [n]
- LOW: [n]

**Counts by status:**
- Open: [n]
- Testing: [n]
- Validated: [n]
- Falsified: [n]
- Mitigated: [n]
- Accepted: [n]
- Escalated: [n]

**Health metrics:**
- Avg RPN: [value]
- Max RPN: [value]
- Avg Post-Mitigation RPN: [value]
- Avg RPN Reduction: [value]

## Handoff

Feeds:

- `Customer Interview`
- `Weekly Discovery Log`
- `Stage Gate Architecture`
- `Competitive Intelligence Log`
