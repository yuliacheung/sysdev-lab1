# Q4: 信号与任务控制

## 操作记录

```bash
# 1. 启动长时间任务
sleep 10000
# 按 Ctrl+Z 挂起
# 输出: [1]+  Stopped                    sleep 10000

# 2. 查看作业状态
jobs
# 输出: [1]+  Stopped                    sleep 10000

# 3. 放到后台运行
bg
# 输出: [1]+ sleep 10000 &

# 4. 确认正在运行
jobs
# 输出: [1]+  Running                    sleep 10000 &

# 5. 查找进程
pgrep -af sleep
# 输出: 394 sleep 10000

# 6. 杀死进程（不手动输入PID）
pkill -f "sleep 10000"

# 7. 验证已终止
jobs
# 输出: [1]+  Terminated                 sleep 10000

pgrep -af sleep
# 无输出（进程已不存在）
```

## 关键知识点

| 命令 | 作用 |
|------|------|
| `Ctrl+Z` | 挂起（暂停）前台进程 |
| `bg` | 将挂起的作业放到后台继续运行 |
| `jobs` | 查看当前 shell 的作业状态 |
| `pgrep -af` | 通过完整命令行查找进程（显示 PID 和命令） |
| `pkill -f` | 通过完整命令行杀死匹配的进程 |

## 注意事项
- `pgrep` 和 `pkill` 的 `-f` 参数匹配完整的命令行，而不仅仅是进程名
- 如果不使用 `-f`，`pkill sleep` 会杀死所有名为 `sleep` 的进程
- `jobs` 只显示当前 shell 的子进程
