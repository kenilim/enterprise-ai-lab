# Docs Knowledge Map

## Purpose

This folder holds the Git-safe durable project memory for the Product Manager
CoPilot lab.

Use it as the default knowledge map for both humans and OpenCode agents.

## WSL Repo Boundary

The WSL repository is the project boundary.

- **Git-safe durable project memory** lives in repository Markdown such as
  requirements, governance files, reports, checkpoints and canonical indexes.
- **Local-only operational evidence** stays under local-only folders such as
  `logs/`, `projects/**/work/`, `projects/**/output/` and raw input paths.

Downloads-folder copies are optional convenience exports only.

They are not the default project-output location.

## Default Retrieval Order

1. `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. relevant project README
4. relevant requirements
5. relevant governance policy
6. latest relevant sanitised report
7. latest milestone checkpoint only when needed

## Canonical Source-of-Truth Files

- `AGENTS.md` — repository-wide operating rules
- `README.md` — high-level repository overview
- `docs/CURRENT_STATE.md` — canonical restart and handoff state
- `docs/requirements/product-manager-copilot-learning-journey-requirements.md`
  — requirements source of truth
- `docs/governance/extraction-quality-gate-matrix.md` — pre-normalisation gate
  policy
- `docs/governance/opencode-agent-run-logging-policy.md` — logging and review
  output policy
- `learnings/LEARNING_JOURNAL.md` — canonical update-in-place learning journal
- `projects/01-doc-to-spec-pilot/README.md` — CircuitFit project status source
  of truth

## Excluded from Default Context

Do not load these by default unless a human asks for historical or audit
reconstruction:

- `logs/`
- `docs/archive/`
- `learnings/archive/`
- `learnings/exports/`
- old bundles
- superseded files
- raw evidence
- private transcripts
- local manifests and extraction output

## Archive and Historical Rules

- Preserve history.
- Prefer milestone checkpoints over micro-checkpoints.
- Prefer canonical files over new summary sprawl.
- Historical files remain available but should not compete with current-state
  files for default retrieval.

## CircuitFit-Specific Read Order

1. `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. `projects/01-doc-to-spec-pilot/README.md`
4. `projects/01-doc-to-spec-pilot/input/README.md`
5. `docs/requirements/product-manager-copilot-learning-journey-requirements.md`
6. `docs/governance/extraction-quality-gate-matrix.md`
7. `docs/governance/opencode-agent-run-logging-policy.md`
8. `docs/reports/20260607_124717_circuitfit_ingestion_quality_review.md`
9. `.opencode/agents/product-manager-copilot.md`
10. `.opencode/commands/pmcp-ingestion-review.md`
11. `.opencode/skills/product-manager-copilot-ingestion-review/SKILL.md`

## Folder Map

- `architecture-decisions/` — durable architecture decisions
- `requirements/` — product and learning requirements
- `governance/` — policy and control rules
- `guides/` — reference guides
- `reports/` — sanitised run or project reports
- `checkpoints/` — milestone checkpoints
- `archive/` — historical reference, not default retrieval
