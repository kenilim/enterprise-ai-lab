# OpenCode Agent-Run Logging Policy

## Purpose

Define how Product Manager CoPilot agent runs should be recorded.

## Logging Layers

| Layer | Content | Storage |
|---|---|---|
| OpenCode native logs | Runtime errors and internal technical events | Local only |
| OpenCode session transcript | User prompts, agent responses and tool interaction context | Local only |
| Agent-run manifest | Structured run identity, model, skills, tools, hashes, warnings and approval state | Local only |
| Sanitised checkpoint | Safe summary of the run and its findings | Public GitHub after human review |
| Git commit | Approved durable record | Public GitHub after human review |

## Local Paths

Use:

```text
logs/opencode/
logs/agent-runs/
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
YYYYMMDD_HHMMSS_pmcp_<workflow>_agent-run-manifest.json
```

## Session Export

At meaningful checkpoints:

1. export the OpenCode session locally
2. record its local path in the agent-run manifest
3. create a sanitised checkpoint
4. show the Git diff
5. request human approval
6. commit and push only safe files

## Approval Rule

The agent may prepare a proposed commit.

The agent must not run `git commit` or `git push`.
