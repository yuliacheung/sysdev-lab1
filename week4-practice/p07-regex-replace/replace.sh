#!/usr/bin/env bash
set -euo pipefail

# 只替换行首的 "- "，不替换正文中的 "-"
sed -i 's/^- /* /' notes.md
