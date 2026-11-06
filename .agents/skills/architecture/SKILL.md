---
name: architecture
description: Design boundaries and cloud dependencies after requirements stabilize.
---

# architecture

## Trigger

Design boundaries and cloud dependencies after requirements stabilize. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Prefer the smallest maintainable architecture and document trade-offs.

## Procedure

1. Compare at least two feasible options including a simpler alternative.
2. Specify frontend/backend boundaries, data model, external APIs, auth and isolation.
3. Define data retention, secrets, logging without PII, error handling, latency and cost limits.
4. Define environment separation (dev/staging/prod), IaC ownership and rollback.
5. Create templates/architecture.md and an ADR for significant irreversible choices.

## Deliverable

Architecture document, service diagram in Mermaid, ADRs and operational risks.

## Exit check

Architecture traces to PRD requirements; no unexplained managed service, data flow or deployment permission.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
