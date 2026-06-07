# Current State

## Project

- Product: `Product Manager CoPilot`
- Repository branch: `main`
- Latest validated remote commit before this consolidation: `c3ae2e4`

## Current Phase

Step 16 knowledge consolidation before extraction-quality remediation resumes.

## What Has Been Achieved

- Multi-format CircuitFit benchmark completed
- First sanitised ingestion-quality review completed
- Major extraction-quality gaps identified
- OpenCode primary agent, subagent, skill and command definitions created
- Pre-normalisation extraction-quality gate policy refined
- Repo-local versus local-only boundary clarified

## What Remains Blocked

- Evidence normalisation
- Conflict detection
- OpenSpec generation
- Application code
- CircuitFit specifications and tests
- Outlook `.msg` ingestion
- Fallback-inspection implementation for XLSX, PPTX, PDF and image-heavy files

## CircuitFit Status

Current CircuitFit status:

```text
benchmark complete
→ first quality review complete
→ extraction gate policy refined
→ knowledge consolidation in progress
→ fallback-scope definition next
```

## Why OpenSpec and Tests Do Not Exist Yet

- Extraction-quality gates are not finished.
- Evidence normalisation has not started.
- No approved evidence register exists yet.
- The lab rule is to delay OpenSpec and coding until evidence quality is strong
  enough to support grounded downstream work.

## Default Read Order for a New Authorised User or Agent

1. `AGENTS.md`
2. `docs/README.md`
3. this file
4. `projects/01-doc-to-spec-pilot/README.md`
5. `docs/requirements/product-manager-copilot-learning-journey-requirements.md`
6. `docs/governance/extraction-quality-gate-matrix.md`
7. `docs/governance/opencode-agent-run-logging-policy.md`
8. `docs/reports/20260607_124717_circuitfit_ingestion_quality_review.md`
9. latest milestone checkpoint only if needed

## Current Git Rule

OpenCode currently prepares and validates changes.

The human currently performs manual Git commit and push from a separate WSL
terminal after review and approval.

## Exact Next Bounded Step

`Step 16R3 — define deterministic fallback-inspection scope and OpenCode-native tool interfaces for CircuitFit.`
