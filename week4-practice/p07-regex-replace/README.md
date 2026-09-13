# p07-regex-replace

用 regex `^- ` 只替换 Markdown 项目符号，不误伤正文中的 `-`。

## 运行

    ./replace.sh
    cat notes.md

## 正则

    ^- 

只匹配行首的 "- "。

## 说明

直接替换所有 "-" 会误伤正文中的 "-"，例如 "Some text with - dash inside."
