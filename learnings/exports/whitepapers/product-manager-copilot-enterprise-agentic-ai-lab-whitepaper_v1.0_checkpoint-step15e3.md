# Product Manager CoPilot
## Designing a Governed, Traceable and Air-Gap-Ready Enterprise Agentic Development Workflow

**Whitepaper v1.0**  
**Checkpoint:** Step 15E.3 complete  
**Repository commit:** `0b19dd2`  
**Generated:** 7 June 2026  
**Primary author:** Keni Lim, product builder  
**AI copilot role:** research, teaching, prototyping, troubleshooting and documentation support  
**Audience:** product managers, engineering leads, platform teams, AI governance teams, risk teams and colleagues evaluating enterprise AI-development agents  

> This is an offline learning whitepaper and architecture checkpoint. It is not a regulatory-compliance attestation and does not contain confidential workplace data.

---

## Contents

1. Executive summary
2. Why this lab exists
3. North-star product: Product Manager CoPilot
4. The role of a non-technical product builder
5. How to prompt an AI copilot to teach a non-technical PM effectively
6. Environment established in the personal lab
7. Models and routing strategy
8. Toolchain and operating model
9. Why manual scripts were useful before orchestration
10. Evidence-ingestion benchmark
11. Current Docling learning and revalidation item
12. Why OpenSpec remains essential
13. Traceability for high-risk environments
14. Logging and progressive disclosure
15. Interactive review, background jobs and enterprise UX
16. First OpenCode orchestration experiments
17. Screenshot-backed walkthrough
18. Architecture decisions
19. Security boundary
20. Achievements
21. Unresolved items
22. Recommended next steps
23. Compact resumption checkpoint
24. Appendices

---

## Executive summary

This whitepaper records a hands-on learning journey to design and validate an open-source-first, air-gap-ready enterprise agentic development workflow. The lab was driven by a non-technical product manager with basic and dated coding knowledge, working iteratively with an AI copilot.

The north-star product is **Product Manager CoPilot**: a governed project workspace with a ChatGPT-style interface. A product manager should be able to create a project, upload fragmented enterprise evidence, ask grounded questions, detect conflicting or stale information, generate versioned product artefacts, approve changes and hand bounded tasks to development agents.

The problem is not simply document storage. Large enterprise programmes accumulate requirements, decisions and operational knowledge through meetings, emails, PowerPoint decks, Word documents, PDFs, spreadsheets, screenshots, whiteboard photographs, chat exports and departmental repositories. If an AI system cannot retrieve the correct evidence, it can produce plausible but unsupported requirements. The failure chain is straightforward:

```text
missing evidence
→ incomplete retrieval
→ hallucinated requirement
→ wrong design
→ wrong task
→ wrong code
→ failed delivery
```

The lab has now validated a controlled first loop:

```text
synthetic enterprise evidence pack
→ provenance manifest
→ multi-format extraction
→ quality review
→ custom OpenCode orchestrator
→ bounded ingestion-review subagent
→ sanitised public report
→ human review gate
→ Git checkpoint
```

The current checkpoint is **Step 15E.3**, committed as `0b19dd2`. The next learning phase is to inspect and resolve the identified extraction-quality gaps, then normalise evidence, detect conflicts and generate the first OpenSpec proposal.

## 1. Why this lab exists

Enterprise product teams rarely suffer from a shortage of information. They suffer from information fragmentation, inconsistent versions, incomplete retrieval and weak traceability.

A typical large programme generates artefacts across departments and channels:

- meeting notes and minutes
- emails and attachments
- PowerPoint decks
- Word documents
- PDFs and scans
- Excel workbooks
- screenshots
- photographs of whiteboards
- chat exports
- product requirements
- architecture notes
- testing records
- production-incident reports

The operational risk is that an AI assistant may respond confidently even when it did not locate the relevant evidence. That is not a minor inconvenience. It can result in incorrect requirements, incorrect specifications and incorrect development work.

The product-management question is therefore:

> How can an enterprise create governed project memory so that product managers and development agents work from the correct evidence, preserve version history and remain accountable for what was decided?

## 2. North-star product: Product Manager CoPilot

The target product is an internal **Product Manager CoPilot** with a simple conversational interface and a governed evidence pipeline behind it.

A product manager should be able to:

1. create a project workspace
2. upload unstructured files
3. preserve source hashes, provenance and permissions
4. ask questions within the project boundary
5. inspect evidence behind each answer
6. distinguish verified facts, draft interpretations, stale sources and unresolved conflicts
7. generate requirements, designs, user stories, acceptance criteria, tasks and tests
8. upload additional evidence later
9. see the impact of new evidence on existing approved artefacts
10. review a versioned change proposal
11. approve or reject changes
12. hand approved bounded work to development agents
13. trace later incidents back to evidence, requirements, tasks, commits, tests and releases

The model interprets evidence. It does not own truth.

```text
new evidence
→ governed ingestion
→ extraction and normalisation
→ grounded analysis
→ impact assessment
→ proposed change
→ human-readable diff
→ human approval
→ bounded implementation
```

## 3. The role of a non-technical product builder

This lab is deliberately important because it was not built by a full-time software engineer. It was driven by a non-technical product manager with basic and dated coding knowledge.

The AI copilot contributed:

- research
- explanations
- options
- scripts
- troubleshooting
- documentation
- iteration speed

The product builder contributed:

- problem framing
- product taste
- priorities
- constraints
- challenge
- debate
- acceptance criteria
- risk judgement
- sequencing decisions

This was not a one-prompt exercise. The direction changed because the product builder repeatedly questioned the approach:

- Why are we writing manual scripts rather than orchestrating them with an agent?
- Why are we testing mostly Markdown files rather than realistic enterprise formats?
- Why is OpenSpec still relevant after introducing Docling?
- How will we trace a production incident back to an approved but incorrect requirement?
- How will the system remain auditable under regulator oversight?
- Why should a product manager scroll through terminal logs rather than receive a compact review artefact?
- Why should an enterprise user approve every low-risk action rather than run background jobs with policy gates?

The correct lesson is not that engineering expertise is obsolete. The lesson is that a product builder with disciplined requirements and a capable copilot can independently research, prototype and evaluate much more of the delivery stack than before.

## 4. How to prompt an AI copilot to teach a non-technical PM effectively

A major learning point is that the AI copilot itself needs a clear operating contract. The most effective pattern used in this lab was:

```text
explain the purpose in plain English
→ provide one bounded step
→ give copy-paste-safe commands
→ log the output
→ validate before continuing
→ commit and push safe artefacts
→ record the learning point
→ only then move to the next step
```

The educator-copilot should:

- explain why a step matters before asking the user to run it
- assume limited technical knowledge without being patronising
- avoid bundling too many changes into one step
- provide commands that are syntax-safe and easy to copy
- generate downloadable scripts when commands become too long
- distinguish local-only outputs from public-safe artefacts
- stop when evidence is incomplete
- ask for validation before proceeding
- record decisions, failures and learning points offline
- provide a compact checkpoint so the user can safely resume later

This teaching pattern should become part of Product Manager CoPilot. The product should not merely automate tasks. It should explain what is happening, why it is happening, what the user needs to approve and what the system still does not know.

## 5. Environment established in the personal lab

The validated personal-lab environment is:

| Layer | Validated state |
|---|---|
| Host | Windows 10 Pro workstation |
| CPU | AMD Ryzen 9 7900, 12 cores / 24 logical processors |
| RAM | Approximately 31 GB |
| GPU | NVIDIA GeForce RTX 4070 Ti; `nvidia-smi` reported 12,282 MiB total GPU memory |
| Linux | WSL2 Ubuntu 24.04.4 LTS |
| Workspace | `/home/kenilim/projects/enterprise-ai-lab` |
| Editor | VS Code connected to Ubuntu through WSL |
| Containers | Docker Desktop with WSL integration; `hello-world` passed |
| Git | Git 2.43.0 |
| GitHub CLI | Installed and authenticated |
| Python | Python 3.12.3 with project virtual environments |
| Node.js | Node.js 24.16.0 and npm 11.13.0 |
| OpenCode | Version 1.16.2 |
| OpenSpec | Version 1.4.1 |
| Docling | Version 2.97.0 in a dedicated CPU-only virtual environment |
| Repository | Public GitHub repository containing synthetic and sanitised assets only |

The repository is:

`https://github.com/kenilim/enterprise-ai-lab`

## 6. Models and routing strategy

The lab validates a dual-route approach.

### Local-model route

Ollama runs on the Windows host and is accessible from Ubuntu through the Windows host IP. The models visible during the lab were:

| Model | Role | Lab observation |
|---|---|---|
| `qwen3:14b` | Primary local text candidate | Direct OpenAI-compatible inference worked; OpenCode adapter behaviour needed further validation |
| `qwen3-vl:8b` | Vision-language candidate | Intended for future image and screenshot review |
| `gemma4:31b` | Larger local candidate | Available but heavier than the personal GPU budget |
| `mistral:latest` | Lightweight comparison model | Used in diagnostic comparisons |
| `llava:latest` | Older multimodal candidate | Retained for comparison |
| `openhermes:latest` | Older lightweight model | Retained for comparison |
| `llama2:latest` | Older baseline model | Retained for comparison |

### OpenAI route

OpenCode was authenticated through a ChatGPT browser flow and the `openai/gpt-5.4` route was validated. The personal lab uses this route as a development accelerator.

### Architectural rule

OpenAI is not the target enterprise dependency.

```text
personal lab
→ OpenAI model allowed as a development accelerator

future air-gapped environment
→ approved local model behind internal model gateway
```

The model should remain replaceable. The workflow contract, provenance rules, skills and deterministic tools should survive a model swap.

## 7. Toolchain and plain-English operating model

The lab deliberately separates runtime, agent, skill, tool, decision record and specification contract.

| Concept | Plain-English meaning | Current example |
|---|---|---|
| OpenCode | Runtime and interface hosting agents | TUI used for the interactive review |
| Primary agent | Main worker coordinating a workflow | `product-manager-copilot` |
| Subagent | Focused specialist invoked by the primary agent | `ingestion-reviewer` |
| Skill | Reusable operating procedure | `product-manager-copilot-ingestion-review/SKILL.md` |
| Tool | Deterministic executable capability | multi-format extraction script |
| Orchestrator | Agent that sequences skills, subagents and tools | Product Manager CoPilot primary agent |
| `AGENTS.md` | Repository-wide operating rules | public-safe boundaries and approval gates |
| ADR | Architecture Decision Record explaining why a decision was made | `ADR-0013` for background jobs and policy gates |
| OpenSpec | Versioned change contract used before coding | future proposal, design, specs and tasks |
| Git commit | Reviewed durable historical record | checkpoint commits in `main` |

OpenCode custom commands are project-local Markdown templates invoked from the TUI. Custom tools can wrap deterministic scripts, including scripts written in languages other than JavaScript or TypeScript.[2][3]

OpenSpec is retained because the workflow must align humans and coding assistants before code is written.[9]

## 8. Why manual scripts were useful before agent orchestration

The early manual phase was not wasted effort. It established deterministic primitives before delegating work to an agent.

Manual validation revealed:

- Docker permissions and WSL integration needed repair
- Windows-host Ollama needed to bind beyond localhost
- OpenCode-to-Ollama behaviour differed from direct API behaviour
- Docling extraction could succeed without proving extraction quality
- email formats needed explicit handling decisions
- local outputs needed separation from public Git artefacts
- security scans needed to occur before making the repository public

The correct division of labour is:

| Deterministic code | Agent judgement |
|---|---|
| hash files | interpret evidence |
| route formats | classify uncertainty |
| parse documents | detect conflicts |
| write metadata | explain limitations |
| enforce folders | draft change proposals |
| run checks | recommend next actions |

The rule is simple:

```text
use code for repeatable facts
use agents for judgement
```

## 9. Evidence-ingestion benchmark

The lab created a realistic synthetic CircuitFit evidence pack rather than relying only on clean Markdown files.

The benchmark covered:

| Format | Count | Example |
|---|---:|---|
| Markdown | 3 | fixture guide and expected conflicts |
| EML | 2 | product-owner and engineering emails |
| DOCX | 2 | meeting minutes and stale feature request |
| XLSX | 1 | workout requirements matrix |
| PPTX | 1 | mobile-wireframe review |
| PDF | 1 | beta-user feedback summary |
| TXT | 1 | architecture chat export |
| PNG | 2 | whiteboard workflow and screenshot feedback |
| CSV | 1 | fixture manifest |

The first multi-format router benchmark completed 14 of 14 files, with zero failed and zero skipped conversions.

The agent-assisted quality review then produced a more honest classification:

| Result | Count |
|---|---:|
| Pass | 9 |
| Pass with caveats | 4 |
| Fail | 1 |

Key caveats identified by the agent:

- XLSX needs workbook-aware fallback review for sheet structure
- PPTX needs slide-aware fallback review for reliable slide boundaries
- PDF reading order was acceptable but not independently validated
- screenshot OCR remained noisy
- whiteboard PNG failed quality review because OCR content was not reliably surfaced in primary Markdown
- Outlook `.msg` remained deferred in the implemented router

The lesson is critical:

```text
conversion success ≠ extraction quality
```

## 10. Current Docling learning and a revalidation item

Docling is the primary local document-conversion layer because it exposes a unified document representation and supports multiple office, PDF, structured-text and image formats.[6][8]

The lab deliberately created a multi-format router rather than pretending that one parser is sufficient for every enterprise artefact.

A new revalidation item has appeared: current Docling documentation now advertises email formats including EML and MSG on its feature overview page, while the dedicated supported-formats page is less explicit.[6][7]

This does not invalidate the lab history. At the time of implementation, the router handled `.eml` through Python's standard-library parser and deferred `.msg`. The correct action is to re-test native Docling email support before adding `extract-msg` or another fallback.

This itself is a useful learning point:

```text
dependencies evolve
→ documentation can drift
→ capability assumptions must be revalidated
```

## 11. OpenSpec remains essential

Docling and OpenSpec solve different problems.

| Layer | Purpose |
|---|---|
| Docling and format router | Extract evidence from files |
| Normalisation layer | Convert extracted evidence into comparable records |
| Conflict analysis | Detect stale, duplicate, contradictory and missing information |
| OpenSpec | Draft a versioned change proposal before implementation |
| OpenCode development agent | Implement approved bounded tasks |

OpenSpec is not being abandoned. It comes after evidence extraction and quality review.

The intended flow is:

```text
unstructured evidence
→ extraction
→ quality audit
→ normalisation
→ conflict detection
→ OpenSpec proposal
→ human review
→ approved tasks
→ development agent
```

OpenSpec's documented quick path is designed to help people and coding assistants agree on what to build before code is written.[9]

## 12. Traceability for high-risk and auditable environments

Traceability must hold up in a high-risk environment with audit and potential regulator oversight.

The traceability spine is:

```text
source evidence
→ source hash
→ extraction run
→ normalised evidence item
→ requirement
→ design decision
→ user story
→ acceptance criterion
→ implementation task
→ agent run
→ code commit
→ automated test evidence
→ merge approval
→ release artefact
→ production event
→ incident investigation
→ remediation decision
```

A production issue is not always a coding bug.

| Root-cause category | Example |
|---|---|
| Implementation defect | Code violates an approved acceptance criterion |
| Test defect | Test does not reflect the approved requirement |
| Missing requirement | Expected behaviour was never specified |
| Incorrect requirement | Software correctly implements the wrong requirement |
| Ambiguous requirement | Teams reasonably interpreted scope differently |
| Design mismatch | Approved design failed under operational conditions |
| Regression gap | Existing behaviour changed without adequate coverage |
| Production-learning gap | Real usage exposed an unknown scenario |
| Control failure | Required approval or safeguard did not operate |
| Unauthorised change | Change occurred outside approved workflow |

The system should be able to answer:

> Did the code fail the requirement, or did the requirement fail the product?

For a production implementation, local log files are insufficient. Detailed events should be stored in an access-controlled, append-only or immutable audit store with retention controls, tamper detection, separation of duties and incident linkage.

This whitepaper does not claim regulatory compliance. It defines the control model that an enterprise implementation would need to harden, independently assess and govern. Singapore Government ICT secure-development controls provide useful reference points such as secret push protection, branch protections, CI tests, static analysis, dependency scanning, secret detection, environment segregation and SSDLC controls.[11][12]

## 13. Logging and progressive disclosure

Long terminal output is a poor human-review interface.

The lab established a progressive-disclosure model:

```text
full local log
→ structured local manifest
→ compact human-readable summary
→ sanitised report
→ Git diff
→ reviewed commit
```

Review order:

1. compact summary
2. manifest
3. sanitised report
4. Git diff
5. full local log only when needed
6. session export only when needed

The detailed evidence remains available for troubleshooting and audit reconstruction. The compact summary becomes the default review object for a product manager.

Every material run should capture:

- run ID
- project ID
- triggering user
- timestamp
- agent and subagent names
- agent-definition hashes
- model identifier
- skills loaded
- tools invoked
- tool versions
- source hashes
- outputs generated
- warnings
- effective permissions
- human-review status
- approver
- Git commit
- token usage

## 14. Interactive review, background jobs and enterprise UX

The first controlled interactive OpenCode run was valuable because it showed the orchestrator reading rules, loading its workflow, invoking deterministic tooling and pausing at a permission gate.

Interactive review should remain available for:

- first-time workflow validation
- debugging
- exception handling
- high-risk approvals
- investigations

It should not be the default UX for large evidence packs.

The enterprise Product Manager CoPilot should evolve toward:

```text
project upload
→ preflight scan
→ workload estimate
→ background job
→ visible progress and ETA
→ policy-defined safe actions
→ exception queue
→ material human approval gate
→ asynchronous notification
```

The progress view should not rely on file count alone. One OCR-heavy PDF may require more work than dozens of Markdown files.

Recommended metrics:

| Category | Metrics |
|---|---|
| Evidence workload | files, pages, slides, sheets, rows, images, attachments, OCR need |
| Runtime | wall-clock duration, queue time, per-stage duration, retries, failures |
| Model economics | input tokens, output tokens, cache usage, model cost |
| Local infrastructure | CPU, RAM, disk IO, GPU utilisation, peak VRAM, GPU-hours |
| Quality | warnings, exceptions, fallback extractors, ETA accuracy |

The design principle is:

```text
background by default
→ interrupt humans when it matters
```

## 15. First OpenCode orchestration experiments

### Step 15E.1: read-only orchestration dry run

The dry run passed:

| Check | Result |
|---|---|
| OpenCode exited successfully | PASS |
| Session ID detected | PASS |
| Skill reference observed | PASS |
| Ingestion-reviewer reference observed | PASS |
| Git tree remained clean | PASS |
| Sanitised session export | Created |

The agent correctly stated that the benchmark proved routing and conversion, but not extraction accuracy, table fidelity, workbook semantics, slide structure, PDF reading order, OCR quality, email metadata quality, stale-document classification or conflict analysis.

### Step 15E.2: controlled interactive review

The interactive run passed the main controls:

| Check | Result |
|---|---|
| OpenCode session detected | PASS |
| Sanitised export created | PASS |
| Git commit remained unchanged | PASS |
| No forbidden paths modified | PASS |
| Sanitised report created | PASS |
| Skill/subagent reference in sanitised export | REVIEW - evidence capture needs improvement |

The screenshots in this whitepaper show the actual OpenCode interaction. The agent also hit its configured maximum-step limit, which is a useful product-learning point: long-running enterprise workflows need explicit job orchestration rather than a single unconstrained conversational loop.

## 16. Screenshot-backed walkthrough of the first interactive run

The following screenshots are retained as learning artefacts. They show the first controlled interactive Product Manager CoPilot ingestion review inside OpenCode.

### Figure 1. OpenCode command selection for the Product Manager CoPilot ingestion review.

![OpenCode command selection for the Product Manager CoPilot ingestion review.](product-manager-copilot-whitepaper-assets/step15e2_01_command_selection.png)

### Figure 2. The custom command loads the bounded ingestion-review workflow.

![The custom command loads the bounded ingestion-review workflow.](product-manager-copilot-whitepaper-assets/step15e2_02_command_prompt_loaded.png)

### Figure 3. The orchestrator reads AGENTS.md, requirements, governance documents and ADRs before acting.

![The orchestrator reads AGENTS.md, requirements, governance documents and ADRs before acting.](product-manager-copilot-whitepaper-assets/step15e2_03_agent_todo_and_rules.png)

### Figure 4. Approved deterministic ingestion tooling runs inside the controlled agent workflow.

![Approved deterministic ingestion tooling runs inside the controlled agent workflow.](product-manager-copilot-whitepaper-assets/step15e2_04_deterministic_tooling_running.png)

### Figure 5. Interactive permission gate for a bounded tool action during the lab run.

![Interactive permission gate for a bounded tool action during the lab run.](product-manager-copilot-whitepaper-assets/step15e2_05_permission_gate.png)

### Figure 6. The agent reports its work, extraction findings and a configured step-limit constraint.

![The agent reports its work, extraction findings and a configured step-limit constraint.](product-manager-copilot-whitepaper-assets/step15e2_06_agent_summary_max_steps.png)

## 17. Architecture decisions made so far

The repository records architecture decisions as ADRs. An ADR is documentation explaining why a direction was chosen; it is not an agent, a skill or a task.

| ADR | Decision |
|---|---|
| ADR-0001 | Use open-source-first dual-model routing |
| ADR-0002 | Use human-triggered document-to-spec automation |
| ADR-0003 | Define the enterprise project-intelligence workspace vision |
| ADR-0004 | Use a multi-format ingestion router |
| ADR-0005 | Defer Outlook `.msg` ingestion and evaluate later |
| ADR-0006 | Rename the north star to Product Manager CoPilot |
| ADR-0007 | Let agents orchestrate deterministic tools |
| ADR-0008 | Preserve end-to-end traceability for error attribution |
| ADR-0009 | Attribute learning points to human insight, copilot recommendation and experiment evidence |
| ADR-0010 | Target regulator-auditable traceability |
| ADR-0011 | Separate OpenCode primary agent, subagent, skill and tool roles |
| ADR-0012 | Produce compact review summaries for material runs |
| ADR-0013 | Evolve toward background jobs, progress estimation and policy-driven approvals |

ADRs appear before implementation tasks because decisions often need to be settled before coding begins.

## 18. Security boundary and public-repository discipline

The GitHub repository is public, so the lab enforces a strict boundary.

Public-safe:

- synthetic fixtures
- sanitised reports
- reviewed scripts
- ADRs
- README files
- offline learning documents
- screenshots that contain no secrets

Local-only:

- credentials
- OAuth files
- API keys
- `.env` files
- private keys
- confidential workplace data
- raw non-synthetic evidence
- local extraction outputs unless sanitised
- raw OpenCode transcripts
- detailed local logs

A Gitleaks scan was run against Git history and the working directory:

| Check | Result |
|---|---:|
| Git-history findings | 0 |
| Directory findings | 0 |
| Suspicious tracked filenames | 0 |

GitHub-side secret-scanning alerts were unavailable because repository secret scanning was disabled. That remains a visible control gap to address.

## 19. What has been achieved

The lab has achieved the following:

1. established a working WSL2 Ubuntu development environment
2. validated Docker Desktop integration
3. configured Git and GitHub backup
4. established a public-safe repository discipline
5. validated local Ollama connectivity from Ubuntu
6. validated direct OpenAI-compatible inference against local Qwen
7. validated OpenAI GPT-5.4 routing through OpenCode
8. installed OpenSpec and generated OpenCode integration commands and skills
9. installed Docling and supporting Python packages in a CPU-only virtual environment
10. created a realistic multi-format synthetic enterprise evidence pack
11. created provenance and manifest scripts
12. created a deterministic multi-format ingestion router
13. ran a 14-file extraction benchmark
14. performed a format-quality review through a custom OpenCode orchestrator
15. created a Product Manager CoPilot primary agent and ingestion-reviewer subagent
16. added repository-wide `AGENTS.md` rules
17. established local manifests, compact summaries and progressive-disclosure logging
18. documented regulator-auditable traceability expectations
19. committed and pushed safe checkpoints after meaningful learning milestones

## 20. What remains unresolved

The lab is not finished. Key unresolved items are:

- workbook-aware XLSX fallback review
- slide-aware PPTX fallback review
- independent PDF reading-order validation
- screenshot OCR improvement
- whiteboard-image OCR or local VLM fallback
- native Docling EML and MSG revalidation
- recursive email-attachment ingestion
- evidence normalisation schema
- conflict detection and stale-source classification
- evidence register with source-level traceability
- explicit event logging for subagent and skill invocation
- background-job orchestration
- work-unit estimation and ETA
- CPU/GPU telemetry and capacity planning
- first OpenSpec proposal
- bounded implementation flow
- CI/CD controls, regression testing and incident traceability

## 21. Recommended next steps

The immediate roadmap is:

### Step 16: extraction-quality remediation

1. inspect the agent-generated quality report
2. define fallback extractors for XLSX, PPTX, PDF and image OCR
3. revalidate Docling-native email support
4. generate a quality-gate matrix
5. rerun the synthetic benchmark

### Step 17: evidence normalisation and conflict analysis

1. define a normalised evidence-record schema
2. preserve source hashes, extraction references and timestamps
3. classify stale, duplicate, conflicting and unresolved sources
4. generate a traceable evidence register

### Step 18: first OpenSpec proposal

1. use the evidence register and conflicts
2. generate a bounded OpenSpec proposal
3. create design and task artefacts
4. stop for human review

### Step 19: development-agent experiment

1. hand approved tasks to OpenCode
2. implement bounded work
3. run tests
4. trace code and tests back to requirements
5. preserve commit and review history

## 22. A compact resumption checkpoint

When this chat is compacted or moved to a new conversation, use the companion handoff file:

`product-manager-copilot-resume-after-compaction_step15e3.md`

The restart instruction is:

```text
Resume the Product Manager CoPilot enterprise AI development lab from Step 16.
Read the attached whitepaper and resumption checkpoint first.
Do not skip validation gates.
Continue with extraction-quality remediation before evidence normalisation or OpenSpec generation.
```

## Appendix A. Timeline of meaningful checkpoints

| Step | Outcome |
|---|---|
| Toolkit validation | Git, curl, Python, Node, npm and Docker checked |
| Docker repair | Added active user to Docker group and validated `hello-world` |
| OpenCode setup | Installed OpenCode 1.16.2 |
| Ollama networking | Bound Windows-host Ollama and validated Ubuntu access |
| Local-model test | Direct Qwen OpenAI-compatible response validated |
| OpenAI route | GPT-5.4 OpenCode route validated |
| GitHub baseline | Private repository created, then made public after local secret audit |
| OpenSpec setup | Core workflow initialised |
| Docling setup | CPU-only Docling 2.97.0 environment installed |
| Step 15A | Multi-format synthetic evidence benchmark imported |
| Step 15B | Multi-format ingestion router added |
| Step 15C | 14/14 first-pass extraction benchmark completed |
| Step 15D | Product Manager CoPilot ingestion-review skill added |
| Step 15D.2 | Primary orchestrator, reviewer subagent and audit model added |
| Step 15D.3 | Compact logging and progressive-disclosure review added |
| Step 15E.1 | Read-only orchestration dry run passed |
| Step 15E.2 | Controlled interactive quality review passed main controls |
| Step 15E.3 | Agent quality report, screenshots and background-processing learning committed |

## Appendix B. Current repository structure

```text
enterprise-ai-lab/
├── AGENTS.md
├── README.md
├── opencode.json
├── .opencode/
│   ├── agents/
│   │   ├── product-manager-copilot.md
│   │   └── ingestion-reviewer.md
│   ├── commands/
│   │   └── pmcp-ingestion-review.md
│   └── skills/
│       └── product-manager-copilot-ingestion-review/
│           └── SKILL.md
├── docs/
│   ├── architecture-decisions/
│   ├── checkpoints/
│   ├── governance/
│   ├── guides/
│   ├── reports/
│   └── requirements/
├── presentations/
├── projects/
│   ├── 01-doc-to-spec-pilot/
│   └── 02-app-build-pilot/
├── shared/
│   ├── scripts/
│   └── templates/
└── logs/                       # local-only
```

## Appendix C. Reference sources

[1] **OpenCode CLI documentation.** Agent management, sessions, scripted runs and CLI operations.  
https://opencode.ai/docs/cli/
[2] **OpenCode commands documentation.** Custom slash commands stored in project command files.  
https://opencode.ai/docs/commands/
[3] **OpenCode custom tools documentation.** Project-local tools that an LLM can invoke, including wrappers around scripts in other languages.  
https://opencode.ai/docs/custom-tools/
[4] **OpenCode TUI documentation.** Interactive terminal interface and permission-attention behaviour.  
https://opencode.ai/docs/tui/
[5] **OpenCode server documentation.** Headless OpenAPI server and programmatic client architecture.  
https://opencode.ai/docs/server/
[6] **Docling supported formats.** Supported input and output formats including office files, PDFs, images and structured text formats.  
https://docling-project.github.io/docling/usage/supported_formats/
[7] **Docling home documentation.** Current feature overview, including document parsing and unified DoclingDocument representation.  
https://docling-project.github.io/docling/
[8] **Docling DocumentConverter reference.** Main document-conversion entry point and batch-conversion model.  
https://docling-project.github.io/docling/reference/document_converter/
[9] **OpenSpec getting started.** Spec-driven workflow intended to align people and coding assistants before code is written.  
https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md
[10] **OpenSpec supported tools.** Tool-specific integration model created by openspec init.  
https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md
[11] **Singapore Government ICT secure-development control catalogue.** Repository secret protection, branch controls, CI testing, scanning and SSDLC controls.  
https://info.standards.tech.gov.sg/control-catalog/cybersecurity/sd/
[12] **Singapore Government ICT software-supply-chain guidance.** Commit signing, peer review, dependency pinning and related software supply-chain controls.  
https://info.standards.tech.gov.sg/ssp/medium-risk-cloud/
[13] **AGENTS.md open format.** Predictable project instructions for coding agents.  
https://agents.md/
[14] **Agent Skills overview.** SKILL.md as a lightweight format for specialised agent workflows.  
https://agentskills.io/home

