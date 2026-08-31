# Q2: 进程替换

## 操作记录
```bash
# 查看格式差异
printenv | head -5
export | head -5

# 比较两者差异
diff <(printenv | sort) <(export | sort) | head -20
```

## 发现的关键差异
- `printenv`: 显示 `变量=值` 格式
  ```
  DISPLAY=:0
  HOME=/home/alienare
  ```

- `export`: 显示 `declare -x 变量="值"` 格式
  ```
  declare -x DISPLAY=":0"
  declare -x HOME="/home/alienare"
  ```

## 关键知识点
- `<(command)` 将命令的输出当作临时文件处理
- 允许两个命令的输出直接进行比较
- 常用于 diff、comm 等需要文件输入的命令
