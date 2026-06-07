# Extraction-Quality Gate Matrix

**Step:** 16R2.1
**Purpose:** Define the minimum pre-normalisation evidence-quality rules that must be satisfied before evidence normalisation may begin.
**Generated:** 2026-06-07T21:48:22+08:00
**Refined after Step 16R2 review outcome:** `REQUEST REFINEMENT`
**Source quality-review report:** `docs/reports/20260607_124717_circuitfit_ingestion_quality_review.md`
**Source report SHA-256:** `41eaeec5d7616c9d6b5dd443b98264515c133f0dc1cdcdb55d3f344a71e656b9`
**Repository branch at generation:** `main`
**Repository commit before generation:** `c3ae2e4`

> This document is a Git-safe governance artefact. It records sanitised quality rules only. Raw evidence, detailed extraction logs and local troubleshooting output remain outside Git.

> This is a **pre-normalisation governance policy**. Approving this matrix does **not** authorise evidence normalisation, OpenSpec generation or application coding.

## Why this gate exists

A file can be converted successfully while still losing meaning. Before evidence is normalised into records that agents may rely on, each risky format needs an explicit quality rule, a deterministic fallback inspection method and a human-review trigger.

The control principle is:

```text
conversion success
→ format-aware inspection
→ quality classification
→ human review where material
→ normalisation eligibility
```

## Status vocabulary

| Status | Meaning |
|---|---|
| PASS | Evidence is sufficiently reliable for normalisation under the defined gate. |
| PASS WITH CAVEATS | Evidence may proceed only with recorded warnings and bounded review. |
| FAIL | Evidence must not enter normalisation until remediation or manual handling is completed. |
| DEFERRED | Capability is deliberately outside the current implementation scope. |

## Normalisation eligibility outcomes

| Eligibility outcome | Meaning |
|---|---|
| Eligible for automatic normalisation | Deterministic inspection passed with no material warning requiring human confirmation for the intended downstream use. |
| Eligible only after bounded human review | Deterministic inspection preserved enough structure to support a limited downstream use, but a human must review the recorded warnings and approve that bounded use first. |
| Blocked | The gate has not been satisfied, failed, or still needs remediation before normalisation may begin. |
| Deferred | The route is intentionally out of scope and must not silently enter normalisation. |

## Required decision sequence

Apply this order for every risky format:

```text
deterministic inspection first
→ agent interpretation second
→ human approval for material conclusions last
→ normalisation eligibility decision
```

Agents may summarise the deterministic results.

Agents must not treat interpretation as a substitute for missing deterministic inspection.

## Quality-gate matrix

| Format or evidence type | Gap found in first interactive review | Required deterministic inspection before normalisation | Agent interpretation allowed only after deterministic inspection | Minimum acceptance criteria | Human-review trigger | Current status before remediation | Normalisation eligibility state now |
|---|---|---|---|---|---|---|---|
| XLSX workbook | Primary extraction does not prove workbook structure, sheet coverage or table fidelity. | Add workbook-aware fallback inspection that enumerates sheets, used ranges, merged cells, hidden sheets, formulas versus displayed values and sampled row/column structure. | Agent may summarise workbook structure, preserved tables and warnings, but must not infer missing sheet meaning or formula intent. | Every non-empty relevant sheet is listed; table headers and representative rows remain readable; hidden or formula-heavy sheets are surfaced as warnings. | Any hidden sheet, merged-cell ambiguity, formula-only value, missing header or unexplained row-count mismatch. | PASS WITH CAVEATS | Blocked — rerun after workbook-aware audit. |
| PPTX deck | Primary extraction does not reliably prove slide boundaries or visual layout meaning. | Add slide-aware fallback inspection that records slide number, title, text blocks, speaker notes where available, images and object counts. | Agent may summarise slide-by-slide content and warnings, but must not merge slide meaning when deterministic slide boundaries are unclear. | Every slide is represented in order; slide boundaries are explicit; key text is associated with its slide; image-heavy slides are flagged. | Missing slide text, unexplained slide-count mismatch, image-heavy slide or layout-dependent meaning. | PASS WITH CAVEATS | Blocked — rerun after slide-aware audit. |
| PDF document | Extracted text looked acceptable, but reading order was not independently validated. | Add independent page-aware inspection that records page count, per-page text and text-block sequence, then compares those results against the primary extraction. | Agent may summarise the validated page sequence and warnings, but must not treat visually plausible ordering as proven without the independent page-aware comparison. | All pages are represented; headings and paragraphs follow a page-aware and materially consistent reading sequence; material omission, duplication or suspicious text-block order is surfaced as a warning rather than silently accepted. | Multi-column page, table-heavy page, page-count mismatch, omitted block, duplicated block or suspicious block order. | PASS WITH CAVEATS | Blocked — rerun after reading-order validation. |
| Screenshot PNG | OCR is noisy and may distort UI labels or short text. | Keep OCR output, record the OCR engine and version, use confidence scores when the engine exposes them, and otherwise apply deterministic heuristics for fragmented or suspicious text. Missing confidence data must trigger a warning and bounded review rather than an automatic fail for every screenshot. | Agent may summarise OCR findings and warnings, but must not upgrade uncertain labels into authoritative evidence without the recorded OCR audit and any required human review. | Material labels and statements are readable enough to support a cited evidence item; uncertainty is explicitly recorded; harmless cosmetic OCR defects do not by themselves force failure; meaning-changing ambiguity must trigger review. | Low-confidence OCR, missing confidence data, fragmented sentences, ambiguous labels or text that materially changes requirement meaning. | PASS WITH CAVEATS | Blocked — OCR-derived assertions are not yet eligible for automatic normalisation and require the refined audit path first. |
| Whiteboard PNG | Current quality gate failed because OCR did not reliably surface the intended workflow. | Add deterministic image metadata and OCR audit first. A local VLM may then be used only as a recorded interpretive fallback to draft a summary for human confirmation. Preserve the original image hash and record the fallback model identifier. | Agent may draft an explicitly labelled interpretation only after deterministic audit; that interpretation remains separate from approved evidence until a human confirms it. | Key workflow nodes, arrows and unresolved ambiguities are captured in a human-reviewed summary linked to the source hash. Machine-generated interpretation must remain distinguishable from approved evidence. | Always require human confirmation before any whiteboard-derived assertion could move beyond review. | FAIL | Blocked — fallback not yet implemented and no automatic route is permitted. |
| Outlook `.msg` email | Ingestion remains deliberately deferred. | None in Step 16R2.1. Maintain an explicit deferred route and avoid silent acceptance. | Agent may report deferred status and provenance metadata only; no interpretive use is allowed. | Router clearly reports deferred status without losing the source file or provenance metadata. | Any attempt to ingest `.msg` evidence into a project that depends on email content. | DEFERRED | Deferred — remain outside current scope. |

## Cross-format rules

1. **No silent fallback.** Every fallback extractor or reviewer must be recorded in the run manifest.
2. **Preserve provenance.** Keep the original source hash, extractor version, fallback method, timestamp and review status.
3. **Separate evidence from interpretation.** Deterministic tooling extracts and measures; agents interpret and propose; humans approve material conclusions.
4. **Normalisation is gated.** A format marked `Blocked` or `Deferred` above cannot flow into evidence normalisation merely because file conversion completed.
5. **Progressive disclosure applies.** Full logs remain local-only; compact summaries and sanitised governance artefacts may enter Git.
6. **Background-processing design remains required.** Future benchmark runs should capture progress, ETA, token usage, CPU, memory and future GPU metrics.
7. **Confidence must be explicit.** When an extractor does not expose a confidence score, the manifest must record that limitation and apply deterministic warning heuristics rather than assuming a pass.
8. **Bounded human review is not the same as automatic normalisation.** A future row may become `Eligible only after bounded human review`, but that still requires the deterministic inspection record and explicit human confirmation for the stated bounded use.
9. **This matrix is pre-normalisation only.** Approval of the matrix does not authorise OpenSpec generation, application coding or downstream evidence normalisation by itself.

## Step 16 remediation sequence

The proposed remediation order, subject to human approval after this matrix is reviewed and refined:

1. XLSX workbook-aware fallback inspection
2. PPTX slide-aware fallback inspection
3. PDF page-aware reading-order validation
4. Screenshot OCR confidence-aware review
5. Whiteboard image-aware fallback with mandatory human confirmation
6. Second benchmark with compact metrics summary
7. Human stop gate before evidence normalisation

Outlook `.msg` ingestion remains deferred and is not included in this remediation sequence.

## Offline learning points

- Successful conversion is not the same as reliable evidence extraction.
- Pre-normalisation policy approval is not the same as permission to start normalisation.
- Format-aware deterministic inspection is required before an agent interprets evidence.
- Visual artefacts need stricter approval rules because OCR can produce plausible but wrong text.
- Whiteboards should be treated as human-reviewed interpretation inputs, not automatically trusted text sources.
- A deliberately deferred format is safer than a partially supported route that fails silently.
- Normalisation should consume only evidence that has passed an explicit quality gate.
- Validation commands must be tested against both tracked and untracked files. A misleading exit code can create a false pass or false fail if the script does not distinguish content differences from actual whitespace defects.

## Material-change rule

Changes to this matrix affect which evidence may enter downstream product analysis. Any change to acceptance criteria, human-review triggers or normalisation eligibility requires a reviewed Git diff and explicit human approval.
