# Product Manager CoPilot Lab Rules

## Purpose

This repository is a hands-on enterprise agentic-development lab.

The north-star product is:

`Product Manager CoPilot`

It helps product managers turn fragmented enterprise evidence into grounded,
versioned and reviewable delivery artefacts before development agents write code.

## Human Role

This lab is driven by a non-technical product builder with basic and dated
coding knowledge.

The product builder owns:

- problem framing
- requirements
- product judgement
- prioritisation
- challenge and debate
- human approval gates
- acceptance of architecture decisions

Agents support research, extraction, analysis, drafting and implementation.

Agents must not silently approve their own work.

## Security Boundary

This public repository may contain only:

- synthetic fixtures
- sanitised documentation
- reviewed scripts
- reviewed agent definitions
- architecture decision records
- safe summaries
- offline presentations

Never commit:

- credentials
- OAuth files
- API keys
- tokens
- `.env` files
- private keys
- confidential workplace data
- raw local evidence unless explicitly synthetic and reviewed
- detailed local extraction output
- raw agent transcripts
- local runtime logs

## Local-Only Folders

Treat these as local-only unless a human explicitly approves a sanitised export:

- `projects/**/input/generated-synthetic-evidence/`
- `projects/**/input/canonical-source-pack/raw/`
- `projects/**/work/`
- `projects/**/output/`
- `logs/`
- `.venv/`

## Current Learning Phase

Current phase:

`agent-assisted ingestion-quality review`

Do not generate application code yet.

Do not generate an OpenSpec proposal until the extraction-quality review is
completed and a human explicitly approves moving forward.

## Operating Model

Use:

- deterministic tools for hashing, routing, parsing, validation and logging
- agents for interpretation, classification, conflict analysis and drafting
- OpenSpec for versioned product-change proposals
- OpenCode development agents only after human-approved OpenSpec tasks exist

## Required Human Approval Gates

Stop and request human approval before:

- committing
- pushing
- creating or changing OpenSpec artefacts
- modifying approved requirements
- generating development tasks
- changing test expectations
- implementing application code
- deploying anything
- exposing local evidence in public documentation

## Traceability Standard

Every meaningful workflow run must preserve:

`source evidence → requirement → design decision → user story → acceptance criterion → task → code commit → automated test → release artefact → production incident`

For each agent run, record:

- run ID
- timestamp
- project ID
- triggering user
- agent name
- agent mode
- model identifier
- model configuration where available
- skills loaded
- tools invoked
- source-file hashes
- generated outputs
- warnings
- human approval state
- Git commit hash after approval
- token usage where available

## Documentation Rule

Every meaningful learning point should record one or more origins:

- `Product-manager insight`
- `Copilot recommendation`
- `Experiment result`
- `Known limitation`
- `Decision`

## Approved Ingestion Tools

- `shared/scripts/generate-source-manifest.py`
- `shared/scripts/extract-docling-document.py`
- `shared/scripts/audit-docling-docx-extraction.py`
- `shared/scripts/extract-multiformat-evidence-pack.py`
- `shared/scripts/capture-opencode-usage.sh`
- `shared/scripts/new-log-path.sh`

## Known Limitations

- Docling is not a universal parser.
- `.eml` uses a deterministic local parser.
- Outlook `.msg` ingestion is deferred.
- `extract-msg` is a later evaluation candidate.
- Recursive email-attachment ingestion is future work.
- OpenCode-to-local-Ollama adapter behaviour requires further validation.

## Repository Orientation

Read these files before making material changes:

- `README.md`
- `docs/requirements/product-manager-copilot-learning-journey-requirements.md`
- `docs/guides/opencode-agent-skill-tool-orchestrator-primer.md`
- `docs/governance/regulator-auditable-agent-traceability.md`
- relevant ADRs under `docs/architecture-decisions/`
