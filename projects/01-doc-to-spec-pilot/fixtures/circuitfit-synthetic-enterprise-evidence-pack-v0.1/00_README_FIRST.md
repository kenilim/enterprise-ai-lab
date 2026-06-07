# CircuitFit Synthetic Enterprise Evidence Pack v0.1

This pack is intentionally messy. It simulates a real enterprise collaboration environment.

## Purpose

Use the files to test:
- Docling multi-format extraction
- Office-format fallbacks
- embedded image extraction
- table handling
- source provenance
- stale-document detection
- conflict detection
- versioned OpenSpec change proposals

## Expected processing order

1. Ingest and hash every file locally.
2. Extract each document with Docling.
3. Use format-specific fallback extractors where required.
4. Build a source register.
5. Compare evidence against the canonical CircuitFit baseline.
6. Flag contradictions and unresolved questions.
7. Draft an OpenSpec change proposal.
8. Do not implement anything before human approval.

## Files

- 01_email_product_owner_priority_change.eml
- 02_email_engineering_storage_privacy.eml
- 03_founder_review_meeting_minutes.docx
- 04_workout_requirements_matrix.xlsx
- 05_mobile_wireframe_review.pptx
- 06_beta_user_feedback_summary.pdf
- 07_architecture_chat_export.txt
- 08_stale_feature_request_v0_8.docx
- 09_whiteboard_workflow_photo.png
- 10_mobile_webapp_screenshot_feedback.png
- 11_EXPECTED_CONFLICTS.md
- 12_EXPECTED_EXTRACTION_FEATURES.md
- 13_manifest.csv

## Important

All names, email addresses and content are synthetic.
