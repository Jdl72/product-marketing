# Job Spec: Synthesize Conversation Set

## Core job

When I have multiple parsed customer conversations, help me synthesize them into PMM evidence that can drive personas, positioning, GTM, and sales enablement.

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

Save the synthesis and hand it to persona, positioning, GTM, or sales jobs.

## Method

1. Cluster by recurring problem and outcome patterns.
2. Keep direct language visible.
3. Separate:
   - strongly supported patterns
   - emerging patterns
   - unresolved contradictions
4. Flag where evidence is too thin to generalize.
5. Produce outputs a PMM can reuse immediately.

## Artifact schema

Use:

- [conversation-synthesis.md](/Users/jacklindberg/Documents/Product%20Marketing/schemas/conversation-synthesis.md)

## Human review gate

Check:

- whether segment boundaries are still clean
- whether the synthesis overstates the evidence
- whether the resulting output is usable for personas and positioning

## Evals

Pass if:

- recurring patterns are clearly supported
- contradictions are preserved where real
- the synthesis can feed at least one downstream PMM artifact directly

Fail if:

- the synthesis sounds insightful but is not grounded
- quotes are missing
- segment-specific differences disappear
