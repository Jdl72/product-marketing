# Coding Rules

## Client Extensions

- `Buying triggers used in coding`:
  - Pacvue dissatisfaction — slow platform load times, limited AI levers (4 vs. Xnurta's 11), static/non-interoperable optimization, ownership uncertainty from Assembly's sale attempts and resulting cost-cutting
  - Intentwise fatigue — 24-hour recommendation lag, recommendations require manual implementation, inflexible 1-of-20 algorithm assignment
  - Skai / rules-based platform limitations — rules run on schedules not continuously, retail media bolted on vs. native, lengthy onboarding
  - Perpetua limitations — no rules-based optimization, keyword stuffing, one-size-fits-all AI with no toggle control
  - Managed service consolidation need — buyer is replacing current agency or internal headcount arrangement
  - AMC attribution gap — buyer lacks visibility into full-funnel attribution or needs custom AMC audience capabilities
  - DAA co-sell context — Amazon GGS AE made the introduction or is co-presenting; flag these leads separately
  - Urgency around business milestone — buyer references Prime Day, Q4, tentpole event, or a go-live deadline
  - Walmart or international expansion intent — buyer is expanding beyond Amazon to Walmart, EU, or China markets
  - Agency seeking portfolio management scale — agency buyer managing multiple client accounts needs centralized control and reporting

- `Objection categories used in coding`:
  - Managed service fee vs. perceived labor — buyer questions cost relative to estimated hours of work ("the same guy is like managing like multiple accounts")
  - AMC incremental fee — buyer already has a free alternative (PackView AMC) and resists paying for AMC access
  - Contract term length and amendment rights — buyer wants protection against unilateral T&C changes; wants pricing tiers in the contract rather than informal renegotiation
  - Onboarding timeline confidence — buyer uncertain whether onboarding will happen on the promised timeline with sufficient senior support
  - Pacvue rules-based depth — buyer values Pacvue's 100+ retailer coverage or hands-on rules controls and questions whether Xnurta matches it
  - Category legitimacy — buyer questions whether "AI-powered retail media optimization" (or alternatives) is a real, differentiated category
  - Pricing transparency — buyer prefers flat fee or spend-based tiers over percentage-of-spend models; wants predictability
  - Data portability — buyer wants explicit contractual language on data export rights

- `Proof categories used in coding`:
  - Amazon Technology Innovation Award (back-to-back 2023, 2024) — third-party validation from Amazon; use when buyer questions market standing
  - Zenith case study — 20% DSP sales increase, 5% spend reduction using AMC audiences; use when buyer questions AMC value or DSP optimization claims
  - AI Copilot scale — 2M+ daily optimization decisions; use when buyer questions autonomous AI vs. rules-based alternatives
  - 11 AI levers vs. 4 — direct comparison against Pacvue; use when buyer is evaluating Pacvue as primary alternative
  - Lock Ad Placement — unique feature; use when buyer wants to defend premium ad positions
  - Real-time optimization — 30-60 minute adjustment cycle vs. Intentwise's 24-hour cycle; use when buyer is evaluating Intentwise
  - Managed service CSM quality — dedicated senior-level support; use when buyer cites managed service quality or continuity concerns
  - Onboarding success and speed-to-value — use when buyer cites onboarding timeline anxiety
  - AI + rules interoperability — best of both worlds; use when buyer doesn't want to choose between automation and control

- `Outcome signals used in coding`:
  - Ready-to-sign language — "if we can get everything I need on Monday, I can sign a contract on Monday"
  - Referral intent — buyer has already referred or explicitly intends to refer a peer
  - Urgency around business milestone — buyer names a specific event or date as a go-live requirement
  - Expansion intent — buyer mentions adding Walmart, DSP, international channels, or additional brand accounts
  - Churn risk language — existing customer expressing dissatisfaction with support, platform performance, or ROI

- `Stage-mapping rules`:
  - If the transcript references pricing terms, contract clauses, AMC fees, or onboarding dates → F3
  - If the transcript references competitive alternatives or evaluation criteria without pricing → F2
  - If the transcript references renewal, QBR, churn risk, or account expansion → F4
  - If first contact or no evaluation criteria are stated → F1 unless transcript content clearly places it later
  - Mark "unresolved" if stage cannot be determined from the transcript alone

- `Segment-mapping rules`:
  - If the buyer is managing ad campaigns on behalf of brand clients (agency structure) → S4
  - If the buyer references multiple storefronts or brands under their own ownership → S1
  - If the buyer references international channels (China, EU, JD, Alibaba) as a primary topic → S3
  - If the buyer is a single-brand domestic operator → S2
  - Mark "unresolved" if the transcript does not provide enough context to determine segment

## Rules

- Extend the generic schema fields; do not replace them.
- Keep direct customer language visible. Quote the buyer verbatim in `notable_quotes`; do not paraphrase objections into generic categories.
- Mark unresolved mappings explicitly instead of forcing a fit.
- "Pack roo" in a Fireflies transcript normalizes to Pacvue. "PackView" in a transcript may refer to PackView AMC (free tool) or to Pacvue — resolve from context.
- Seller-side statements can be captured as context but should not be treated as buyer evidence. Customer-side signals are primary.
- If a conversation is commercial (F3 context), preserve specific pricing objections and contract redlines rather than smoothing them into generic "budget concerns."
