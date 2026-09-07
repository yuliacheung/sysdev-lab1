high_quality = {
    "title": "How to filter a list of dictionaries by key value in Python?",
    "has_code": True,
    "has_error": True,
    "has_expected": True,
    "clear_title": True
}

low_quality = {
    "title": "Python no work",
    "has_code": False,
    "has_error": False,
    "has_expected": False,
    "clear_title": False
}

def analyze(q):
    score = sum([q["has_code"], q["has_error"], q["has_expected"], q["clear_title"]])
    print(f"标题: {q['title']}")
    print(f"质量得分: {score}/4")
    print(f"评估: {'✅ 高质量 - 很可能得到好答案' if score >= 3 else '❌ 低质量 - 可能被关闭或点踩'}")
    print("-" * 50)

print("=== Stack Overflow 问题质量分析 ===\n")
analyze(high_quality)
analyze(low_quality)

print("\n💡 高质量问题的关键要素:")
print("1. 具体的标题")
print("2. 包含代码示例")
print("3. 有错误信息")
print("4. 说明期望输出")
