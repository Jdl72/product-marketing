# Workflow Contracts

This directory defines reusable workflow input/output contracts for schema-backed PMM artifacts.

Use these contracts to answer:

- what inputs must exist before a workflow should run
- what optional inputs can improve the result without changing the core method
- which schema the workflow must satisfy
- where human review must happen
- what failure or fallback behavior is allowed
- which downstream artifacts should be able to consume the output

## Available documents

- `workflow-input-output-template.md`
- `positioning-brief-workflow-contract.md`
- `persona-pack-workflow-contract.md`
- `gtm-plan-workflow-contract.md`
- `battle-card-workflow-contract.md`
- `content-calendar-workflow-contract.md`
