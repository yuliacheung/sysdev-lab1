# p02-agent-lint

用 AI agent 在迭代循环中修复 ruff linter 错误。

## 原始错误

    import os
    import sys
    import json

    def f( x ):
        unused = 1
        return x+ 1

ruff check . 报告：
- I001 import 未排序
- F401 os / sys / json 未使用
- F841 unused 变量未使用

## 修复后

    def f(x):
        return x + 1

    def g():
        return 2

## 验证

    ruff check .
    ruff format --check .

两者都通过。
