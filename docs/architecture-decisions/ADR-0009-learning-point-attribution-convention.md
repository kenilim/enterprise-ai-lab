# ADR-0009: Attribute Learning Points to Human Insight, Copilot Recommendation and Experiment Evidence

## Status

Accepted.

## Decision

Each major learning point, checkpoint and architecture decision should identify
its origin.

Use one or more of these labels:

| Label | Meaning |
|---|---|
| `Product-manager insight` | A requirement, challenge or product judgement raised by the human product builder |
| `Copilot recommendation` | An option, script, architecture or explanation proposed by the AI copilot |
| `Experiment result` | Evidence produced by the local lab |
| `Known limitation` | A gap recorded for later work |
| `Decision` | A reviewed direction accepted by the human reviewer |

## Reasoning

The lab is not a one-prompt artefact.

It is an iterative collaboration.

The repository should preserve the difference between:

- what the product builder asked
- what the copilot proposed
- what the experiments proved
- what remains unresolved
- what was finally approved

## Working Model

`product judgement → debate → experiment → evidence → decision → documented learning`

## Future Documentation Rule

Every new meaningful learning point should include an `Origin` subsection.
