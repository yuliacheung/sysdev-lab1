# 实例1：ls -l 的作用

`-l` 参数以长格式（long format）显示，比默认 `ls` 展示更多信息。

运行 `ls -l /` 的输出中，每行开头10个字符含义：
- 第1位：文件类型（d=目录，-=普通文件，l=符号链接）
- 第2-4位：owner权限（读r/写w/执行x）
- 第5-7位：group权限
- 第8-10位：other权限

例如 `drwxr-xr-x` 表示：目录，owner有rwx，group和other只有rx（不能写）。
`lrwxrwxrwx` 表示符号链接（如 bin -> usr/bin）。
`drwxrwxrwt` 中的末位 t 是sticky bit（如/tmp），只有文件所有者能删除自己的文件。
