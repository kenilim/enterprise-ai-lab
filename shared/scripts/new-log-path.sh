#!/usr/bin/env bash
set -euo pipefail

CATEGORY="${1:-setup}"
DETAIL="${2:-activity}"

LAB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
mkdir -p "${LAB_ROOT}/logs/${CATEGORY}"

printf '%s/logs/%s/%s_%s.log\n' \
  "$LAB_ROOT" \
  "$CATEGORY" \
  "$(date +%Y%m%d_%H%M%S)" \
  "$DETAIL"
