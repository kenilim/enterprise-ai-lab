#!/usr/bin/env python3

from __future__ import annotations

import csv
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: generate-source-manifest.py <source-folder> <output-csv>",
            file=sys.stderr,
        )
        return 1

    source_folder = Path(sys.argv[1]).resolve()
    output_csv = Path(sys.argv[2]).resolve()

    if not source_folder.is_dir():
        print(f"Source folder not found: {source_folder}", file=sys.stderr)
        return 1

    output_csv.parent.mkdir(parents=True, exist_ok=True)

    rows = []

    for path in sorted(source_folder.iterdir()):
        if not path.is_file() or path.name == ".gitkeep":
            continue

        rows.append(
            {
                "filename": path.name,
                "extension": path.suffix.lower(),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
                "manifest_generated_utc": datetime.now(timezone.utc).isoformat(),
            }
        )

    with output_csv.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "filename",
                "extension",
                "size_bytes",
                "sha256",
                "manifest_generated_utc",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Manifest written: {output_csv}")
    print(f"Files recorded: {len(rows)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
