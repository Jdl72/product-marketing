---
name: lpa-workflow-map
description: Follow the Workflow Map tab from the Lindberg launch workbook. Use when you need the exact phase-by-phase and tab-by-tab sequence, including what each tab takes in, what it produces, and which tabs consume its outputs.
---

# Workflow Map

Portable markdown module for workbook artifact `Workflow Map`.

## Purpose

Use this tab to govern order of operations across the full launch process.

## How to read this map

- Numbers like `1.1` and `2.1` mean `phase.sequence`.
- `Inputs` means what must exist before starting the tab.
- `Outputs` means what the tab produces.
- `Feeds` means which downstream tabs consume those outputs.

## Non-negotiables

- Work left to right through the six phases.
- Complete tabs in numbered order within each phase.
- Do not skip ahead because a later narrative artifact feels more urgent.
- Stop if required inputs are missing and name the missing prerequisite explicitly. The two dependencies that run against tab order are the only exceptions, and both are resolved under Data fidelity rules rather than by skipping the input.
- Carry chain data exactly; a paraphrase is a new claim and needs its own source.
- When a finding changes an upstream tab, update that tab before continuing downstream.

## Phase sequence

### Phase 1: Frame

- `1.1 START HERE`
- `1.2 Risk & Assumption Register`
- `1.3 Launch Triage Matrix`

### Phase 2: Evidence

- `2.1 Customer Interview`
- `2.2 Eval Framework`
- `2.3 Weekly Discovery Log`

### Phase 3: Narrative

- `3.1 Positioning Canvas`
- `3.2 PR-FAQ Template`
- `3.3 Elevator Pitch`
- `3.4 Attack Matrix`

### Phase 4: Validate

- `4.1 Bar Test`
- `4.2 Segment Playbooks`
- `4.3 Battle Cards`
- `4.4 ROI Calculator`

### Phase 5: Launch

- `5.1 Stage Gate Architecture`
- `5.2 Impact Protocol`
- `5.3 Certification Rubric`

### Phase 6: Publish

- `6.1 Demo Script`
- `6.2 Release Article`
- `6.3 Monthly Innovation Roundup`

## Critical data chains

The phase sequence says what order to work in. It does not say what travels between tabs. These six chains do, and they are where fidelity is actually lost.

Each chain names what flows, the rule that governs it, and what breaks downstream when the rule is ignored. A cascade is silent by default: the receiving tab cannot tell that what it was handed is degraded.

### Chain 1 — Customer language

```
2.1 Customer Interview -> 3.1 Positioning Canvas -> 3.3 Elevator Pitch -> 4.1 Bar Test -> 5.3 Certification Rubric
```

Carries the customer's exact words.

Rule: verbatim, not summarized. `Customer Interview` marks any paraphrase `[paraphrased]`, and paraphrased quotes cannot be used in downstream positioning artifacts.

Cascade: paraphrase at 3.1 and the `Bar Test` validates language no customer ever used. The Bar Test cannot catch this — it scores whether a message is clear, not whether it came from a customer. `Certification Rubric` then certifies invented language as validated.

### Chain 2 — Proof and evidence

```
2.2 Eval Framework -> 4.3 Battle Cards -----------------> 5.3 Certification Rubric
2.2 Eval Framework -> 4.4 ROI Calculator -> 5.2 Impact Protocol -> 5.3 Certification Rubric
```

Carries EV-IDs, golden datasets, and pass/fail thresholds.

Rule: exact data. Move numbers as the `Eval Framework` produced them. Do not round, restate, or re-derive a metric downstream.

Cascade: `Certification Rubric` scores a Proof dimension. If a claim reaches it through a tab that restated the number, certification passes on a figure no eval supports.

Known break: `EV-ID` is defined in `Eval Framework` and referenced nowhere else. `Battle Cards` carries proof claims with no citation requirement — tracked in #41.

### Chain 3 — Competitive and alternatives

```
Competitive Intelligence Log (continuous) -> 3.4 Attack Matrix -> 4.2 Segment Playbooks -> 4.3 Battle Cards
```

Carries the status quo alternatives, their weaknesses, and competitor claims.

Rule: update on the staleness trigger, within one sprint. Do not wait for the phase that owns the downstream tab to come up in sequence.

Cascade: one stale alternative in the `Attack Matrix` reaches every segment playbook and every battle card built after it. Sales finds out before PMM does.

### Chain 4 — Risk, assumption, and hypothesis status

```
1.2 Risk & Assumption Register -> 2.1 Customer Interview -> 2.3 Weekly Discovery Log -> 1.2 Risk & Assumption Register -> 5.1 Stage Gate Architecture
```

Carries R/A/H IDs and their `Validation Status`.

This chain is a loop, and the return leg is the one that gets skipped. `Weekly Discovery Log` writes status back to the register; the register — not the log — is what `Stage Gate Architecture` reads.

Rule: update upstream first. Write the status change into the register before using the finding anywhere else.

Cascade: skip the return leg and Stage Gate reads `Open` for a hypothesis that discovery already falsified, then passes a gate on it.

### Chain 5 — Segment definitions

```
2.1 Customer Interview -> 3.1 Positioning Canvas -> 4.2 Segment Playbooks -> 4.3 Battle Cards / 4.4 ROI Calculator / 6.2 Release Article
```

Carries segment names, boundaries, and which buyer sits in each.

Rule: exact data. A segment keeps one name and one definition across every tab that references it.

Cascade: rename or re-cut a segment at 4.2 and the artifacts downstream address a different audience than the positioning was built for. Nothing errors; the messages just stop matching the buyer.

### Chain 6 — Narrative

```
1.1 START HERE -> 3.2 PR-FAQ Template -> 6.1 Demo Script -> 6.2 Release Article -> 6.3 Monthly Innovation Roundup
                          |
                          freezes at Narrative Lock (Stage Gate, Stage 3)
```

Carries the core claim: what this is, who it is for, why now.

Rule: the `PR-FAQ` updates weekly during discovery and freezes at `Narrative Lock`. After the lock, copy edits are allowed and strategic pivots are not — `Stage Gate Architecture` names post-lock scope creep as an anti-pattern.

Cascade: change the claim after the lock and the published `Release Article` no longer matches the narrative the gate approved. The `Monthly Innovation Roundup` then repeats the drifted claim, because it summarizes published articles rather than re-deriving them.

## Data fidelity rules

These apply across every chain above.

- **Exact data.** Move values as the producing tab wrote them. Rounding, restating, and re-deriving all count as new claims and need their own source.
- **Update upstream first.** When a downstream tab produces a finding that changes an upstream artifact, write the upstream change before continuing. The upstream tab stays the source of truth; the downstream tab is never the record.
- **Mark degraded input.** If an input is paraphrased, stale, or assumed, label it at the point of use rather than passing it on clean. An unlabeled input is treated as verified by every tab after it.
- **Two dependencies run against tab order.** These are the only two, they are shaped differently, and each resolves differently. Neither is a licence to start a tab whose inputs are missing.
  - `Bar Test` (4.1) requires `Segment Playbooks` (4.2). The dependency is one-directional — `Segment Playbooks` does not require `Bar Test` — so only the tab numbers are inverted relative to the data flow. Complete `Segment Playbooks` first and run `Bar Test` against it. This is the one place where numbered order yields to a declared input.
  - `ROI Calculator` (4.4) and `Impact Protocol` (5.2) each require the other. No ordering resolves that, so it resolves in two passes: build `ROI Calculator` from `Customer Interview` and `Eval Framework`, record the `Impact Protocol` input as pending under `Degraded Inputs Flagged`, then revise once `Impact Protocol` exists. Until that revision is done the `ROI Calculator` is provisional, and no downstream tab may cite its figures as final.
- **Launch Tier routes, it does not degrade.** `START HERE` (1.1) sets the tier and `Launch Triage Matrix` (1.3) confirms it. Tier 3 skips `Demo Script` and `Release Article` and rolls into the `Monthly Innovation Roundup`. A skipped tab is a routing decision, not a missing input — do not treat it as a blocked prerequisite.

## Cross-cutting artifacts

Not a numbered tab — runs continuously alongside the phases above rather than at one point in the sequence.

- `Competitive Intelligence Log` — ongoing from Phase 2 (Evidence) through post-launch. Log signals as encountered; review before every competitive deal and on a fixed monthly cadence. Feeds `Positioning Canvas` (3.1), `Attack Matrix` (3.4), and `Battle Cards` (4.3) — update those tabs within one sprint of a staleness trigger, don't wait for the phase that owns them to come up in sequence.
- `Campaign Messaging House` — campaign layer, not release layer. Runs on the campaign calendar in Draft or Release Ready mode. Normalizes workbook artifacts or user-supplied sources into a portable Campaign Evidence Pack, so standalone means no workbook dependency rather than no evidence requirement. Release Ready houses use the campaign paths in `Bar Test` (4.1) and `Certification Rubric` (5.3); Draft houses stop before external derivatives and return proof gaps.

## Instructions

1. Work left to right through the six phases.
2. Complete tabs in numbered order within each phase.
3. Before starting any tab, confirm its listed inputs exist.
4. After finishing any tab, record its outputs and route them to the downstream tabs that consume them.
5. Check which of the six critical data chains the tab sits on, and carry that chain's data under its stated rule.
6. If the tab produced a finding that changes an upstream artifact, update the upstream tab before moving on.
7. Use this tab to stop work from jumping ahead of missing prerequisites.
8. When there is conflict between speed and sequence, favor sequence.

## Output

Return:

- `Current Phase`
- `Current Tab`
- `Confirmed Inputs`
- `Expected Outputs`
- `Downstream Tabs Fed`
- `Chains Touched`
- `Upstream Updates Required`
- `Degraded Inputs Flagged`
- `Next Required Tab`
