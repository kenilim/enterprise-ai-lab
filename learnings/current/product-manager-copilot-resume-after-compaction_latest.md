# Product Manager CoPilot Lab - Resume After Chat Compaction

## Purpose

Use this file to continue the lab in a fresh ChatGPT conversation without relying on the full original chat history.

## Current checkpoint

- Repository: `https://github.com/kenilim/enterprise-ai-lab`
- Latest validated commit: `0b19dd2`
- Completed step: **Step 15E.3**
- Working tree after push: clean
- Current phase: extraction-quality remediation before evidence normalisation and OpenSpec generation

## What has already been proven

1. WSL2 Ubuntu, Docker, GitHub and VS Code workflow work.
2. Ollama is reachable from Ubuntu through the Windows host.
3. Direct OpenAI-compatible local Qwen inference works.
4. OpenAI GPT-5.4 routing through OpenCode works.
5. OpenSpec is installed and retained for versioned product contracts.
6. Docling 2.97.0 is installed in a dedicated CPU-only virtual environment.
7. A synthetic multi-format CircuitFit evidence pack exists.
8. The first router benchmark processed 14/14 files.
9. A custom Product Manager CoPilot OpenCode orchestrator and ingestion-reviewer subagent exist.
10. Step 15E.1 read-only orchestration passed.
11. Step 15E.2 controlled interactive review passed its main safeguards.
12. Step 15E.3 committed the agent-generated sanitised quality report, screenshots and background-processing learning.

## Current extraction-quality findings

- 9 pass
- 4 pass with caveats
- 1 fail

Caveats or failures:

- XLSX needs workbook-aware fallback review.
- PPTX needs slide-aware fallback review.
- PDF reading order requires independent validation.
- screenshot OCR is noisy.
- whiteboard-image OCR quality failed.
- native Docling email support should be revalidated because current docs now advertise EML and MSG support.

## Product rules to preserve

- Explain before executing.
- One bounded step at a time.
- Validate before proceeding.
- Record meaningful learning points offline.
- Log full local evidence, but review compact summaries first.
- Keep sensitive or raw local artefacts out of public Git.
- Human approval is required for material changes.
- Do not generate OpenSpec proposals until extraction quality and normalisation are ready.
- Do not write application code until OpenSpec tasks are approved.

## Next step

Start with **Step 16: extraction-quality remediation**.

Proposed sequence:

1. inspect `docs/reports/20260607_124717_circuitfit_ingestion_quality_review.md`
2. define fallback-audit tools for XLSX, PPTX, PDF and images
3. revalidate Docling-native EML and MSG ingestion
4. generate a quality-gate matrix
5. run a second benchmark
6. capture timings, tokens, CPU, memory and future GPU-metric requirements
7. stop for review before normalisation

## Prompt to paste into a fresh chat

```text
Resume my Product Manager CoPilot enterprise AI development lab from Step 16.
Read the attached whitepaper and this resumption checkpoint first.

Act as an educator and copilot for a non-technical product manager. Explain the
purpose of each step in plain English, provide only one bounded step at a time,
make commands copy-paste safe, generate downloadable scripts when commands are
long, log outputs with timestamps, create compact summaries, distinguish
local-only from Git-safe artefacts, validate results before proceeding, and
record meaningful learning points in offline documents.

Do not generate OpenSpec artefacts yet. First resolve the extraction-quality
gaps from Step 15E.2 and create a quality-gate matrix. Preserve the
open-source-first, air-gap-ready and regulator-auditable target architecture.
```
