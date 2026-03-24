---
name: lpa-eval-framework
description: Build the Eval Framework from the Lindberg launch workbook. Use when defining failure modes, EV-IDs, golden datasets, pass/fail logic, and marketing-safe proof translation for a launch.
---

# Eval Framework

Portable markdown module for workbook artifact `2.2 Eval Framework`.

## Purpose

Translate product behavior and launch claims into explicit evaluation logic before amplification. Each section produces a living artifact that downstream tools — Battle Cards, ROI Calculator, Certification Rubric — can cite by ID.

## Method

Use the bottom-up evaluation methodology:

1. Catalog failure modes from real traces
2. Build golden datasets
3. Design evaluators with binary pass/fail criteria
4. Validate human-model alignment before trusting LLM judges
5. Track eval results against thresholds
6. Translate passing results into marketing-safe proof points

---

## Section 1 — FAILURE MODE CATALOG (Bottom-Up Error Analysis)

Start from observed behavior — traces, user reports, customer interviews, internal tests. Open-code individual errors before clustering. Prioritize 4–7 failure modes for automated evaluation and launch relevance.

### Fields per FM Entry

| Field | Description |
|---|---|
| `FM-ID` | Unique identifier, e.g., FM-01, FM-02 |
| `Failure Mode Name` | Short label for the error type |
| `Category` | Desirability / Usability / Feasibility / Safety |
| `Description` | What the failure looks like with a concrete example from a real trace |
| `Severity` | Critical / High / Medium / Low |
| `Frequency` | How often observed in trace analysis (count or %) |
| `Discovery Method` | trace review / user report / internal test / customer interview |
| `Example Trace` | Link or reference to the supporting trace |
| `Eval Type Recommendation` | code-based / LLM-judge / hybrid |

### Failure Mode Summary

| Metric | Count |
|---|---|
| Total Cataloged | |
| Prioritized for Eval | |
| Evals Built | |
| Coverage — Critical | |
| Coverage — High | |
| Coverage — Medium | |
| Coverage — Low | |

---

## Section 2 — GOLDEN DATASET REGISTRY

Minimum standard: **100 input-output pairs** per dataset before an evaluator is considered production-ready. Fewer than 100 pairs yields Moderate evidence at best (see Section 6 — Evidence Level Definitions).

### Fields per Dataset

| Field | Description |
|---|---|
| `Dataset ID` | Unique identifier, e.g., DS-01 |
| `Dataset Name` | Short descriptive name |
| `Linked FM-IDs` | Which failure modes this dataset covers |
| `Description / Scope` | What inputs and outputs are included and why |
| `Input-Output Pairs` | Target minimum: 100 pairs |
| `Coverage Flag` | Does it cover edge cases? Y / N |
| `Last Updated` | Date of last update |
| `Update Cadence` | How often it is refreshed |
| `Owner / DRI` | Person responsible for maintaining the dataset |
| `Location / Link` | Where the dataset lives |
| `Status` | draft / active / stale |

---

## Section 3 — EVALUATOR DESIGN AND RESULTS TRACKER

Each evaluator must have a binary success criterion — pass or fail on a specific, measurable condition. No Likert scales. If you cannot define a binary pass criterion, the failure mode is not yet well-specified enough to evaluate.

When EV-IDs are referenced in downstream artifacts (Battle Cards, ROI Calculator, Certification Rubric), they must cite the exact EV-ID from this section.

### Fields per Evaluator

| Field | Description |
|---|---|
| `Eval ID` | Unique identifier, e.g., EV-01 |
| `Eval Name` | Short descriptive name |
| `Linked FM-IDs` | Which failure modes this evaluator covers |
| `Eval Type` | code-based / LLM-judge / hybrid |
| `Binary Success Criterion` | The exact pass/fail condition — no Likert scales |
| `Threshold` | Minimum pass rate to consider the eval passing, e.g., 95% |
| `Golden Dataset ID` | Which dataset this evaluator runs against |
| `Human-Model Alignment %` | From Section 4 calibration — must be ≥90% for LLM judges |
| `Current Pass Rate` | Latest run result |
| `Pass / Fail vs. Threshold` | Pass / Fail |
| `Last Run Date` | Date of most recent run |
| `Trend` | improving / stable / degrading |

### Evaluator Health Dashboard

| Metric | Count |
|---|---|
| Total Evaluators | |
| Passing | |
| Failing | |
| Not Yet Run | |
| CI/CD Integrated | |
| Human-Aligned (≥90%) | |
| PMM-Ready | |

---

## Section 4 — HUMAN-MODEL ALIGNMENT TRACKER

Verify that LLM judges agree with human raters at ≥90% before trusting eval results in production. Do not use an LLM judge whose alignment is below 90% for marketing-facing claims.

### Fields per LLM Judge Calibration

| Field | Description |
|---|---|
| `Judge Model` | Model name and version |
| `Human Graders` | How many graders, their background |
| `Sample Size` | Number of examples graded by both human and model |
| `True Positives` | Cases where human and model both marked pass |
| `False Positives` | Cases where model marked pass but human marked fail |
| `True Negatives` | Cases where human and model both marked fail |
| `False Negatives` | Cases where model marked fail but human marked pass |
| `Precision` | TP / (TP + FP) |
| `Recall` | TP / (TP + FN) |
| `Alignment %` | Overall agreement rate — must be ≥90% before use in production |

**Rule:** Do not use an LLM judge whose alignment is below 90% for marketing-facing claims.

---

## Section 5 — PMM MARKETING TRANSLATION

Map each passing EV-ID to a marketing-safe claim. Only claims traceable to a passing EV-ID from Section 3 appear in this table. Aspirational claims that have not been evaluated go in the "Claims to Avoid" list below.

### Fields per Translation Row

| Field | Description |
|---|---|
| `EV-ID` | Must reference a passing eval from Section 3 |
| `Marketing Asset Type` | website copy / sales deck / press release / battle card / etc. |
| `Headline / Claim` | The exact claim that is safe to make |
| `Target Audience` | Who this claim is for |
| `Channel` | Where this claim appears |
| `Competitor Benchmark` | What this compares against, if applicable |
| `Win Rate vs. Competitor` | If benchmarked |
| `ROI Translation` | Dollar or time value equivalent |

**Rule:** Only claims with a passing EV-ID appear in this table.

### Claims to Avoid

List aspirational or unverified claims here. These claims may not appear in marketing materials until a passing EV-ID exists to support them.

| Claim | Reason Not Yet Approved | EV-ID Needed |
|---|---|---|
| | | |

---

## Section 6 — METHODOLOGY REFERENCE

### Eval Type Selection Guide

| Eval Type | When to Use | Pros | Cons | Cost | Speed | Deterministic |
|---|---|---|---|---|---|---|
| Code-based | Output has a definable correct answer | Fast, cheap, deterministic | Narrow, requires structured output | Low | Fast | Yes |
| LLM-judge | Output requires semantic judgment | Flexible | Non-deterministic, needs calibration | Medium | Medium | No |
| Hybrid | Structured pass/fail + semantic quality | Best coverage | Highest complexity | High | Slow | Partial |

Prefer code-based evaluators where they are reliable. Reserve LLM judges for cases that require semantic judgment and only after calibration in Section 4.

### Critical Rule Against Likert Scales

Likert scales (1–5 ratings) produce non-deterministic, non-auditable results that cannot be compared run-to-run. Use binary pass/fail criteria with specific measurable conditions instead. If you cannot define a binary pass criterion, the failure mode is not yet well-specified enough to evaluate.

### Evidence Level Definitions

| Level | Criteria |
|---|---|
| None | No evaluation data exists |
| Weak | 1 eval run, fewer than 50 examples |
| Moderate | 2+ runs, 50–99 examples, no human alignment check |
| Strong | 3+ runs, 100+ examples, human alignment ≥90% |

---

## Non-Negotiables

- Start from real traces, user reports, or internal tests.
- Open-code errors before clustering them.
- Prioritize 4–7 failure modes for automated evaluation.
- Separate evaluable truth from marketing aspiration at all times.
- Only translate claims that a passing eval can support.
- EV-ID citation is required in every downstream artifact (Battle Cards, ROI Calculator, Certification Rubric) that references an eval result.
- Prefer code-based evaluators where they are reliable.

## Handoff

Feeds:

- `Battle Cards`
- `ROI Calculator`
- `Impact Protocol`
- `PR-FAQ Template`
- `Certification Rubric`
