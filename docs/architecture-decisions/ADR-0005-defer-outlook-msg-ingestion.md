# ADR-0005: Defer Outlook MSG Ingestion and Record Email Routing Limitation

## Status

Accepted for the current learning phase.

## Decision

Docling remains the preferred first-pass parser for supported document,
spreadsheet, presentation, PDF and image formats.

Do not treat Docling as a universal parser.

For the current benchmark:

| Format | Current route |
|---|---|
| `.eml` | Python standard-library email parser |
| `.msg` | Deferred |
| Email attachments | Count only for now; recursive routing later |

## Known Limitation

Microsoft Outlook `.msg` files are not supported in the current learning phase.

This limitation must remain visible in documentation and presentations because
enterprise project evidence often exists in email before formal documents are
updated.

## Possible Later Solution

Evaluate:

`extract-msg`

The evaluation should cover:

- extraction fidelity
- attachment handling
- nested-message handling
- encoding behaviour
- maintenance status
- dependency footprint
- licence suitability
- air-gap packaging

## Reason for Deferral

The current priority is to complete the end-to-end learning flow:

`multi-format evidence → extraction → normalisation → conflict detection → OpenSpec proposal → human review`

MSG support can be evaluated after this core flow works.
