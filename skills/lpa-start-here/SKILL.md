---
name: lpa-start-here
description: Complete the START HERE artifact exactly as defined in the Lindberg playbook. Use when beginning a release and you need the four problem-alignment questions, release identification, launch tier logic, and initial launch path before any downstream GTM work.
---

# START HERE

Portable markdown module for workbook artifact `1.1 START HERE`.

## Purpose

Complete the release identification and the four problem-alignment questions exactly enough to decide whether the release is ready for GTM planning.

## Section order

1. `SECTION 1: RELEASE IDENTIFICATION`
2. `SECTION 2: PROBLEM ALIGNMENT -- THE FOUR QUESTIONS`
3. `SECTION 3: LAUNCH TIER CALIBRATION`
4. `SECTION 4: LAUNCH PATH`

## Non-negotiables

- PM and PMM answer the four questions together.
- If you can only describe what the feature does but not what problem it solves, stop here.
- Use the customer's language, not feature language.
- Be precise about the customer segment and persona.
- Treat the status quo as the real competition, not just named competitors.

## Required sections

- `Release Name`
- `Release Date (Target)`
- `PM Owner`
- `PMM Owner`
- `Date Completed`
- `Q1: What customer problem does this solve?`
- `Q2: Who has this problem?`
- `Q3: What are they doing today instead?`
- `Q4: How does solving this change our competitive position?`

## Launch Tier Definitions

### Tier 1 — Redefines Competitive Position

A Tier 1 release shifts how the market perceives the product's category or core value. It requires the full five-stage GTM process.

**Stage sequence:**
1. Narrative Hypothesis
2. Low-Signal Deploy
3. Narrative Lock
4. Distribution Test
5. Lightning Strike GA

**Duration:** 6–10 weeks GTM effort.

### Tier 2 — Adds Meaningful Capability

A Tier 2 release adds meaningful capability within existing positioning. It does not redefine the category but does require deliberate market communication.

**Stage sequence:**
1. Problem Alignment
2. Positioning Check
3. Enablement Package
4. Ship + Announce

**Duration:** 2–3 weeks.

**Process mechanics:** GTM prep begins when engineering confirms the ship date — either QA sign-off or release branch cut. PM owns communicating that date to PMM before copy or CS briefing starts.

### Tier 3 — Makes Existing Capability Better

A Tier 3 release improves an existing capability without changing positioning or competitive stance. It requires minimal GTM overhead.

**Stage sequence:**
1. Problem Alignment
2. Slack Announcement
3. CS Heads-Up

**Duration:** 2–3 hours.

## Tier 3 Slack Announcement Template

```
[Feature Name] is live as of [date]

What: [one sentence — what changed]
Why: [one sentence — what customer problem this solves]
Who it affects: [which customers / segments]
How to use it: [brief instructions or link to help doc]
Known limitations: [anything CS should know]

Questions? Tag [PMM owner]
```

## Tier 3 Approval Protocol

- PM drafts the Slack announcement.
- PMM has a 30-minute review window.
- PMM silence = approval.
- Release notes serve as the CS heads-up if shared before ship — no separate Slack DM required.

## Disagreement Escalation Protocol

If PM and PMM disagree on tier, escalate to the leadership pair.

**Tiebreaker question:** "If we get the positioning wrong on this release, does it cost us a deal? If yes, it is at least Tier 2. If it could cost us our market position, it is Tier 1."

The leadership pair resolves the disagreement and records the rationale in the Launch Triage Matrix.

## Instructions

1. Answer Q1 in customer language, not feature language.
2. Answer Q2 with a precise segment and persona, not "all customers."
3. Answer Q3 with the real status quo alternatives, including manual workarounds.
4. Answer Q4 by calibrating launch tier and competitive impact.
5. If any answer is weak, say the release is not ready for GTM planning.
6. If multiple segments appear, name them separately rather than blending them.
7. Assign a launch tier based on the definitions above.
8. If tier is disputed, apply the escalation protocol before proceeding.

## Q1–Q4 Outputs-To Mapping

| Q | Feeds | Where it lands |
|---|---|---|
| Q1 (problem) | Risk & Assumption Register | Failure mode framing |
| Q2 (who) | Customer Interview | Screener criteria |
| Q3 (status quo) | Positioning Canvas | Competitive alternatives (Step 2) |
| Q1–Q4 | PR-FAQ Template | Problem Statement, Target Customer, FAQ Section |
| Release info + tier | Launch Triage Matrix | Release row |
| Tier | Stage Gate Architecture | Launch path |

## Output

Return:

- `Release Identification`
- `Four Question Responses`
- `Launch Tier Calibration`
- `Launch Path Recommendation`
- `Readiness Warning`
- `Next Required Artifact`

## Handoff

Feeds:

- `Risk & Assumption Register`
- `Customer Interview`
- `PR-FAQ Template`
- `Launch Triage Matrix`
- `Positioning Canvas`
