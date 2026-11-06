---
name: documentation
description: Keep operational and product docs aligned with actual code.
---

# documentation

## Trigger

Keep operational and product docs aligned with actual code. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Write for the next contributor, not the current coding agent.

## Procedure

1. Update README setup, supported versions, env example and run commands.
2. Explain non-obvious decisions in ADRs, with options and consequences.
3. Update API schema, examples and error behavior when contracts change.
4. Add migration, monitoring and rollback details for operational changes.
5. Check internal links and examples against the implementation.

## Deliverable

Accurate docs and examples with links to PRD/ADR as relevant.

## Exit check

A new contributor can reproduce local setup without private tribal knowledge.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
