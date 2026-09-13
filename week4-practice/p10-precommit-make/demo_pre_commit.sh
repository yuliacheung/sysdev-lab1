#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
if ! make all; then
  echo "Build failed. Commit rejected." >&2
  exit 1
fi
