# Job Spec: Synthesize Conversation Set

## Core job

When I have multiple parsed customer conversations, help me synthesize them into PMM evidence. Today that evidence directly produces a gated `positioning-brief` for the PMM asset workflow; personas, GTM, and sales enablement are roadmap consumers with no implementing skill yet (see Downstream linkage below).

## Trigger

Run this job when:

- at least several conversation records exist
- you need segment-level insights
- you need recurring patterns rather than single anecdotes

## Inputs

- multiple `conversation-record` artifacts
- optional segment filter
- optional time window
- optional PMM objective

## Desired outputs

- `conversation-synthesis`
- recurring pain patterns
- desired outcomes
- objections and buying triggers
- alternatives and competitive references
- language to use / avoid
- evidence confidence summary
- `positioning-brief` — only when the Positioning Brief gate below is met. This is the one downstream artifact this job is built to hand off directly into the PMM asset workflow (`lpa-positioning-canvas`, workbook tab 3.1). Persona pack, buyer journey, win-loss, and GTM plan are NOT produced by this job — they remain roadmap items with no implementing skill yet (see `docs/architecture/discovery-system-flow.md`).

## Positioning Brief gate

Produce a `positioning-brief` artifact only if all of the following hold. If any fail, omit it and say why in `recommended_downstream_artifacts`.

- At least 5 independent records support the target segment (the same threshold `strongly_supported` segment-level claims already require).
- The synthesis has `strongly_supported_patterns` covering, at minimum, the core problem, at least one status quo alternative, and at least one competitor or substitute.
- `language_to_use` has enough signal to draft a one-liner in the customer's own words, not invented category language.

When the gate passes, populate every field in [positioning-brief.md](../schemas/positioning-brief.md) directly from the synthesis — `evidence_basis` must cite the specific `convrec-ID`s behind each claim, matching the citation discipline used elsewhere in this synthesis. Run [positioning-brief-rubric.md](../evals/positioning-brief-rubric.md) before treating the brief as ready to hand off.

`lpa-positioning-canvas` treats this brief as an optional first-draft accelerant, not a substitute for its own April Dunford sequence or for `Customer Interview` evidence — the workbook skill still owns the final Positioning Canvas.

## Universal job map

### 1. Define

Define the synthesis scope:

- which segment
- which time period
- which PMM objective

### 2. Locate

Locate all parsed records that match the scope.

### 3. Prepare

Group records by:

- segment
- role
- source type
- date

### 4. Confirm

Confirm the set is large and balanced enough to synthesize responsibly.

### 5. Execute

Extract recurring patterns and meaningful differences.

### 6. Monitor

Watch for:

- overweighting loud anecdotes
- collapsing buyer and user into one
- ignoring contradictory evidence
- inventing confidence not supported by volume or quality

### 7. Modify

Re-scope or split the synthesis if segments are blending together.

### 8. Conclude

Save the synthesis. If the Positioning Brief gate is met, produce the brief and hand it to `lpa-positioning-canvas`. Persona, GTM, and sales-enablement handoffs are roadmap only until those skills exist.

## Method

1. Cluster by recurring problem and outcome patterns.
2. Keep direct language visible.
3. Carry forward record-level citations (`convrec-ID`) and representative quotes for every important pattern. Every entry in `strongly_supported_patterns`, `emerging_patterns`, and `contradictory_signals` must cite at least one specific record ID. No pattern claim without a citation.
4. Separate:
   - **strongly supported patterns** — cite supporting record IDs; use only when the pattern appears in two or more independent records
   - **emerging patterns** — cite supporting record IDs; note that support is limited and indicate how many records it appears in
   - **unresolved contradictions** — name the specific records or stakeholders in tension
5. **Overgeneralization guard:** Before claiming a pattern represents segment-level truth, apply the following minimums:
   - A pattern may be labeled `strongly_supported` only if it appears in at least two independent records.
   - Segment-level claims (e.g., "this segment prioritizes X") require at least five independent records. If the record count is below five, describe the pattern as directional or hypothesis-forming, not as a confirmed segment truth.
   - Include a `coverage_notes` field that states the record count and any obvious sampling limitations.
6. Produce outputs a PMM can reuse immediately.

## Downstream linkage

This synthesis is designed to feed one downstream PMM artifact directly today, plus several planned ones:

- **Positioning brief** — built. See the Positioning Brief gate above. Uses `strongly_supported_patterns`, `competitors_and_substitutes`, `language_to_use`, and `strategic_implications` as the evidence inputs, and hands off to `lpa-positioning-canvas` (workbook 3.1). Positioning claims must trace back to specific record citations in the synthesis.
- **Persona pack** (roadmap, issue #10 — no implementing skill exists yet): once built, would use `top_recurring_pains`, `desired_outcomes`, `evaluation_criteria`, `stakeholder_map` signals, and `representative_quotes` as the primary evidence base.
- **Objection handling assets** (roadmap — no implementing skill exists yet): would use `objections`, `contradictory_signals`, and `trust_requirements`.
- **Sales enablement** (roadmap — no implementing skill exists yet): would use `buying_triggers`, `evaluation_criteria`, and `language_to_use` / `language_to_avoid`.

When producing the synthesis, set `recommended_downstream_artifacts` to name the specific artifacts this synthesis can credibly support given its record count and coverage — today that list can only ever include `positioning-brief`, since it's the only downstream artifact with a skill built to consume it.

## Artifact schema

Use:

- [conversation-synthesis.md](../schemas/conversation-synthesis.md)
- [positioning-brief.md](../schemas/positioning-brief.md) — only when the Positioning Brief gate above is met

## Human review gate

Check all of the following before the synthesis is treated as ready for downstream use:

- **Record-level traceability:** Every strongly supported and emerging pattern cites at least one specific `convrec-ID`. No pattern without a citation.
- **Overgeneralization:** Segment-level claims are not made from fewer than five records. Patterns from smaller sets are labeled directional or hypothesis-forming, not as confirmed segment truth.
- **Pattern separation:** Strongly supported, emerging, and contradictory signals are in distinct sections. Contradictions are preserved, not resolved by averaging.
- **Segment boundaries:** All records in scope belong to the stated segment. Cross-segment signals are either excluded or explicitly flagged.
- **Quote traceability:** Representative quotes include speaker attribution and a record ID citation. They can be traced back to the source record and, when available, to a sentence or timestamp anchor.
- **Downstream usability:** The synthesis is specific enough to drive at least one named downstream artifact. Generic or abstract syntheses that could apply to any product or segment do not pass.

## Evals

Pass if:

- every strongly supported and emerging pattern cites at least one `convrec-ID`
- strongly supported, emerging, and contradictory patterns are in separate named sections
- segment-level claims come from at least five records, or the claim is explicitly labeled directional
- `coverage_notes` states the record count and sampling limitations
- representative quotes include speaker attribution, record-level citation, and a transcript anchor when available
- the synthesis names at least one downstream artifact it can credibly support
- contradictions are preserved and not collapsed into a single summary
- if a `positioning-brief` was produced, it passes [positioning-brief-rubric.md](../evals/positioning-brief-rubric.md)
- if the Positioning Brief gate was not met, `positioning-brief` was omitted rather than produced with placeholder or invented fields

Fail if:

- the synthesis sounds insightful but is not grounded
- any strongly supported or emerging pattern has no record citation
- quotes are missing or unattributed
- patterns are not traceable to underlying records
- segment-specific differences disappear
- segment-level truth is claimed from fewer than five records without a qualifying label
