---
name: product-manager-copilot-doc-to-spec
description: Run the resumable OpenCode-native Product Manager CoPilot document-to-spec workflow for the CircuitFit pilot, routing deterministically from the latest valid manifest and respecting bounded approval gates.
---

# Product Manager CoPilot Document-to-Spec Pipeline

## Purpose

Run one governed OpenCode-native workflow for the CircuitFit pilot:

`evidence pack → extraction → quality audit → eligibility summary → human gate → normalisation → conflict review → OpenSpec proposal`

The primary orchestrator owns the state machine.

This skill defines the routing rules and deterministic boundaries.

## Pipeline stages

1. preflight
2. extraction
3. quality audit
4. image decisions
5. eligibility summary
6. human gate
7. normalisation
8. conflict review
9. OpenSpec proposal

## Resumable routing rules

Inspect the latest valid local manifest first.

Route automatically:

- no manifest → start at `preflight`
- `awaiting_human_approval_before_normalisation` without recorded approval → show the evidence gate
- `awaiting_human_approval_before_normalisation` with recorded approval → resume at `normalisation`
- `awaiting_human_review_of_normalised_evidence_and_conflicts` → show the conflict-review gate
- later approved conflict-review state → resume at `openspec_proposal`

Do not rerun completed stages unless:

- the manifest is missing
- the manifest is invalid
- the user explicitly requests a rerun
- an upstream source file hash changed

## Deterministic-tool boundaries

Deterministic tools perform:

- source hashing
- format classification
- Docling extraction
- XLSX workbook audit
- PPTX slide audit
- PDF page-aware Docling-JSON audit
- manifest writing

## Agent judgement boundaries

The agent may:

- explain warnings in plain English
- summarise eligibility decisions
- highlight material exceptions

The agent must not:

- treat weak extraction as trustworthy evidence
- normalise evidence before approval
- create OpenSpec artefacts in this stage
- write application code

The ingestion-reviewer remains a bounded specialist subagent only.

It must not silently expand permissions or take ownership of later phases.

## Human approval gates

Stop at the pre-normalisation evidence gate.

Required approval phrase:

`APPROVE ELIGIBLE CIRCUITFIT EVIDENCE FOR NORMALISATION`

This approval authorises only the next bounded phase:

- `normalisation`

It does not authorise:

- conflict resolution approval
- OpenSpec generation
- application coding
- test creation
- deployment

## Blocked and deferred evidence handling

- screenshot PNG: bounded human review only
- whiteboard PNG: blocked for the first OpenSpec experiment
- Outlook `.msg`: deferred

## Resumability

The pipeline must write a local-only manifest with:

- run identity
- stage progress
- warnings
- per-file eligibility
- blocked evidence
- deferred formats
- pipeline state
- resume stage

Expected state after the Step 16 ingestion-quality phase:

- `pipeline_state: awaiting_human_approval_before_normalisation`
- `resume_stage: normalisation`

## Local-only versus Git-safe outputs

- local-only: extraction outputs, audit JSON, pipeline manifest, runtime logs
- future Git-safe output: sanitised eligibility summary after human review

## Future post-approval stages

After approval in later steps only:

1. normalisation
2. conflict detection
3. first OpenSpec proposal
4. specifications
5. tasks
6. acceptance criteria
7. tests

OpenSpec remains blocked until the later conflict-review approval state has been
recorded.
