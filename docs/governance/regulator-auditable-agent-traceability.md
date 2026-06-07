# Regulator-Auditable Agent Traceability Requirements

## Purpose

This guide defines the traceability standard for Product Manager CoPilot in a
high-risk enterprise environment subject to internal audit, risk oversight and
potential regulatory review.

This is an architectural baseline, not a claim of regulatory compliance.

## Principle

A high-risk system must be able to reconstruct:

```text
who triggered what
→ against which evidence
→ using which agent, model, skill and tool
→ under which permissions
→ producing which output
→ reviewed and approved by whom
→ committed in which change
→ tested by which controls
→ released in which artefact
→ linked to which incident if something later fails
```

## Audit-Grade Traceability Spine

```text
source evidence
→ source hash
→ extraction run
→ normalised evidence item
→ requirement
→ design decision
→ user story
→ acceptance criterion
→ implementation task
→ agent run
→ code commit
→ automated test evidence
→ merge approval
→ release artefact
→ production event
→ incident investigation
→ remediation decision
```

## Minimum Agent-Run Record

Every agent run should preserve:

| Field | Purpose |
|---|---|
| `run_id` | Unique reference |
| `project_id` | Project boundary |
| `triggered_at_utc` | Timestamp |
| `triggered_by` | Human or approved service identity |
| `agent_name` | Which agent ran |
| `agent_mode` | Primary or subagent |
| `agent_definition_hash` | Which instructions were used |
| `model_provider` | Local gateway or provider |
| `model_name` | Model identifier |
| `model_configuration` | Relevant configuration |
| `skills_loaded` | Which procedures were loaded |
| `tools_invoked` | Which deterministic tools ran |
| `tool_versions` | Exact versions or commit IDs |
| `source_hashes` | Evidence chain of custody |
| `permissions_effective` | Allowed and denied actions |
| `outputs_generated` | Local and sanitised artefacts |
| `warnings` | Known limitations or failures |
| `human_review_status` | Pending, approved or rejected |
| `approved_by` | Reviewer identity |
| `approval_timestamp_utc` | Approval timestamp |
| `git_commit` | Approved Git record |
| `token_usage` | Usage and cost metadata where available |

## Integrity Controls

For a regulator-auditable environment, use:

- immutable or append-only audit records
- trusted timestamps
- strong identity and access controls
- source hashes
- signed or verifiable artefacts where appropriate
- separation of duties
- restricted production access
- change approvals
- retention policy
- tamper detection
- environment segregation
- test evidence
- model and tool versioning
- incident linkage
- exception handling

## Human Approval Gates

Require human approval before:

- changing approved requirements
- creating implementation tasks
- merging code
- changing tests
- risk-accepting failures
- deploying to staging or production
- exposing sensitive evidence
- overriding controls

## Error Attribution

A production incident should be classified as one or more of:

- implementation defect
- incorrect test
- missing requirement
- incorrect requirement
- ambiguous requirement
- design mismatch
- regression gap
- production-learning gap
- control failure
- unauthorised change

## Regulatory Review Questions

A reviewer should be able to ask:

1. What evidence justified this requirement?
2. Which version of the requirement was approved?
3. Who approved it?
4. Which task implemented it?
5. Which agent, model and tools were involved?
6. What permissions did the agent have?
7. Which tests covered the behaviour?
8. Which commit and release introduced it?
9. Was an exception accepted?
10. Was the incident caused by code, requirement, test, design or governance?

## Current Lab Decision

The personal lab will create local traceability manifests and sanitised public
summaries.

A future enterprise implementation should store detailed audit events in an
internal append-only evidence store.

## Limitation

The personal lab does not yet provide regulator-certified controls.

It is building the traceability model that an enterprise implementation would
need to harden, independently review and formally govern.
