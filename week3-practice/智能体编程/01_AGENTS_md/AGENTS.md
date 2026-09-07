# AGENTS.md - 编程智能体配置

## 项目上下文
- 项目：系统开发工具基础
- 语言：Python 3.10+
- 包管理：pip + venv
- 测试框架：pytest

## 编码规范
- 遵循PEP 8
- 所有函数必须有类型注解
- 文档字符串使用Google风格
- 最大函数长度：50行

## 工作流程
1. 分析需求
2. 编写测试
3. 实现功能
4. 运行测试
5. 代码审查

## 安全限制
- 禁止eval/exec
- 禁止直接os.system()
- 环境变量管理敏感信息

## 常用命令
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装包
pip install -e .

# 运行测试
pytest -v
```
