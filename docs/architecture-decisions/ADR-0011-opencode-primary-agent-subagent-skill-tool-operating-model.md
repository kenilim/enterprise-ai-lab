# ADR-0011: OpenCode Primary Agent, Subagent, Skill and Tool Operating Model

## Status

Accepted for the next learning phase.

## Decision

Use a bounded OpenCode structure:

```text
Product Manager CoPilot primary agent
→ ingestion-reviewer subagent
→ ingestion-review skill
→ deterministic extraction tools
→ local run manifest
→ sanitised report
→ human approval gate
```

## Reasoning

Avoid treating OpenCode as one giant autonomous agent.

Use:

- `AGENTS.md` for repository-wide rules
- primary agent for orchestration
- subagents for focused analysis
- skills for reusable procedures
- tools and scripts for deterministic work
- ADRs for decisions
- OpenSpec later for versioned proposed product changes

## Next Step

Run the first agent-assisted ingestion-quality review and observe whether the
agent:

- loads project rules
- loads the skill
- invokes the reviewer
- uses deterministic tools
- writes a local manifest
- creates a sanitised report
- stops before commit or push
