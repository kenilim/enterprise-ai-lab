# Learning Journal

## Purpose

This is the canonical update-in-place learning journal for the Product Manager
CoPilot lab.

Use concise dated entries with:

`Origin → Finding → Learning Point → Decision`

---

## 2026-06-07 — OpenCode-first product-manager interaction

- **Origin:** Product-manager insight + Copilot recommendation
- **Finding:** The non-technical product-manager persona can work more safely
  through OpenCode orchestration than by repeatedly running long shell scripts.
- **Learning Point:** The default interaction should be OpenCode-first, with
  deterministic scripts behind approved tools and workflows.
- **Decision:** Keep OpenCode as the primary operating interface for this lab
  phase.

## 2026-06-07 — WSL repo boundary discipline

- **Origin:** Architecture decision + Experiment result
- **Finding:** Keeping local-only evidence, runtime logs and operational output
  inside the WSL repo boundary but outside Git improves auditability and reduces
  scattered private state.
- **Learning Point:** The project boundary should be the WSL repository, with a
  strong separation between Git-safe durable memory and local-only operational
  evidence.
- **Decision:** Keep `logs/` and local evidence folders local-only; keep durable
  summaries in repo-local Markdown.

## 2026-06-07 — Repo-local outputs versus Downloads convenience exports

- **Origin:** Failure lesson + Product-manager insight
- **Finding:** Download-folder exports can help temporarily, but they are weak as
  primary handoff artefacts because they sit outside the shared repository.
- **Learning Point:** Durable handoff artefacts should live inside the repo when
  they are intended for another authorised reviewer.
- **Decision:** Treat Downloads-folder copies as optional convenience only, not
  the default project-output location.

## 2026-06-07 — Tracked-versus-untracked validation behaviour

- **Origin:** Failure lesson
- **Finding:** Validation commands can behave differently for tracked and
  untracked files, especially for whitespace or diff-based checks.
- **Learning Point:** Validation must deliberately cover both tracked and
  untracked documentation drafts when a step includes new files.
- **Decision:** Use explicit tracked and untracked validation logic before human
  review.

## 2026-06-07 — Validation logic needs edge-case tests

- **Origin:** Failure lesson
- **Finding:** A command can run successfully while still testing the wrong
  condition.
- **Learning Point:** Validation logic itself needs edge-case thinking; passing a
  command is not enough if the check is aimed at the wrong thing.
- **Decision:** Treat validation design as a control surface, not just an
  administrative afterthought.

## 2026-06-07 — Documentation entropy is a retrieval and hallucination risk

- **Origin:** Experiment result + Copilot recommendation
- **Finding:** Overlapping current-state files, many micro-checkpoints and
  repeated handoff bundles increase retrieval noise.
- **Learning Point:** Documentation entropy is an anti-hallucination problem,
  because agents and humans can both anchor on stale or duplicate context.
- **Decision:** Build a small canonical knowledge spine and prefer update-in-place
  files.

## 2026-06-07 — Git-safe versus local-only artefact classification

- **Origin:** Architecture decision + Known limitation
- **Finding:** The repo now contains both durable Git-safe documents and local
  audit evidence, but the boundary must stay explicit.
- **Learning Point:** Classification is part of governance: safe summaries in
  Git, operational evidence in local-only paths.
- **Decision:** Keep local logs as audit evidence and out of default retrieval and
  out of Git.

## 2026-06-07 — Smallest correct context beats largest possible context

- **Origin:** Copilot recommendation
- **Finding:** OpenCode agents do not benefit from loading every Markdown file.
- **Learning Point:** Good retrieval means loading the smallest correct set of
  source-of-truth files for the current question.
- **Decision:** Use canonical current-state, project README, requirements,
  governance and latest report as the default read order.

## 2026-06-07 — Explicit human Git handoff remains necessary

- **Origin:** Known limitation + Experiment result
- **Finding:** Approved documentation changes still cannot be committed from the
  current OpenCode agent because Git write permissions remain restricted.
- **Learning Point:** The workflow already supports safe preparation and
  validation inside OpenCode, but manual Git checkpoint handoff is still needed.
- **Decision:** Preserve explicit human commit-and-push handoff from a separate
  WSL terminal until a governed checkpoint tool exists.

## 2026-06-07 — Resumable workflows after external-model limits

- **Origin:** Failure lesson
- **Finding:** External-model request limits can interrupt progress even when the
  work itself is well structured.
- **Learning Point:** Durable checkpoints, canonical current state and concise
  journals are necessary for resumable multi-user workflows.
- **Decision:** Preserve repo-local restart structure and avoid private-context
  dependence.

## 2026-06-07 — Anti-hallucination control begins before retrieval

- **Origin:** Experiment result + Architecture decision
- **Finding:** Bad extraction can become false structured evidence before any
  later retrieval or reasoning logic runs.
- **Learning Point:** Pre-normalisation quality gates are an anti-hallucination
  control, not just an ingestion-quality nicety.
- **Decision:** Keep extraction-quality remediation ahead of normalisation,
  OpenSpec and coding.

## 2026-06-07 — CircuitFit still needs visible downstream outcomes

- **Origin:** Product-manager insight
- **Finding:** Governance and documentation work has been valuable, but Step 16
  became too broad and drifted away from a visible CircuitFit outcome.
- **Learning Point:** After the minimum Step 16 gates pass, the project must move
  toward evidence normalisation, first OpenSpec proposal, first specifications
  and first tests.
- **Decision:** Keep Step 16 narrow from here: finish extraction gates, rerun the
  benchmark, approve eligible evidence, then normalise and move toward OpenSpec.

## 2026-06-07 — Figma MCP is a future design-phase experiment only

- **Origin:** Future product requirement
- **Finding:** Figma MCP may be relevant later for design-phase work, but it is
  not needed during extraction-quality remediation and knowledge consolidation.
- **Learning Point:** Design tooling should enter only after evidence quality,
  normalisation and OpenSpec foundations are ready.
- **Decision:** Record Figma MCP in backlog only; do not explore it in Step 16.
