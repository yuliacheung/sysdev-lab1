# regex vs json parser

## regex 尝试

    grep -oP '"name":\s*"\K.*(?=",\s*"college")' input.json
    grep -oP '"name":\s*"\K.*?(?=",\s*"college")' input.json

两者都输出：Alyssa P. Hacker

因为 lookahead (?=",\s*"college") 已经限制了匹配末尾，
所以贪婪和非贪婪在这里结果相同。

更明显的贪婪示例（没有 lookahead）：

    grep -oP '"name":\s*"\K.*' input.json

会输出整行后面的内容。

## 含转义 \" 时 regex 很难写

input2.json 中 name 为：Alyssa \"P\" Hacker

regex 需要处理转义引号，非常容易出错，不推荐。

## json 解析器

    python3 extract_name.py < input.json
    python3 extract_name.py < input2.json

输出：

    Alyssa P. Hacker
    Alyssa "P" Hacker

一行版：

    python3 -c 'import json,sys; print(json.load(sys.stdin)["name"])' < input.json

## 结论

复杂 JSON 解析不要用 regex，用 json 解析器。
