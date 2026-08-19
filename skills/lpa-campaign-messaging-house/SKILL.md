---
name: lpa-campaign-messaging-house
description: Build the Campaign Messaging House — the master messaging document that governs a multi-asset campaign. Use when a campaign theme (not a single product launch) needs a GACCS brief, an April Dunford Setup & Follow-Through narrative spine, message pillars with claim IDs and proof status, and derivative asset structures for copy, video, and headlines. Runs standalone; uses launch workbook artifacts when they exist.
---

# Campaign Messaging House

Portable markdown module for the campaign-layer artifact `Campaign Messaging House`.

This artifact sits **above** the launch workbook. The workbook governs one release against one competitive set. This governs one campaign theme across many assets, channels, and releases.

## Purpose

Produce the single master messaging document that every campaign asset must trace back to, so creative work stays aligned to one argument and messaging cannot drift asset by asset.

## Core rule

The house is a guardrail, not a story. If the output cannot be used to reject a piece of collateral, it is not finished.

A narrative alone does not do that. The guardrail is `SECTION 3 — MESSAGE PILLARS & CLAIM LEDGER`: every asset cites the claim ID it is serving, and any claim marked `Unsupported` is barred from external use.

## Freedom level

Low. Follow the section order exactly. Use the field names exactly as written — downstream assets cite them. Do not add, rename, merge, or reorder sections. Do not substitute a different narrative framework for Dunford.

## Section order

1. `SECTION 0 — CAMPAIGN HEADER & VERSION`
2. `SECTION 1 — GACCS BRIEF` (gate)
3. `SECTION 2 — NARRATIVE SPINE` (Dunford Setup & Follow-Through, 7 steps)
4. `SECTION 3 — MESSAGE PILLARS & CLAIM LEDGER` (guardrail)
5. `SECTION 4 — DERIVATIVE STRUCTURES` (PAISA, Contrast Loop, Hooks)
6. `SECTION 5 — GOVERNANCE & CHANGE LOG`

Complete each section in order. Do not draft Section 2 before Section 1 passes its gate. Do not draft Section 4 before Section 3 has at least one `Proven` claim per pillar.

## Non-negotiables

- Stop at the `SECTION 1` gate if any GACCS field is missing or unquantified. Name the missing field. Do not proceed on assumptions.
- Use the Dunford Setup & Follow-Through spine. Do not substitute Raskin, StoryBrand, or a hybrid.
- The Setup (steps 1-3) is about the market, not the product. The product does not appear until step 4.
- `Insight` is the reverse of your differentiated value. Derive it from the value, not the other way around.
- `Alternatives` must include the status quo — manual work, spreadsheets, hiring, doing nothing.
- `Perfect World` criteria are agreed before the product appears. Every criterion must be one a buyer would state without prompting.
- Produce 3-4 pillars. Not 2, not 6. A campaign with 6 pillars has no argument.
- Every pillar traces to a `Perfect World` criterion. A pillar that does not is a feature list entry — cut it.
- Every claim carries an ID, a named proof source, and a proof status. No exceptions.
- Claims marked `Unsupported` are barred from external collateral. Record them; do not use them.
- Derivative structures (Section 4) inherit their content from Sections 2 and 3. They do not introduce new claims.
- Every claim ID must appear in at least one derivative, or it is dead weight — cut the claim or cut the pillar.

## Language constraints

These bind every line of drafted copy in this artifact.

- No adverbs. If a verb needs one, pick a stronger verb.
- No hype vocabulary: `game-changing`, `revolutionary`, `unlock`, `supercharge`, `next-level`, `seamless`, `effortless`.
- No throat-clearing: `It is important to note`, `In today's landscape`, `As you know`.
- Active voice. The doer is the grammatical subject.
- **Competitor naming**: name real competitors by name inside `SECTION 2 STEP 2` and the claim ledger's internal notes. Use generic category labels in anything customer-facing that Section 4 produces.
- **Do not lead on efficiency multipliers.** Time saved and speed multiples are supporting evidence, never the headline claim or the pillar name. Lead on the capability that becomes possible.

## Inputs

This skill runs standalone. Repo artifacts are optional accelerants.

**Required — elicit from the user if not supplied:**

- Campaign name and theme
- Business goal with a number attached
- Target ICP or persona
- Channel list and campaign dates

**Optional — use when present, do not block when absent:**

| Artifact | Feeds | If absent |
|---|---|---|
| `Positioning Canvas` | Steps 1, 2, 4, 5 | Elicit differentiated value and alternatives from the user; mark the spine `Unvalidated Positioning` |
| `Eval Framework` | Claim ledger proof IDs | Use `Customer Interview` quotes or published metrics; mark unproven claims `Provisional` |
| `Customer Interview` | Steps 1, 3; pillar language | Draft `Perfect World` from the user's stated buyer criteria; mark the pillar `Speculative` |
| `Attack Matrix` | Step 2; step 7 objections | Elicit the top three alternatives and one objection each |
| `Segment Playbooks` | Pillar-to-audience mapping | Map pillars to the single ICP named in GACCS |
| `ROI Calculator` | Step 6 proof | Use customer-reported outcomes; do not model numbers here |

When an optional input is absent, say so in the output under `Unresolved Claims` rather than filling the gap with invention.

## Instructions

1. **Gate on GACCS.** Complete `SECTION 1` using the five fields in `references/campaign-messaging-house-template.md`. Stop and name the gap if: `Goals` has no number, `Audience` names more than two ICPs, `Creative` restates a product feature instead of an angle, `Channels` is empty, or `Submission` has no dates. Do not proceed past a failed gate.
2. **Load positioning.** If a `Positioning Canvas` exists for the products in scope, read it before drafting. Pull differentiated value from its Step 4 and alternatives from its Step 2. Do not re-derive what it already settles.
3. **Draft the Setup (steps 1-3).** Follow `references/dunford-setup-followthrough.md` exactly. Write `Insight` last within the Setup even though it appears first — derive it by inverting the differentiated value, then check it reads as a market truth a buyer would accept before hearing about any product.
4. **Draft the Follow-Through (steps 4-7).** Introduce the product inside a named market category. Map each `Differentiated Value` entry to the `Perfect World` criterion it satisfies. Attach proof to each. End with objections and one ask.
5. **Check spine integrity.** Every `Perfect World` criterion must be answered in step 5, and every step 5 entry must answer a criterion. Unmatched items on either side mean the Setup and the Follow-Through disagree — fix the Setup, not the product claims.
6. **Build the pillars.** Convert `Perfect World` criteria into 3-4 pillars. A criterion qualifies as a pillar only when it has both differentiated value (step 5) and proof (step 6). Criteria with value but no proof become pillars with `Provisional` claims. Criteria with neither are cut and recorded under `Cut Criteria`.
7. **Build the claim ledger.** Give each pillar an ID (`P1`-`P4`) and at most 3 claims (`CLM-P1.1`). Each claim gets: claim text, proof source, proof status (`Proven` / `Provisional` / `Unsupported`), and approved phrasing. Add banned phrasings where a claim has a known overreach.
8. **Generate derivatives.** Produce one PAISA sequence, one Contrast Loop beat sheet, and 12 hook candidates using `references/derivative-generators.md`. Each derivative line cites the claim IDs it uses. Narrow the 12 hooks to 3 recommended.
9. **Verify coverage.** List any claim ID that appears in no derivative and any derivative line citing no claim. Both are defects. Resolve before returning.
10. **Set governance.** Fill `SECTION 5`: owner, version, effective date, review date, and the change-log rule. Version starts at `v1.0`.

## Required outputs

Return the completed template with every section filled, plus:

- `Campaign Name`
- `GACCS Gate Status` (`Pass` / `Blocked: <field>`)
- `Narrative Spine` (7 Dunford steps)
- `Message Pillars` (3-4, with IDs)
- `Claim Ledger` (all claims with IDs, proof source, proof status)
- `Derivative Structures` (PAISA, Contrast Loop, 3 recommended hooks)
- `Unsupported Claims` (barred from external use)
- `Unresolved Claims` (missing input, named)
- `Cut Criteria`
- `Version & Owner`
- `Next Required Artifact`

## Tips and tricks

- Write the Setup for someone who will never buy anything. If it only makes sense to a buyer who already wants the product, the Insight is a sales line, not an insight.
- The `Perfect World` step is where campaigns are won. Buyers who agree to your criteria have already scored the competition against you.
- If two pillars need the same proof point, they are one pillar.
- Pillar names should survive a year. Claim text will not — that is what the version log is for.
- When a stakeholder asks to add a message, ask which pillar it serves. If none, the answer is no, and the doc has done its job.

## Handoff

Feeds:

- `Bar Test` (test the 3 recommended hooks and each pillar's approved phrasing verbatim)
- `Certification Rubric` (score the house before any asset ships; `Proof / Evidence` scores against the claim ledger)
- `Segment Playbooks` (pillar-to-segment mapping when a campaign runs across more than one ICP)
- `Content Calendar` (every asset logs the claim IDs it cites)

Standalone use: skip the handoff and run step 9 coverage plus a manual read of `SECTION 3` before releasing the doc to creative.
