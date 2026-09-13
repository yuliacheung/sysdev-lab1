# p01-quality

演示 ruff 格式化、lint 和 pre-commit 钩子。

## 运行

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -U pip ruff pre-commit
    ruff format .
    ruff check . --fix
    ruff format --check .
    ruff check .

## pre-commit 钩子

本目录提供 hooks/pre-commit，可复制到仓库 .git/hooks/pre-commit 使用：

    cp hooks/pre-commit ../../../.git/hooks/pre-commit
    chmod +x ../../../.git/hooks/pre-commit

为避免影响整个 sysdev-lab1 仓库，这里只演示钩子脚本本身，不实际安装。
