# p04-agent-coverage

用 AI agent 在迭代循环中提高测试覆盖率。

## 提示

    目标：提高本仓库测试覆盖率。
    约束：不要修改 src/ 下的实现代码，只添加/修改 tests/ 下的测试。
    命令：
      coverage run -m pytest
      coverage report -m
      coverage html
    要求：每次改完运行 coverage report -m，直到覆盖率 >= 95%。

## 结果

- 初始覆盖率：calc.py 50%
- agent 补全后：calc.py 100%

## 人工检查

- agent 只改了 tests/ 下的文件
- 没有 assert True 之类的无效断言
- 覆盖了 div 除零分支
