# ADR-0013: Background Agent Jobs, Progress Estimation and Policy-Driven Approval Gates

## Status

Proposed after the first controlled interactive ingestion-review run.

## Context

The first interactive OpenCode ingestion-review run demonstrated that manual
permission prompts are useful for learning and early validation.

However, large enterprise evidence packs are too large for constant human
permission prompts.

## Decision

The Product Manager CoPilot should evolve toward background job execution with
policy-defined permission profiles and clear human approval gates.

## Target Pattern

```text
user creates project
→ uploads evidence
→ preflight scan estimates workload
→ background job starts
→ deterministic tools process evidence
→ agent reviews extracted evidence
→ progress and ETA update continuously
→ exceptions are surfaced
→ human approves material changes
→ OpenSpec proposal is generated only after approval
```

## Approval Principle

Do not ask the human to approve every safe read or approved deterministic
script.

Require approval for:

- new or unapproved tool use
- writing public artefacts
- changing approved requirements
- creating OpenSpec proposals
- changing tests
- implementation work
- deployment
- policy exceptions
- suspicious or failed extraction results

## Metrics Requirement

Every background run should track:

- files processed
- work units processed
- wall-clock time
- per-stage duration
- queue wait time
- token usage
- model cost where applicable
- CPU and memory usage
- GPU utilisation where applicable
- peak VRAM
- GPU-hours
- retries
- failures
- quality warnings
- ETA accuracy

## Enterprise Implication

Interactive review remains useful for exception handling and high-risk approval
points.

Routine ingestion should run asynchronously with observable progress and
auditable checkpoints.
