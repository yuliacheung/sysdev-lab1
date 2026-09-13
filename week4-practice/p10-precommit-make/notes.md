# pre-commit 钩子说明

仓库根目录 .git/hooks/pre-commit 会执行：

    make all

失败则退出非零，Git 拒绝提交。

本目录用 demo_pre_commit.sh 演示同样的逻辑，避免影响整个仓库。

## 测试

正常 Makefile：

    ./demo_pre_commit.sh
    echo $?    # 0

故意失败的 Makefile：

    all: out.txt
    out.txt: in.txt
    	false

    ./demo_pre_commit.sh
    echo $?    # 1
