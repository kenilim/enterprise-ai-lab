# Enterprise AI Development Lab

Open-source-first, air-gap-ready evidence-to-application workflow for enterprise agentic product development.

> **Current checkpoint:** Step 14D complete  
> **Status:** Local Docling DOCX smoke test completed. Multi-format synthetic enterprise benchmark is the next step.  
> **Repository:** `kenilim/enterprise-ai-lab`  
> **Primary audience:** Colleagues evaluating enterprise AI development agents in restricted or air-gapped environments.

---

## 1. What this lab is trying to accomplish

Large enterprise programmes generate information across many channels:

- meetings and meeting minutes
- email threads
- PowerPoint decks
- Word documents
- PDFs
- spreadsheets
- screenshots
- photographs of hand-drawn whiteboards
- chat exports
- department-specific folders and repositories
- stale, duplicate and conflicting versions

The practical problem is not simply storing these files. The problem is finding the **correct, current and authorised evidence** before generating product requirements, specifications or development tasks.

A language model cannot be treated as the source of truth. When relevant information is missing or poorly retrieved, the model may generate plausible but unsupported requirements. That can create a chain of failure:

```text
missing evidence
→ hallucinated requirement
→ wrong design
→ wrong implementation task
→ wrong code
→ failed delivery
```

This lab tests a safer workflow:

```text
unstructured evidence
→ immutable local storage
→ hashing and provenance
→ local document extraction
→ source-aware retrieval
→ grounded analysis
→ versioned specifications
→ human approval
→ bounded development tasks
→ automated tests
→ controlled deployment
```

---

## 2. North-star product vision

The target product is an internal **Enterprise Project Intelligence Workspace** with a ChatGPT-style interface.

A product manager should be able to:

1. create a project workspace
2. upload unstructured evidence into the project
3. ask questions within the project
4. inspect source evidence behind each answer
5. generate requirements, design documents, user stories, tasks and test plans
6. upload additional evidence later
7. detect what is new, stale, contradictory or delivery-relevant
8. receive a proposed versioned change plan
9. approve or reject the proposed revision
10. hand approved incremental tasks to development agents

The interface is simple. The underlying controls are not.

### Core design rule

The model interprets evidence. It does not own truth.

```text
new evidence
→ local ingestion
→ impact analysis
→ proposed specification change
→ human-readable diff
→ human approval
→ incremental development tasks
```

New documents must never silently rewrite approved requirements or trigger autonomous code changes.

---

## 3. Target 4D product-development workflow

| Stage | Activities | Required outputs | Human control point |
|---|---|---|---|
| Discover | Ingest evidence, map processes, identify pain points, detect conflicts and missing information | Evidence register, source references, process map, stakeholder map, open questions | Product manager validates problem statement and evidence quality |
| Define | Compile requirements, design decisions, user stories, acceptance criteria, non-functional requirements and risks | Versioned product contract: requirements, design, tasks, stories, acceptance criteria and test traceability | Product manager and reviewers approve before coding |
| Develop | Plan work, implement bounded stories, review code and resolve issues | Branches, commits, diffs, updated tests and documentation | Engineer reviews plan and code before merge |
| Test & Deploy | Run unit, integration, end-to-end, regression, security and deployment checks | Test results, signed artefact, release record, rollback plan and release notes | Risk-based review before staging and production |

### Traceability spine

```text
source evidence
→ requirement
→ user story
→ acceptance criterion
→ implementation task
→ code commit
→ automated test
→ release artefact
```

---

## 4. Personal-lab architecture

```text
raw evidence
→ local immutable copy
→ SHA-256 manifest
→ Docling + format-specific extractors
→ normalised evidence
→ local-model analysis
→ proposed OpenSpec change
→ human approval
→ OpenCode development agent
→ automated tests
→ Docker
```

### Air-gapped enterprise replacement path

```text
raw evidence
→ internal immutable object store
→ local ingestion workers
→ hybrid retrieval with ACL filters
→ internal model gateway
→ approved local models on enterprise GPUs
→ versioned OpenSpec change proposals
→ human approval
→ internal coding agent
→ deterministic CI/CD
```

OpenAI is used only as a personal-lab accelerator for coding. It is not part of the enterprise target architecture.

---

## 5. Current workstation and validated environment

| Layer | Validated state |
|---|---|
| Workstation | AMD Ryzen 9 7900, approximately 32 GB RAM, NVIDIA RTX 4070 Ti with approximately 12 GB VRAM |
| Windows | Windows 10 Pro, 64-bit |
| Linux workspace | WSL2 with Ubuntu 24.04 |
| Workspace path | `/home/kenilim/projects/enterprise-ai-lab` |
| Editor | VS Code connected to Ubuntu through WSL |
| Containers | Docker Desktop integrated with WSL; `hello-world` test passed |
| Python | Python 3.12 with dedicated virtual environments |
| Node.js | Node.js 24 with npm |
| Version control | Git with private GitHub repository |
| Logging | Timestamped logs and checkpoint files |
| Token tracking | OpenCode usage snapshots by project and step |

---

## 6. Models currently available in the lab

### Local Ollama models visible from Ubuntu

| Model | Role | Notes |
|---|---|---|
| `qwen3:14b` | Primary local text model | Validated through direct Ollama API; partially offloaded because model size exceeds available VRAM |
| `qwen3-vl:8b` | Local vision-language candidate | Intended for future screenshots, scans and whiteboard-image experiments |
| `gemma4:31b` | Larger local candidate | Available locally; heavier than current GPU memory |
| `mistral:latest` | Lightweight text-model candidate | Useful for simple comparisons |
| `llava:latest` | Older vision-language candidate | Retained for reference testing |
| `openhermes:latest` | Older local text candidate | Retained for reference testing |
| `llama2:latest` | Older local baseline | Retained for reference testing |

### OpenAI personal-lab development route

| Model | Role | Status |
|---|---|---|
| `openai/gpt-5.4` | OpenCode coding and development accelerator | Validated |
| `openai/gpt-5.2-codex` | Earlier attempted route | Rejected by ChatGPT-account route; not used |

### Important integration lesson

The direct local inference route works:

```text
Ubuntu WSL
→ Windows-hosted Ollama
→ local open-weight model
→ response
```

However, the tested OpenCode-to-Ollama provider path did not reliably surface the final answer.

```text
direct model API working
≠
agent-framework adapter working
```

Every model-server-agent combination must be validated separately.

---

## 7. Installed tooling

| Component | Purpose | Current status |
|---|---|---|
| OpenCode | Development-agent interface | Installed and validated with OpenAI GPT-5.4 |
| OpenSpec | Spec-driven workflow | Installed and initialised in `02-app-build-pilot` |
| Docling | First-pass local document parser | Installed and validated |
| `python-docx` | DOCX-specific fallback extraction | Installed |
| `python-pptx` | PPTX-specific fallback extraction | Installed |
| `openpyxl` | XLSX workbook extraction | Installed |
| `pandas` | Tabular analysis | Installed |
| `pillow` | Image processing | Installed |
| Ollama | Local workstation model runner | Installed on Windows and reachable from WSL |
| Docker | Local packaging and runtime | Installed and validated |
| GitHub CLI | Private repository access | Installed and authenticated |

### Docling virtual environment

```text
projects/01-doc-to-spec-pilot/.venv
```

Installed baseline:

| Package | Version |
|---|---:|
| `docling` | `2.97.0` |
| `python-docx` | `1.2.0` |
| `python-pptx` | `1.0.2` |
| `openpyxl` | `3.1.5` |
| `pandas` | `3.0.3` |
| `pillow` | `12.2.0` |
| `torch` | `2.12.0+cpu` |

CPU-only extraction is intentional for the first baseline. GPU optimisation comes later.

---

## 8. Repository directory guide

```text
enterprise-ai-lab/
├── README.md
├── .gitignore
├── opencode.json
├── configs/
│   └── opencode/
│       └── OpenCode configuration snapshots
├── docs/
│   ├── architecture-decisions/
│   │   └── ADRs explaining major architecture choices
│   ├── checkpoints/
│   │   └── timestamped milestone records
│   ├── reports/
│   │   └── detailed internal reports
│   └── tooling-register.md
├── learnings/
│   ├── current/
│   │   └── evergreen learning report
│   └── exports/
│       └── immutable report snapshots
├── presentations/
│   ├── enterprise-project-intelligence-workspace-presentation_v0.1.html
│   ├── enterprise-project-intelligence-workspace-presentation_latest.html
│   ├── enterprise-project-intelligence-workspace-presentation_bundle_v0.1.zip
│   └── presentation README
├── projects/
│   ├── 01-doc-to-spec-pilot/
│   │   ├── input/
│   │   │   ├── inbox/
│   │   │   ├── canonical-source-pack/
│   │   │   └── generated-synthetic-evidence/
│   │   ├── manifests/
│   │   ├── config/
│   │   ├── work/
│   │   │   ├── extracted/
│   │   │   └── normalized/
│   │   ├── output/
│   │   ├── specs/
│   │   │   ├── draft/
│   │   │   └── approved/
│   │   └── tests/
│   └── 02-app-build-pilot/
│       ├── input/
│       ├── openspec/
│       ├── .opencode/
│       └── future application code
├── shared/
│   ├── scripts/
│   │   ├── capture-opencode-usage.sh
│   │   ├── new-log-path.sh
│   │   ├── generate-source-manifest.py
│   │   ├── extract-docling-document.py
│   │   └── audit-docling-docx-extraction.py
│   └── templates/
└── logs/
    └── timestamped local logs
```

### Folder rules

| Folder | Rule |
|---|---|
| `input/inbox` | Landing zone for new local files |
| `input/canonical-source-pack/raw` | Immutable approved benchmark evidence; local only |
| `work/extracted` | Docling output; local only |
| `output/reports` | Local audit outputs unless explicitly sanitised |
| `docs` | Safe architecture and checkpoint records suitable for GitHub |
| `learnings` | Evergreen report and immutable snapshots |
| `presentations` | Offline HTML deck and export bundle |
| `shared/scripts` | Reusable automation scripts suitable for version control |

---

## 9. Completed experiments and checkpoints

| Step | Result |
|---|---|
| WSL2 setup | Ubuntu 24.04 configured as the default Linux workspace |
| Docker integration | Docker Desktop reachable from Ubuntu; container smoke test passed |
| OpenCode installation | OpenCode installed in Ubuntu |
| Local Ollama routing | Windows-hosted Ollama exposed to Ubuntu WSL |
| Direct local inference | `qwen3:14b` responded successfully through Ollama-compatible API |
| OpenCode local-model test | Adapter issue isolated: reasoning surfaced, final answer unreliable |
| OpenAI route | OpenCode with `openai/gpt-5.4` validated |
| GitHub backup | Private repo created and pushed |
| Token snapshots | Before-and-after usage tracking added |
| OpenSpec | Core workflow initialised: `propose → explore → apply → sync → archive` |
| CircuitFit canonical pack | Raw files copied locally, hashed and excluded from GitHub |
| Docling installation | CPU-only ingestion toolkit installed |
| First Docling smoke test | Native DOCX converted locally to Markdown, JSON and metadata |
| Extraction timing | `0.069 seconds` for the first CircuitFit DOCX |
| Reusable extraction scripts | Docling extraction and DOCX quality-audit scripts committed |
| HTML presentation | 16:9 offline deck added under `presentations/` |

---

## 10. Current learning phase

The lab is still in the **document-ingestion phase**.

```text
CURRENT
multi-format Docling and fallback extraction
→ provenance
→ extraction-quality review

NEXT
normalisation
→ source register
→ stale-document detection
→ conflict detection
→ impact analysis

THEN
OpenSpec change proposal
→ human approval
→ incremental development tasks

THEN
OpenCode implementation
→ automated tests
→ Docker

LATER
Project Intelligence Workspace web UI
```

OpenSpec has not been abandoned. It is deliberately downstream of evidence extraction.

---

## 11. Synthetic enterprise benchmark

The next benchmark simulates the real enterprise environment rather than a clean Markdown pack.

Expected synthetic files:

| File type | Purpose |
|---|---|
| `.eml` emails | late requirements and conflicting stakeholder requests |
| `.docx` meeting minutes | headings, bullets, tables and embedded whiteboard image |
| `.xlsx` requirements matrix | multiple worksheets, structured tables and conflict register |
| `.pptx` design review | embedded UI screenshot, bullet notes and decision table |
| `.pdf` feedback summary | paragraphs, table and embedded screenshot |
| `.txt` chat export | unstructured architecture discussion |
| `.docx` stale draft | superseded requirements that must not override current scope |
| `.png` whiteboard image | visual workflow with handwritten-style late questions |
| `.png` UI screenshot | visual design evidence |

The benchmark should test:

```text
Can the pipeline extract content accurately?
Can it preserve source references?
Can it detect embedded images and tables?
Can it identify stale and conflicting evidence?
Can it avoid silently modifying approved scope?
Can it draft a versioned OpenSpec change proposal?
```

---

## 12. OpenSpec role in the journey

Docling and OpenSpec solve different problems.

| Component | Job |
|---|---|
| Docling | Read and structure messy files |
| Format-specific extractors | Catch file-type-specific details |
| Retrieval layer | Find relevant evidence with provenance and ACL filters |
| Local model | Summarise, classify, compare and propose changes |
| OpenSpec | Convert approved changes into a versioned delivery contract |
| OpenCode | Implement approved tasks |
| CI/CD | Validate software against acceptance criteria |

The controlled bridge is:

```text
Docling output
→ evidence register
→ conflict detection
→ impact analysis
→ OpenSpec proposal
→ human approval
→ bounded OpenCode tasks
```

---

## 13. Security boundary

Use only:

- synthetic data
- public information
- sanitised documents

Do not place confidential workplace documents in this personal lab.

Raw evidence, extraction outputs, credentials, model weights and runtime logs remain excluded from GitHub unless explicitly reviewed and sanitised.

---

## 14. Logging and checkpoint convention

Log filenames follow:

```text
YYYYMMDD_HHMMSS_stepXX_component_action.log
```

Each completed step should end with:

```text
review Git status
→ stage only safe files
→ inspect staged files
→ commit
→ push
→ confirm clean working tree
```

---

## 15. Version history

| Version | Date | Summary |
|---|---|---|
| `0.1` | 7 June 2026 | Initial repository scaffold, pilot folders, logging convention and security boundary |
| `0.2` | 7 June 2026 | Expanded README with product vision, architecture, model inventory, directory guide, completed experiments, OpenSpec role and current roadmap |

---

## 16. Immediate next steps

1. Load the deterministic multi-format CircuitFit synthetic enterprise evidence pack.
2. Hash and register every synthetic file.
3. Run local Docling extraction across DOCX, XLSX, PPTX, PDF, email, TXT and PNG files.
4. Apply format-specific fallbacks where Docling output is incomplete.
5. Record source references, extracted structures and warnings.
6. Detect stale documents, contradictions and proposed enhancements.
7. Generate the first OpenSpec change proposal.
8. Review the proposal before development work begins.

---

## 17. Presentation

The offline HTML presentation is stored under:

```text
presentations/enterprise-project-intelligence-workspace-presentation_latest.html
```

Open it locally in a browser and press `F` for fullscreen.
