---
name: deployment
description: Prepare safe, reversible cloud releases only after authorization.
---

# deployment

## Trigger

Prepare safe, reversible cloud releases only after authorization. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

No automatic provisioning, production secrets, or release without explicit permission.

## Procedure

1. Confirm target cloud, project/account and environment.
2. Verify IaC changes, secret references, IAM, network exposure and budget alerts.
3. Define deployment health checks, monitoring, rollback and database compatibility.
4. Test in staging and verify backups/restore for stateful changes.
5. Obtain human release approval and record deployment evidence.

## Deliverable

Release plan with checklist, health indicators and rollback steps.

## Exit check

Do not deploy if permissions, migration, secrets, rollback or authorization are unresolved.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
