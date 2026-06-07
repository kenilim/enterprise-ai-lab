# OpenCode Operating Model Primer for Product Managers

## Purpose

This guide explains the OpenCode concepts used in the Product Manager CoPilot
lab.

It is written for offline review by a product manager rather than for an
experienced software engineer.

## The Plain-English Model

| Concept | Plain-English meaning | Product Manager CoPilot example |
|---|---|---|
| OpenCode | The runtime and user interface that hosts AI coding agents | The application you launch from the terminal |
| Agent | A worker with a role, prompt, model and permissions | `product-manager-copilot` |
| Primary agent | The main worker you interact with directly | Product Manager CoPilot orchestrator |
| Subagent | A focused specialist invoked by a primary agent | `ingestion-reviewer` |
| Skill | A reusable operating procedure loaded when relevant | `product-manager-copilot-ingestion-review/SKILL.md` |
| Tool | Executable function or script used for deterministic work | Docling router script |
| Orchestrator | A primary agent that coordinates subagents, skills and tools | Product Manager CoPilot orchestrator |
| `AGENTS.md` | Project rules automatically placed into agent context | Repository security and approval rules |
| ADR | Architecture Decision Record explaining why a decision was made | Why agents orchestrate deterministic tools |
| OpenSpec | Versioned product-change contract | Future proposal, design and tasks |
| Git commit | Reviewed historical record of an approved change | Safe checkpoint pushed after review |

## Why These Concepts Are Separate

A reliable enterprise workflow should not rely on one giant AI prompt.

Use:

```text
OpenCode runtime
→ primary orchestrator agent
→ bounded subagent
→ reusable skill
→ deterministic tools
→ structured outputs
→ human review
→ Git history
```

### Agent

An agent is the worker.

It has:

- a role
- a model
- a prompt
- permissions
- allowed subagents
- allowed skills
- maximum steps

### Skill

A skill is the playbook.

It explains how a workflow should be performed.

A skill is not an autonomous worker.

### Tool

A tool performs repeatable work.

Examples:

- hash files
- route formats
- parse documents
- write metadata
- produce reports

### Orchestrator

The orchestrator sequences the work.

It should not improvise every extraction itself.

### ADR

An ADR is documentation.

It records:

- the decision
- the reasoning
- the trade-offs
- the implication

It is not executable.

### OpenSpec

OpenSpec comes later.

It records a proposed product or software change after evidence has been
extracted, reviewed and normalised.

Typical future structure:

```text
openspec/
├── specs/
│   └── approved current behaviour
└── changes/
    └── proposed-change/
        ├── proposal.md
        ├── design.md
        ├── tasks.md
        └── specs/
            └── delta specification
```

## Why ADRs Exist Before OpenSpec Tasks

Some lab-wide decisions must be settled before implementation begins.

Example:

```text
Decision:
Use deterministic extraction tools and let agents orchestrate them.

Later implementation work:
Expose those tools cleanly and connect them to Product Manager CoPilot.
```

The ADR records the reasoning.

The future OpenSpec task records the work.

## Current Lab Structure

```text
.opencode/
├── agents/
│   ├── product-manager-copilot.md
│   └── ingestion-reviewer.md
├── commands/
│   └── pmcp-ingestion-review.md
└── skills/
    └── product-manager-copilot-ingestion-review/
        └── SKILL.md
```

## Offline Reference Rule

When confused, review:

1. this guide
2. `AGENTS.md`
3. relevant ADRs
4. current checkpoint
5. current README
