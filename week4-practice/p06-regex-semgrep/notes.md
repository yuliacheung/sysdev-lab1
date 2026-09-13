# grep vs semgrep

## grep 命令

    grep -nE 'subprocess\.Popen\(.*shell=True' sample.py

匹配：
- 第 3 行 subprocess.Popen("ls", shell=True)
- 第 9 行 subprocess.Popen('echo "a b"', shell=True)

漏掉：
- 第 5-8 行多行调用

## semgrep 命令

    semgrep -e 'subprocess.Popen(...)' --lang python sample.py --no-git-ignore
    semgrep -e 'subprocess.Popen($CMD, shell=True)' --lang python sample.py --no-git-ignore

第一条匹配 4 处，包括 shell=False。
第二条匹配 3 处，只匹配 shell=True，包括多行调用。

## 结论

- grep 基于行文本，只能匹配单行，适合快速粗筛
- semgrep 基于 AST，能匹配多行、变量、复杂结构，适合安全审计
- semgrep 的 -e 通用模式不需要联网规则，本地即可运行
