---
name: prd
description: Convert approved discovery into a testable requirements document.
---

# prd

## Trigger

Convert approved discovery into a testable requirements document. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Keep requirements independent of implementation unless a technology is constrained.

## Procedure

1. Start from templates/PRD.md and the discovery brief.
2. Define personas, prioritized user stories and acceptance criteria using Given/When/Then.
3. Cover empty states, permissions, accessibility, latency, observability and data deletion.
4. Distinguish P0 MVP from later ideas; add measurable success and non-goals.
5. Identify dependencies, risks and decisions needing product signoff.

## Deliverable

Updated PRD.md with unique IDs for requirements, acceptance criteria and open decisions.

## Exit check

Every P0 user story must have testable acceptance criteria and an owner for unresolved issues.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
