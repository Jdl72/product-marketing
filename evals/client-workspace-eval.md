# Client Workspace Evaluation

## Purpose

Evaluate whether a client workspace is complete enough to support repeatable PMM work without editing the core system.

## Pass criteria

- the required workspace folders exist
- all required config files exist
- the config pack is specific enough to scope evidence work
- evidence inventory exists with source provenance
- parsed records are stored separately from syntheses
- briefs are stored separately from raw evidence
- decisions and owners are captured in a dedicated location
- outputs preserve quote traceability

## Fail criteria

- the workspace is just a folder of briefs with no config pack
- evidence and client-facing conclusions are mixed together
- segment and stage definitions are missing
- strategic questions are implicit rather than written down
- source provenance is lost
- actions are not routed to owners

## Review prompts

- Can a new person understand the client's segment and stage model from `config/` alone?
- Can the source inventory be inspected without opening briefs?
- Can a synthesis claim be traced to a record and source?
- Can an insight be routed to PMM, Sales, Product, CS, or Cross-functional ownership?
- Could another client reuse the same core workflow without inheriting this client's vocabulary?
