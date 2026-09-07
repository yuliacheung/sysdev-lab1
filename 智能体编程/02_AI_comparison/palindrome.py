"""不同AI编程方式对比 - 回文检测"""

# 方式1: 手动编码
def is_palindrome_manual(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# 方式2: AI自动补全
def is_palindrome_ai_complete(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# 方式3: 内联聊天优化
def is_palindrome_chat(s: str) -> bool:
    import re
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]

# 方式4: 智能体生成
def is_palindrome_agent(s: str) -> bool:
    import unicodedata
    normalized = unicodedata.normalize("NFKD", s)
    chars = [c.lower() for c in normalized if c.isalnum()]
    return chars == chars[::-1]

# 测试
test_cases = [("A man, a plan, a canal: Panama", True), ("race a car", False)]
for name, func in [("Manual", is_palindrome_manual), ("AI Complete", is_palindrome_ai_complete), ("Chat", is_palindrome_chat), ("Agent", is_palindrome_agent)]:
    for s, expected in test_cases:
        result = func(s)
        status = "✅" if result == expected else "❌"
        print(f"{name}: {s[:30]} -> {result} {status}")
