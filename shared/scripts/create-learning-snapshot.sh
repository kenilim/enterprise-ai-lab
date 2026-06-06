#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:?Usage: create-learning-snapshot.sh <version> <checkpoint-step> <status-slug>}"
CHECKPOINT="${2:?Usage: create-learning-snapshot.sh <version> <checkpoint-step> <status-slug>}"
STATUS="${3:?Usage: create-learning-snapshot.sh <version> <checkpoint-step> <status-slug>}"

LAB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SOURCE="${LAB_ROOT}/learnings/current/enterprise-agentic-ai-development-lab.md"
EXPORT_DIR="${LAB_ROOT}/learnings/exports"
TS="$(date +%Y%m%d_%H%M%S)"

mkdir -p "$EXPORT_DIR"

TARGET="${EXPORT_DIR}/enterprise-agentic-ai-development-lab_v${VERSION}_checkpoint-${CHECKPOINT}_${STATUS}_${TS}.md"

cp "$SOURCE" "$TARGET"

echo "$TARGET"
