# OpenCode Agent-Run Logging and Export Policy

## Purpose

Define how Product Manager CoPilot agent runs should be recorded and reviewed.

The terminal is a runtime interface.

It is not the durable audit artefact and it should not be the main review
interface for a human product manager.

## Core Principle

Every meaningful run should produce:

```text
full local log
→ compact machine-readable manifest
→ short human-readable summary
→ sanitised public checkpoint after review
→ Git commit only after approval
```

Do not require a human reviewer to scroll through hundreds of terminal lines.

## Logging Layers

| Layer | Content | Storage | Audience |
|---|---|---|---|
| OpenCode native logs | Runtime errors and internal technical events | Local only | Troubleshooting |
| OpenCode session record | User prompts, agent responses and tool interaction context | Local only | Detailed investigation |
| Local full-run log | Complete wrapper-script output | Local only | Technical review |
| Agent-run manifest | Structured run identity, model, skills, tools, hashes, warnings and approval state | Local only | Audit reconstruction |
| Human-readable summary | Concise review output and next action | Local first; sanitise before commit | Product manager |
| Sanitised checkpoint | Safe public learning record | GitHub after human review | Colleagues |
| Git commit | Approved durable change record | GitHub after human review | Historical trace |

## Local Paths

Use:

```text
logs/opencode/
logs/agent-runs/
logs/setup/
projects/01-doc-to-spec-pilot/output/reports/
```

These remain local-only.

## Public Paths

Use:

```text
docs/reports/
docs/checkpoints/
```

Only sanitised, reviewed outputs may be committed.

## Naming Convention

```text
YYYYMMDD_HHMMSS_stepXX_component_action.log
YYYYMMDD_HHMMSS_stepXX_component_summary.md
YYYYMMDD_HHMMSS_stepXX_component_manifest.json
```

## Session Export

At meaningful OpenCode checkpoints:

1. identify the session ID
2. export the session locally where supported
3. record the export path in the manifest
4. produce a compact summary
5. show the Git diff
6. request human approval
7. commit and push only safe files

OpenCode session export is supplementary evidence.

It does not replace the agent-run manifest.

## Human Review Rule

The default review object is the compact summary file.

The full log and transcript should be opened only when:

- a check fails
- a warning appears
- a decision is disputed
- audit evidence is requested
- a production incident is under investigation

## Approval Rule

The agent may prepare a proposed commit.

The agent must not run `git commit` or `git push`.
