# ADR-0007: Agent Orchestrates Deterministic Tools

## Status

Accepted.

## Decision

Use deterministic scripts for repeatable extraction and validation tasks.

Use an agent to orchestrate those tools, interpret outputs, identify gaps and
prepare reviewable reports.

## Reasoning

A production-quality workflow should not depend on an agent improvising every
step.

The preferred division of labour is:

| Deterministic tools | Agent reasoning |
|---|---|
| hash files | interpret evidence |
| route formats | identify contradictions |
| parse documents | explain uncertainty |
| record metadata | draft changes |
| enforce folders | propose OpenSpec artefacts |
| run tests | recommend next actions |

## Lab Implementation

Create an OpenCode skill:

`product-manager-copilot-ingestion-review`

The skill runs tested local tools and stops for human approval before commit or
push.

## Production Implication

The final Product Manager CoPilot web application should invoke a workflow
orchestrator and backend workers.

OpenCode is the lab and developer-facing orchestration environment, not
necessarily the final production runtime.
