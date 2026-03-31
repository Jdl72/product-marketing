# Funnel Stages

## Stage Definitions

- `F1`:
  - `Name`: Awareness / Intro
  - `Definition`: First or second conversation. The buyer is evaluating whether Xnurta addresses their retail media problem. No formal evaluation criteria stated yet.
  - `Included conversation types`: Discovery calls, intro demos, initial outreach follow-ups, cold-qualified referrals
  - `Excluded conversation types`: Renewal, pricing negotiation, support calls, structured competitive comparisons
  - `Success signal`: Buyer articulates a specific pain and agrees to a next step

- `F2`:
  - `Name`: Active Evaluation
  - `Definition`: Buyer is comparing Xnurta to alternatives. Technical or commercial due diligence is underway. Evaluation criteria have been stated.
  - `Included conversation types`: Platform demos with feature comparison, competitive deep-dives, capability assessments
  - `Excluded conversation types`: Intro calls without explicit evaluation framing, pricing or contract discussions
  - `Success signal`: Buyer identifies blockers or specifies decision criteria

- `F3`:
  - `Name`: Late-Stage Commercial
  - `Definition`: Buyer is working through pricing, contract terms, managed service scope, and onboarding logistics. A decision is expected within weeks.
  - `Included conversation types`: Pricing calls, contract follow-ups, term negotiations, onboarding scope discussions, AMC fee conversations
  - `Excluded conversation types`: Discovery, early demos, competitive evaluations without pricing context
  - `Success signal`: Buyer states conditions for signature or moves to contract review

- `F4`:
  - `Name`: Expansion / Retention
  - `Definition`: Existing customer conversations about expanding channels, modules, or international scope; or retention risk conversations.
  - `Included conversation types`: QBRs, expansion calls, channel-add discussions, churn-risk calls, renewal negotiations
  - `Excluded conversation types`: Net new acquisition conversations
  - `Success signal`: Customer articulates a new job-to-be-done or confirms renewal

## Stage-Mapping Rules

- If the transcript references pricing terms, contract clauses, AMC fees, or onboarding dates → F3
- If the transcript references competitive alternatives without pricing or contract context → F2
- If the transcript references renewal, QBR, or account expansion → F4
- If no prior context is stated and no evaluation criteria are named → F1 (unless transcript content clearly places it later)
- Mark "unresolved" if stage cannot be determined from transcript alone
