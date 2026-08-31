# Q1: 参数与 Globs

## 操作记录
```bash
touch -- -myfile
ls -la | grep myfile
# 输出: -rw-r--r--  1 alienare alienare 0 Aug 31 13:53 -myfile

rm -myfile
# 错误: rm: invalid option -- 'm'

rm -- -myfile
ls -la | grep myfile
# 无输出，文件已删除
```

## 关键知识点
- `--` 告诉命令：后面所有内容都当作位置参数处理，不再解析为选项（flag）
- 以 `-` 开头的文件名会被误认成选项，必须用 `--` 隔离才能正确 touch/rm
