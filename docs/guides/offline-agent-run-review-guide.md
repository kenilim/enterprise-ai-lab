# Offline Agent-Run Review Guide

## Purpose

This guide explains how to review Product Manager CoPilot agent runs without
scrolling through long terminal output or reopening the original chat.

## Review Order

Use this sequence:

```text
1. compact summary
2. manifest
3. sanitised report
4. Git diff
5. full local log only if needed
6. OpenCode session export only if needed
```

## Why This Order Matters

A product manager should not need to inspect raw technical output for every
successful run.

The system should provide progressive disclosure:

| Review layer | Use it when |
|---|---|
| Compact summary | Every run |
| Manifest | Confirm traceability fields |
| Sanitised report | Review findings |
| Git diff | Approve public changes |
| Full local log | Troubleshoot failures |
| Session export | Investigate agent reasoning and actions |

## Readiness-Audit Helper

Run:

```bash
shared/scripts/run-opencode-agent-readiness-audit.sh
```

The helper generates:

```text
logs/setup/<timestamp>_step15e0_opencode_agent_readiness_audit.log
logs/agent-runs/<timestamp>_step15e0_readiness_summary.md
logs/agent-runs/<timestamp>_step15e0_readiness_manifest.json
logs/agent-runs/<timestamp>_step15e0_pre-run_opencode_sessions.json
logs/agent-runs/<timestamp>_step15e0_pre-run_opencode_stats.log
```

Review the summary first.

## Next Agent-Run Convention

Every future agent workflow should follow the same pattern:

```text
run workflow wrapper
→ save full output locally
→ generate summary
→ generate manifest
→ review summary
→ inspect detailed artefacts only when required
```

## Regulatory Perspective

In a high-risk environment, concise summaries improve usability but do not
replace detailed evidence.

The detailed records must remain available, access-controlled and tamper
evident.
