# p05-ci

GitHub Actions：format / lint / test。

## CI 流程

- ruff format --check .
- ruff check .
- pytest

## 故意破坏

把 break-example/break_me.py 复制到 p05-ci 根目录：

    cp break-example/break_me.py ./break_me.py

提交后 CI 会在 Lint 步骤失败：

    ruff check .
    → F401 os imported but unused

删除 break_me.py 后 CI 恢复通过。
