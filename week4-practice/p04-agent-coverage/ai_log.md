# AI agent 提高覆盖率记录

## 提示
目标：提高本仓库测试覆盖率。
约束：不要修改 src/ 下的实现代码，只添加/修改 tests/ 下的测试。
命令：
  coverage run -m pytest
  coverage report -m
  coverage html
要求：每次改完运行 coverage report -m，直到覆盖率 >= 95%。

## 初始覆盖率
calc.py 50%，未覆盖 sub / mul / div / div 除零分支。

## agent 改动
- 增加 sub / mul / div 测试
- 增加 div 除零异常测试

## 人工验证
- coverage report -m 覆盖率 100%
- 没有 assert True 之类的无效断言
- 没有修改 src/ 下的实现
