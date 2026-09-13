#!/usr/bin/env bash
set -euo pipefail

URL="http://127.0.0.1:8000/packages.json"

{
  echo "# Active Packages Report"
  echo
  echo "| name | version | downloads |"
  echo "|---|---|---|"
  curl -fsS "$URL" | jq -r '
    [ .[]
      | select(.status == "active" and .downloads >= 100)
    ]
    | sort_by(-.downloads, .name)
    | .[]
    | "| \(.name) | \(.version) | \(.downloads) |"
  '
} > summary.md
