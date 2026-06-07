# 01-doc-to-spec-pilot

## Purpose

This pilot tests how Product Manager CoPilot can ingest fragmented enterprise
evidence and convert it into grounded, reviewable inputs before OpenSpec
generation begins.

## Current Learning Phase

```text
multi-format extraction completed
→ first agent-assisted ingestion review completed
→ quality gaps identified
→ extraction-quality remediation next
```

Do **not** generate OpenSpec artefacts yet.

## Current Benchmark

The CircuitFit synthetic enterprise evidence pack contains:

- Markdown
- TXT
- CSV
- EML
- DOCX
- XLSX
- PPTX
- PDF
- PNG screenshots
- PNG whiteboard-style image

## Current Quality Gaps

- XLSX needs workbook-aware fallback inspection
- PPTX needs slide-aware fallback inspection
- PDF reading order needs explicit validation
- screenshot OCR is noisy
- whiteboard PNG failed the current quality gate
- Outlook `.msg` remains deferred

## Folder Guide

```text
projects/01-doc-to-spec-pilot/
├── config/
├── fixtures/
├── input/
├── manifests/
├── output/
├── specs/
├── src/
├── tests/
└── work/
```

## Data Boundary

Public Git contains only reviewed synthetic fixtures and sanitised summaries.

Local raw evidence, extraction output and detailed logs remain outside Git.
