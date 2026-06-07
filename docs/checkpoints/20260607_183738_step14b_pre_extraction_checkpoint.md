# Checkpoint: Step 14B

## Status

Pre-extraction baseline complete.

## Current Lab Objective

Test an open-source-first, air-gap-ready workflow for converting fragmented
enterprise information into grounded, versioned and reviewable product
specifications before development agents write code.

## Completed Foundation

- Windows PC development environment
- WSL2 Ubuntu workspace
- VS Code WSL integration
- Docker integration
- Git and private GitHub backup
- Timestamped logs
- OpenCode
- Local Windows Ollama route exposed to WSL
- OpenAI GPT-5.4 personal-lab coding route
- OpenSpec core workflow
- Local CircuitFit canonical-source manifest
- Dedicated Docling ingestion virtual environment
- CPU-only document-ingestion baseline

## Current Hybrid Personal-Lab Pipeline

`raw evidence → local immutable storage → SHA-256 manifest → Docling and format-specific extractors → local model drafting → human approval → OpenSpec → OpenCode with OpenAI GPT-5.4 → tests → Docker`

## Air-Gapped Enterprise Replacement Path

`raw evidence → internal immutable object store → local ingestion workers → hybrid retrieval with ACL filters → internal model gateway → approved local models → versioned OpenSpec change proposals → human approval → internal coding agent → deterministic CI/CD`

## Installed Ingestion Packages

| Package | Version |
|---|---:|
| docling | 2.97.0 |
| python-docx | 1.2.0 |
| python-pptx | 1.0.2 |
| openpyxl | 3.1.5 |
| pandas | 3.0.3 |
| pillow | 12.2.0 |
| torch | 2.12.0+cpu |

## Important Learning Points

- The language model must not become the source of truth.
- Retrieval and provenance are separate enterprise controls.
- New evidence should produce proposed deltas, not silent rewrites.
- Requirements, user stories, tasks, tests and releases require traceability.
- Start with deterministic local scripts before adding autonomous agents.
- Validate local parsing on CPU before optimising GPU execution.

## Next Experiment

Convert:

`CircuitFit MVP stress test and spec pack.docx`

into:

- Markdown
- lossless JSON
- extraction metadata
- timing metrics

No additional format should be processed until the first DOCX output has been
reviewed.
