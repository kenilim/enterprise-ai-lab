# Product Manager CoPilot — Learning Journey and Product Requirements

## Document Purpose

This document records the requirements provided by the product manager for the
Enterprise AI Development Lab.

The lab is intentionally being built hands-on by a non-technical product person
with basic and dated coding knowledge, using an AI copilot to research,
understand, test and document the end-to-end workflow.

The goal is not to claim that software engineering expertise is unnecessary.

The goal is to test a more practical question:

> Can a product builder with a clearly defined problem, disciplined
> requirements and the right copilot independently learn enough to prototype,
> evaluate and explain an enterprise-grade agentic development workflow?

## Product North Star

The north-star product is called:

`Product Manager CoPilot`

It is an internal project workspace with a ChatGPT-style interface for product
teams working on complex enterprise programmes.

The Product Manager CoPilot should help product managers:

1. create a governed project workspace
2. upload fragmented and unstructured project evidence
3. ask grounded questions within that project
4. inspect the sources behind answers
5. detect missing, stale, duplicated and conflicting information
6. generate draft requirements, design documents, user stories, tasks and test
   plans
7. upload new evidence later
8. understand the impact of that new evidence
9. review a versioned change proposal
10. approve or reject revisions before development work begins
11. hand approved bounded tasks to development agents
12. trace implementation and tests back to source evidence

## Why This Problem Matters

Large enterprise products and programmes generate knowledge through:

- meetings
- minutes
- emails
- Word documents
- PowerPoint decks
- PDFs
- spreadsheets
- screenshots
- images
- photographs of whiteboards
- chat exports
- department-specific repositories
- duplicate and contradictory versions

The problem is not merely file storage.

The problem is retrieving the correct, current and authorised evidence before a
decision is made.

The risk chain is:

`missing evidence → incomplete retrieval → hallucinated requirement → wrong design → wrong task → wrong code → failed delivery`

## Learning-Journey Requirements

### REQ-LJ-001: Hands-On Learning by a Non-Technical Product Builder

The lab must be executable by a product manager with limited current coding
knowledge.

The documentation should explain:

- what each component does
- why it is required
- what was installed
- what worked
- what failed
- what remains unresolved
- what the next step is

### REQ-LJ-002: Open-Source-First and Air-Gap-Ready Design

The majority of the architecture should use open-source or replaceable
components so the workflow can later be adapted for an air-gapped enterprise
environment.

OpenAI models may be used in the personal lab as a development accelerator, but
the target enterprise architecture must preserve a replacement path through
approved local models and an internal model gateway.

### REQ-LJ-003: Reproducible, Stepwise Experiments

Each meaningful step should:

1. run one bounded experiment
2. capture logs
3. document the learning
4. stage only safe files
5. review Git changes
6. commit
7. push
8. confirm a clean working tree

### REQ-LJ-004: Evergreen Documentation

The lab must maintain:

- a root README for quick orientation
- a detailed evergreen learning report
- immutable checkpoint snapshots
- architecture decision records
- an offline HTML presentation
- version history
- a directory guide
- a current roadmap

### REQ-LJ-005: Safe Public Repository

The public repository must contain only:

- synthetic fixtures
- sanitised documentation
- reviewed scripts
- architecture decisions
- presentations
- safe checkpoints

It must not contain:

- credentials
- tokens
- private keys
- OAuth files
- `.env` files
- confidential workplace data
- raw local evidence unless explicitly synthetic and reviewed
- local extraction outputs unless explicitly sanitised

### REQ-LJ-006: Track Known Limitations Honestly

Known gaps must be visible in the README, learning report and presentation.

Example:

- Docling does not cover every enterprise format
- `.eml` requires a dedicated email parser
- Outlook `.msg` ingestion is deferred
- `extract-msg` is a possible later evaluation candidate
- attachment recursion and nested-thread reconstruction remain future work

## Product Requirements

### REQ-PMCP-001: Project Workspaces

A user should be able to create a project and keep its evidence, specifications,
conversations and approvals within a controlled workspace boundary.

### REQ-PMCP-002: Multi-Format Local Ingestion

The system should ingest:

- DOCX
- PPTX
- XLSX
- PDF
- common image formats
- TXT
- Markdown
- CSV
- EML through a separate email parser

Outlook `.msg` is deferred for later evaluation.

### REQ-PMCP-003: Immutable Evidence and Provenance

Every uploaded file should preserve:

- project ID
- source-document ID
- filename
- file type
- hash
- upload timestamp
- owner
- department
- classification
- version
- approval status
- superseded status
- extraction status
- extraction warnings
- source-reference metadata

### REQ-PMCP-004: Grounded Project Chat

Answers should distinguish:

- verified evidence
- approved specification
- draft interpretation
- conflicting information
- stale or superseded information
- unsupported inference
- unresolved question

When evidence is insufficient, the system should say so.

### REQ-PMCP-005: Impact Analysis

When new evidence arrives, the system should:

1. ingest it
2. detect new facts
3. detect conflicts
4. identify affected requirements
5. identify affected stories, tasks and tests
6. draft a versioned change proposal
7. show a human-readable diff
8. require human approval

### REQ-PMCP-006: Controlled OpenSpec Handoff

The Product Manager CoPilot should generate a controlled OpenSpec proposal:

`proposal → specs → design → tasks`

The proposal must be reviewed before implementation.

### REQ-PMCP-007: Controlled Development-Agent Handoff

Development agents should receive only approved bounded tasks linked to:

`source evidence → requirement → story → acceptance criterion → task → code commit → automated test → release`

### REQ-PMCP-008: Human Approval Gates

Agents may:

- retrieve
- summarise
- compare
- classify
- draft
- recommend

Agents must not silently:

- approve their own specification changes
- weaken tests
- rewrite release criteria
- deploy changes
- override access controls

## Current Lab Position

Completed:

- WSL2 Ubuntu workspace
- Docker integration
- private then public GitHub repository workflow
- local Ollama direct inference
- OpenAI GPT-5.4 OpenCode development route
- OpenSpec core workflow installation
- Docling CPU-only toolkit installation
- native DOCX smoke test
- multi-format synthetic evidence pack
- multi-format ingestion router
- public-repository local secret scan

Next:

`run multi-format extraction benchmark → inspect output quality → normalise evidence → detect conflicts → generate first OpenSpec proposal`
