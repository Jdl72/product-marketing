# LPA Eval Framework Rubric

## Purpose

Evaluate whether a completed eval framework artifact is good enough for PMM use — meaning it can be cited in Battle Cards, ROI Calculators, and Certification Rubrics with confidence.

Use this rubric after every `lpa-eval-framework` run before promoting claims to market-facing assets.

## Dimensions

### 1. FM Coverage

Question:

Are the most critical failure modes cataloged with FM-IDs and sufficient detail?

High score:

- FM-IDs are assigned to all cataloged failure modes
- Critical and High severity failure modes are present
- Each entry includes a description with a concrete example
- Discovery method and example trace are populated

Low score:

- Failure modes are listed as labels only with no description or severity
- No FM-IDs assigned
- Critical failures are missing

### 2. Dataset Quality

Question:

Do golden datasets meet the 100-pair minimum and cover the failure modes they are linked to?

High score:

- Each active dataset has at least 100 input-output pairs
- Coverage Flag is Y for edge cases
- Dataset is linked to at least one FM-ID
- Status is active and Last Updated is recent

Low score:

- Datasets have fewer than 100 pairs
- No FM-IDs are linked
- Status is stale or draft with no plan to update

### 3. Evaluator Design

Question:

Are pass/fail criteria binary and measurable, with explicit thresholds?

High score:

- Binary Success Criterion is a specific, measurable condition
- Threshold is stated as a percentage
- No Likert scales present
- Each evaluator links to a Dataset ID

Low score:

- Criteria are vague or qualitative
- Thresholds are missing
- Likert-style ratings are used

### 4. Human Alignment

Question:

Are LLM judges calibrated at ≥90% agreement with human raters before use?

High score:

- All LLM judges have a Section 4 calibration record
- Alignment % is ≥90% for every judge used in production
- Confusion matrix fields (True Positives, False Positives, True Negatives, False Negatives, Precision, Recall) are populated

Low score:

- LLM judges are used without calibration records
- Alignment % is below 90%
- Confusion matrix fields are missing or empty

### 5. Marketing Translation

Question:

Are all claims in Section 5 traceable to a passing EV-ID from Section 3?

High score:

- Every row in the Marketing Translation table includes a valid EV-ID
- The cited EV-ID shows Pass vs. Threshold in Section 3
- Claims to Avoid list is populated with aspirational claims that have not yet been evaluated

Low score:

- Claims appear in Section 5 without an EV-ID
- EV-IDs cited do not match any entry in Section 3
- Claims to Avoid list is absent

### 6. Completeness

Question:

Does the framework cover all six required sections with populated fields?

High score:

- All six sections are present: Failure Mode Catalog, Golden Dataset Registry, Evaluator Design and Results Tracker, Human-Model Alignment Tracker, PMM Marketing Translation, Methodology Reference
- Summary and dashboard tables are populated
- No section is empty or placeholder-only

Low score:

- One or more sections are missing
- Summary tables are blank
- Sections contain headers only with no content

## Pass / Fail Rule

Pass if:

- All six sections are present and populated
- No claim in Section 5 lacks an EV-ID
- No LLM judge is used in production below 90% alignment
- At least one FM-ID, one Dataset ID, and one EV-ID exist with full fields

Fail if:

- Any claim in Section 5 lacks an EV-ID citation
- Any LLM judge is used below 90% alignment without a documented exception
- The Failure Mode Catalog has no FM-IDs
- Golden datasets have no target pair counts stated
- Binary Success Criterion is replaced with a Likert scale or vague quality descriptor
- Any Critical-severity failure mode has no linked evaluator

## Review Notes to Capture Every Time

- strongest section in the framework
- weakest section in the framework
- failure modes not yet covered by an evaluator
- datasets below the 100-pair minimum
- claims in aspirational use that need an eval before launch
- schema gap exposed
