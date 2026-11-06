---
name: ai-agent-engineering
description: Engineer LLM/agent features with measurable behavior and safety.
---

# ai-agent-engineering

## Trigger

Engineer LLM/agent features with measurable behavior and safety. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Prompts are versioned code, not unreviewable magic.

## Procedure

1. Document each agent's tools, permissions, boundaries and input/output schema.
2. Keep tools least privilege; require confirmation for destructive or external side effects.
3. Handle prompt injection as untrusted content; isolate retrieved text from instructions.
4. Assemble a small reproducible eval set including adversarial, irrelevant and failure cases.
5. Track cost, latency, trace redaction, fallback and failure handling.

## Deliverable

Agent/tool contracts, eval cases, model configuration and known failure modes.

## Exit check

Evals run with recorded results; no secret leakage, unlimited autonomous spending or unapproved side effects.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
