# p06-regex-semgrep

对比 grep 正则与 semgrep 在查找 subprocess.Popen(..., shell=True) 上的差异。

## 运行

    grep -nE 'subprocess\.Popen\(.*shell=True' sample.py

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -U pip semgrep

    semgrep -e 'subprocess.Popen(...)' --lang python sample.py --no-git-ignore
    semgrep -e 'subprocess.Popen($CMD, shell=True)' --lang python sample.py --no-git-ignore

## 结果

- grep：匹配 2 处单行，漏掉多行
- semgrep：匹配 3 处 shell=True，包括多行调用

详见 notes.md。
