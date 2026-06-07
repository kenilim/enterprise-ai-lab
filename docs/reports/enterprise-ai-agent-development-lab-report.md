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
## LP-016: Traceability Must Explain Whether a Production Issue Is Actually a Bug

### Finding

A production incident is not always an implementation defect.

Sometimes the software behaves exactly as specified, but the approved
requirement, task or acceptance criterion was incomplete or wrong.

### Enterprise Reality

This is common in large software programmes.

One team may report a bug.

Another team may point out that the delivered behaviour matched the approved
scope.

The system needs enough lineage to determine what happened.

### Required Traceability Spine

`source evidence → requirement → design decision → user story → acceptance criterion → task → code commit → automated test → release artefact → production incident`

### Root-Cause Categories

- implementation defect
- test defect
- missing requirement
- incorrect requirement
- ambiguous requirement
- design mismatch
- regression gap
- production-learning gap

### Learning Point

Product Manager CoPilot should not only generate requirements.

It should preserve the history needed to explain why a requirement, task,
test or production behaviour exists.

## LP-017: Human Product Judgement, Challenge and Debate Shaped the Journey

### Finding

This lab was not generated from one prompt.

The product manager repeatedly challenged and redirected the learning path.

Examples:

- requiring an air-gap-ready open-source-first architecture
- insisting on realistic multi-format evidence
- questioning whether manual scripts should become agent tools
- preserving OpenSpec as a controlled specification layer
- exposing Docling email-format limitations
- requiring repository secret scanning before public sharing
- renaming the north-star product to Product Manager CoPilot
- requiring production-incident traceability

### Learning Point

AI can accelerate research, prototyping, scripting and documentation.

It still needs a product builder with experience and product taste to frame the
problem, debate trade-offs and decide what matters.
## LP-018: Preserve Attribution for Human Insight, Copilot Recommendation and Experiment Evidence

### Origin

`Product-manager insight`

### Finding

The repository should not read like a one-prompt artefact.

This journey was shaped through repeated product judgement, challenge, debate,
experiments and decisions.

### Documentation Rule

Each major learning point should identify one or more origins:

- `Product-manager insight`
- `Copilot recommendation`
- `Experiment result`
- `Known limitation`
- `Decision`

### Learning Point

The value is not merely that an AI copilot generated scripts.

The value is that a product builder used experience and product taste to decide
which problem to solve, which assumptions to challenge and which experiments to
run.
## LP-019: Regulator-Auditable Traceability Is a Product Requirement

### Origin

`Product-manager insight`

### Finding

The traceability model must hold up in a high-risk enterprise environment with
internal audit, risk oversight and potential regulatory scrutiny.

### Learning Point

Traceability is not merely a debugging convenience.

It must preserve:

`who → did what → against which evidence → using which agent, model, skill and tool → under which permissions → producing which output → approved by whom → released where → linked to which incident`

### Decision

Adopt an audit-grade traceability target with identities, timestamps, hashes,
versioning, approval records, test evidence, exception handling and
incident linkage.

## LP-020: OpenCode Is a Runtime, Not One Giant Agent

### Origin

`Product-manager question` and `Copilot explanation`

### Finding

OpenCode should be understood as the runtime and interface hosting agents.

### Learning Point

- agent = worker
- skill = reusable procedure
- tool = deterministic executable capability
- orchestrator = coordinating primary agent
- subagent = focused specialist
- `AGENTS.md` = shared project rules
- ADR = written decision record
- OpenSpec = later versioned change contract

### Decision

Add a primary Product Manager CoPilot orchestrator and a focused
`ingestion-reviewer` subagent.

## LP-021: Offline Learning Documents Are a First-Class Deliverable

### Origin

`Product-manager insight`

### Finding

The chat context is too large to remain the only source of learning.

### Learning Point

The repository must function as an offline learning system.

It should preserve:

- README
- primer guides
- requirements
- ADRs
- checkpoints
- learning points
- presentations
- version history
- next steps

### Decision

Add a standalone OpenCode operating-model primer and a regulator-auditable
traceability guide before the first agent-run experiment.
## LP-022: Logging Is a Product Output, Not a Terminal Scroll

### Origin

`Product-manager insight`

### Finding

Long terminal output is not an effective review interface.

A product manager should not need to scroll through hundreds of lines or paste
large terminal dumps back into a chat.

### Learning Point

Every meaningful workflow should produce:

`full local log → compact manifest → human-readable summary → sanitised checkpoint → reviewed Git commit`

The full log remains available for troubleshooting and audit reconstruction.

The compact summary becomes the default review object.

### Decision

Add reusable wrapper scripts that generate local logs, manifests and short
summaries automatically.

## LP-023: Traceability Must Be Usable as Well as Complete

### Origin

`Product-manager insight` and `Copilot recommendation`

### Finding

Regulator-auditable evidence can become operationally unusable if every routine
review requires raw transcript inspection.

### Learning Point

Use progressive disclosure:

1. summary
2. manifest
3. sanitised report
4. Git diff
5. full log only when needed
6. session export only when needed

### Decision

Treat concise summaries and structured manifests as first-class workflow
artefacts without discarding the detailed underlying evidence.
## LP-024: Interactive Review Is a Lab Guardrail, Not the Final Enterprise UX

### Origin

`Product-manager insight`

### Finding

The OpenCode interactive permission flow is useful for learning, debugging and
first-time validation.

It is not the ideal end-state user experience for a product manager processing
large enterprise evidence packs.

### Learning Point

The enterprise Product Manager CoPilot should run evidence processing as a
background job with policy-defined permissions.

Human approval should be required at material gates, not for every low-risk
read or approved deterministic script.

### Enterprise Pattern

Use:

`background job → policy engine → progress estimator → exception queue → human approval gate`

rather than:

`human manually approves every individual tool call`

## LP-025: Large Enterprise Evidence Packs Need Time and Resource Forecasting

### Origin

`Product-manager insight`

### Finding

Large enterprise programmes may contain hundreds or thousands of files.

The user experience must show expected processing time, progress, queue state
and resource usage.

### Learning Point

Track both commercial tokenomics and infrastructure resource economics:

- number of files
- file sizes
- pages
- slides
- sheets
- images
- attachments
- OCR workload
- wall-clock duration
- queue waiting time
- per-stage duration
- token input, output and cache usage
- model cost where applicable
- CPU time
- memory usage
- GPU utilisation
- peak VRAM
- GPU-hours
- retries and failures
- throughput by file type

### Enterprise Pattern

For large jobs, Product Manager CoPilot should support overnight processing,
scheduled runs and asynchronous notifications.

## LP-026: Progress Should Be Estimated by Work Units, Not File Count Alone

### Origin

`Product-manager insight` and `Copilot recommendation`

### Finding

A simple progress bar based on file count is misleading.

One PDF with OCR-heavy scanned pages may take longer than dozens of clean
Markdown files.

### Learning Point

Estimate work using weighted units:

| Evidence type | Example weighting signal |
|---|---|
| Markdown or text | bytes and lines |
| DOCX | paragraphs, tables, images |
| PPTX | slides, tables, embedded images |
| XLSX | sheets, rows, formulas, tables |
| PDF | pages, OCR requirement, image density |
| PNG/JPEG | OCR complexity, resolution |
| EML | attachments and nested messages |

### Product Implication

The UI should show:

- estimated time remaining
- confidence range
- files completed
- current stage
- work units completed
- stage countdown
- tasks remaining
- exception count
- "safe to leave running" status

## LP-027: Permission Strategy Must Evolve From Manual Prompts to Policy Gates

### Origin

`Product-manager insight`

### Finding

Manual permission prompts are painful for long-running enterprise workflows.

### Learning Point

The system needs pre-approved execution profiles.

Examples:

| Profile | Behaviour |
|---|---|
| Read-only review | Allow reads, deny writes |
| Ingestion processing | Allow approved extraction scripts, local logs and sanitised reports |
| Spec proposal | Allow OpenSpec draft creation, require human approval |
| Development implementation | Allow bounded code edits, require tests |
| Release | Require formal approval and deployment controls |

### Decision

Keep strict manual approval in the lab until the toolchain is proven.

Later, define policy-driven background execution with explicit approval gates.

## LP-028: Whitepaper Snapshots Are Compaction Boundaries

At meaningful architectural milestones, create an offline whitepaper and a
compact resumption checkpoint before compacting or starting a new chat.

## LP-029: README Files Need a Maintenance Cadence

README maintenance is not cosmetic. Audit README files at meaningful milestones
and update them deliberately after reviewing their intended purpose.

## LP-030: README Audits Must Distinguish Historical Context From Stale Instructions

Historical references are not automatically stale instructions.

Preserve useful history and refresh an explicit current-checkpoint block rather
than destructively deleting earlier milestones.
