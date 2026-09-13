# p10-precommit-make

pre-commit 钩子执行 make，失败则拒绝提交。

本目录的钩子只用于演示，实际钩子路径是仓库根目录的 .git/hooks/pre-commit。

## 运行

    ./demo_pre_commit.sh
    echo $?

## 说明

- demo_pre_commit.sh 执行 make all
- 失败时输出 Build failed. Commit rejected. 并返回 1
- 正常时返回 0
