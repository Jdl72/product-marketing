---
name: lpa-stage-gate-architecture
description: Run the Stage Gate Architecture from the Lindberg launch workbook and guide. Use when making go/no-go stage decisions, enforcing readiness gates, and preventing anti-patterns across the five-stage Deploy/Launch Decoupling model.
---

# Stage Gate Architecture

Portable markdown module for workbook artifact `5.1 Stage Gate Architecture`.

## Purpose

Govern stage progression through the exact launch model from the guide.

## Foundational axiom

Deploy does not equal launch.

Deployment is a learning instrument.
Launch is a commercial event.

## Section order

1. `SECTION 1 — LAUNCH PROGRESS DASHBOARD`
2. `THREE READINESS TYPES`
3. `SECTION 2 — THE FIVE STAGES`
4. stage deliverables
5. gate criteria
6. anti-pattern flags

## Stage sequence

1. `Narrative Hypothesis + Eval Design`
2. `Low-Signal Deployment`
3. `Narrative Lock`
4. `Distribution Test`
5. `Lightning Strike`

## Gate logic

- `Learning Readiness` gates Stage 1.
- `Compliance/Security Readiness` is a hard-stop before Stage 2.
- `Narrative Readiness` gates Stage 3.

## Anti-patterns to actively guard against

- endless discovery loop
- compliance shortcut
- premature launch before narrative lock
- conflating low-signal deployment with invisibility
- skipping distribution testing before lightning strike

## Instructions

1. Review required artifacts for the current stage.
2. Identify missing deliverables and unresolved high-priority risks.
3. Call out anti-patterns explicitly.
4. Return a go / no-go recommendation with rationale.
5. Do not advance a stage because of stakeholder impatience.

## Output

- `Current Stage`
- `Required Artifacts Reviewed`
- `Gate Status`
- `Anti-Pattern Flags`
- `Go / No-Go Decision`
- `Next Required Artifact`
