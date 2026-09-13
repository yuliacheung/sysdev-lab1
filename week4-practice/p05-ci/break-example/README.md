故意破坏示例：

把 break_me.py 复制到 p05-ci 根目录：

    cp break-example/break_me.py ./break_me.py

提交后 CI 会在 Lint 步骤失败：

    ruff check .
    → F401 os imported but unused

删除 break_me.py 后 CI 恢复通过。

注意：break-example/ 已在 pyproject.toml 的 ruff.exclude 中排除，
所以它本身不会影响正常状态的 ruff 检查。
