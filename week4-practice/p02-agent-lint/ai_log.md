# AI agent 修复 linter 记录

## 提示
目标：修复本仓库所有 ruff linter 错误。
约束：不改变函数行为，不删除公共 API，只做最小改动。
命令：
  ruff check .
  ruff format --check .
要求：每次修改后运行 ruff check .，直到返回 0。

## 原始错误
- I001 import 未排序
- F401 os / sys / json 未使用
- F841 unused 变量未使用
- 格式问题：def f( x ):、x+ 1

## agent 改动
- 删除未使用的 import
- 删除未使用的变量 unused
- 修正函数定义和运算符空格

## 人工验证
- ruff check . 返回 0
- ruff format --check . 通过
- f(2) == 3，g() == 2
