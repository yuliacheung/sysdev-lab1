# p03-coverage

单元测试与覆盖率 HTML 报告。

## 运行

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -U pip pytest coverage
    python -m pip install -e .

    coverage run -m pytest
    coverage report -m
    coverage html

## 结果

- 初始覆盖率：calc.py 50%
- 补全 sub / mul / div / div_zero 测试后：calc.py 100%

## 未覆盖行分析

初始未覆盖：
- 第 6 行：sub 函数体
- 第 10 行：mul 函数体
- 第 14-16 行：div 函数体

补全后全部覆盖。
