# Product Manager CoPilot Enterprise AI Lab
## Step 16K.3 Learning Snapshot — Canonical Knowledge and Return to OpenSpec

**Checkpoint before snapshot:** `93be068`
**Branch:** `main`
**Date:** 7 June 2026

## Executive summary

The Product Manager CoPilot lab temporarily expanded from ingestion-quality remediation into documentation, handoff and governance-design work. That work produced valuable lessons, but it also exposed a second-order risk: documentation itself can become fragmented, stale and difficult for agents to retrieve safely.

The lab has now established a canonical knowledge spine and is returning to its main experiment: using CircuitFit as the synthetic pilot for an agentic unstructured-evidence-to-OpenSpec workflow.

## Core operating model

```text
OpenCode
→ product-manager workspace for CircuitFit workflow simulation

External educator-copilot
→ learning records
→ whitepaper snapshots
→ offline presentations
→ reviewed installation packages
```

## Key learning: documentation entropy is an AI risk

More documents do not automatically create better project memory.

```text
too many overlapping Markdown files
→ retrieval noise
→ stale or competing context
→ agent confusion
→ increased hallucination exposure
```

The solution is a canonical read order:

1. `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. relevant project README
4. relevant governance policy
5. latest sanitised report
6. relevant agent, skill and command definitions

## Anti-hallucination architecture

Hallucination control begins before retrieval:

```text
source quality
→ extraction quality
→ format-aware quality gates
→ normalisation
→ conflict detection
→ retrieval ranking
→ context budgeting
→ citations
→ abstention
→ evaluation
```

## Current CircuitFit status

Completed:

- synthetic multi-format evidence pack
- deterministic extraction benchmark
- first OpenCode ingestion-quality review
- extraction-quality gap identification
- pre-normalisation quality-gate matrix
- canonical knowledge consolidation

Still pending:

- minimum extraction remediation
- benchmark rerun
- eligible-evidence approval
- normalisation
- conflict detection
- first OpenSpec proposal
- specifications
- acceptance criteria
- tests

## Decision

Stop expanding documentation after this milestone refresh.

Return to:

```text
minimum extraction remediation
→ benchmark rerun
→ eligible-evidence approval
→ normalisation
→ conflict detection
→ first OpenSpec proposal
```
