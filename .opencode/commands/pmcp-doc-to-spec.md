---
description: Run the resumable one-shot Product Manager CoPilot document-to-spec workflow for the CircuitFit pilot, routing automatically from the latest valid local manifest.
agent: product-manager-copilot
---

Run the Product Manager CoPilot one-shot document-to-spec pipeline for:

`circuitfit`

Requirements:

1. Read `AGENTS.md`.
2. Load the `product-manager-copilot-doc-to-spec` skill.
3. Explain progress and any resumed stage in plain English.
4. Inspect the latest valid local pipeline manifest and route automatically.
5. Do not rerun completed stages unless the manifest is missing, invalid, the user explicitly requests a rerun, or an upstream source file hash changed.
6. Run the required deterministic stage only for the routed phase.
7. Surface material exceptions only.
8. Respect recorded human approval as authorising only the next bounded phase.
9. Keep OpenSpec blocked until the later conflict-review approval state.
10. Do not write application code.
