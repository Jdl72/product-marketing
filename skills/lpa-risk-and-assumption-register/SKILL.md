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

## Non-negotiables

- Convert vague concerns into explicit failure modes.
- Write root cause, not just symptom.
- Score `SEV`, `OCC`, and `DET` on a 1-10 scale.
- Re-score after mitigation to track whether risk actually reduced.
- Test high-priority items first in downstream evidence work.

## Required fields

- `ID`
- `Type`
- `Risk Category`
- `Statement / Failure Mode`
- `Potential Effect / Impact`
- `Root Cause / Underlying Reason`
- `Customer Segment`
- `Current Controls / Monitors`
- `Severity`
- `Occurrence`
- `Detectability`
- `Priority`
- `Test Plan`

## Instructions

1. Convert each issue into a specific failure mode or testable belief.
2. Assign an `R`, `A`, or `H` style identifier if one does not exist.
3. Use the workbook categories when possible: AI & Autonomy, Operational, Desirability / Value, Market / Competitive, and related launch categories.
4. Write the root cause, not just the symptom.
5. Define the test or mitigation path clearly enough for downstream evidence work.
6. Capture current controls honestly, including `none` when no monitor exists.

## Output

Return:

- `Register Entries`
- `Top Priority Risks`
- `Hypotheses to Validate in Customer Interview`
- `Risks that must reach Stage Gate review`
- `Next Required Artifact`

## Handoff

Feeds:

- `Customer Interview`
- `Weekly Discovery Log`
- `Stage Gate Architecture`
- `Competitive Intelligence Log`
