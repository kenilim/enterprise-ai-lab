#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from docx import Document


def count_markdown_tables(markdown: str) -> int:
    separator_pattern = re.compile(
        r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$",
        re.MULTILINE,
    )

    return len(separator_pattern.findall(markdown))


def count_markdown_headings(markdown: str) -> list[str]:
    return re.findall(
        r"^(#{1,6})\s+(.+?)\s*$",
        markdown,
        flags=re.MULTILINE,
    )


def count_markdown_images(markdown: str) -> int:
    return len(
        re.findall(
            r"!\[[^\]]*\]\([^)]+\)",
            markdown,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare DOCX source structure against Docling exports."
    )

    parser.add_argument("--source-docx", required=True)
    parser.add_argument("--docling-markdown", required=True)
    parser.add_argument("--docling-json", required=True)
    parser.add_argument("--output-json", required=True)

    args = parser.parse_args()

    source_path = Path(args.source_docx).resolve()
    markdown_path = Path(args.docling_markdown).resolve()
    json_path = Path(args.docling_json).resolve()
    output_path = Path(args.output_json).resolve()

    source_document = Document(source_path)
    markdown = markdown_path.read_text(encoding="utf-8")
    docling_json = json.loads(
        json_path.read_text(encoding="utf-8")
    )

    source_paragraphs = [
        paragraph.text.strip()
        for paragraph in source_document.paragraphs
        if paragraph.text.strip()
    ]

    source_table_rows = 0
    source_table_cells = 0

    for table in source_document.tables:
        source_table_rows += len(table.rows)

        for row in table.rows:
            source_table_cells += len(row.cells)

    source_inline_shapes = len(
        source_document.inline_shapes
    )

    markdown_headings = count_markdown_headings(markdown)

    report = {
        "source_docx": {
            "path": str(source_path),
            "non_empty_paragraph_count": len(source_paragraphs),
            "table_count": len(source_document.tables),
            "table_row_count": source_table_rows,
            "table_cell_count": source_table_cells,
            "inline_shape_count": source_inline_shapes,
            "character_count_from_paragraphs": sum(
                len(paragraph)
                for paragraph in source_paragraphs
            ),
        },
        "docling_markdown": {
            "path": str(markdown_path),
            "character_count": len(markdown),
            "line_count": len(markdown.splitlines()),
            "heading_count": len(markdown_headings),
            "headings": [
                {
                    "level": len(prefix),
                    "text": text,
                }
                for prefix, text in markdown_headings
            ],
            "markdown_table_count": count_markdown_tables(markdown),
            "markdown_image_reference_count": count_markdown_images(markdown),
        },
        "docling_json": {
            "path": str(json_path),
            "top_level_keys": sorted(docling_json.keys()),
            "character_count": len(
                json.dumps(
                    docling_json,
                    ensure_ascii=False,
                )
            ),
        },
        "review_required": [
            "Confirm headings appear in the correct reading order.",
            "Compare Docling Markdown against the original DOCX visually.",
            "Confirm whether the source contains tables and whether each table was retained.",
            "Confirm whether the source contains embedded images or charts.",
            "Inspect the Docling JSON structure before designing retrieval chunks.",
        ],
    }

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        json.dumps(
            report,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            report,
            indent=2,
            ensure_ascii=False,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
