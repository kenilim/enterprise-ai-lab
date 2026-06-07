# Product Manager CoPilot Lab — Resume After Step 16K.3

## Current checkpoint

- Repository: `https://github.com/kenilim/enterprise-ai-lab`
- Branch: `main`
- Latest validated commit before this refresh: `93be068`
- Working tree after `93be068`: clean
- Current phase: return from knowledge consolidation to minimum extraction-quality remediation before evidence normalisation
- OpenSpec status: not started
- Application implementation: not started

## Canonical read order

1. `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. `projects/01-doc-to-spec-pilot/README.md`
4. `docs/governance/extraction-quality-gate-matrix.md`
5. `docs/reports/20260607_124717_circuitfit_ingestion_quality_review.md`
6. relevant OpenCode agent, skill and command definitions

Do not load every Markdown file by default.

## Operating-model clarification

OpenCode is the primary product-manager workspace for the CircuitFit simulation:

```text
unstructured evidence
→ extraction
→ quality review
→ normalisation
→ conflict detection
→ OpenSpec proposal
→ human approval
→ specifications
→ tasks
→ acceptance criteria
→ tests
```

The educator-copilot maintains milestone learning records, whitepaper snapshots, offline presentations and reviewed installation packages separately.

## Preserved architecture principles

- open-source-first
- air-gap-ready
- regulator-auditable traceability
- deterministic tools for repeatable work
- agents for interpretation and orchestration
- human approval at material gates
- background processing with progress, ETA, token, CPU and GPU metrics
- exception-based review
- repo-local operational logs excluded from Git
- Git-backed durable shared knowledge

## Known extraction-quality gaps

- XLSX requires workbook-aware fallback inspection
- PPTX requires slide-aware fallback inspection
- PDF reading order requires explicit validation
- screenshot OCR remains noisy
- whiteboard PNG failed the current quality gate
- Outlook `.msg` remains deferred

## Immediate next step

Use OpenCode to define and implement only the minimum trustworthy Step 16 extraction-remediation scope needed for the controlled CircuitFit experiment.

Then:

```text
benchmark rerun
→ eligible-evidence approval
→ normalisation
→ conflict detection
→ first OpenSpec proposal
```

Do not generate OpenSpec artefacts until the Step 16 exit gate passes.
