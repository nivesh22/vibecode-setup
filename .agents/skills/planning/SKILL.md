---
name: planning
description: Turn an approved spec and architecture into small mergeable tasks.
---

# planning

## Trigger

Turn an approved spec and architecture into small mergeable tasks. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Do not establish a second project management framework.

## Procedure

1. Identify dependencies and split vertical slices that can be tested in isolation.
2. For each task provide issue title, owner, affected files/services, acceptance criteria and tests.
3. Flag tasks that share files or database migrations so they are serialized.
4. Prioritize a working end-to-end thin slice before polish.
5. Separate exploratory spikes from production implementation.

## Deliverable

Ordered issue-ready task list, dependencies and merge checkpoints.

## Exit check

Each task can land independently, is reasonably reviewable and has an observable done condition.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
