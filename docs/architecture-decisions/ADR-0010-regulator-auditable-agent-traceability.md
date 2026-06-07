# ADR-0010: Regulator-Auditable Agent Traceability

## Status

Accepted as the target control standard.

## Decision

Product Manager CoPilot must preserve an audit-grade traceability model suitable
for a high-risk enterprise environment with internal risk oversight, audit
review and potential regulatory scrutiny.

## Required Chain

`source evidence → hash → extraction run → normalised evidence → requirement → design → story → acceptance criterion → task → agent run → code commit → test evidence → approval → release → incident`

## Required Controls

- append-only or immutable audit evidence
- trusted timestamps
- identities
- approval records
- separation of duties
- model and tool versioning
- source hashes
- Git commit linkage
- test evidence
- incident linkage
- exception handling
- retention and access-control policy

## Important Boundary

The current personal lab is not regulator certified.

It is defining the control model that an enterprise implementation would need
to harden, independently assess and govern.
