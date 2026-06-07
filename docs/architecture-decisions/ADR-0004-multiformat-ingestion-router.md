# ADR-0004: Multi-Format Local-Ingestion Router

## Status

Accepted for the document-to-spec pilot.

## Decision

Do not send every file blindly to a single parser.

Use an explicit local-ingestion router:

| Input type | First-pass extractor | Fallback or supplementary extractor |
|---|---|---|
| DOCX | Docling | python-docx |
| PPTX | Docling | python-pptx |
| XLSX | Docling | openpyxl and pandas |
| PDF | Docling | rendered-page review and later OCR validation |
| PNG and image formats | Docling | later OCR and local vision-model enrichment |
| EML email | Python standard-library email parser | later MIME attachment extraction |
| TXT and Markdown | deterministic text extraction | none |
| CSV | deterministic CSV extraction | pandas where required |

## Reasoning

Docling is the preferred first-pass document parser, but enterprise ingestion
must remain explicit, testable and format-aware.

Each extraction result must record:

- source filename
- file hash
- file size
- processor used
- conversion status
- output paths
- timing
- warnings or errors
- Docling text, table and picture counts where available

## Enterprise Implication

A production ingestion service should be modular.

New extractors can be added without replacing the project workspace,
retrieval layer or specification workflow.
