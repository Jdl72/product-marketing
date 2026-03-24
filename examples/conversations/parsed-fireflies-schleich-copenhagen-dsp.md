# Parse Single Conversation Example: Schleich / Copenhagen Commerce DSP Conversation

## Raw source metadata

- `source_id`: `01KMDFR8SB2ZEPT3452AFH85F9`
- `source_type`: `fireflies_transcript`
- `date`: `2026-03-23`
- `account_or_company`: `Schleich with Copenhagen Commerce`
- `segment`: `brand plus agency evaluation of AMC / DSP partnership`
- `persona_or_role`: `agency lead and brand stakeholder evaluating analytics and audience-building partner`
- `conversation_context`: `discovery and solution-shaping call focused on AMC strategy, agency fit, DSP relationship structure, RFP constraints, and near-term rollout`
- `stakeholder_map`: `Silas = agency operator focused on workflow, scale, and packaging fit; Larysa = brand stakeholder focused on kicking off AMC quickly and preserving relationship flexibility`

## Raw source summary

This is a multi-party conversation about whether and how to structure a partnership around AMC and DSP while an agency RFP is in progress. The strongest signal is around unmet workflow needs, desired partnership shape, evaluation criteria, and the boundary between analytics, audience creation, and campaign execution.

It was chosen because it contains richer discovery signal than a pure pricing call and shows how customer needs translate into partnership design.

## Parsed conversation record

### `record_id`

`convrec-fireflies-01KMDFR8SB2ZEPT3452AFH85F9`

### `primary_pains`

- Current AMC / campaign support has not delivered the level of strategy expected.
- The team needs stronger audience building and AMC workflow support without overloading internal resources.
- The current RFP process creates uncertainty around who should own the relationship and how implementation should proceed.
- The team lacks a clean, scalable way to connect audience strategy to campaign execution.

### `secondary_pains`

- Existing tools are limited for advanced AMC use cases.
- Coding and query-building in AMC is frustrating and resource-intensive.
- The team does not want to spend time setting something up if the partnership structure changes soon.
- Campaign creation at scale remains a missing piece even if reporting and audience capabilities improve.

### `desired_outcomes`

- Get AMC strategy moving quickly.
- Improve reporting, audience creation, and full-funnel AMC strategy.
- Preserve flexibility if the brand changes agencies.
- Support Prime Day readiness without stalling on org changes.
- Reduce manual work required to generate recurring insights and audience actions.

### `current_alternatives`

- Building AMC technology internally
- `Intentwise` for retail / apps data, reporting, and dashboards
- Existing agency workflows and in-house tools
- Other DSP partners under consideration

### `objections`

- The team does not want to commit to a structure that becomes unhelpful if the agency relationship changes.
- Reporting and audience creation alone may not be enough if campaign execution still requires too much manual work.
- Pricing and packaging need to align with the agency's current client contract model.
- There is uncertainty about where the product boundary sits between analytics, audience enrichment, and campaign management.

### `contract_or_legal_objections`

- No major legal redlines surfaced directly in this call.
- Commercial structure risk is present indirectly through agency RFP uncertainty and the need for transfer-safe partnership design.

### `buying_triggers`

- Need to get AMC strategies "kickstarted" quickly.
- Prime Day creates a near-term execution deadline.
- Strong audience-building capability is seen as a meaningful advantage.
- Flexibility around seat transfer and future agency changes reduces risk.

### `evaluation_criteria`

- Ability to support a "full AMC strategy" across the funnel
- Strength of audience-building capabilities
- Quality of reporting and analytics
- Ease of use for teams without dedicated data science support
- Flexibility of partnership model
- Compatibility with existing tools and agency workflows
- Time to value and onboarding speed

### `trust_requirements`

- Confidence that the platform can cover the majority of real use cases
- Clear explanation of what is manual vs automated
- A structure that protects continuity if the agency changes
- Concrete next steps and pre-work so legal / procurement friction does not slow rollout

### `competitors_mentioned`

- `Intentwise`
- unnamed alternative DSP / tech partners
- internal build option

### `language_to_use`

- "full AMC strategy"
- "covering all the different steps of the funnel"
- "get those kickstarted"
- "better reporting"
- "audience building capabilities are super strong"
- "super simple to navigate"
- "won't lose any data"

### `language_to_avoid`

- framing the product as only a reporting tool
- implying full campaign automation if campaign creation remains partly manual
- rigid partnership language that ignores the active RFP context

### `notable_quotes`

- `Silas Moestrup Pedersen`: "a DSP partnership is, like, would be the right way for us to, as a company, 100%."
- `Silas Moestrup Pedersen`: "we'll be building our own tech out for amc."
- `Silas Moestrup Pedersen`: "that's really not what we want. Like, we want, like, a full AMC strategy."
- `Larysa Gruner`: "how quickly can we, you know, get those kickstarted?"
- `Silas Moestrup Pedersen`: "they're super limited when it Comes to EMC and just like more advanced stuff."
- `Silas Moestrup Pedersen`: "the missing piece is basically how do you do audience at a scale?"
- `Silas Moestrup Pedersen`: "we're all ready for that also, because I think the next thing coming up is obviously Prime Day in June."

### `term_normalization_notes`

- `EMC` normalized to `AMC` in interpretation fields based on surrounding transcript context.
- `amc` normalized to `AMC` and `dsp` normalized to `DSP` in interpretation fields, while quotes preserve original phrasing.

### `summary_of_signal`

This conversation is a strong source for discovery around workflow design and partnership structure. The buyers are not only evaluating feature fit; they are deciding how AMC, DSP, agency ownership, and internal build plans should intersect. The strongest signal is that audience building, reporting, and full-funnel AMC strategy are valuable, but the offering has to fit a flexible agency context and be honest about where manual campaign work still exists.

### `evidence_strength`

`strong`

### `confidence`

`high`

### `missing_context`

- We do not know the exact pricing terms discussed outside this call.
- We do not have the full RFP criteria or final agency decision.
- Some statements reflect agency-side needs and some reflect brand-side needs; they should not be collapsed into a single buyer voice.

### `open_questions`

- Which decision-maker has final authority over AMC vs DSP structure?
- Is the strongest wedge here `audience building`, `AMC strategy`, or `transition-safe partnership`?
- How important is campaign creation automation relative to reporting and audience enrichment?
- What proof would most reduce hesitation during an active RFP?

## Review notes

- what felt easy
  The call surfaced clear desired outcomes, current alternatives, and evaluation criteria.
- what was ambiguous
  This is a three-party conversation, so there are multiple buyer perspectives with slightly different priorities.
- what the schema missed
  It would help to capture `stakeholder map` or `speaker-by-speaker priorities` for multi-party discovery calls.
- what the job spec should clarify
  For multi-party calls, the parser should preserve role-specific viewpoints instead of flattening them into one composite customer.
- what should become an eval rule
  If a source has multiple external stakeholders, the output should explicitly note where needs diverge or only partially overlap.

## Output quality verdict

`usable as-is`

This is already a strong PMM evidence record for downstream persona, positioning, and synthesis work. The main caution is preserving stakeholder distinctions in future downstream artifacts.
