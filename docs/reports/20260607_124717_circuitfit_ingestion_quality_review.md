# CircuitFit ingestion quality review

- Run timestamp (UTC): 2026-06-07T12:47:17+00:00
- Dataset: `circuitfit-synthetic-enterprise-evidence-pack-v0.1`
- Deterministic extraction run reviewed: `20260607_204303_circuitfit_multiformat`
- Scope: extraction-quality review only
- OpenSpec generation: not started

## Summary

Processed files: 14  
Extraction failures: 0  
Quality classifications: 9 pass, 4 pass-with-caveats, 1 fail, 0 deferred

Successful conversion did not always equal review-quality extraction. The main risk areas were workbook structure, slide segmentation, PDF reading-order confidence, and image OCR quality.

## File-by-file classification

| File | Format | Classification | Review outcome |
|---|---|---|---|
| 00_README_FIRST.md | MD | pass | Plain-text extraction looked complete. |
| 01_email_product_owner_priority_change.eml | EML | pass | Metadata and body preserved. |
| 02_email_engineering_storage_privacy.eml | EML | pass | Metadata, CC field and body preserved. |
| 03_founder_review_meeting_minutes.docx | DOCX | pass | Headings, text, action table and embedded-image detection all present. |
| 04_workout_requirements_matrix.xlsx | XLSX | pass-with-caveats | Tables extracted, but worksheet structure was not clear without supplementary workbook inspection. |
| 05_mobile_wireframe_review.pptx | PPTX | pass-with-caveats | Text, table and picture detected, but slide boundaries were weak in markdown output. |
| 06_beta_user_feedback_summary.pdf | PDF | pass-with-caveats | Paragraphs, table and screenshot marker present; reading-order confidence remains limited. |
| 07_architecture_chat_export.txt | TXT | pass | Plain-text extraction looked complete. |
| 08_stale_feature_request_v0_8.docx | DOCX | pass | Superseded-draft warning and stale requirement list preserved. |
| 09_whiteboard_workflow_photo.png | PNG | fail | Whiteboard OCR was not reliably surfaced in primary markdown output. |
| 10_mobile_webapp_screenshot_feedback.png | PNG | pass-with-caveats | OCR found key UI labels, but text merging reduced reliability. |
| 11_EXPECTED_CONFLICTS.md | MD | pass | Plain-text extraction looked complete. |
| 12_EXPECTED_EXTRACTION_FEATURES.md | MD | pass | Plain-text extraction looked complete. |
| 13_manifest.csv | CSV | pass | Structured rows parsed as expected. |

## Required checks

| Check | Assessment |
|---|---|
| Headings | Good on reviewed DOCX/PDF samples. |
| Text items | Strong on text-first formats; mixed on image OCR. |
| Table items | Present on DOCX, XLSX, PPTX, PDF and CSV samples. |
| Picture items / embedded-image detection | Detected on DOCX, PPTX, PDF and PNG samples. |
| Workbook sheet structure | Needs supplementary workbook-aware extraction to preserve sheet boundaries reliably. |
| Slide structure | Needs supplementary slide-aware extraction to preserve slide boundaries reliably. |
| PDF reading order | Acceptable on this simple sample, but confidence is limited without rendered-page validation. |
| PNG OCR behaviour | Weakest area; screenshot OCR was noisy and whiteboard OCR was not usable in primary markdown. |
| Email metadata | Good on both `.eml` samples. |
| Warnings / uncertainty | Must remain visible for image-heavy and layout-heavy files. |

## Fallback extractors

### Required

- `04_workout_requirements_matrix.xlsx`: workbook-aware fallback such as `openpyxl` for sheet structure.
- `05_mobile_wireframe_review.pptx`: slide-aware fallback such as `python-pptx` for reliable slide segmentation.
- `09_whiteboard_workflow_photo.png`: specialist OCR fallback for whiteboard-style images.

### Recommended

- `06_beta_user_feedback_summary.pdf`: rendered-page PDF validation for stronger reading-order assurance.
- `10_mobile_webapp_screenshot_feedback.png`: specialist OCR fallback for screenshot text quality.

## Known limitations and uncertainties

- Docling success status overstated quality for some non-text-first files.
- The DOCX extraction reviewed here did not expose useful page provenance in JSON.
- The PDF sample appeared coherent, but this review could not independently validate reading order with a separate local PDF parser.
- Outlook `.msg` remains deferred outside this benchmark.

## Recommended next action

1. Keep current deterministic outputs for audit.
2. Add sheet-aware and slide-aware supplementary extraction to normal review flow.
3. Treat whiteboard-style PNGs as requiring specialist OCR before downstream requirement synthesis.
4. Re-run image-heavy review after fallback OCR is available.

This report is sanitised and excludes raw extracted evidence text and workstation paths.
