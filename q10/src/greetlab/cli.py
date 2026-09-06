import argparse
import sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args()
    
    # 检查姓名是否为空或仅包含空白字符
    if not a.name or a.name.isspace():
        sys.exit(2)
    
    print(f"Hello, {a.name}!")
