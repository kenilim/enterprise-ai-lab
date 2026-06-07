# Document-to-Spec Pilot Inputs

## Purpose

This folder separates local working evidence from reviewed synthetic fixtures.

## Folder Rules

```text
input/
├── canonical-source-pack/
│   └── raw/
├── generated-synthetic-evidence/
├── inbox/
├── processed/
└── rejected/
```

## Git Safety Rules

Treat these as local-only unless explicitly sanitised and approved:

- `canonical-source-pack/raw/`
- `generated-synthetic-evidence/`
- `inbox/`
- extracted outputs
- local reports
- runtime logs

Reviewed synthetic fixtures intended for public Git live under:

```text
projects/01-doc-to-spec-pilot/fixtures/
```

## Current Benchmark

The working benchmark is the CircuitFit multi-format synthetic evidence pack.

It exists to test realistic enterprise ingestion rather than clean Markdown-only
inputs.

## Known Limitations

- Outlook `.msg` ingestion is deferred
- recursive attachment ingestion remains future work
- OCR quality needs explicit review
