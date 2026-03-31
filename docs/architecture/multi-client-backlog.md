# Multi-Client PMM Backlog

## Purpose

Track the cross-cutting work required to make the Product Marketing repo reusable across clients while supporting a real [client] implementation.

This backlog complements the existing capability epics by adding the platform, configuration, reference-client, and operating-rhythm work needed for consulting use.

## Epic: Core PMM System Hardening

GitHub:

- `#65`

Goal:

Make the generic Product Marketing repo explicitly multi-client and consumer-friendly.

Child issues:

- `#66` Document core-vs-client architecture in system docs
- `#67` Add a client workspace contract
- `#68` Add example client workspace and config templates
- `#69` Add a config-aware customer conversation runbook
- `#70` Add a client-workspace evaluation artifact

## Epic: Client Configuration Framework

GitHub:

- `#71`

Goal:

Define the reusable configuration layer a consultant can adapt for any client without editing core logic.

Child issues:

- `#72` Define minimum client config pack structure
- `#73` Define configurable versus fixed fields in conversation workflows
- `#74` Define config validation rules and fallback behavior
- `#75` Add generic markdown config templates
- `#76` Add one generic example client config pack

## Epic: Reference Client Implementation - [client]

GitHub:

- `#77`

Goal:

Implement [client] as the first full client workspace that consumes the reusable PMM system.

Child issues:

- `#78` Create [client] client workspace structure
- `#79` Create [client] client profile and segment taxonomy
- `#80` Create [client] funnel-stage map and coding rules
- `#81` Create [client] competitor map and alternative categories
- `#82` Create [client] strategic questions and scorecard
- `#83` Organize [client] evidence inventories
- `#84` Organize [client] record indexes
- `#85` Organize [client] synthesis indexes
- `#86` Organize [client] brief indexes and outputs
- `#87` Add [client] decision and cross-functional action trackers

## Epic: Cross-Functional Operating Rhythm

GitHub:

- `#88`

Goal:

Ensure evidence outputs drive recurring business action rather than one-off research.

Child issues:

- `#89` Define monthly evidence review format
- `#90` Define issue-routing rules across PMM, Sales, Product, and CS
- `#91` Define insight-to-action tracker schema
- `#92` Define decision-log format for Proceed / Pivot / Kill / Defer
- `#93` Define minimal transcript-informed scorecard

## Notes

- Existing capability epics remain the main artifact and workflow roadmap.
- These epics are foundational and should be treated as enabling work for reusable consulting deployment.
- [client] is a reference client, not a permanent exception to the core method.
