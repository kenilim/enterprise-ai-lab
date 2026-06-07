# Enterprise AI Agent Development Lab Report

## Purpose

Build a hands-on, enterprise-style agentic development workflow on a personal
Windows PC while maintaining a clear migration path to an air-gapped,
open-source-first enterprise environment.

## Operating Principles

1. Prefer open-source and air-gap-compatible components.
2. Use OpenAI models only as a temporary personal-development accelerator.
3. Keep raw documents and sensitive evidence local.
4. Convert unstructured information into reviewed specifications before coding.
5. Log experiments, failures, decisions and token usage.
6. Preserve a human approval gate before development and deployment.

## Current Environment

- Windows workstation
- WSL2 with Ubuntu 24.04
- Linux workspace: `/home/kenilim/projects/enterprise-ai-lab`
- VS Code connected to WSL
- Docker Desktop integrated with Ubuntu
- Python, pip, virtual environments, Node.js, npm and Git installed
- OpenCode installed inside Ubuntu
- Windows-hosted Ollama accessible from WSL
- ChatGPT OAuth login completed for the personal OpenCode development route

## Model Routes

### Local Route

`WSL → Windows Ollama → local models → RTX 4070 Ti`

Available experimental models include:

- `qwen3:14b`
- `qwen3-vl:8b`
- `gemma4:31b`
- `mistral:latest`

### Cloud Development Route

`OpenCode → ChatGPT OAuth plugin → OpenAI coding model`

This is a personal-lab exception and must not become an enterprise dependency.

## Completed Learning Points

### LP-001: Linux-Style Development Environment on Windows

WSL2 and Ubuntu provide a Linux development workspace on a Windows PC.

### LP-002: Containerised Development

Docker Desktop is integrated with Ubuntu and validated using `hello-world`.

### LP-003: Local Model Serving

Windows Ollama is accessible from WSL and uses the RTX 4070 Ti.

### LP-004: Adapter Compatibility Failure

Direct Ollama API requests work, including streaming responses.
The tested OpenCode-to-Ollama adapter does not reliably surface final model
responses. The defect was isolated and the local route was retained for direct
API experimentation rather than used as the critical development path.

### LP-005: Dual Provider Configuration

OpenCode now permits both `ollama` and `openai` providers.
OpenAI is used only for personal development acceleration.

### LP-006: Workspace Organisation

The lab now separates shared assets, logs and pilot projects.

## Pilot Projects

### 01-doc-to-spec-pilot

Goal:

`Local documents → local ingestion → local model → reviewed specifications`

### 02-app-build-pilot

Goal:

`Approved specifications → OpenCode with OpenAI model → tested Dockerised app`

## Outstanding Work

- Capture OpenCode token-usage baseline
- Validate the OpenAI coding route
- Install and configure OpenSpec
- Initialise Git repositories
- Build the first specification-driven application
- Install Docling and format-specific fallback extractors
- Parse synthetic unstructured documents locally
- Add local specification drafting
- Map the personal lab to an enterprise air-gapped deployment pattern

### LP-007: Human-Triggered Document-to-Spec Automation

New evidence should not require manual copy-and-paste into an AI assistant.

The preferred pattern is:

`new local files → human trigger → local parsing → local model draft → Git diff → human approval`

A server-resident agent such as Hermes Agent may later invoke this workflow as
a reusable skill. The initial implementation should remain deterministic and
script-driven so that the pipeline is understandable, testable and auditable.

For production, a durable workflow engine should govern retries, state,
approvals and audit trails.

### LP-009: Private GitHub Backup Established

The root lab workspace has been committed and pushed to the private repository:

`kenilim/enterprise-ai-lab`

The root repository tracks reusable documentation, scripts, templates,
configuration files and pilot scaffolding.

Raw evidence, secrets, authentication files, runtime logs and model weights are
excluded.

The working rule is:

`review → stage → scan → commit → push → verify visibility`

### LP-010: OpenAI-Backed OpenCode Development Route Validated

The personal-lab development route has been validated:

`VS Code in Ubuntu WSL → OpenCode → ChatGPT OAuth plugin → OpenAI GPT-5.4`

The controlled test returned the required response without modifying tracked
files.

Recorded model-level usage:

- Model: `openai/gpt-5.4`
- Messages: `1`
- Input tokens: approximately `2.3K`
- Output tokens: `29`
- Cache read: approximately `4.1K`
- Reported cost: `$0.0000`

The earlier `openai/gpt-5.2-codex` smoke test failed because the model was not
supported through the ChatGPT-account route.

The enterprise lesson is that every model-provider-authentication combination
requires an active validation test.

### LP-011: OpenSpec Core Workflow Initialised

OpenSpec has been installed and initialised inside:

`projects/02-app-build-pilot`

The generated OpenCode core workflow contains:

- `opsx-propose`
- `opsx-explore`
- `opsx-apply`
- `opsx-sync`
- `opsx-archive`

OpenSpec now provides the structured handoff layer:

`approved intent → proposal → specs → design → tasks → human review → implementation → archive`

The initial empty OpenSpec directories were preserved with `.gitkeep`
placeholders so that the baseline structure remains visible in Git.

### LP-012: Enterprise Project Intelligence Workspace Vision

The lab target has expanded from a document parser into an enterprise project
intelligence workspace.

The intended user experience is a ChatGPT-style internal web application where
a product manager creates a project, uploads unstructured files, asks questions,
inspects evidence, generates specifications, reviews impact analysis after new
documents arrive and approves incremental tasks for development agents.

The model is not the system of record.

The controlled flow is:

`immutable evidence → local parsing → grounded retrieval → versioned specification proposal → human approval → incremental development handoff`

### LP-013: Local Docling Ingestion Toolkit Installed

A dedicated CPU-only document-ingestion environment has been created under:

`projects/01-doc-to-spec-pilot/.venv`

Installed components include:

- `docling 2.97.0`
- `python-docx 1.2.0`
- `python-pptx 1.0.2`
- `openpyxl 3.1.5`
- `pandas 3.0.3`
- `pillow 12.2.0`
- `torch 2.12.0+cpu`

No document extraction has run yet.

The next experiment is the first CircuitFit DOCX conversion into Markdown and
lossless JSON.
## LP-015: Product Manager CoPilot and the Product-Builder Learning Journey

### Context

This lab is being built hands-on by a non-technical product person with basic
and dated coding knowledge.

The product manager defined the problem, constraints, north-star vision,
learning sequence and required controls.

An AI copilot supported research, explanation, script generation,
troubleshooting, documentation and iteration.

### Learning Point

Product builders with clear requirements and disciplined problem framing can
independently research, prototype and evaluate more of the delivery stack than
before.

This does not replace software-engineering expertise.

It creates a stronger product-to-engineering handoff and helps product managers
test assumptions before committing larger teams.

### North-Star Product Name

`Product Manager CoPilot`

### Requirements Record

`docs/requirements/product-manager-copilot-learning-journey-requirements.md`
