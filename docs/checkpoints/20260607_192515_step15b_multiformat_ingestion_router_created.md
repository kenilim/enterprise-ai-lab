# Checkpoint: Step 15B

## Completed

- Stray Windows Zone.Identifier files removed
- Reusable multi-format local-ingestion router created
- Explicit file-type routing documented
- Docling retained as the first-pass parser for supported document and image formats
- Deterministic local fallbacks added for EML, TXT, Markdown and CSV
- Architecture decision recorded

## Next Planned Action

Run the synthetic CircuitFit evidence pack through the router and measure:

- completed conversions
- failed conversions
- skipped files
- timing
- tables detected
- pictures detected
- extractor used per file
- formats requiring supplementary fallback inspection
