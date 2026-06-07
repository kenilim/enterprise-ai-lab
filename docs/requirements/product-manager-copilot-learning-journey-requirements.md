# Product Manager CoPilot — Learning Journey and Product Requirements v0.2

## Document Purpose

This document records the requirements supplied by the product manager for the
Enterprise AI Development Lab.

The lab is intentionally being built hands-on by a non-technical product person
with basic and dated coding knowledge, using an AI copilot to research,
understand, test and document the end-to-end workflow.

The lab is not a one-prompt exercise.

The product manager continuously shapes the work through:

- product judgement
- prioritisation
- challenge
- debate
- architecture constraints
- governance requirements
- acceptance criteria
- sequencing decisions

## North-Star Product

`Product Manager CoPilot`

An internal project workspace with a ChatGPT-style interface that helps product
managers turn fragmented enterprise evidence into grounded, versioned and
reviewable delivery artefacts.

## Core Product Problem

Large enterprise programmes produce fragmented and contradictory information
across:

- meetings
- minutes
- email
- Word
- PowerPoint
- PDF
- spreadsheets
- screenshots
- whiteboard photographs
- chat exports
- department-specific repositories

The risk chain is:

`missing evidence → incomplete retrieval → hallucinated requirement → wrong design → wrong task → wrong code → failed delivery`

## Learning-Journey Requirements

### REQ-LJ-001: Hands-On Learning by a Non-Technical Product Builder

The lab must remain understandable and executable by a product manager with
limited current coding knowledge.

The default interaction model for this persona should be OpenCode-first, with
deterministic scripts sitting behind approved tools and workflows rather than
becoming the normal day-to-day interface.

### REQ-LJ-002: Open-Source-First and Air-Gap-Ready Design

The majority of the architecture should use open-source or replaceable
components suitable for later enterprise deployment inside an air-gapped
environment.

### REQ-LJ-003: Reproducible Stepwise Experiments

Each bounded step should capture logs, document learning, stage safe files,
review changes, commit, push and confirm a clean tree.

### REQ-LJ-004: Evergreen Documentation

Maintain README, ADRs, checkpoints, reports, requirements, presentations,
version history and roadmap.

Major learning points should be captured in detailed repo-local Markdown so the
repository remains the durable handoff surface.

Major validated learning points should be appended to the canonical
`learnings/LEARNING_JOURNAL.md` unless a milestone clearly needs a separate
durable record.

### REQ-LJ-005: Safe Public Repository

The public repo must contain only synthetic or sanitised reviewed assets.

### REQ-LJ-006: Honest Limitation Tracking

Known gaps must be documented rather than hidden.

### REQ-LJ-007: Human Product Judgement Must Be Visible

The documentation must make clear that the journey was not produced by a
single prompt.

It was shaped iteratively by product-manager judgement, challenge and debate.


### REQ-LJ-008: Preserve Learning Attribution

Every major learning point, checkpoint and architecture decision should identify
whether it originated from:

- product-manager insight
- copilot recommendation
- experiment result
- known limitation
- human-approved decision

The repository should not read like a one-prompt artefact.

It should preserve the actual collaborative working model:

`product judgement → debate → experiment → evidence → decision → documented learning`


## Product Requirements

### REQ-PMCP-001: Governed Project Workspaces

Create project-specific evidence and approval boundaries.

### REQ-PMCP-002: Multi-Format Ingestion

Support DOCX, PPTX, XLSX, PDF, common images, TXT, Markdown, CSV and EML through
an explicit format router.

Outlook `.msg` remains deferred.

### REQ-PMCP-003: Immutable Evidence and Provenance

Preserve source-document ID, hash, file type, owner, department,
classification, version, approval status, superseded status and extraction
warnings.

### REQ-PMCP-004: Grounded Project Chat

Answers should distinguish verified evidence, approved scope, draft
interpretation, stale information, conflict, unsupported inference and
unresolved question.

### REQ-PMCP-005: Impact Analysis

New evidence should produce a proposed delta rather than silently rewriting
approved scope.

### REQ-PMCP-006: Controlled OpenSpec Handoff

Generate versioned proposal, specs, design and tasks before development.

### REQ-PMCP-007: Controlled Development-Agent Handoff

Development agents should receive bounded approved tasks linked to stories and
acceptance criteria.

### REQ-PMCP-008: Human Approval Gates

Agents may retrieve, classify, compare, draft and recommend.

Agents must not silently approve specification changes, weaken tests, override
controls or deploy.

### REQ-PMCP-009: Full Delivery Traceability

The system must preserve traceability across:

`source evidence → requirement → design decision → user story → acceptance criterion → task → code commit → automated test → release artefact → production incident`

### REQ-PMCP-010: Root-Cause Attribution

When a defect or incident is found during CI/CD, regression testing or
production use, the system should help classify whether the root cause is:

- implementation defect
- incorrect test
- missing requirement
- incorrect requirement
- ambiguous requirement
- design mismatch
- regression gap
- production-learning gap

### REQ-PMCP-011: Requirement-to-Incident Review

The Product Manager CoPilot should support investigation of whether a reported
bug was actually caused by:

- code violating an approved requirement
- software correctly implementing an approved but wrong requirement
- behaviour never raised as a requirement
- a later scope change not propagated into tasks and tests
- an incomplete acceptance criterion

### REQ-LJ-009: Offline Learning System

The repository must act as the primary offline learning reference.

A future reviewer should not need the original chat transcript to understand:

- the architecture
- terminology
- requirements
- completed experiments
- decisions
- limitations
- current position
- next action

Sanitised review bundles, detailed learning records and checkpoints should live
inside the repository as Git-safe Markdown artefacts.

Local raw logs, transcripts and detailed local extraction outputs remain
excluded from Git under local-only folders.

Another authorised user should be able to continue from the latest repo-local
checkpoint, review bundle and learning record without depending on private chat
history.

Humans and agents should resume from canonical repo-local files rather than from
the largest available collection of Markdown.

Documentation entropy must be controlled so stale or duplicate summaries do not
become retrieval noise or hallucination risk.

### REQ-PMCP-012: Regulator-Auditable Agent Runs

Every meaningful agent run must generate a traceability record containing:

- run ID
- project ID
- triggering identity
- timestamp
- agent and subagent names
- agent-definition hashes
- model identifier
- skills loaded
- tools invoked
- tool versions
- source hashes
- generated outputs
- warnings
- permissions
- approval state
- approver
- Git commit
- token usage where available

### REQ-PMCP-013: Append-Only Audit Evidence

A production implementation should store detailed audit evidence in an
append-only or immutable internal store with access control, retention policy
and tamper detection.

### REQ-PMCP-014: Separation of Duties

Agents must not approve their own:

- requirements
- task definitions
- test changes
- merge requests
- control overrides
- deployment decisions

### REQ-PMCP-015: Incident-to-Evidence Reconstruction

A reviewer must be able to reconstruct a production issue backwards from:

`incident → release → commit → task → acceptance criterion → story → requirement → evidence → approval`

### REQ-PMCP-016: Background Evidence Processing Jobs

The Product Manager CoPilot should process large evidence packs as background
jobs rather than requiring a human to approve every low-risk operation.

### REQ-PMCP-017: Progress, Countdown and ETA

The UI should show:

- files completed
- total files
- work units completed
- total work units
- current stage
- estimated time remaining
- confidence range
- exceptions
- next human approval gate

### REQ-PMCP-018: Capacity and Resource Metrics

Each processing run should capture:

- wall-clock duration
- queue time
- per-stage duration
- token usage
- model usage
- model cost where applicable
- CPU and memory use
- GPU utilisation where applicable
- peak VRAM
- GPU-hours
- throughput by file type

### REQ-PMCP-019: Policy-Driven Approval Profiles

The system should support permission profiles that allow low-risk approved
operations to run automatically while requiring human approval for material
changes, unapproved tools, OpenSpec proposals, implementation work and
deployment.

### REQ-PMCP-020: Exception-Based Human Review

Humans should be interrupted for exceptions and approval gates, not every safe
read or approved deterministic tool call.


## Current Position

Completed:

- environment setup
- public-repository local secret scan
- OpenCode and OpenSpec setup
- Docling toolkit
- synthetic multi-format benchmark
- first agent-orchestration skill

Next:

`agent-assisted ingestion-quality review → normalisation → conflict detection → first OpenSpec proposal`
