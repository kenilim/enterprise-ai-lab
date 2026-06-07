#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from openpyxl import load_workbook
except Exception:  # pragma: no cover
    load_workbook = None  # type: ignore

try:
    from pptx import Presentation
except Exception:  # pragma: no cover
    Presentation = None  # type: ignore


LAB_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ID = "01-doc-to-spec-pilot"
PROJECT_DIR = LAB_ROOT / "projects" / PROJECT_ID
DOC_TO_SPEC_VENV_PYTHON = PROJECT_DIR / ".venv" / "bin" / "python"
DEFAULT_FIXTURE_DIR = PROJECT_DIR / "fixtures" / "circuitfit-synthetic-enterprise-evidence-pack-v0.1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_slug(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in value)


def format_classification(path: Path) -> str:
    ext = path.suffix.lower()
    mapping = {
        ".md": "text",
        ".txt": "text",
        ".csv": "csv",
        ".eml": "email",
        ".docx": "docx",
        ".xlsx": "xlsx",
        ".pptx": "pptx",
        ".pdf": "pdf",
        ".png": "image",
        ".jpg": "image",
        ".jpeg": "image",
    }
    return mapping.get(ext, "unsupported")


def estimate_file_work_units(path: Path) -> dict[str, Any]:
    ext = path.suffix.lower()
    estimate: dict[str, Any] = {
        "file": path.name,
        "format": ext,
        "files": 1,
        "pages": 0,
        "slides": 0,
        "sheets": 0,
        "images": 0,
        "ocr_needed": False,
        "weighted_units": 1,
    }

    if ext == ".xlsx" and load_workbook is not None:
        workbook = load_workbook(path, read_only=True, data_only=True)
        estimate["sheets"] = len(workbook.sheetnames)
        estimate["weighted_units"] = max(2, len(workbook.sheetnames) * 2)
    elif ext == ".pptx" and Presentation is not None:
        deck = Presentation(path)
        estimate["slides"] = len(deck.slides)
        image_count = 0
        for slide in deck.slides:
            for shape in slide.shapes:
                if getattr(shape, "shape_type", None) == 13:
                    image_count += 1
        estimate["images"] = image_count
        estimate["weighted_units"] = max(2, len(deck.slides) * 2 + image_count)
    elif ext == ".pdf":
        estimate["ocr_needed"] = True
        estimate["weighted_units"] = 6
    elif ext in {".png", ".jpg", ".jpeg"}:
        estimate["images"] = 1
        estimate["ocr_needed"] = True
        estimate["weighted_units"] = 4
    elif ext == ".docx":
        estimate["weighted_units"] = 2
    elif ext == ".eml":
        estimate["weighted_units"] = 1
    return estimate


def stage_record(name: str, status: str, started: float, **extra: Any) -> dict[str, Any]:
    record = {
        "stage": name,
        "status": status,
        "completed_utc": utc_now(),
        "duration_seconds": round(time.perf_counter() - started, 3),
    }
    record.update(extra)
    return record


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the first OpenCode-native pre-normalisation Product Manager CoPilot pipeline."
    )
    parser.add_argument(
        "project",
        choices=["circuitfit"],
        help="Synthetic pilot project to process.",
    )
    parser.add_argument(
        "--input-dir",
        default=str(DEFAULT_FIXTURE_DIR),
        help="Evidence-pack directory to process.",
    )
    parser.add_argument(
        "--output-dir",
        help="Optional local-only output directory. Defaults to logs/step16/<run-id>/",
    )
    args = parser.parse_args()

    if not DOC_TO_SPEC_VENV_PYTHON.is_file():
        raise FileNotFoundError(f"Docling environment python not found: {DOC_TO_SPEC_VENV_PYTHON}")

    input_dir = Path(args.input_dir).resolve()
    if not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    run_id = f"pmcp-{args.project}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    output_dir = Path(args.output_dir).resolve() if args.output_dir else LAB_ROOT / "logs" / "step16" / safe_slug(run_id)
    output_dir.mkdir(parents=True, exist_ok=True)
    extraction_dir = output_dir / "extracted"
    extraction_report_json = output_dir / "extraction_report.json"
    audit_dir = output_dir / "audit_results"
    manifest_path = output_dir / "pipeline_manifest.json"

    manifest: dict[str, Any] = {
        "run_id": run_id,
        "project_id": PROJECT_ID,
        "project_slug": args.project,
        "triggered_at_utc": utc_now(),
        "git_commit": subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=LAB_ROOT, text=True).strip(),
        "agent_name": "product-manager-copilot",
        "skill_name": "product-manager-copilot-doc-to-spec",
        "model_identifier": "openai/gpt-5.4",
        "input_directory": str(input_dir),
        "local_output_directory": str(output_dir),
        "stages": [],
        "files": [],
        "warnings": [],
        "blocked_evidence": [],
        "deferred_formats": [".msg"],
        "reviewer_attention_items": [],
        "pipeline_state": "running",
        "resume_stage": None,
    }

    files = sorted(path for path in input_dir.iterdir() if path.is_file() and path.name != ".gitkeep")

    preflight_started = time.perf_counter()
    work_units = [estimate_file_work_units(path) for path in files]
    files_summary = []
    for path, estimate in zip(files, work_units):
        files_summary.append(
            {
                "filename": path.name,
                "extension": path.suffix.lower(),
                "classification": format_classification(path),
                "source_sha256": sha256(path),
                "size_bytes": path.stat().st_size,
                "work_unit_estimate": estimate,
            }
        )
    manifest["files"] = files_summary
    manifest["format_counts"] = dict(Counter(item["classification"] for item in files_summary))
    manifest["work_unit_estimate"] = {
        key: sum(item[key] for item in work_units)
        for key in ["files", "pages", "slides", "sheets", "images", "weighted_units"]
    }
    manifest["work_unit_estimate"]["ocr_needed_files"] = sum(1 for item in work_units if item["ocr_needed"])
    manifest["stages"].append(stage_record("preflight", "completed", preflight_started))

    extraction_started = time.perf_counter()
    subprocess.run(
        [
            str(DOC_TO_SPEC_VENV_PYTHON),
            str(LAB_ROOT / "shared" / "scripts" / "extract-multiformat-evidence-pack.py"),
            "--input-dir",
            str(input_dir),
            "--output-dir",
            str(extraction_dir),
            "--report-json",
            str(extraction_report_json),
        ],
        cwd=LAB_ROOT,
        check=True,
    )
    extraction_report = json.loads(extraction_report_json.read_text(encoding="utf-8"))
    manifest["extraction_report_json"] = str(extraction_report_json)
    manifest["stages"].append(
        stage_record(
            "extraction",
            "completed",
            extraction_started,
            files_completed=extraction_report.get("completed_count"),
            files_failed=extraction_report.get("failed_count"),
        )
    )

    extraction_results_by_file = {item["source_filename"]: item for item in extraction_report.get("results", [])}

    audit_started = time.perf_counter()
    audit_results: dict[str, Any] = {}
    for filename, fmt in [
        ("04_workout_requirements_matrix.xlsx", "xlsx"),
        ("05_mobile_wireframe_review.pptx", "pptx"),
        ("06_beta_user_feedback_summary.pdf", "pdf"),
    ]:
        source = input_dir / filename
        audit_output = audit_dir / f"{safe_slug(source.stem)}.{fmt}.audit.json"
        command = [
            sys.executable,
            str(LAB_ROOT / "shared" / "scripts" / "audit-multiformat-extraction-quality.py"),
            "--source",
            str(source),
            "--format",
            fmt,
            "--output-json",
            str(audit_output),
        ]
        if fmt == "pdf":
            docling_json = extraction_results_by_file[filename]["output_json"]
            command.extend(["--docling-json", str(docling_json)])
        subprocess.run(command, cwd=LAB_ROOT, check=True)
        audit_results[filename] = json.loads(audit_output.read_text(encoding="utf-8"))

    manifest["audit_results"] = audit_results
    manifest["stages"].append(stage_record("quality_audit", "completed", audit_started))

    image_started = time.perf_counter()
    image_decisions = {
        "10_mobile_webapp_screenshot_feedback.png": {
            "disposition": "bounded_human_review",
            "normalisation_eligibility": "eligible_with_review",
            "human_review_requirement": "Confirm the exact screenshot-derived labels or statements used in the first normalisation pass.",
        },
        "09_whiteboard_workflow_photo.png": {
            "disposition": "blocked",
            "normalisation_eligibility": "blocked",
            "human_review_requirement": "Do not use whiteboard-derived assertions in the first OpenSpec experiment.",
        },
        ".msg": {
            "disposition": "deferred",
            "normalisation_eligibility": "deferred",
            "human_review_requirement": "Maintain explicit deferred route only; do not ingest silently.",
        },
    }
    manifest["image_and_deferred_decisions"] = image_decisions
    manifest["blocked_evidence"].append("09_whiteboard_workflow_photo.png")
    manifest["reviewer_attention_items"].append(
        "10_mobile_webapp_screenshot_feedback.png requires bounded human review before any screenshot-derived assertions may be normalised."
    )
    manifest["reviewer_attention_items"].extend(
        warning
        for result in audit_results.values()
        for warning in result.get("warnings", [])
    )
    manifest["stages"].append(stage_record("image_decisions", "completed", image_started))

    summary_started = time.perf_counter()
    eligibility_summary = []
    baseline_eligible = {
        "00_README_FIRST.md": "eligible",
        "01_email_product_owner_priority_change.eml": "eligible",
        "02_email_engineering_storage_privacy.eml": "eligible",
        "03_founder_review_meeting_minutes.docx": "eligible",
        "07_architecture_chat_export.txt": "eligible",
        "08_stale_feature_request_v0_8.docx": "eligible",
        "11_EXPECTED_CONFLICTS.md": "eligible",
        "12_EXPECTED_EXTRACTION_FEATURES.md": "eligible",
        "13_manifest.csv": "eligible",
    }
    for item in files_summary:
        filename = item["filename"]
        if filename in audit_results:
            eligibility = audit_results[filename]["normalisation_eligibility"]
            disposition = audit_results[filename]["disposition"]
            warnings = audit_results[filename].get("warnings", [])
        elif filename == "10_mobile_webapp_screenshot_feedback.png":
            eligibility = "eligible_with_review"
            disposition = "bounded_human_review"
            warnings = [image_decisions[filename]["human_review_requirement"]]
        elif filename == "09_whiteboard_workflow_photo.png":
            eligibility = "blocked"
            disposition = "blocked"
            warnings = [image_decisions[filename]["human_review_requirement"]]
        else:
            eligibility = baseline_eligible.get(filename, "blocked")
            disposition = "pass" if eligibility == "eligible" else "warning"
            warnings = []
        eligibility_summary.append(
            {
                "filename": filename,
                "classification": item["classification"],
                "disposition": disposition,
                "normalisation_eligibility": eligibility,
                "warnings": warnings,
            }
        )

    manifest["normalisation_eligibility_summary"] = eligibility_summary
    manifest["pipeline_state"] = "awaiting_human_approval_before_normalisation"
    manifest["resume_stage"] = "normalisation"
    manifest["stages"].append(stage_record("eligibility_summary", "completed", summary_started))

    human_gate_started = time.perf_counter()
    manifest["human_gate"] = {
        "approval_phrase": "APPROVE ELIGIBLE CIRCUITFIT EVIDENCE FOR NORMALISATION",
        "what_this_authorises": [
            "Normalisation of evidence explicitly marked eligible or eligible_with_review after the required human review.",
            "Progression to the next bounded Step 17 normalisation work.",
        ],
        "what_remains_blocked": [
            "09_whiteboard_workflow_photo.png",
            "Outlook .msg",
            "Any evidence file still marked blocked",
        ],
        "what_this_does_not_authorise": [
            "OpenSpec generation",
            "Application coding",
            "Test creation",
            "Deployment",
        ],
    }
    manifest["stages"].append(stage_record("human_gate", "completed", human_gate_started))

    write_json(manifest_path, manifest)
    print(json.dumps({
        "run_id": run_id,
        "manifest_path": str(manifest_path),
        "pipeline_state": manifest["pipeline_state"],
        "resume_stage": manifest["resume_stage"],
        "approval_phrase": manifest["human_gate"]["approval_phrase"],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
