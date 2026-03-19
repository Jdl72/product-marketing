---
name: lpa-eval-framework
description: Build the Eval Framework from the Lindberg launch workbook. Use when defining failure modes, EV-IDs, golden datasets, pass/fail logic, and marketing-safe proof translation for a launch.
---

# Eval Framework

Portable markdown module for workbook artifact `2.2 Eval Framework`.

## Purpose

Translate product behavior and launch claims into explicit evaluation logic before amplification.

## Method

Use the bottom-up evaluation methodology:

1. catalog failure modes from real traces
2. build golden datasets
3. design evaluators
4. validate human-model alignment
5. track eval results
6. translate results into marketing-safe proof points

## Section order

1. `SECTION 1: FAILURE MODE CATALOG — Bottom-Up Error Analysis`
2. `Golden datasets`
3. `Evaluator logic`
4. `Results tracking`
5. `Marketing translation`

## Non-negotiables

- Start from real traces, user reports, or internal tests.
- Open-code errors before clustering them.
- Prioritize 4-7 failure modes for automated evaluation.
- Separate evaluable truth from marketing aspiration.
- Only translate claims that the eval can actually support.

## Required sections

- `Failure Mode Catalog`
- `EV-IDs`
- `Golden Datasets`
- `Evaluator Logic`
- `Pass / Fail Thresholds`
- `Marketing Translation`

## Instructions

1. Start from failure modes observed in traces, user reports, or customer evidence.
2. Prioritize 4-7 failure modes for automation and launch relevance.
3. Define EV-IDs with clear measurement logic.
4. Mark which claims are safe to translate into market-facing proof.
5. Keep the distinction between evaluable proof and aspirational promise.
6. Prefer code-based evaluators where they are reliable and reserve model-judgment for cases that require it.

## Output

- `Prioritized Failure Modes`
- `EV-ID Table`
- `Golden Dataset Plan`
- `Pass / Fail Criteria`
- `Marketing-Safe Proof Claims`
- `Next Required Artifact`

## Handoff

Feeds:

- `Battle Cards`
- `ROI Calculator`
- `Impact Protocol`
- `PR-FAQ Template`
- `Certification Rubric`
