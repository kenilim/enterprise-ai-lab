# Background Processing, Progress Estimation and Capacity Planning

## Purpose

This guide records the product learning from the first interactive OpenCode
ingestion-review run.

The interactive review was useful, but the enterprise Product Manager CoPilot
must support long-running background jobs.

## Why Background Jobs Matter

Enterprise evidence packs can contain:

- thousands of files
- large PDFs
- OCR-heavy scanned documents
- PowerPoint decks with images
- Excel workbooks with many sheets
- email threads with attachments
- duplicated and stale versions
- documents across multiple departments

A product manager should not wait in a terminal approving each low-risk action.

## Target UX

The Product Manager CoPilot web UI should show:

```text
Project: CircuitFit MVP
Status: Processing evidence
Files: 138 / 1,240
Work units: 8,930 / 54,100
Current stage: OCR and table extraction
Estimated remaining: 6h 20m to 8h 10m
Confidence: medium
Exceptions: 7
Next human gate: Requirement-impact review
```

## Workload Estimation

Do not estimate only by file count.

Use weighted work units:

| File type | Signals |
|---|---|
| TXT/MD/CSV | bytes, rows, columns |
| DOCX | paragraphs, tables, images |
| PPTX | slides, shapes, tables, images |
| XLSX | sheets, cells, formulas, tables |
| PDF | pages, scanned/OCR requirement, image density |
| Images | resolution, OCR density |
| Email | attachments, nested messages, thread length |

## Metrics to Capture

### Commercial Tokenomics

- input tokens
- output tokens
- cache read tokens
- cache write tokens
- model used
- cost where available

### Runtime Economics

- wall-clock duration
- queue wait time
- per-stage duration
- throughput by file type
- retry count
- failure count

### Local Infrastructure

- CPU usage
- memory usage
- disk IO
- OCR model time
- GPU utilisation
- GPU memory peak
- GPU-hours
- power draw where available

## GPU Monitoring

For an enterprise GPU environment, use platform telemetry rather than manual
inspection.

For NVIDIA GPU clusters, DCGM Exporter exposes GPU metrics for Prometheus and
can feed Grafana dashboards.

## Permission Strategy

Use permission profiles:

| Profile | Allowed automatically | Requires approval |
|---|---|---|
| Read-only | read files and metadata | external access |
| Ingestion | approved extraction tools | unapproved tool or write path |
| Spec proposal | draft OpenSpec artefacts | mark approved |
| Development | bounded task implementation | tests weakened or scope changed |
| Release | none by default | deployment approval |

## Product Rule

The system should optimise for:

```text
background processing
→ visible progress
→ exception-based human review
→ auditable checkpoints
```

not:

```text
constant human approvals for every safe operation
```
