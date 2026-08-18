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
- Stop if required inputs are missing and name the missing prerequisite explicitly.

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

## Cross-cutting artifacts

Not a numbered tab — runs continuously alongside the phases above rather than at one point in the sequence.

- `Competitive Intelligence Log` — ongoing from Phase 2 (Evidence) through post-launch. Log signals as encountered; review before every competitive deal and on a fixed monthly cadence. Feeds `Positioning Canvas` (3.1), `Attack Matrix` (3.4), and `Battle Cards` (4.3) — update those tabs within one sprint of a staleness trigger, don't wait for the phase that owns them to come up in sequence.

## Instructions

1. Work left to right through the six phases.
2. Complete tabs in numbered order within each phase.
3. Before starting any tab, confirm its listed inputs exist.
4. After finishing any tab, record its outputs and route them to the downstream tabs that consume them.
5. Use this tab to stop work from jumping ahead of missing prerequisites.
6. When there is conflict between speed and sequence, favor sequence.

## Output

Return:

- `Current Phase`
- `Current Tab`
- `Confirmed Inputs`
- `Expected Outputs`
- `Downstream Tabs Fed`
- `Next Required Tab`
