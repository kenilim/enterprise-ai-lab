#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${1:-$PWD}"
cd "$ROOT_DIR"

TS=$(date +%Y%m%d_%H%M%S)
STEP="step15e0"
LOG_DIR="logs/setup"
RUN_DIR="logs/agent-runs"

mkdir -p "$LOG_DIR" "$RUN_DIR" logs/opencode

FULL_LOG="$LOG_DIR/${TS}_${STEP}_opencode_agent_readiness_audit.log"
SUMMARY="$RUN_DIR/${TS}_${STEP}_readiness_summary.md"
MANIFEST="$RUN_DIR/${TS}_${STEP}_readiness_manifest.json"
SESSIONS="$RUN_DIR/${TS}_${STEP}_pre-run_opencode_sessions.json"
STATS="$RUN_DIR/${TS}_${STEP}_pre-run_opencode_stats.log"
AGENTS_LIST="$RUN_DIR/${TS}_${STEP}_discovered_agents.txt"

run_audit() {
  echo "===== STEP 15E.0: OPENCODE AGENT-READINESS AUDIT ====="
  echo "Timestamp: $TS"
  echo ""

  echo "===== WORKSPACE ====="
  pwd
  echo ""

  echo "===== GIT STATUS ====="
  git status --short || true
  echo ""

  echo "===== OPENCODE VERSION ====="
  opencode --version
  echo ""

  echo "===== DISCOVERED AGENTS ====="
  opencode agent list | tee "$AGENTS_LIST"
  echo ""

  echo "===== REQUIRED FILE CHECK ====="
  REQUIRED_FILES=(
    "AGENTS.md"
    ".opencode/agents/product-manager-copilot.md"
    ".opencode/agents/ingestion-reviewer.md"
    ".opencode/commands/pmcp-ingestion-review.md"
    ".opencode/skills/product-manager-copilot-ingestion-review/SKILL.md"
    "docs/guides/opencode-agent-skill-tool-orchestrator-primer.md"
    "docs/governance/regulator-auditable-agent-traceability.md"
    "docs/governance/opencode-agent-run-logging-policy.md"
  )

  for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
      printf 'OK   %s\n' "$file"
    else
      printf 'MISS %s\n' "$file"
    fi
  done
  echo ""

  echo "===== DEFINITION HASHES ====="
  sha256sum \
    AGENTS.md \
    .opencode/agents/product-manager-copilot.md \
    .opencode/agents/ingestion-reviewer.md \
    .opencode/commands/pmcp-ingestion-review.md \
    .opencode/skills/product-manager-copilot-ingestion-review/SKILL.md
  echo ""

  echo "===== PRE-RUN SESSION SNAPSHOT ====="
  if opencode session list --format json > "$SESSIONS" 2>/dev/null; then
    echo "Created: $SESSIONS"
  else
    printf '[]\n' > "$SESSIONS"
    echo "Session list JSON command unavailable or returned an error."
    echo "Created empty placeholder: $SESSIONS"
  fi
  echo ""

  echo "===== PRE-RUN TOKEN SNAPSHOT ====="
  if opencode stats --models 20 > "$STATS" 2>/dev/null; then
    echo "Created: $STATS"
  else
    : > "$STATS"
    echo "Stats command unavailable or returned an error."
    echo "Created empty placeholder: $STATS"
  fi
  echo ""

  echo "===== NATIVE LOG LOCATION ====="
  mkdir -p ~/.local/share/opencode/log
  echo "~/.local/share/opencode/log"
  echo ""

  echo "===== FINAL GIT STATUS ====="
  git status --short || true
  echo ""

  echo "===== STEP 15E.0 AUDIT COMPLETE ====="
}

run_audit 2>&1 | tee "$FULL_LOG"

python3 - "$TS" "$FULL_LOG" "$SUMMARY" "$MANIFEST" "$SESSIONS" "$STATS" "$AGENTS_LIST" <<'PYEOF'
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ts, full_log, summary_path, manifest_path, sessions_path, stats_path, agents_path = sys.argv[1:]

required = [
    "AGENTS.md",
    ".opencode/agents/product-manager-copilot.md",
    ".opencode/agents/ingestion-reviewer.md",
    ".opencode/commands/pmcp-ingestion-review.md",
    ".opencode/skills/product-manager-copilot-ingestion-review/SKILL.md",
    "docs/guides/opencode-agent-skill-tool-orchestrator-primer.md",
    "docs/governance/regulator-auditable-agent-traceability.md",
    "docs/governance/opencode-agent-run-logging-policy.md",
]

def digest(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def command_output(*args: str) -> str:
    try:
        return subprocess.check_output(args, text=True).strip()
    except Exception:
        return ""

def contains_agent(text: str, name: str) -> bool:
    return name.lower() in text.lower()

agents_text = Path(agents_path).read_text(encoding="utf-8", errors="replace")
missing = [path for path in required if not Path(path).is_file()]
git_status = command_output("git", "status", "--short")
opencode_version = command_output("opencode", "--version")

checks = {
    "git_tree_clean": git_status == "",
    "required_files_present": len(missing) == 0,
    "product_manager_copilot_discovered": contains_agent(agents_text, "product-manager-copilot"),
    "ingestion_reviewer_discovered": contains_agent(agents_text, "ingestion-reviewer"),
}

manifest = {
    "step": "step15e0",
    "timestamp_local": ts,
    "workflow": "opencode-agent-readiness-audit",
    "opencode_version": opencode_version,
    "checks": checks,
    "missing_files": missing,
    "definition_hashes": {
        path: digest(path)
        for path in required
        if Path(path).is_file()
    },
    "local_only_outputs": {
        "full_log": full_log,
        "summary": summary_path,
        "manifest": manifest_path,
        "sessions": sessions_path,
        "stats": stats_path,
        "agents_list": agents_path,
    },
    "human_review_status": "pending",
    "approved_by": None,
    "git_commit": None,
}

Path(manifest_path).write_text(
    json.dumps(manifest, indent=2),
    encoding="utf-8",
)

overall = all(checks.values())
result = "PASS" if overall else "REVIEW REQUIRED"
next_action = (
    "Proceed to Step 15E.1: launch the first orchestrated ingestion-review session."
    if overall
    else "Review the local full log and repair the failed readiness checks before launching the agent workflow."
)

summary = f"""# Step 15E.0 OpenCode Agent-Readiness Summary

## Result

`{result}`

## Checks

| Check | Result |
|---|---|
| Git tree clean | {"PASS" if checks["git_tree_clean"] else "REVIEW"} |
| Required files present | {"PASS" if checks["required_files_present"] else "FAIL"} |
| `product-manager-copilot` discovered | {"PASS" if checks["product_manager_copilot_discovered"] else "FAIL"} |
| `ingestion-reviewer` discovered | {"PASS" if checks["ingestion_reviewer_discovered"] else "FAIL"} |

## OpenCode Version

`{opencode_version or "Unavailable"}`

## Missing Files

{chr(10).join(f"- `{item}`" for item in missing) if missing else "- None"}

## Local-Only Evidence Files

- Full log: `{full_log}`
- Manifest: `{manifest_path}`
- Session baseline: `{sessions_path}`
- Token baseline: `{stats_path}`
- Discovered-agent list: `{agents_path}`

## Next Action

{next_action}
"""

Path(summary_path).write_text(summary, encoding="utf-8")

print("")
print("===== COMPACT HUMAN-READABLE SUMMARY =====")
print(summary)
print(f"Summary saved to:  {summary_path}")
print(f"Manifest saved to: {manifest_path}")
PYEOF
