#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import time
from datetime import datetime, timezone
from email import policy
from email.parser import BytesParser
from pathlib import Path
from typing import Any

from docling.document_converter import DocumentConverter


DOCLING_EXTENSIONS = {
    ".docx",
    ".xlsx",
    ".pptx",
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
}

TEXT_EXTENSIONS = {
    ".txt",
    ".md",
}

CSV_EXTENSIONS = {
    ".csv",
}

EMAIL_EXTENSIONS = {
    ".eml",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def write_json(path: Path, data: Any) -> None:
    path.write_text(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def safe_slug(path: Path) -> str:
    return "".join(
        character
        if character.isalnum() or character in {"-", "_"}
        else "_"
        for character in path.stem
    )


def extract_docling(
    converter: DocumentConverter,
    source: Path,
    output_dir: Path,
) -> dict[str, Any]:
    result = converter.convert(source)

    document = result.document

    markdown = document.export_to_markdown()
    document_dict = document.export_to_dict()

    markdown_path = output_dir / "content.docling.md"
    json_path = output_dir / "content.docling.json"

    markdown_path.write_text(
        markdown,
        encoding="utf-8",
    )

    write_json(
        json_path,
        document_dict,
    )

    return {
        "processor": "docling",
        "output_markdown": str(markdown_path),
        "output_json": str(json_path),
        "markdown_size_bytes": markdown_path.stat().st_size,
        "json_size_bytes": json_path.stat().st_size,
        "docling_top_level_keys": sorted(
            document_dict.keys()
        ),
        "docling_text_items": len(
            getattr(document, "texts", []) or []
        ),
        "docling_table_items": len(
            getattr(document, "tables", []) or []
        ),
        "docling_picture_items": len(
            getattr(document, "pictures", []) or []
        ),
    }


def extract_text(
    source: Path,
    output_dir: Path,
) -> dict[str, Any]:
    text = source.read_text(
        encoding="utf-8",
        errors="replace",
    )

    markdown_path = output_dir / "content.text.md"

    markdown_path.write_text(
        text,
        encoding="utf-8",
    )

    return {
        "processor": "deterministic-text",
        "output_markdown": str(markdown_path),
        "character_count": len(text),
        "line_count": len(text.splitlines()),
    }


def extract_csv(
    source: Path,
    output_dir: Path,
) -> dict[str, Any]:
    rows: list[list[str]] = []

    with source.open(
        "r",
        encoding="utf-8",
        errors="replace",
        newline="",
    ) as file:
        reader = csv.reader(file)

        for row in reader:
            rows.append(row)

    json_path = output_dir / "content.csv.json"

    write_json(
        json_path,
        {
            "rows": rows,
        },
    )

    return {
        "processor": "deterministic-csv",
        "output_json": str(json_path),
        "row_count": len(rows),
        "maximum_column_count": max(
            (len(row) for row in rows),
            default=0,
        ),
    }


def extract_email(
    source: Path,
    output_dir: Path,
) -> dict[str, Any]:
    with source.open("rb") as file:
        message = BytesParser(
            policy=policy.default
        ).parse(file)

    body_parts: list[str] = []

    if message.is_multipart():
        for part in message.walk():
            if (
                part.get_content_type()
                == "text/plain"
            ):
                body_parts.append(
                    part.get_content()
                )
    else:
        body_parts.append(
            message.get_content()
        )

    email_data = {
        "from": message.get("From"),
        "to": message.get("To"),
        "cc": message.get("Cc"),
        "date": message.get("Date"),
        "subject": message.get("Subject"),
        "body": "\n\n".join(body_parts),
        "attachment_count": sum(
            1
            for part in message.walk()
            if part.get_content_disposition()
            == "attachment"
        ),
    }

    markdown_path = output_dir / "content.email.md"
    json_path = output_dir / "content.email.json"

    markdown_path.write_text(
        "\n".join(
            [
                f"# {email_data['subject']}",
                "",
                f"From: {email_data['from']}",
                f"To: {email_data['to']}",
                f"Cc: {email_data['cc']}",
                f"Date: {email_data['date']}",
                "",
                email_data["body"],
            ]
        ),
        encoding="utf-8",
    )

    write_json(
        json_path,
        email_data,
    )

    return {
        "processor": "python-email-parser",
        "output_markdown": str(markdown_path),
        "output_json": str(json_path),
        "attachment_count": email_data[
            "attachment_count"
        ],
    }


def extract_one(
    converter: DocumentConverter,
    source: Path,
    output_root: Path,
) -> dict[str, Any]:
    started = time.perf_counter()

    output_dir = (
        output_root
        / f"{safe_slug(source)}_{sha256(source)[:12]}"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    extension = source.suffix.lower()

    metadata: dict[str, Any] = {
        "source_filename": source.name,
        "source_extension": extension,
        "source_sha256": sha256(source),
        "source_size_bytes": source.stat().st_size,
        "started_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "status": "pending",
    }

    try:
        if extension in DOCLING_EXTENSIONS:
            metadata.update(
                extract_docling(
                    converter,
                    source,
                    output_dir,
                )
            )

        elif extension in EMAIL_EXTENSIONS:
            metadata.update(
                extract_email(
                    source,
                    output_dir,
                )
            )

        elif extension in TEXT_EXTENSIONS:
            metadata.update(
                extract_text(
                    source,
                    output_dir,
                )
            )

        elif extension in CSV_EXTENSIONS:
            metadata.update(
                extract_csv(
                    source,
                    output_dir,
                )
            )

        else:
            metadata.update(
                {
                    "processor": "none",
                    "status": "skipped",
                    "warning": (
                        "No extractor configured "
                        f"for extension: {extension}"
                    ),
                }
            )

        if metadata["status"] == "pending":
            metadata["status"] = "completed"

    except Exception as exception:
        metadata.update(
            {
                "status": "failed",
                "error_type": type(
                    exception
                ).__name__,
                "error_message": str(
                    exception
                )[:1000],
            }
        )

    metadata["completed_utc"] = datetime.now(
        timezone.utc
    ).isoformat()

    metadata["duration_seconds"] = round(
        time.perf_counter() - started,
        3,
    )

    metadata_path = output_dir / "metadata.json"

    write_json(
        metadata_path,
        metadata,
    )

    return metadata


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run a local multi-format evidence "
            "extraction benchmark."
        )
    )

    parser.add_argument(
        "--input-dir",
        required=True,
    )

    parser.add_argument(
        "--output-dir",
        required=True,
    )

    parser.add_argument(
        "--report-json",
        required=True,
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    report_path = Path(args.report_json).resolve()

    if not input_dir.is_dir():
        raise FileNotFoundError(
            f"Input folder not found: {input_dir}"
        )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    report_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    converter = DocumentConverter()

    sources = sorted(
        path
        for path in input_dir.iterdir()
        if path.is_file()
        and path.name != ".gitkeep"
    )

    results = [
        extract_one(
            converter,
            source,
            output_dir,
        )
        for source in sources
    ]

    summary = {
        "run_started_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "input_directory": str(
            input_dir
        ),
        "output_directory": str(
            output_dir
        ),
        "file_count": len(
            results
        ),
        "completed_count": sum(
            result["status"] == "completed"
            for result in results
        ),
        "failed_count": sum(
            result["status"] == "failed"
            for result in results
        ),
        "skipped_count": sum(
            result["status"] == "skipped"
            for result in results
        ),
        "results": results,
    }

    write_json(
        report_path,
        summary,
    )

    print(
        json.dumps(
            summary,
            indent=2,
            ensure_ascii=False,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
