---
name: backend-engineering
description: Implement reliable APIs, databases and integrations.
---

# backend-engineering

## Trigger

Implement reliable APIs, databases and integrations. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Make correctness and backwards compatibility explicit.

## Procedure

1. Define API contracts, validation, status codes and idempotency for write operations.
2. Separate business logic, persistence and transport layers.
3. Plan schema migrations with forward and rollback procedures; never modify production directly.
4. Bound timeouts, retries and rate limits; prevent duplicate side effects.
5. Add structured logs, metrics, integration tests and least-privilege auth.

## Deliverable

API contracts, migration notes, tests and operations considerations.

## Exit check

No undocumented breaking change, unbounded retries or unvalidated input; integration tests cover failure paths.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
