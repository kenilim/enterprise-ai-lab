#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="${1:?Usage: capture-opencode-usage.sh <project-dir> <step-label> <phase>}"
STEP_LABEL="${2:?Usage: capture-opencode-usage.sh <project-dir> <step-label> <phase>}"
PHASE="${3:?Usage: capture-opencode-usage.sh <project-dir> <step-label> <phase>}"

LAB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
PROJECT_SLUG="$(basename "$PROJECT_DIR")"
TS="$(date +%Y%m%d_%H%M%S)"

GLOBAL_USAGE_DIR="${LAB_ROOT}/logs/usage"
PROJECT_METRICS_DIR="${PROJECT_DIR}/metrics"

mkdir -p "$GLOBAL_USAGE_DIR" "$PROJECT_METRICS_DIR"

LOG_FILE="${GLOBAL_USAGE_DIR}/${TS}_${STEP_LABEL}_${PROJECT_SLUG}_${PHASE}_opencode_stats.log"
SESSION_FILE="${GLOBAL_USAGE_DIR}/${TS}_${STEP_LABEL}_${PROJECT_SLUG}_${PHASE}_opencode_sessions.json"

{
  echo "===== OPENCODE USAGE SNAPSHOT ====="
  echo "Timestamp: $TS"
  echo "Project: $PROJECT_SLUG"
  echo "Project directory: $PROJECT_DIR"
  echo "Step: $STEP_LABEL"
  echo "Phase: $PHASE"
  echo ""

  cd "$PROJECT_DIR"

  echo "===== TOKEN AND COST STATISTICS ====="
  opencode stats --project "" --models 20 || true

  echo ""
  echo "===== AUTHENTICATED PROVIDERS ====="
  opencode auth list || true
} | tee "$LOG_FILE"

cd "$PROJECT_DIR"
opencode session list --format json > "$SESSION_FILE" || true

cp "$LOG_FILE" "$PROJECT_METRICS_DIR/"
cp "$SESSION_FILE" "$PROJECT_METRICS_DIR/"

echo ""
echo "Usage log: $LOG_FILE"
echo "Session snapshot: $SESSION_FILE"
