#!/bin/bash

# marco: 保存当前工作目录到环境变量
marco() {
    export MARCO_DIR=$(pwd)
    echo "Saved directory: $MARCO_DIR"
}

# polo: 跳转到保存的目录
polo() {
    if [ -n "$MARCO_DIR" ]; then
        cd "$MARCO_DIR"
        echo "Jumped to: $MARCO_DIR"
    else
        echo "Error: No directory saved. Run 'marco' first."
    fi
}

# 测试记录
# $ pwd                    # /home/alienare
# $ marco                  # Saved directory: /home/alienare
# $ cd /tmp               # 切换到 /tmp
# $ polo                   # Jumped to: /home/alienare
# $ pwd                    # /home/alienare
#
# 函数已添加到 ~/.bashrc 使其永久生效
