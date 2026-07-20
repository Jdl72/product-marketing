---
name: lpa-weekly-discovery-log
description: Maintain the Weekly Discovery Log from the Lindberg launch workbook. Use when consolidating interview learnings, evidence updates, positioning pivots, and validation rates into a weekly synthesis that feeds the narrative artifacts.
---

# Weekly Discovery Log

Portable markdown module for workbook artifact `2.3 Weekly Discovery Log`.

## Purpose

Create the weekly synthesis layer between raw evidence and narrative decisions.

## Inputs

- `Interview Snapshot` (§2F) and `Cross-Interview Pattern Synthesis` (§2H) from `Customer Interview`
- `Risk & Assumption Register`
- `Eval Framework` pass/fail results, when a run validated or falsified a hypothesis this week
- `Conversation Synthesis` (optional — if the discovery workflow produced one covering this week's period, fold its patterns into Section 3, cited by `convrec-ID`)

## Section order

1. `SECTION 1 — DISCOVERY DASHBOARD`
2. `SECTION 2 — WEEKLY DISCOVERY LOG`
3. `SECTION 3 — INSIGHT PATTERN TRACKER`
4. `SECTION 4 — POSITIONING PIVOT LOG`
5. `SECTION 5 — HOW TO USE THIS LOG`

## Non-negotiables

- This is stakeholder-facing synthesis, not a duplicate of item-level detail from the register.
- Capture the `so what`, not just the raw observation.
- Reference risk and assumption IDs rather than rewriting them.
- Use direct customer voice in the log.
- Record the resulting decision as `Proceed`, `Pivot`, `Kill`, or `Defer`.

## Instructions

1. Summarize the week's validated learnings.
2. Update which risks, assumptions, and hypotheses moved.
3. Record positioning pivots explicitly.
4. Log competitive signals surfaced during discovery.
5. Keep a running view of validation rate and confidence.
6. Cite source count when labeling evidence strength as strong, moderate, or weak.

---

## SECTION 1 — DISCOVERY DASHBOARD

| Field | Value |
|---|---|
| Total Weeks Logged | |
| Hypotheses Tested | |
| Validated | |
| Falsified | |
| Inconclusive | |
| Validation Rate | green if ≥60% / red if <40% |
| Pivots Triggered | |

**Validation Rate thresholds:**
- Green: ≥60%
- Yellow: 40–59%
- Red: <40% → triggers escalation to Stage Gate review

---

## SECTION 2 — WEEKLY DISCOVERY LOG

14-column structure. Add one row per week.

| Week # | Date Range | Sprint Theme | RAR IDs Tested | # Validated | # Falsified | # Inconclusive | Key Insight / Synthesis (the "so what") | Customer Voice (direct quote) | Evidence Strength | Strategic Implication | Decision | Confidence Shift | Next Week Priorities |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

**Evidence Strength definitions:**
- Strong: 3+ independent sources with consistent signal
- Moderate: 2 sources, or 3+ with mixed signal
- Weak: 1 source or single anecdote
- Anecdotal: unconfirmed, no second source yet

**Decision options:** Proceed / Pivot / Kill / Defer

---

## SECTION 3 — INSIGHT PATTERN TRACKER

Track recurring signals across interviews. Add a new row when a pattern appears for the second time.

| Pattern ID | Theme | First Seen (Week #) | Times Observed | Weeks Referenced | RAR IDs Linked | Supporting Quotes (top 3 verbatim) | Strength | Strategic Action Taken | Status |
|---|---|---|---|---|---|---|---|---|---|

**Pattern ID format:** PAT-01, PAT-02, PAT-03, etc.

**Theme naming rule:** Name themes in buyer language, not consultant language.

**Strength definitions:**
- Strong: 3+ independent sources with consistent signal
- Moderate: 2 sources
- Weak: 1 source
- Anecdotal: unconfirmed

**Saturation rule:** When a pattern appears in 3+ independent interviews with consistent signal, mark Strength as Strong and flag it for downstream action. Stop adding interviews for that specific pattern.

**Status options:** Active / Acted On / Contradicted

**Conversation Synthesis patterns:** When a `Conversation Synthesis` covers this week's period, add its `strongly_supported_patterns` and `emerging_patterns` as rows here, citing `convrec-ID`s in the Weeks Referenced / evidence columns alongside interview IDs. Do not merge a call-mined pattern with an interview-derived pattern in the same row unless both cite the same underlying signal — keep the two sourcing chains traceable.

---

## SECTION 4 — POSITIONING PIVOT LOG

Log pivots immediately when they occur. Do not batch.

| Pivot # | Date | Triggered By (Pattern ID) | Previous Position | New Position | Evidence Base (source count) | Customer Validation | Implemented In |
|---|---|---|---|---|---|---|---|

**Pivot # format:** PIV-01, PIV-02, PIV-03, etc.

**Customer Validation options:** Validated / Pending / Speculative

**Implemented In:** list which downstream artifacts were updated (e.g., Positioning Canvas, PR/FAQ, Battle Cards)

---

## SECTION 5 — HOW TO USE THIS LOG

**Update cadence:**
- Section 2: update weekly, within 48 hours of each interview or discovery session
- Section 3: update when a pattern appears for the second time
- Section 4: log pivots immediately when they occur — do not batch

**Stakeholder distribution:**
- Sections 1–2: leadership
- Section 3: product and engineering
- Section 4: marketing and sales

**Escalation rule:** If the validation rate drops below 40%, escalate to Stage Gate review with:
1. Current validation rate
2. List of consistently falsified hypotheses
3. Recommended path: Proceed / Pivot / Kill

**Eval Framework as evidence source:** Eval pass/fail results count as discovery evidence. When an eval run validates or falsifies a hypothesis, log it in Section 2 and update the relevant RAR IDs.

---

## Output

- `Insight Patterns`
- `Validated / Invalidated IDs`
- `Positioning Pivots`
- `Validation Rates`
- `Competitive Signals`
- `Next Required Artifact`

## Handoff

Feeds:

- `Risk & Assumption Register`
- `Positioning Canvas`
- `Stage Gate Architecture`
- `Competitive Intelligence Log`
