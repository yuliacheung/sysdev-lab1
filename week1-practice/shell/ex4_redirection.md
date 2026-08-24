# 实例4：stdout/stderr 重定向

三条标准流：stdin(0)、stdout(1)、stderr(2)

分开重定向：
ls /nonexistent /tmp > out.log 2> err.log
- out.log: /tmp 的正常列表（stdout）
- err.log: ls: cannot access '/nonexistent': No such file or directory（stderr）

合并到同一文件：
ls /nonexistent /tmp > both.log 2>&1
- 关键：2>&1 表示把stderr重定向到stdout"目前指向"的地方，
  必须放在 > both.log 之后，顺序反了不会合并成功
  （若写成 2>&1 > both.log，stderr会先跟到旧的stdout即终端，之后才改stdout指向文件，两者就分开了）
- both.log 里同时包含错误信息和正常输出
