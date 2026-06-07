---
name: product-manager-copilot-doc-to-spec
description: Run the first OpenCode-native Product Manager CoPilot document-to-spec pre-normalisation pipeline for the CircuitFit pilot, using deterministic tools behind the scenes and stopping at the human evidence-eligibility gate.
---

# Product Manager CoPilot Document-to-Spec Pipeline

## Purpose

Run one governed OpenCode-native workflow for the CircuitFit pilot:

`evidence pack → extraction → quality audit → eligibility summary → human gate`

This skill stops before normalisation.

## Pipeline stages

1. preflight
2. extraction
3. quality audit
4. image decisions
5. eligibility summary
6. human gate

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

## Human approval gates

Stop at the pre-normalisation evidence gate.

Required approval phrase:

`APPROVE ELIGIBLE CIRCUITFIT EVIDENCE FOR NORMALISATION`

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

Expected state after this skill:

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
