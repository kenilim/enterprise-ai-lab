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

<!-- PMCP_MANAGED_BLOCK:STEP16K3_CURRENT_STATE:START -->
## Current milestone: Step 16K.3 learning refresh

- **Latest validated Git checkpoint before this refresh:** `93be068`
- **Branch:** `main`
- **Validated state:** canonical knowledge spine committed and pushed; working tree was clean.
- **Primary workspace for the product-manager simulation:** OpenCode.
- **OpenCode scope:** CircuitFit unstructured evidence → extraction review → quality gates → normalisation → conflict detection → first OpenSpec proposal.
- **External educator-copilot scope:** milestone learning records, whitepaper snapshots, offline presentations and reviewed installation scripts.
- **WSL project boundary:** `/home/kenilim/projects/enterprise-ai-lab`
- **Git rule:** OpenCode prepares and validates changes; the human currently performs reviewed `git commit` and `git push` from a separate WSL terminal.
- **OpenSpec status:** not started.
- **CircuitFit specifications and tests:** not generated yet.
- **Reason:** evidence normalisation and conflict review remain intentionally blocked until the minimum Step 16 extraction-quality exit gate passes.

### Immediate next bounded technical step

Return to OpenCode and define the minimum Step 16 extraction-remediation scope required for the controlled CircuitFit experiment:

`minimum extraction remediation → benchmark rerun → eligible-evidence approval → normalisation → conflict detection → first OpenSpec proposal`

### Default read order

1. `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. `projects/01-doc-to-spec-pilot/README.md`
4. `docs/governance/extraction-quality-gate-matrix.md`
5. `docs/reports/20260607_124717_circuitfit_ingestion_quality_review.md`
6. relevant OpenCode agent, skill and command definitions
<!-- PMCP_MANAGED_BLOCK:STEP16K3_CURRENT_STATE:END -->
