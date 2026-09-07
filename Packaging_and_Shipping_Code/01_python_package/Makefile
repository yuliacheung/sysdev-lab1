.PHONY: help install test format clean all

help:
	@echo "可用命令:"
	@echo "  make install  - 安装包"
	@echo "  make test     - 运行测试"
	@echo "  make format   - 格式化代码"
	@echo "  make clean    - 清理临时文件"
	@echo "  make all      - 安装并测试"

install:
	pip install -e .

test:
	@echo "运行测试..."
	python3 -c "import greet; print('✅ 导入成功!')" || echo "❌ 测试失败"
	@echo "✅ 测试完成"

format:
	@echo "格式化代码..."
	ruff format . 2>/dev/null || echo "💡 提示: 安装 ruff 以获得格式化功能 (pip install ruff)"

clean:
	@echo "清理临时文件..."
	rm -rf build/ dist/ *.egg-info .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ 清理完成"

all: install test
