#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from docling.document_converter import DocumentConverter


def sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract a local document with Docling into Markdown and JSON."
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to the source document.",
    )

    parser.add_argument(
        "--output-dir",
        required=True,
        help="Folder for extracted Markdown, JSON and metadata outputs.",
    )

    args = parser.parse_args()

    source = Path(args.source).resolve()
    output_dir = Path(args.output_dir).resolve()

    if not source.is_file():
        raise FileNotFoundError(f"Source file not found: {source}")

    output_dir.mkdir(parents=True, exist_ok=True)

    started_utc = datetime.now(timezone.utc).isoformat()
    started = time.perf_counter()

    converter = DocumentConverter()
    result = converter.convert(source)

    duration_seconds = time.perf_counter() - started

    document = result.document

    markdown = document.export_to_markdown()
    json_dict = document.export_to_dict()

    stem = source.stem

    markdown_path = output_dir / f"{stem}.docling.md"
    json_path = output_dir / f"{stem}.docling.json"
    metadata_path = output_dir / f"{stem}.docling.metadata.json"

    markdown_path.write_text(markdown, encoding="utf-8")

    json_path.write_text(
        json.dumps(json_dict, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    metadata = {
        "source_filename": source.name,
        "source_path": str(source),
        "source_sha256": sha256(source),
        "source_size_bytes": source.stat().st_size,
        "started_utc": started_utc,
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "duration_seconds": round(duration_seconds, 3),
        "output_markdown": str(markdown_path),
        "output_markdown_size_bytes": markdown_path.stat().st_size,
        "output_json": str(json_path),
        "output_json_size_bytes": json_path.stat().st_size,
        "output_metadata": str(metadata_path),
        "docling_status": "conversion_completed",
    }

    metadata_path.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(json.dumps(metadata, indent=2, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
