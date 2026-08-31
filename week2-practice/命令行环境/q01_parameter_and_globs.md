# Q1: 参数与 Globs

## 操作记录
```bash
# 创建以 - 开头的文件
touch -- -myfile

# 验证文件存在
ls -la | grep myfile
# 输出: -rw-r--r--  1 alienare alienare 0 Aug 31 13:53 -myfile

# 错误删除（失败）
rm -myfile
# 错误: rm: invalid option -- 'm'

# 正确删除（成功）
rm -- -myfile

# 验证已删除
ls -la | grep myfile
# 无输出

---

## 📝 创建 Q2 文件

```bash
cat > q02_process_substitution.md << 'EOF'
# Q2: 进程替换

## 操作记录
```bash
# 查看格式差异
printenv | head -5
export | head -5

# 比较两者差异
diff <(printenv | sort) <(export | sort) | head -20
DISPLAY=:0
HOME=/home/alienare
declare -x DISPLAY=":0"
declare -x HOME="/home/alienare"

---

## 📝 创建 Q3 文件

```bash
cat > q03_marco_polo.sh << 'EOF'
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
