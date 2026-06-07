---
description: Run the Product Manager CoPilot ingestion-quality review workflow and stop for human approval.
agent: product-manager-copilot
---

Run the Product Manager CoPilot ingestion-quality-review workflow against:

`projects/01-doc-to-spec-pilot/input/generated-synthetic-evidence/circuitfit-synthetic-enterprise-evidence-pack-v0.1`

Requirements:

1. Read `AGENTS.md`.
2. Load the `product-manager-copilot-ingestion-review` skill.
3. Invoke the `ingestion-reviewer` subagent.
4. Use deterministic local tools rather than improvising parsers.
5. Create a local agent-run manifest.
6. Create a sanitised public quality-review report.
7. Show limitations and proposed Git changes.
8. Stop before commit or push.
9. Do not generate OpenSpec artefacts yet.
10. Do not write application code.
