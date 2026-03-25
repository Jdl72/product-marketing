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

- `Learning Readiness` gates Stage 2. Required before low-signal deployment: eval framework defined, learning agenda set, hypotheses documented in RAR.
- `Compliance/Security Readiness` is a hard-stop before Stage 2. Non-negotiable. Even 5% deployment = full regulatory exposure. Requires: threat model, data flow audit, regulatory pre-clearance.
- `Narrative Readiness` gates Stage 5 (Lightning Strike). Required: positioning locked, messaging validated, value prop clear.

---

## SECTION 2 — THE FIVE STAGES

### Stage 1 — Narrative Hypothesis + Eval Design

**Deliverables:**
- PR/FAQ co-authored by PM and PMM
- Eval framework with test datasets and success criteria
- Market hypothesis in XYZ format: "At least X% of Y will do Z"
- Customer segments and use cases identified
- Risk and Assumption Register initialized
- Positioning Canvas Steps 1–4 first draft

**Gate 1 criteria (Discovery Readiness) — all must pass:**
- PM and PMM aligned on narrative hypothesis (signed off)
- Exec buy-in and sponsor identified
- Eval criteria are measurable and falsifiable
- Target customer validated (≥3 early conversations)
- Compliance/Security pre-screen: no showstoppers

---

### Stage 2 — Low-Signal Deployment (5–10% of users)

**Deliverables:**
- Compliance/Security Readiness complete (HARD STOP — no exceptions)
- Feature deployed to limited user set (5–10%)
- Weekly learning reports (hypotheses validated/falsified)
- Eval metric dashboard live and monitored
- Positioning feedback from 5+ customer interviews
- Narrative Containment Plan: holding statements, social monitoring, designated spokesperson
- Organic narrative leakage assessed

**Stage 2 prohibition:** ZERO proactive commercial communication while in Stage 2. The feature is live but not amplified. No press releases, no social posts, no customer emails about the new feature.

**Gate 2 criteria (Hypothesis Validation) — all must pass:**
- Core hypotheses validated or clearly falsified with documented learning
- No major regressions in product metrics
- Positioning resonates with early users (evidence from 5+ interviews)
- Narrative leakage assessed — no surprises
- Compliance/Security: no incidents or near-misses

---

### Stage 3 — Narrative Lock (30–50% deployment)

**Deliverables:**
- Locked Narrative doc (positioning, messaging, target customer — FINAL, no more changes)
- Sales enablement deck and talking points
- Support FAQ and handling guides
- Launch communication draft
- Deployment expanded to 30–50%
- Pricing approved and implemented

**Gate 3 criteria (Narrative Lock) — all must pass:**
- Narrative is locked and signed (no more positioning changes)
- Sales enablement complete and team trained
- Support prepared with FAQ and handling guides

---

### Stage 4 — Distribution Test

**Deliverables:**
- Channel tests complete
- Messaging A/B results reviewed
- Competitive monitoring current

**Gate 4 criteria (Distribution Ready) — all must pass:**
- Channel tests complete with results documented
- A/B results reviewed and winning message selected

---

### Stage 5 — Lightning Strike GA

**Deliverables:**
- Certification Rubric passed
- All assets live
- All channels coordinated

**Gate 5 criteria (Launch Complete) — all must pass:**
- Certification Rubric average ≥3.0 with zero dimensions below 3
- All launch assets live
- Monitoring in place

---

## Anti-patterns to actively guard against

**Endless Discovery Loop:** Team runs hypothesis after hypothesis without committing. Fix: set decision rules BEFORE discovery begins. Default thresholds: ≥30% validation = proceed, <15% = kill, 15–30% = iterate once more.

**Compliance Shortcut:** Deploying "just to a few users" without threat model or data audit. Fix: Compliance/Security gates Stage 2, not Stage 3. No exceptions.

**Premature Launch Before Narrative Lock:** Advancing to Stage 5 before Stage 3 gate is passed. Fix: Gate 3 must have written sign-off.

**Stakeholder Impatience:** Advancing a stage because leadership wants to ship, not because gate criteria are met. Fix: gate criteria are binary pass/fail, not subject to negotiation.

**Scope Creep After Narrative Lock:** Changing positioning, messaging, or target customer after Stage 3. Fix: Stage 3 freeze means no major narrative changes. Small copy fixes allowed; strategic pivots are not.

**Conflating low-signal deployment with invisibility:** Stage 2 means limited users, not zero visibility. Narrative leakage can still happen. Assess it.

**Skipping distribution testing before lightning strike:** Channel assumptions that are untested at Stage 4 become launch failures at Stage 5.

---

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
