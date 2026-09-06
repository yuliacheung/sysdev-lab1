# Issue: 空白 --name 参数未正确处理

**环境**：Ubuntu 22.04（待确认），Python 3.14.4，greetlab 0.1.0

**复现步骤**：
sdt-greet --name "   "

**期望结果**：退出码 2，不输出问候语

**实际结果**：输出 "Hello,    !"，退出码 0

---

## 提交信息

fix: reject blank --name with exit code 2

When --name contains only whitespace characters, the program
currently outputs a greeting with empty name and exits with 0.
This violates CLI conventions for required arguments.

Add validation to check for isspace() and call sys.exit(2)
when the condition is met.

---

## 评审意见 (Blocking)

- 当前实现将空白字符串视为有效输入，违反 CLI 工具约定
- 建议在解析后增加 if not name or name.isspace(): sys.exit(2)
- 需补充测试用例覆盖此场景
