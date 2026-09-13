# p08-json-regex

演示 regex 捕获 JSON name 的局限，并推荐使用 json 解析器。

## 运行

    grep -oP '"name":\s*"\K.*(?=",\s*"college")' input.json
    grep -oP '"name":\s*"\K.*?(?=",\s*"college")' input.json

    python3 extract_name.py < input.json
    python3 extract_name.py < input2.json

## 结论

- 贪婪 regex 容易多吃内容
- 非贪婪 regex 对简单情况可用
- 含转义 \" 时 regex 很难写
- 推荐用 json 解析器
