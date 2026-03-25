---
name: lpa-customer-interview
description: Run the Customer Interview artifact from the Lindberg launch workbook. Use when gathering primary evidence, validating pain, capturing customer language, and scoring evidence against the risks and hypotheses defined upstream.
---

# Customer Interview

Portable markdown module for workbook artifact `2.1 Customer Interview`.

## Purpose

Gather primary evidence that validates pain, alternatives, trust requirements, and customer language. Every interview produces a §2F snapshot that feeds downstream artifacts directly.

## Inputs

- `START HERE`
- `Risk & Assumption Register`

## Four Core Principles

1. **Two-person team** — driver (asks questions) + note-taker (captures verbatim). Never run solo. Solo interviews produce degraded notes because the driver cannot listen and write simultaneously.
2. **80/20 rule** — the customer talks 80% of the time. If you are talking more, stop and ask an open question.
3. **Past over future** — ask about what they have done, not what they would do. Future-oriented answers are aspirational; past behavior is evidence.
4. **Behavior over opinion** — "walk me through the last time you did X" beats "how do you feel about X." Behavior is specific; opinion is cheap.

## Six Interview Phases

### Phase 1 — Prepare

- Read `START HERE` and `Risk & Assumption Register` before opening a scheduling link.
- Complete §2C Research Brief for the participant.
- Write §2D Learning Goals (3 goals tied to specific RAR hypotheses).
- Confirm the participant passes §2A screener criteria.

### Phase 2 — Open

- Introduce yourself and the note-taker.
- Set context: explain the purpose of the session (learning, not selling).
- State explicitly that there are no right or wrong answers.
- Get consent to record if applicable.

### Phase 3 — Core Questions

- Work through the structured question guide in §2E.
- Note-taker captures verbatim quotes in the dedicated quotes column.
- Driver stays on the question arc; do not improvise new topics mid-phase.

### Phase 4 — Probe Deeper

- Follow up on specific signals that emerged in Phase 3.
- Use "tell me more," "what happened next," and "how did that affect you" to go deeper.
- Do not introduce new topic areas here — deepen what surfaced.

### Phase 5 — Close

- Ask final open questions: "Is there anything I didn't ask that you think I should know?"
- Confirm any follow-up actions promised during the call.
- Thank the participant and set expectations for next contact.

### Phase 6 — Synthesize

- Complete §2F Snapshot within 24 hours. Signal degrades after that.
- Update §2G Interview Tracker with this interview's row.
- If saturation threshold is reached (3+ consistent signals across segments), contribute to §2H Cross-Interview Pattern Synthesis.

---

## §2A — SCREENER

Run before scheduling. A participant who fails the screener wastes the team's time and produces misleading evidence.

Qualification criteria:

- Confirm the participant fits the target segment and persona defined in `START HERE`.
- Confirm they have direct experience with the problem domain — not adjacent or secondhand exposure.
- Confirm they are an active practitioner, not a former or aspirational user.
- Confirm they have not been interviewed in the last 90 days (check CRM; see CRM Guidance below).
- Document screener pass status in §2B.

---

## §2B — INTERVIEW METADATA

Capture before the call starts. Required for every interview.

| Field | Value |
|---|---|
| record_id | |
| Date | |
| Participant Name | |
| Segment / Persona | |
| Format | video / phone / in-person |
| Duration (minutes) | |
| Recruiting Channel | |
| Screener Pass Status | pass / fail / conditional |

---

## §2C — PRE-INTERVIEW RESEARCH BRIEF

Complete before the call. Do not open the interview without it.

- **Background Summary** — who is this person and what do they do?
- **Company Context** — size, industry, stage, relevant business model details.
- **Prior Product Interactions** — have they used the product, attended a demo, participated in a beta? Note dates.
- **Hypothesis-About-Pain Pre-Write** — before the interview, write your best current guess about what pain this person experiences and why. This forces you to surface assumptions you will test rather than confirm.

---

## §2D — LEARNING GOALS

Write 3 explicit goals before the interview starts. Each goal must map to a specific hypothesis ID in the Risk & Assumption Register.

| # | Learning Goal | RAR Hypothesis ID |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

If you cannot tie a learning goal to a RAR hypothesis, the interview is not yet justified. Add the hypothesis first.

---

## §2E — INTERVIEW NOTES

Use a two-column format: questions/observations on the left, verbatim quotes on the right.

### Phase structure for notes

| Phase | Question / Observation | Verbatim Quote (exact wording) |
|---|---|---|
| Open | | |
| Core Questions | | |
| Core Questions | | |
| Core Questions | | |
| Probe Deeper | | |
| Probe Deeper | | |
| Close | | |

Verbatim means verbatim. If you paraphrase, mark it explicitly as `[paraphrased]`. Paraphrased quotes cannot be used in downstream positioning artifacts.

---

## §2F — INTERVIEW SNAPSHOT

Complete within 24 hours of the interview. This is the primary output that feeds downstream artifacts.

**Memorable Quote**

> (exact words, attributed to participant)

**3 Key Insights**

1.
2.
3.

**2 Identified Opportunities**

1.
2.

**Hypothesis Impact**

| Field | Value |
|---|---|
| Hypothesis Tested | (RAR hypothesis ID and text) |
| Cumulative Evidence Rating | Validated / Partially Validated / Inconclusive / Falsified |
| Confidence Shift | Increased / Decreased / No change |
| Evidence Summary | (2–4 sentences: what was heard, what it means for the hypothesis) |

**Follow-Up Actions**

| Promise Made | Next Action | Owner | Due Date |
|---|---|---|---|
| | | | |

---

## §2G — INTERVIEW TRACKER

Running log. Add one row per completed interview.

| Date | Participant | Segment | Top Insight | Hypothesis ID | Evidence Rating | Snapshot Done (Y/N) |
|---|---|---|---|---|---|---|
| | | | | | | |

Review this tracker before scheduling new interviews. If evidence rating on a hypothesis has reached Validated, stop scheduling interviews for that hypothesis.

---

## §2H — CROSS-INTERVIEW PATTERN SYNTHESIS

Complete when saturation is reached for a segment (3+ consistent signals). One synthesis document per segment.

**Segment Summary**

- Segment name:
- Number of interviews completed:
- Date range:

**Saturation Reached** — Y / N

**Recurring Pain Patterns**

| Pattern | Frequency | Interview IDs | Representative Quote | Severity (H/M/L) |
|---|---|---|---|---|
| | | | | |

**Hypothesis Scorecard**

| Hypothesis ID | Hypothesis Text | Evidence Rating | Interview IDs | Notes |
|---|---|---|---|---|
| | | | | |

---

## Evidence Calibration Rubric

Apply this rubric to every Cumulative Evidence Rating in §2F and §2H.

| Level | Definition |
|---|---|
| **Validated** | 3+ independent sources, consistent signal, no contradictions |
| **Partially Validated** | 2 sources, or 3+ sources with contradictions present |
| **Inconclusive** | 1 source, or contradictory evidence that cannot be resolved |
| **Falsified** | Evidence directly contradicts the hypothesis |

Decision triggers:

- Reach Validated → use the evidence in downstream artifacts, flag hypothesis as confirmed in RAR.
- Reach Falsified → update RAR immediately, brief the team, revise affected downstream artifacts.
- Remain Inconclusive after 4+ interviews → the hypothesis is poorly formed. Rewrite it before scheduling more interviews.

---

## Common Mistakes

1. **Pitching during the interview** — share nothing about the product unless the participant asks directly. Pitching contaminates the evidence.
2. **Leading questions** — "don't you find X frustrating?" implies the answer. Ask "how do you handle X?" instead.
3. **Accepting vague generalizations** — "I always struggle with reporting" tells you nothing. Push for a specific recent example: "Tell me about the last time that happened."
4. **Interviewing the wrong people** — check screener criteria strictly. One bad participant poisons the pattern synthesis.
5. **Recording without synthesizing** — complete §2F within 24 hours or signal degrades. A stack of unprocessed recordings is not evidence.
6. **Over-interviewing** — stop scheduling interviews when patterns saturate (3+ consistent signals for a segment). More interviews do not increase confidence after saturation; they waste participant time and delay downstream work.
7. **Treating one anecdote as validation** — one interview is a hypothesis, not evidence. Update the RAR only after reaching Partially Validated or stronger.

---

## CRM Guidance

Before scheduling any participant:

- Check whether the contact was interviewed in the last 90 days.
- If yes, do not schedule. Reach back in the next cycle.
- Add an **Interview Participant** field in CRM to track interview history and last contact date.

This rule protects participants from over-solicitation and keeps the evidence pool from being dominated by the most available contacts rather than the most representative ones.

---

## Non-negotiables

- This tab is the primary evidence engine for the playbook.
- Read upstream tabs before interviewing.
- High-priority risks and hypotheses should be tested first.
- Use exact customer wording in downstream artifacts.
- If a segment has not been interviewed, call any downstream segment narrative speculative.
- Never run an interview without completing §2C and §2D first.
- Never mark a snapshot complete if §2F fields are missing.

---

## Output

- `Interview Snapshot` (§2F)
- `Validated Pain Patterns` (§2H)
- `Customer Language`
- `Evidence Scores`
- `Alternatives and Workarounds`
- `Hypotheses Confirmed / Weakened`
- `Next Required Artifact`

---

## Handoff

Feeds:

- `Weekly Discovery Log`
- `Positioning Canvas`
- `PR-FAQ Template`
- `Segment Playbooks`
- `Attack Matrix`
- `ROI Calculator`
- `Elevator Pitch`
- `Battle Cards`
- `Bar Test`
- `Impact Protocol`
- `Stage Gate Architecture`
- `Certification Rubric`
