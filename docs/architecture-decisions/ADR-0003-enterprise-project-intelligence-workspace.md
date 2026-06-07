# ADR-0003: Enterprise Project Intelligence Workspace

## Status

Accepted as the target product vision for the lab

## Problem

Large enterprise programmes generate information across many channels:

- meetings
- minutes
- emails
- PowerPoint decks
- Word documents
- PDFs
- spreadsheets
- screenshots
- whiteboard photographs
- chat exports
- department-specific repositories
- duplicated and conflicting versions

The volume of information creates a practical knowledge-management problem.

A language model cannot be treated as the system of record. When relevant
evidence is missing, poorly indexed or not retrieved, the model may generate
plausible but unsupported requirements, specifications or implementation
decisions.

Incorrect retrieval can therefore create a chain of failure:

`missing evidence → hallucinated requirement → wrong design → wrong task → wrong code → failed delivery`

## Decision

Build an internal project-oriented intelligence workspace with a chat-style web
interface.

The interface should feel familiar to users of modern chat applications while
operating as a governed evidence, specification and delivery-control system.

## User Experience

A product manager should be able to:

1. create a project
2. upload unstructured files into that project
3. ask questions within the project
4. inspect the source evidence behind an answer
5. generate requirements, user stories, design documents, tasks and test plans
6. review contradictions and unresolved questions
7. upload new documents later
8. receive an impact-analysis proposal showing what changed
9. approve or reject proposed revisions
10. hand approved incremental tasks to development agents

## Evidence Rule

The language model is not the database.

Every uploaded file should remain immutable and receive:

- project ID
- source-document ID
- hash
- filename
- file type
- upload timestamp
- source owner
- department
- classification
- document version
- approval state
- superseded state
- extraction status
- extraction warnings
- source-reference metadata

## Grounding Rule

Generated answers should distinguish:

- verified evidence
- approved specification
- draft interpretation
- conflicting information
- stale or superseded information
- unsupported inference
- unresolved question

When evidence is insufficient, the system should say so rather than invent an
answer.

## Change-Control Rule

New evidence must not silently rewrite approved requirements.

The intended flow is:

`new evidence → local ingestion → impact analysis → proposed OpenSpec change → Git diff → human review → approval or rejection → new version`

## Development-Handoff Rule

Development agents should receive bounded incremental tasks linked to approved
requirements and user stories.

The traceability spine is:

`source evidence → requirement → user story → acceptance criterion → task → code commit → automated test → release`

## Enterprise Architecture Principle

The preferred enterprise implementation is modular and open-source-first.

The personal lab may use proprietary OpenAI models temporarily for coding
acceleration, but the air-gapped enterprise design must retain a replacement
path through approved local models and an internal model gateway.
