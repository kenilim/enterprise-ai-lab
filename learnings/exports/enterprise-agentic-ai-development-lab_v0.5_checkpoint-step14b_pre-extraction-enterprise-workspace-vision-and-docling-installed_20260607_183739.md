**Enterprise Agentic AI  
Development Lab**

Open-Source-First, Air-Gap-Ready Evidence-to-Application Workflow

**Evergreen Learning Report**

Version 0.1 \| 7 June 2026

*Prepared for internal knowledge sharing*

| **Primary learning focus** | Convert unstructured documents into traceable, approved specifications before coding begins.                     |
|----------------------------|------------------------------------------------------------------------------------------------------------------|
| **Development approach**   | 4D product lifecycle, spec-driven development, user stories, test-driven validation and human approval gates.    |
| **Enterprise constraint**  | Prefer open-source and air-gap-compatible components; use OpenAI only as a personal-lab development accelerator. |

# Document Control

| **Field**         | **Value**                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Document status   | Evergreen working document                                                                                       |
| Current version   | 0.1                                                                                                              |
| Date              | 7 June 2026                                                                                                      |
| Owner             | Keni Lim                                                                                                         |
| Update rule       | Revise this document after each meaningful learning point, architecture decision or validated experiment.        |
| Intended audience | Colleagues assessing enterprise agentic product-development approaches in air-gapped or restricted environments. |

## Version History

| **Version** | **Date**    | **Summary of change**                                                                                                                                           |
|-------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.1         | 7 June 2026 | Initial export. Captures the lab purpose, target workflow, completed setup, local-model experiment results, GitHub-backup status and next implementation steps. |

# Contents

1\. Executive Summary

2\. What We Are Trying to Build

3\. Target 4D Product-Development Workflow

4\. Comparison with the Current Proposed Squad Design

5\. Open-Source-First Architecture

6\. Hands-On Lab Environment Completed So Far

7\. Experiment Results and Learning Points

8\. Unstructured-Document Ingestion Strategy

9\. Specification, User-Story and Test Traceability Model

10\. Human-Triggered Automation and Future Agent Roles

11\. GitHub Backup and Repository Strategy

12\. Logging and Token-Usage Measurement

13\. Roadmap

Appendix A. Current Folder Structure

Appendix B. Tooling Register

Appendix C. Source References

# 1. Executive Summary

This lab is a hands-on investigation into the best way to convert messy
enterprise evidence - such as emails, PDFs, Word files, PowerPoint
decks, spreadsheets, scanned pages and screenshots - into a workable,
tested application through an agent-assisted product-development
lifecycle.

The central design principle is that raw evidence must not flow directly
into autonomous coding. The system should first convert unstructured
information into a versioned product contract: requirements, design
decisions, implementation tasks, user stories, acceptance criteria and
test cases. Humans approve this contract before a coding agent begins
implementation.

The personal lab deliberately uses an open-source-first architecture so
that most of the workflow can later be reproduced inside an air-gapped
enterprise environment. OpenAI models are treated as a temporary
personal-lab exception for development acceleration, not as a dependency
of the enterprise target state.

The experiment has already validated the Windows-to-WSL development
environment, Docker integration, local Ollama inference, GPU use,
structured logging and token snapshots. It has also surfaced a real
integration defect: local Ollama models respond correctly through direct
API calls, but the tested OpenCode-to-Ollama adapter does not reliably
surface final responses. This is a useful enterprise lesson:
model-server validation and agent-framework validation are separate
gates.

# 2. What We Are Trying to Build

The objective is an evidence-to-application workflow that mirrors a real
product-development lifecycle rather than a one-shot 'vibe coding'
workflow.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Unstructured evidence<br />
PDFs | DOCX | PPTX | XLSX | emails | scans | screenshots<br />
|<br />
v<br />
Local document ingestion and normalization<br />
|<br />
v<br />
Evidence-backed product definition<br />
requirements.md | design.md | tasks.md | user stories | acceptance
criteria<br />
|<br />
v<br />
Human product-manager approval<br />
|<br />
v<br />
Planning agent<br />
implementation plan | dependencies | risk assessment | test plan<br />
|<br />
v<br />
Coding agent<br />
implements one approved story at a time<br />
|<br />
v<br />
Deterministic tests and quality gates<br />
unit | integration | end-to-end | security | regression<br />
|<br />
v<br />
Human review, merge and controlled deployment</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The immediate learning focus is the first half of the flow: how to read
unstructured documents reliably, preserve source evidence, draft
specifications locally and convert the resulting work into small user
stories that can be built and tested.

# 3. Target 4D Product-Development Workflow

The lab uses the traditional 4D structure - Discover, Define, Develop,
and Test & Deploy - but adds traceability, explicit approval gates and
deterministic quality controls.

| **4D stage**  | **Primary activities**                                                                                            | **Required outputs**                                                                                  | **Human control point**                                                    |
|---------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Discover      | Ingest evidence, identify business processes, map pain points, detect conflicts and missing information.          | Evidence register, source references, process map, stakeholder map, open questions.                   | Product manager validates the problem statement and evidence quality.      |
| Define        | Compile requirements, design decisions, user stories, acceptance criteria, non-functional requirements and risks. | Versioned product contract: requirements.md, design.md, tasks.md, user stories and test traceability. | Product manager and relevant reviewers approve the contract before coding. |
| Develop       | Plan the work, implement bounded stories, review code and resolve issues.                                         | Feature branches, commits, merge requests, code diffs, updated tests and documentation.               | Engineer reviews the plan and code changes before merge.                   |
| Test & Deploy | Execute unit, integration, end-to-end, regression, security and deployment checks.                                | Test results, signed release artefact, deployment record, rollback plan and release notes.            | Risk-based review before staging and production deployment.                |

The key control is the traceability spine:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Source evidence<br />
-&gt; Requirement<br />
-&gt; User story<br />
-&gt; Acceptance criteria<br />
-&gt; Implementation task<br />
-&gt; Code commit<br />
-&gt; Test case<br />
-&gt; Release</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 4. Comparison with the Current Proposed Squad Design

The current proposed squad design is directionally strong. It already
separates product-manager-led discovery from engineer-led development,
uses human review gates, includes planning and development agents, and
recognises testing, regression, security and deployment activities.

The main improvement is to make the workflow less agent-centric and more
contract-centric. The strongest enterprise pattern is not a large swarm
of loosely governed agents. It is a governed evidence plane, a versioned
product contract, bounded engineering agents, deterministic CI/CD and
end-to-end traceability.

| **Area**           | **Current proposed approach**                                                               | **Recommended refinement**                                                                                                                                |
|--------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Discovery          | Unstructured documents and user research flow into product agents and prototype generation. | Add a governed evidence layer first: immutable source files, metadata, classification, access controls, hashes, parsing confidence and source citations.  |
| Definition         | PRD, prototype and user stories are created before development.                             | Formalise a versioned product contract in Git: requirements, design, tasks, non-functional requirements, ADRs, acceptance criteria and test traceability. |
| Agent design       | Many named agents and subagents perform specialist activities.                              | Use a smaller set of reusable roles: product, planner, builder, reviewer, test, security and resolver. Treat specialist capabilities as skills or tools.  |
| Testing            | Test, code-fix, regression, security and performance agents are present.                    | Make CI/CD controls deterministic. Agents may propose fixes, but cannot waive failures or self-approve.                                                   |
| Deployment         | Human reviews precede test and production deployment.                                       | Add signed artefacts, SBOMs, release provenance, rollback, monitoring and policy enforcement.                                                             |
| Air-gap operations | Open-source engineering tools and dedicated GPU infrastructure are assumed.                 | Add a controlled import lane for models, packages, vulnerability feeds, containers and approved tool versions.                                            |

# 5. Open-Source-First Architecture

The standing rule for the lab is: other than OpenAI models used
temporarily for personal development, prefer open-source components that
can be imported, installed and operated inside an air-gapped enterprise
environment.

Open-weight models must still undergo licence review. 'Open-weight' is
not automatically equivalent to 'open source'.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PERSONAL LAB<br />
Local evidence route:<br />
documents -&gt; Docling + format-specific extractors -&gt; local model
-&gt; draft specs<br />
<br />
Development route:<br />
approved synthetic or sanitised specs -&gt; OpenCode -&gt; OpenAI coding
model -&gt; code<br />
<br />
ENTERPRISE TARGET<br />
Local evidence route:<br />
documents -&gt; same local ingestion stack -&gt; approved local model
-&gt; draft specs<br />
<br />
Development route:<br />
approved specs -&gt; OpenCode or approved coding interface<br />
-&gt; internal model gateway<br />
-&gt; validated local coding model on enterprise GPUs</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 5.1 Current and Candidate Components

| **Component**             | **Role**                           | **Classification**       | **Enterprise position** | **Notes**                                                                         |
|---------------------------|------------------------------------|--------------------------|-------------------------|-----------------------------------------------------------------------------------|
| OpenCode                  | Coding-agent interface             | Open source              | Candidate               | Supports multiple providers, local models, permissions and project instructions.  |
| Docling                   | Document parsing and normalization | Open source              | Candidate               | Supports multiple document formats and advanced PDF understanding.                |
| OpenSpec                  | Spec-driven workflow               | Open source              | Candidate               | Provides proposal -\> specs -\> design -\> tasks -\> implement workflow.          |
| Python                    | Local orchestration                | Open source              | Candidate               | Used for deterministic ingestion scripts, logging and fallbacks.                  |
| pandas / openpyxl         | Spreadsheet extraction             | Open source              | Candidate               | Use when spreadsheet semantics, formulas or workbook structure matter.            |
| python-docx / python-pptx | Office-format fallbacks            | Open source              | Candidate               | Use when embedded objects or Office-specific structure need explicit extraction.  |
| Ollama                    | Workstation model runner           | Local-lab convenience    | Evaluate                | Useful for local experiments; enterprise inference server may differ.             |
| OpenAI models             | Development acceleration           | Proprietary exception    | Replace                 | Personal lab only. Do not make the enterprise workflow depend on it.              |
| ChatGPT OAuth plugin      | Personal OpenCode authentication   | Personal-lab exception   | Replace                 | Not an enterprise authentication design.                                          |
| Docker Desktop / WSL2     | Windows workstation development    | Personal-lab convenience | Replace or review       | Enterprise target should use approved Linux infrastructure and container runtime. |

# 6. Hands-On Lab Environment Completed So Far

| **Layer**               | **Validated state**                                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| Workstation             | Windows PC with AMD Ryzen 9 7900, approximately 32 GB RAM and NVIDIA RTX 4070 Ti with approximately 12 GB VRAM.        |
| Linux development layer | WSL2 with Ubuntu 24.04 installed and used as the development workspace.                                                |
| Workspace               | /home/kenilim/projects/enterprise-ai-lab                                                                               |
| Editor                  | VS Code connected to Ubuntu through WSL.                                                                               |
| Containers              | Docker Desktop integrated with Ubuntu; hello-world container test succeeded.                                           |
| Developer tooling       | Git, Python, pip, virtual environments, Node.js, npm and OpenCode installed.                                           |
| Local model serving     | Windows-hosted Ollama exposed to WSL; local models visible from Ubuntu.                                                |
| Cloud coding route      | OpenCode authenticated to OpenAI through a personal ChatGPT OAuth route for personal-lab development only.             |
| Governance scaffolding  | Open-source-first rule, tooling register, architecture-decision records, timestamped logs and usage snapshots created. |

# 7. Experiment Results and Learning Points

## 7.1 Local Inference Path

The direct local inference route works:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Ubuntu WSL<br />
-&gt; Windows Ollama API<br />
-&gt; local open-weight model<br />
-&gt; RTX 4070 Ti</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The qwen3:14b model was loaded through Ollama. The experiment recorded
approximately 8.4 GB loaded into VRAM and approximately 14.9 GB total
model size, indicating that the model exceeds available VRAM and is
likely partially offloaded. This is acceptable for learning but may
reduce speed.

## 7.2 OpenCode-to-Ollama Adapter Defect

Direct Ollama native and OpenAI-compatible API requests succeeded,
including streaming responses. However, OpenCode 1.16.2 did not reliably
surface the final assistant answer when using the tested Ollama provider
route.

An isolated raw-event test showed reasoning events but no final
assistant-text event. The official Ollama-generated OpenCode payload
used the same provider adapter and endpoint style as the manual
configuration. The decision was to retain Ollama for direct local
scripts and use OpenAI models temporarily for OpenCode-driven
development.

Enterprise implication: validate each model-server-agent combination
independently. A model working through curl is not proof that it works
correctly through an agent framework.

## 7.3 Usage Baseline

| **Metric**                    | **Recorded baseline**                                                                                |
|-------------------------------|------------------------------------------------------------------------------------------------------|
| Sessions                      | 5                                                                                                    |
| Messages                      | 10                                                                                                   |
| Input tokens                  | 20.3K                                                                                                |
| Output tokens                 | 360                                                                                                  |
| Primary recorded local models | ollama/qwen3:14b and ollama/mistral:latest                                                           |
| Reported monetary cost        | \$0.00 for local inference                                                                           |
| Caveat                        | This baseline includes earlier troubleshooting sessions and is not yet a clean per-project baseline. |

## 7.4 Learning Points to Date

| **ID** | **Learning point**                 | **Practical implication**                                                                                      |
|--------|------------------------------------|----------------------------------------------------------------------------------------------------------------|
| LP-001 | Linux-style development on Windows | WSL2 and Ubuntu provide a practical Linux workspace on a Windows PC.                                           |
| LP-002 | Containerised development          | Docker Desktop works from Ubuntu after enabling integration and Docker-group permissions.                      |
| LP-003 | Local model serving                | Windows Ollama can serve local models to WSL and use the RTX 4070 Ti.                                          |
| LP-004 | Adapter compatibility              | Direct model APIs and agent-framework adapters require separate validation.                                    |
| LP-005 | Dual-provider configuration        | OpenCode can retain a local provider while using an OpenAI route for personal development.                     |
| LP-006 | Workspace organisation             | Logs, shared assets and pilot projects must be separated early.                                                |
| LP-007 | Human-triggered automation         | A deterministic script should process new documents before adding an autonomous agent wrapper.                 |
| LP-008 | Backup discipline                  | Local files are not backed up until Git is initialised, a remote repository is created and changes are pushed. |

# 8. Unstructured-Document Ingestion Strategy

Docling is the preferred first-pass ingestion engine because it supports
PDF, DOCX, XLSX, PPTX and common image formats, and it provides advanced
PDF understanding such as page layout, reading order and table
structure. It can export structured outputs such as Markdown and
lossless JSON.

Docling should not be treated as the only extractor. The production
pattern is a layered ingestion pipeline with format-specific fallbacks
and validation.

| **Input type**                             | **First-pass treatment**                                    | **Fallback or validation**                                                                                       |
|--------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Native PDF                                 | Docling text, layout, reading order and tables              | Validate extracted tables and page references against rendered pages.                                            |
| Scanned PDF or image                       | Docling OCR and image handling                              | Use OCR confidence thresholds; send visual extracts to a local vision model where needed.                        |
| DOCX                                       | Docling conversion                                          | Use python-docx to inspect embedded images, tables, paragraphs and relationships when fidelity matters.          |
| PPTX                                       | Docling conversion                                          | Use python-pptx to inspect slides, shapes, speaker notes and embedded media where needed.                        |
| XLSX                                       | Docling conversion for broad ingestion                      | Use openpyxl and pandas for workbook structure, sheet-level semantics, formulas, merged cells and data analysis. |
| Charts, OLE objects and embedded artefacts | Preserve original file and export references where possible | Use file-type-specific inspection; do not assume a generic parser captured all semantics.                        |

## 8.1 Evidence Package

Each input file should become an evidence package rather than a loose
text chunk:

- Original immutable file

- File hash and metadata

- Classification and access-control metadata

- Structured extraction in JSON

- Readable Markdown rendering

- Exported images, tables and figures where relevant

- Source references at document, page, slide, sheet and section level

- Extraction warnings, OCR confidence and fallback decisions

# 9. Specification, User-Story and Test Traceability Model

The target workflow is spec-driven and test-driven. The coding agent
must build from approved user stories, and tests must verify the
acceptance criteria attached to those stories.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>EVID-0042 Source document, page or sheet reference<br />
|<br />
REQ-0137 Requirement<br />
|<br />
STORY-0088 User story<br />
|<br />
AC-0088-1 Acceptance criterion<br />
|<br />
TASK-0214 Implementation task<br />
|<br />
TEST-0045 Unit / integration / end-to-end test<br />
|<br />
COMMIT Code change<br />
|<br />
RELEASE Deployment artefact</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

When a test fails, the system should not blindly patch code until CI
turns green. It should check whether the failure arises from
implementation, test design, requirement ambiguity or a stale plan.

| **Failure type**             | **Correct response**                                                                   |
|------------------------------|----------------------------------------------------------------------------------------|
| Implementation defect        | Coding agent proposes a bounded code fix and reruns the relevant tests.                |
| Incorrect or incomplete test | Reviewer checks the acceptance criterion and updates the test only with approval.      |
| Ambiguous user story         | Return to the requirement and clarify the story before continuing.                     |
| Design mismatch              | Revisit design.md and update the implementation plan before making broad code changes. |
| Requirement change           | Update the requirement, dependent stories, design, tasks and tests together.           |

## 9.1 Minimum Versioned Product Contract

- requirements.md - business requirements, scope, constraints,
  assumptions and exclusions

- design.md - architecture, interfaces, data model, security
  considerations and design decisions

- tasks.md - small implementation tasks linked to stories

- user-stories.md - story IDs, acceptance criteria and dependencies

- test-plan.md - test cases linked to story and requirement IDs

- traceability.csv or traceability.json - evidence-to-release linkage

- ADRs - architecture decisions and rationale

# 10. Human-Triggered Automation and Future Agent Roles

New files should eventually trigger a repeatable local document-to-spec
pipeline after an explicit human action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>New document arrives<br />
-&gt; human clicks Run or invokes a command<br />
-&gt; system hashes files and identifies changes<br />
-&gt; Docling and fallbacks parse locally<br />
-&gt; local model drafts proposed spec changes<br />
-&gt; Git diff and review summary generated<br />
-&gt; human approves or rejects<br />
-&gt; approved specs become development input</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The first implementation should be a deterministic Bash or Python
script. An agent such as Hermes may later invoke that script as a
constrained skill after a human request. A durable workflow engine can
be introduced later for retries, long-running jobs, state and approval
checkpoints.

| **Automation level** | **Trigger**                       | **Implementation pattern**                                                 |
|----------------------|-----------------------------------|----------------------------------------------------------------------------|
| Level 1              | Human command                     | Deterministic local script                                                 |
| Level 2              | Human button click                | Small internal UI or approved workflow interface                           |
| Level 3              | Human asks an agent               | Constrained agent skill that invokes the deterministic script              |
| Level 4              | Event detected with approval gate | Durable workflow engine with audit trail, policy checks and human approval |

# 11. GitHub Backup and Repository Strategy

As of this version, the lab is not yet backed up to GitHub. Git is
installed, but the root workspace has not been initialised as a Git
repository, a root .gitignore is not present, Git user details are not
configured and the GitHub CLI is not installed.

The recommended immediate approach is one private root repository for
the learning lab. Mature applications can later move into separate
repositories.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>enterprise-ai-lab (private GitHub repository)<br />
docs/<br />
configs/<br />
shared/<br />
projects/<br />
README.md<br />
opencode.json<br />
<br />
Do not push:<br />
OAuth credentials | auth.json | .env files | private keys<br />
raw workplace documents | sensitive evidence extracts | model
weights</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 12. Logging and Token-Usage Measurement

The experiment uses timestamped filenames so that each log can be
correlated to a step and component.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>YYYYMMDD_HHMMSS_stepXX_component_action.log<br />
<br />
Examples:<br />
20260607_045841_opencode-step9-debug.log<br />
20260607_053513_step10c_workspace_structure_setup.log<br />
20260607_053741_step10d_02-app-build-pilot_baseline_opencode_stats.log</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Token usage must be measured per project and per milestone. Cloud and
local routes should be logged separately.

| **Route**            | **Metrics to capture**                                                                                                                |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| OpenCode with OpenAI | Project, step, phase, session count, input tokens, output tokens, cache read/write, model, reported cost and approval decisions.      |
| Direct local Ollama  | Project, step, source file, prompt tokens, output tokens, model, total duration, load duration and optional GPU utilisation snapshot. |
| Document ingestion   | File count, pages/slides/sheets processed, extraction duration, warning count, OCR confidence and fallback usage.                     |

# 13. Roadmap

| **Priority** | **Next action**                                                                                                                   | **Purpose**                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Immediate    | Configure Git identity, install GitHub CLI, create a root .gitignore, initialise a root Git repository and push a private backup. | Protect the work before continuing.                                             |
| Immediate    | Capture a clean project-specific usage baseline.                                                                                  | Ensure future token deltas are meaningful.                                      |
| Next         | Validate the OpenAI-backed OpenCode development route with a controlled test.                                                     | Confirm the coding-agent path.                                                  |
| Next         | Install and initialise OpenSpec.                                                                                                  | Create a formal proposal -\> specs -\> design -\> tasks -\> implement workflow. |
| Next         | Install Docling and fallback extractors inside the document-to-spec pilot.                                                        | Process synthetic PDFs, DOCX, PPTX, XLSX and images locally.                    |
| Next         | Build a deterministic run-doc-to-spec script.                                                                                     | Create human-triggered local automation.                                        |
| Later        | Wrap the deterministic pipeline with a constrained agent skill.                                                                   | Test operator-facing automation without losing control.                         |
| Later        | Map all workstation shortcuts to air-gapped enterprise equivalents.                                                               | Create the enterprise deployment blueprint.                                     |

# Appendix A. Current Folder Structure

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>enterprise-ai-lab/<br />
configs/<br />
opencode/<br />
docs/<br />
architecture-decisions/<br />
checkpoints/<br />
reports/<br />
logs/<br />
ingestion/<br />
opencode/<br />
setup/<br />
usage/<br />
shared/<br />
sample-documents/<br />
scripts/<br />
templates/<br />
projects/<br />
01-doc-to-spec-pilot/<br />
02-app-build-pilot/<br />
opencode.json<br />
README.md</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Appendix B. Tooling Register

The tooling register is maintained locally under
docs/tooling-register.md. Each new component should record its
repository, licence, version, offline installation approach, telemetry
behaviour, security considerations and enterprise replacement if
applicable.

| **Decision test** | **Question**                                                                                                |
|-------------------|-------------------------------------------------------------------------------------------------------------|
| Licence           | Can the component be legally imported, modified and operated in the target enterprise environment?          |
| Offline operation | Can it run without internet access after controlled import?                                                 |
| Supply chain      | Can packages, containers, model weights and vulnerability data be mirrored internally?                      |
| Observability     | Can actions, model calls, tool calls, diffs and approvals be logged?                                        |
| Replaceability    | Can a personal-lab shortcut be swapped for an approved enterprise component without rewriting the workflow? |

# Appendix C. Source References

| **Ref** | **Source**                                                               | **URL**                                                            |
|---------|--------------------------------------------------------------------------|--------------------------------------------------------------------|
| \[1\]   | Docling supported formats                                                | https://docling-project.github.io/docling/usage/supported_formats/ |
| \[2\]   | Docling documentation overview                                           | https://docling-project.github.io/docling/                         |
| \[3\]   | Docling CLI image export modes                                           | https://docling-project.github.io/docling/reference/cli/           |
| \[4\]   | OpenCode models and local-model support                                  | https://opencode.ai/docs/models/                                   |
| \[5\]   | OpenCode permissions                                                     | https://opencode.ai/docs/permissions/                              |
| \[6\]   | OpenCode project rules through AGENTS.md                                 | https://opencode.ai/docs/rules/                                    |
| \[7\]   | OpenSpec concepts: proposal -\> specs -\> design -\> tasks -\> implement | https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md  |
| \[8\]   | GitHub CLI authentication quickstart                                     | https://docs.github.com/en/github-cli/github-cli/quickstart        |
| \[9\]   | GitHub CLI repository creation                                           | https://cli.github.com/manual/gh_repo_create                       |
| \[10\]  | GitHub remote repositories                                               | https://docs.github.com/articles/about-remote-repositories         |

Note: This report is an evergreen snapshot. Update the version history,
completed learning points, architecture decisions and roadmap after each
validated milestone.

## LP-009: Private GitHub Backup Established

### What Was Tested

The root `enterprise-ai-lab` workspace was reviewed, staged, scanned for obvious
secret files, committed locally and pushed to a private GitHub repository.

### Result

The private GitHub repository is:

`kenilim/enterprise-ai-lab`

The default branch is:

`main`

The first backup commit is:

`338accb chore: initialise enterprise AI development lab`

### Repository Boundary

Only the contents of:

`/home/kenilim/projects/enterprise-ai-lab`

are tracked.

The wider parent folder:

`/home/kenilim/projects`

is not part of the repository.

### Security Controls Applied

- Root `.gitignore` created
- OAuth credentials excluded
- `.env`, private-key and authentication files excluded
- Raw evidence folders excluded
- Runtime logs excluded except for folder placeholders
- Model-weight files excluded
- Windows `Zone.Identifier` metadata files removed
- Nested pilot repositories flattened into one root learning repository

### Learning Point

A local Git repository is not a backup until:

1. files are staged
2. files are reviewed
3. secrets are excluded
4. a commit is created
5. a private remote repository exists
6. the commit is pushed successfully
7. repository visibility is verified

### Current Checkpoint

`Step 10E4 complete: private GitHub backup established`

### Next Planned Action

Capture a clean per-project token baseline and run the first controlled
OpenAI-backed OpenCode request.

## LP-010: OpenAI-Backed OpenCode Development Route Validated

### What Was Tested

A controlled OpenCode request was sent through the personal ChatGPT OAuth route
using:

`openai/gpt-5.4`

The prompt instructed the model to return a fixed text response without
creating files, invoking tools or running shell commands.

### Result

The route succeeded and returned:

`OPENAI GPT54 OPENCODE ROUTE WORKS.`

No tracked project files were modified.

### Validated Route

`VS Code in Ubuntu WSL → OpenCode → ChatGPT OAuth plugin → OpenAI GPT-5.4`

### Token Usage

| Metric | Recorded value |
|---|---:|
| Model | `openai/gpt-5.4` |
| Messages | 1 |
| Input tokens | approximately 2.3K |
| Output tokens | 29 |
| Cache read | approximately 4.1K |
| Cache write | 0 |
| Reported cost | `$0.0000` |

The monetary value is not treated as an invoice because the route uses ChatGPT
OAuth rather than metered API billing.

### Learning Point

A configured model catalogue is not an entitlement check.

The first tested model:

`openai/gpt-5.2-codex`

appeared in the OpenCode model list but was rejected for the ChatGPT-account
route.

The currently validated personal-development model is:

`openai/gpt-5.4`

### Enterprise Implication

Model availability, authentication and end-to-end response handling must be
validated through an active smoke test.

A model appearing in a static provider catalogue does not prove that it is
authorised or operational.

### Current Checkpoint

`Step 11B complete: OpenAI-backed OpenCode development route validated`

### Next Planned Action

Install and initialise OpenSpec inside the app-build pilot to establish the
spec-driven workflow:

`proposal → specs → design → tasks → implementation`

## LP-011: OpenSpec Core Workflow Initialised for the App-Build Pilot

### What Was Tested

OpenSpec was installed globally inside Ubuntu and initialised only inside:

`projects/02-app-build-pilot`

OpenSpec telemetry was disabled to align the personal lab with the intended
privacy-sensitive and air-gapped enterprise operating model.

### Generated OpenCode Integration

OpenSpec created the OpenCode-specific integration under:

`projects/02-app-build-pilot/.opencode`

The core workflow contains:

- `opsx-propose`
- `opsx-explore`
- `opsx-apply`
- `opsx-sync`
- `opsx-archive`

Matching skills were also generated.

### Generated OpenSpec Structure

The project now contains:

`openspec/specs`

`openspec/changes`

`openspec/changes/archive`

The folders were initially empty. `.gitkeep` placeholders were added so that
the baseline structure is preserved in Git before the first proposal exists.

### Role in the Target Workflow

OpenSpec becomes the structured handoff layer between product definition and
coding:

`approved intent → proposal → specs → design → tasks → human review → implementation → archive`

### Learning Point

The agent should not begin coding from a loose conversation.

The coding agent should implement tasks that are traceable to reviewed
specifications and user stories.

### Current Checkpoint

`Step 12A complete: OpenSpec core workflow initialised for the app-build pilot`

### Next Planned Action

Create the first synthetic application scenario and use OpenSpec to generate
the first proposal, design, implementation tasks, user stories and acceptance
criteria before any code is written.

## LP-012: Enterprise Project Intelligence Workspace Vision

### Enterprise Problem

Large enterprise programmes create fragmented knowledge across meetings,
minutes, emails, PowerPoint decks, Word documents, PDFs, spreadsheets,
screenshots, photographs of hand-drawn whiteboards and department-specific
repositories.

The challenge is not simply document storage.

The challenge is identifying the correct, current and authorised evidence before
generating requirements, specifications or implementation tasks.

### Failure Chain

When retrieval fails, a language model may generate a plausible answer without
the required evidence.

This can create:

`missing evidence → hallucinated requirement → wrong design → wrong task → wrong code → failed delivery`

### Product Vision

Build a ChatGPT-style internal project workspace.

A product manager should be able to:

1. create a project
2. upload unstructured files
3. ask questions within the project
4. inspect source references
5. generate requirements, stories, design documents, tasks and test plans
6. upload additional files later
7. receive proposed requirement and plan changes
8. review a versioned diff
9. approve or reject revisions
10. hand approved incremental work to development agents

### Critical Design Rule

The model must not become the system of record.

Original evidence remains immutable.

Generated answers are derived interpretations.

Approved specifications are versioned contracts.

New evidence creates proposed changes rather than silent overwrites.

### Target Traceability Spine

`source evidence → requirement → user story → acceptance criterion → implementation task → code commit → automated test → release`

### Human-Control Principle

Agents may retrieve, summarise, draft, compare and recommend.

Agents must not silently approve their own specification changes.

## LP-013: Local Docling Ingestion Toolkit Installed

### Installed Environment

The document-ingestion pilot now has a dedicated Python virtual environment:

`projects/01-doc-to-spec-pilot/.venv`

### Installed Packages

| Component | Version | Purpose |
|---|---:|---|
| `docling` | `2.97.0` | First-pass local document conversion |
| `python-docx` | `1.2.0` | DOCX-specific fallback inspection |
| `python-pptx` | `1.0.2` | PPTX-specific fallback inspection |
| `openpyxl` | `3.1.5` | XLSX workbook extraction |
| `pandas` | `3.0.3` | Tabular processing |
| `pillow` | `12.2.0` | Image handling |
| `torch` | `2.12.0+cpu` | CPU-only parsing baseline |

### Installation Decision

The first Docling experiment uses a CPU-only PyTorch baseline.

GPU optimisation is deferred until the native-document extraction flow has been
validated.

### Current Local Benchmark

The CircuitFit benchmark pack has been copied into a local immutable folder and
hashed using SHA-256.

Raw files remain excluded from GitHub.

Safe manifest metadata and reusable hashing scripts are version controlled.

### Current Checkpoint

`Step 14A complete: local Docling ingestion toolkit installed, no extraction run`

### Next Planned Experiment

Run the first local Docling conversion against:

`CircuitFit MVP stress test and spec pack.docx`

Export:

- Markdown
- lossless JSON
- extraction metadata
- timing information

Then review extraction quality before processing additional formats.
