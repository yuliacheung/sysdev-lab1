# 实例2：glob 通配符

glob 是 shell 在执行命令前，对 `*`、`?`、`{}` 等特殊字符做的文件名匹配展开，
和正则表达式不同，规则更简单，展开发生在shell层面，命令本身收到的是已经展开好的文件名列表。

测试（glob_test/ 目录下有 a.txt b.txt c.txt file1.txt file2.txt notes.md）：

- `ls *.txt` → a.txt b.txt c.txt file1.txt file2.txt
  （* 匹配任意长度字符，notes.md 后缀不符不匹配）
- `ls file?.txt` → file1.txt file2.txt
  （? 只匹配恰好1个字符）
- `ls {a,b,c}.txt` → a.txt b.txt c.txt
  （{} 是大括号展开，命令执行前先展开成 a.txt b.txt c.txt 三个词，不依赖文件是否存在）
