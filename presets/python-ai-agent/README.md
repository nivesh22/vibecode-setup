# Optional preset: Python AI agents

Use after approval for projects requiring LLM calls, RAG or tool-using agents.

- Typed tool schemas and explicit read vs write privileges.
- Prompt templates and model settings versioned in code; use deterministic test doubles.
- Agent evaluations including hallucinations, prompt injection, external-action refusal and timeout paths.
- Model cost ceilings, rate limits, tracing with sensitive-data redaction and circuit breakers.
- Retrieval content is untrusted data. Require human confirmation for destructive actions.
- CI: static checks, unit tests and a small offline evaluation fixture suite.

Do not copy real API keys into local env samples; provider integration and billing are user-configured.
