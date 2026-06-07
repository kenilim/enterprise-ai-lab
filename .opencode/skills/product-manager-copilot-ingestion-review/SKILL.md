---
name: product-manager-copilot-ingestion-review
description: Run and review the Product Manager CoPilot multi-format evidence-ingestion benchmark. Use deterministic local extraction tools first, classify quality gaps, create safe reports, and stop for human approval before committing changes.
---

# Product Manager CoPilot Ingestion Review

## Purpose

Review a project evidence pack using tested local extraction tools.

This is a bounded specialist skill for ingestion-quality review only.

Do not improvise document parsing when a deterministic script already exists.

Do not implement application code.

Do not generate an OpenSpec proposal yet.

Stop for human approval before committing or pushing anything.

Do not take ownership of resumable workflow routing, evidence normalisation,
conflict review or OpenSpec generation.

## Inputs

Default synthetic benchmark working copy:

`projects/01-doc-to-spec-pilot/input/generated-synthetic-evidence/circuitfit-synthetic-enterprise-evidence-pack-v0.1`

Reusable router:

`shared/scripts/extract-multiformat-evidence-pack.py`

Dedicated ingestion virtual environment:

`projects/01-doc-to-spec-pilot/.venv`

## Operating Rules

1. Preserve raw evidence.
2. Do not modify source fixtures.
3. Keep extracted content local-only.
4. Store local extraction outputs under:
   `projects/01-doc-to-spec-pilot/work/extracted`
5. Store local detailed reports under:
   `projects/01-doc-to-spec-pilot/output/reports`
6. Create only sanitised public summaries under:
   `docs/reports`
7. Preserve source hashes and processor names.
8. Never include credentials, workstation paths or extracted sensitive text in a public summary.
9. Treat conversion success and extraction quality as separate checks.
10. Stop for human review before running Git commit or Git push.

## Format Routing

| Input | Primary route | Supplementary review |
|---|---|---|
| DOCX | Docling | python-docx |
| PPTX | Docling | python-pptx |
| XLSX | Docling | openpyxl and pandas |
| PDF | Docling | rendered-page review |
| PNG and image formats | Docling | OCR and later local-VLM review |
| EML | Python standard-library email parser | attachment recursion later |
| TXT and Markdown | deterministic text extraction | none |
| CSV | deterministic CSV extraction | pandas if required |
| Outlook MSG | deferred | evaluate extract-msg later |

## Review Classification

For each processed file, classify:

- `pass`
- `pass-with-caveats`
- `fail`
- `deferred`

## Required Review Checks

Inspect:

- extraction status
- processing time
- headings
- text items
- table items
- picture items
- embedded-image detection
- workbook sheet structure
- PowerPoint slide structure
- PDF reading order
- image OCR behaviour
- email metadata
- warnings
- fallback-extractor requirements

## Required Output

Create a sanitised Markdown review report under:

`docs/reports`

The report must contain:

- run timestamp
- dataset name
- format coverage
- quality classification per file
- known limitations
- fallback extractors required
- next recommended action
- explicit statement that OpenSpec generation has not started

## Human Approval Gate

Before committing:

1. show the generated safe report
2. show `git status --short`
3. show `git diff --cached --name-status` if files were staged
4. ask the human reviewer whether to commit and push

Do not commit or push without explicit human approval.
