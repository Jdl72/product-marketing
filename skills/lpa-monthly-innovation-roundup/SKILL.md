---
name: lpa-monthly-innovation-roundup
description: Assemble the Monthly Innovation Roundup from the Lindberg launch workbook. Use when bundling a month's shipped releases — published Release Articles plus rolled-up Tier 3 work — into one recurring email/blog that demonstrates sustained innovation velocity.
---

# Monthly Innovation Roundup

Portable markdown module for workbook artifact `6.2 Monthly Innovation Roundup`.

## Purpose

Turn a month of shipped releases into one recurring proof point of velocity, so Tier 3 work earns marketing value in aggregate even though no single item deserved a standalone launch.

## Core rule

The roundup summarizes and groups; it does not originate new claims. Every Tier 1/2 item comes from an already-published `Release Article`. Every Tier 3 item is a one-line rollup, not a new narrative.

## Non-negotiables

- Pull Tier 1/2 items only from a published `Release Article`; do not draft new claims here.
- Roll up Tier 3 items by name and one-line customer benefit only, sourced from the `Content Calendar`.
- Group items under 1-2 themes; do not list chronologically.
- Exactly one roundup per month — do not split into multiple sends.
- If zero Tier 1/2 releases shipped that month, say so plainly and lead with the Tier 3 rollup rather than padding.

## Required sections

- `Month`
- `Theme(s)`
- `Featured Releases` (Tier 1/2)
- `Also Shipped` (Tier 3 rollup)
- `Customer Impact Callout`
- `What's Next Teaser`
- `Distribution Channels`
- `Next Required Artifact`

## Inputs

- `Release Article` (Tier 1/2, published within the target month)
- `Content Calendar` (all entries dated within the target month)
- `Positioning Canvas` (for theme framing)
- `Segment Playbooks` (if audience-specific cuts are needed)

## Instructions

1. Pull every `Content Calendar` entry dated within the target month.
2. Split entries into those with a linked, published `Release Article` (Tier 1/2) and those without (Tier 3).
3. Group the Tier 1/2 entries under 1-2 themes drawn from the `Positioning Canvas`; do not list them in ship-date order.
4. Summarize each Tier 3 entry in one line: name plus customer benefit — no new claims, no expansion into a narrative.
5. If no Tier 1/2 releases shipped this month, state that directly and lead with the Tier 3 rollup instead.
6. Log the roundup itself back into the `Content Calendar` as `asset_type: Monthly Roundup`.

## Output

Return:

- `Month`
- `Theme(s)`
- `Featured Releases`
- `Also Shipped`
- `Customer Impact Callout`
- `What's Next Teaser`
- `Distribution Channels`
- `Next Required Artifact`

## Handoff

Feeds:

- `Content Calendar` (log as `asset_type: Monthly Roundup`)
- `Quarterly Innovation Moment` (if later added) — stitches 3 months of roundups into one bigger analyst/market beat
