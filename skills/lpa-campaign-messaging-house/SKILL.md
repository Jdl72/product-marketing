---
name: lpa-campaign-messaging-house
description: Build or revise a Campaign Messaging House that governs claims and derivatives across a multi-asset campaign. Use for campaign briefs, narrative spines, message pillars, claim ledgers, hooks, campaign copy guardrails, or campaign-level messaging spanning products or releases. Runs without the launch workbook by eliciting a portable Campaign Evidence Pack; returns Draft when evidence is incomplete and Release Ready only after proof and validation gates pass.
---

# Campaign Messaging House

Build the campaign-layer master messaging document. Keep every external asset traceable to an approved claim instead of allowing messaging to drift asset by asset.

## Core rule

Standalone means independent of repository artifacts, not independent of evidence. Never invent positioning, product facts, buyer criteria, alternatives, or proof.

## Resources

Read these files before drafting:

- `references/campaign-evidence-pack.md` — normalize repository artifacts or user-supplied evidence into one portable input.
- `references/dunford-setup-followthrough.md` — apply the eight-part narrative spine exactly.
- `assets/campaign-messaging-house-template.md` — use this output structure without renaming sections or fields.

Read `references/derivative-generators.md` only after the Release Ready proof gate passes. When repository quality-gate skills are unavailable, read `references/standalone-validation.md` before returning a Release Ready result.

## Operating modes

Choose one mode and record it in `SECTION 0`.

### Draft

Use when the campaign brief is complete but positioning, product facts, buyer evidence, or proof is missing or unverified.

- Complete Sections 0–3 to the extent the evidence permits. When Gate 2 is blocked, keep Sections 2–3 as explicit blocked shells and put the missing inputs in the Proof Gap Register; never fill them with invented hypotheses.
- Mark unverified claims `Provisional` and internal-only.
- Record missing evidence, owner, and due date in the Proof Gap Register.
- Omit Section 4 derivatives; do not write external-ready copy from unverified claims.
- Complete Section 5 governance even though Section 4 is withheld.
- Return `Artifact Status: Draft — blocked on <specific evidence>`.

### Release Ready

Use only when the Campaign Evidence Pack contains validated positioning, approved product facts, and at least one `Proven` claim per retained pillar.

- Complete Sections 0–5.
- Generate derivatives from `Proven` claims only.
- Run the deterministic validator.
- Run Bar Test and Certification using the repository campaign paths when available, or the bundled standalone protocol when they are not.
- Return `Artifact Status: Release Ready` only after every validation passes.

Never promote Draft to Release Ready merely because the user asks for finished copy.

## Section order

1. `SECTION 0 — CAMPAIGN HEADER & VERSION`
2. `SECTION 1 — GACCS BRIEF` (Gate 1)
3. `SECTION 2 — NARRATIVE SPINE` (eight Dunford components)
4. `SECTION 3 — MESSAGE PILLARS & CLAIM LEDGER` (Gates 2 and 3)
5. `SECTION 4 — DERIVATIVE STRUCTURES` (Release Ready only)
6. `SECTION 5 — GOVERNANCE & CHANGE LOG` (always complete)

## Required inputs

Elicit these when absent:

- Campaign name, theme, products in scope, and requested operating mode.
- Correct GACCS brief: `Goals`, `Audience`, `Channels`, `Creative`, and `Stakeholders`.
- Execution timeline: campaign dates and creative freeze date. Timeline is not the `S` in GACCS.
- Campaign Evidence Pack fields from `references/campaign-evidence-pack.md`.

Repository artifacts are optional sources for the Evidence Pack:

| Artifact | Evidence Pack fields |
|---|---|
| `Positioning Canvas` | positioning, alternatives, differentiated value, target market |
| `Eval Framework` | verified claim IDs, thresholds, product evidence |
| `Customer Interview` | buyer language, criteria, objections, customer evidence |
| `Attack Matrix` | alternatives, trade-offs, objections |
| `Segment Playbooks` | audience definitions and pillar relevance |
| `ROI Calculator` | verified financial proof and assumptions |

User-supplied source documents, interview notes, approved product specifications, case studies, and published metrics may populate the same fields. Record source and date for every fact.

## Gates

### Gate 1 — Brief complete

Block when any GACCS field is missing, the goal lacks a number and date, Audience names more than two ICPs, Creative merely restates a feature, Channels is empty, Stakeholders lacks an owner and approver, or execution dates are absent.

On failure, return Sections 0–1, named blockers, and Section 5 governance. Do not draft the narrative.

### Gate 2 — Narrative grounded

Require enough Evidence Pack content to state product facts, alternatives, buyer criteria, and differentiated value without invention. Record `Narrative Grounding Status: Pass` only when all four are supported. Otherwise record `Blocked: <missing evidence>`, keep the artifact in Draft mode, and leave unsupported narrative, pillar, and claim fields unfilled.

### Gate 3 — External-use proof

Require every retained pillar to have at least one `Proven` claim. Section 4 may cite only `Proven` claims. Failure keeps the artifact in Draft mode and produces a Proof Gap Register.

## Claim statuses

- `Proven` — named evidence source, source date, and verification recorded; allowed in external derivatives.
- `Provisional` — plausible but awaiting verification; internal use only; requires evidence owner and due date.
- `Unsupported` — no viable evidence, contradicted, or rejected; barred from external use and removed from derivatives.

Both `Provisional` and `Unsupported` are prohibited from Section 4.

## Instructions

1. Normalize all supplied material into the Campaign Evidence Pack. Preserve sources and dates.
2. Select Draft or Release Ready from evidence state, not desired output length.
3. Complete Gate 1 using the five GACCS fields plus the separate execution timeline.
4. If Gate 2 passes, build the Setup: `Insight`, `Alternatives`, and `Perfect World`. Keep the product out of all three. If it is blocked, preserve the section headings, record the blocker, and continue to governance without inventing content.
5. Build the Follow-Through: `Introduction`, `Differentiated Value`, `Proof`, `Objections`, and `Ask`.
6. Check one-to-one integrity between `Perfect World` criteria and differentiated value. Record honest product gaps instead of rigging the criteria.
7. Build 3–4 pillars from criteria that have differentiated value. Keep proofless pillars only in Draft mode with `Provisional` claims.
8. Build the claim ledger with at most three claims per pillar. Give every claim an ID, source, source date, verifier, status, approved phrasing, banned phrasing, evidence owner, and due date.
9. If Gate 3 passes, generate PAISA, Contrast Loop, and twelve hooks using `references/derivative-generators.md`; narrow hooks to three recommendations.
10. Complete Section 5 in every mode. Record owner, approvers, version, effective date, review date, and changes.
11. From this skill's directory, run `python3 scripts/validate_campaign_messaging_house.py <output.md>`. Resolve every error before claiming Release Ready.
12. Run campaign message testing and certification. In repository use, route through the campaign modes in `Bar Test` and `Certification Rubric`; otherwise use `references/standalone-validation.md`.

## Language constraints

- Use active voice and concrete verbs.
- Avoid hype vocabulary such as `game-changing`, `revolutionary`, `unlock`, `supercharge`, `next-level`, `seamless`, and `effortless`.
- Name competitors only in internal alternatives and ledger notes; use category labels in external derivatives.
- Treat time saved and speed multiples as supporting evidence, never the headline or pillar name.
- Do not add claims in derivatives. Every derivative line must cite a ledger ID.

## Required outputs

Always return:

- `Campaign Name`
- `Operating Mode`
- `Artifact Status`
- `GACCS Gate Status`
- `Narrative Spine` (eight components when Gate 2 passes, otherwise the named blocker)
- `Message Pillars`
- `Claim Ledger`
- `Proof Gap Register`
- `Unsupported Claims`
- `Cut Criteria`
- `Version, Owner & Approvers`
- `Validation Results`
- `Next Required Action`

Return `Derivative Structures` only in Release Ready mode.

## Handoff

When the launch-workbook skills are available, feed:

- `Bar Test` — campaign mode tests the three recommended hooks and approved pillar phrasing verbatim.
- `Certification Rubric` — campaign mode scores the validated house and claim ledger.
- `Segment Playbooks` — optional campaign-to-segment mapping.
- `Content Calendar` — every external asset records the claim IDs it cites.

For standalone use, complete the bundled validation protocol instead of pretending these repository skills ran.
