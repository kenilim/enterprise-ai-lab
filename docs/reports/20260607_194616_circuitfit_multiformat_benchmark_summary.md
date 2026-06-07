# CircuitFit Multi-Format Extraction Benchmark Summary

## Run

Timestamp:

`20260607_194616`

## Dataset

`circuitfit-synthetic-enterprise-evidence-pack-v0.1`

## Scope

This report contains sanitised benchmark metadata only.

It does not contain extracted document text, credentials or local workstation
paths.

## Summary

| Metric | Result |
|---|---:|
| Total files | 14 |
| Completed | 14 |
| Failed | 0 |
| Skipped | 0 |

## File-Level Results

| File | Extension | Processor | Status | Seconds | Text items | Table items | Picture items | Warning or error |
|---|---|---|---|---:|---:|---:|---:|---|
| 00_README_FIRST.md | .md | deterministic-text | completed | 0.001 | - | - | - | - |
| 01_email_product_owner_priority_change.eml | .eml | python-email-parser | completed | 0.001 | - | - | - | - |
| 02_email_engineering_storage_privacy.eml | .eml | python-email-parser | completed | 0.001 | - | - | - | - |
| 03_founder_review_meeting_minutes.docx | .docx | docling | completed | 0.14 | 18 | 1 | 1 | - |
| 04_workout_requirements_matrix.xlsx | .xlsx | docling | completed | 0.011 | 0 | 3 | 0 | - |
| 05_mobile_wireframe_review.pptx | .pptx | docling | completed | 0.034 | 8 | 1 | 1 | - |
| 06_beta_user_feedback_summary.pdf | .pdf | docling | completed | 15.348 | 19 | 1 | 1 | - |
| 07_architecture_chat_export.txt | .txt | deterministic-text | completed | 0.001 | - | - | - | - |
| 08_stale_feature_request_v0_8.docx | .docx | docling | completed | 0.013 | 11 | 0 | 0 | - |
| 09_whiteboard_workflow_photo.png | .png | docling | completed | 2.515 | 11 | 0 | 1 | - |
| 10_mobile_webapp_screenshot_feedback.png | .png | docling | completed | 2.2 | 12 | 0 | 2 | - |
| 11_EXPECTED_CONFLICTS.md | .md | deterministic-text | completed | 0.001 | - | - | - | - |
| 12_EXPECTED_EXTRACTION_FEATURES.md | .md | deterministic-text | completed | 0.001 | - | - | - | - |
| 13_manifest.csv | .csv | deterministic-csv | completed | 0.001 | - | - | - | - |

## Current Interpretation Rule

A successful conversion does not prove extraction quality.

The next step must inspect:

- heading order
- table structure
- embedded-image detection
- workbook semantics
- slide structure
- PDF layout
- image OCR behaviour
- email metadata
- stale-document classification
- conflicting evidence

## Known Limitation

Outlook `.msg` ingestion remains deferred.

Possible later evaluation candidate:

`extract-msg`

## Next Planned Action

Run format-specific quality audits and identify where supplementary extractors
are required before normalisation and OpenSpec generation.
