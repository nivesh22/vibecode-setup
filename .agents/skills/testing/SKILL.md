---
name: testing
description: Use test-first thinking and enforce evidence before declaring done.
---

# testing

## Trigger

Use test-first thinking and enforce evidence before declaring done. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Tests belong to the implementation task, not a separate orchestration phase.

## Procedure

1. Derive tests from acceptance criteria before implementation where practical.
2. Cover unit, integration and e2e layers according to risk.
3. Test negative paths, permission boundaries, retries and data migration.
4. Keep tests deterministic; use fixtures and avoid reliance on live production services.
5. Run lint, type checks, tests and build where available; report exact commands and failures.

## Deliverable

Automated test changes, run commands and actual results.

## Exit check

No invented green status, skipped critical test without explanation or silently disabled checks.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
