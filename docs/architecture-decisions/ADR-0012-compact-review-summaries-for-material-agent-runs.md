# ADR-0012: Produce Compact Review Summaries for Every Material Agent Run

## Status

Accepted.

## Decision

Every material Product Manager CoPilot workflow should produce:

```text
full local log
→ structured local manifest
→ concise human-readable summary
→ sanitised public checkpoint after review
```

## Problem

Terminal output is useful during execution but is not a suitable human-review
interface or durable audit artefact.

Long terminal dumps are difficult to review, compare, share and preserve.

## Reasoning

A high-risk environment needs both:

- complete evidence for reconstruction
- concise evidence for routine human review

## Implementation Rule

Wrapper scripts should generate:

- timestamped local log
- timestamped manifest
- timestamped Markdown summary
- explicit next action

## Audit Principle

The compact summary does not replace the underlying detailed log.

It is the first layer in a progressive-disclosure review model.
