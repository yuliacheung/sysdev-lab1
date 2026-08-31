# 补: IDE 扩展与语言服务器配置

## 操作记录
- MUD C++ 项目已安装 VS Code 的 C/C++ 扩展（ms-vscode.cpptools）
- 验证 "Go to Definition"（F12）功能正常，能正确跳转到函数/类定义处

## 关键知识点
- 语言服务器（Language Server）为编辑器提供跳转定义、自动补全、错误检查等功能，依赖项目的编译配置（如 compile_commands.json）才能准确解析跨文件引用
