---
name: lpa-release-article
description: Draft the external Release Article from the Lindberg launch workbook. Use when a release has cleared Certification and needs the customer-facing blog/article that converts the PR-FAQ narrative into a publishable, proof-grounded piece.
---

# Release Article

Portable markdown module for workbook artifact `6.1 Release Article`.

## Purpose

Convert a certified narrative into the external article that proves innovation and educates the market on the customer outcome — not the feature.

## Core rule

Market the customer outcome, not the feature. If the draft can be summarized as "we shipped X," it is not ready.

## Non-negotiables

- Do not draft until `Certification Rubric` status is `Certified` (average >= 3.0, no dimension below 3).
- Tier 3 releases do not get a standalone article — route them to the monthly roundup instead.
- Open with the customer problem or outcome, never the internal feature name.
- Every claim traces to a source artifact; no claim stands on its own.
- Do not publish any claim the `PR-FAQ` flagged as outrunning proof or current product reality.
- Match effort to `Launch Tier`: Tier 1 gets a pillar piece, Tier 2 gets a standard post.

## Required sections

- `Release Name`
- `Launch Tier`
- `Headline`
- `Subhead`
- `Customer Problem / Hook`
- `What Shipped`
- `Why It Matters`
- `Proof / Evidence`
- `How It Works`
- `Availability & CTA`
- `Next Required Artifact`

## Inputs

- `PR-FAQ Template`
- `Positioning Canvas`
- `Certification Rubric` (status must be `Certified`)
- `Battle Cards`
- `Customer Interview`
- `Segment Playbooks`

## Instructions

1. Confirm `Certification Rubric` status is `Certified` before drafting anything. If not certified, stop and name the blocking dimension.
2. If `Launch Tier` is `Tier 3`, stop and route to the monthly roundup instead of drafting a standalone article.
3. Pull the headline and subhead from the `PR-FAQ`; do not invent new ones at this stage.
4. Open with the customer problem or outcome from `START HERE` and the `PR-FAQ`, never the internal feature name.
5. Attach one proof point to every claim, citing the source artifact (`Customer Interview`, `Eval Framework`, `Impact Protocol`).
6. Check `Segment Playbooks` for more than one relevant audience; if found, note which segment-specific variants are needed rather than writing them inline.
7. Flag any claim that cannot be traced to an upstream artifact as unresolved — do not publish it.

## Output

Return:

- `Release Name`
- `Launch Tier`
- `Draft Article` (all required sections)
- `Proof Point Citations`
- `Segment Variants Needed`
- `Unresolved Claims`
- `Next Required Artifact`

## Handoff

Feeds:

- `Content Calendar` (log as `asset_type: Release Article`)
- `Segment Playbooks` (for audience-tailored variants)
- `Monthly Innovation Roundup` (rolls up after publish)
