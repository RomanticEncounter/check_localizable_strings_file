#!/usr/bin/env python3
import sys
import re

def check_strings_file(file_path):
    
    # 用于检测未转义的双引号
    unescaped_quote = re.compile(r'(?<!\\)"')
    # 用于检测引号数量是否成对
    quote_pattern = re.compile(r'"')
    # 正则表达式匹配键值对格式
    # line_pattern = re.compile(r'^\s*"((?:[^"\\]|\\.)*)"s*=s*"((?:[^"\\]|\\.)*)"\s*;$')
     # 正则表达式匹配键值对格式
    kv_pattern = re.compile(r'^\s*"((?:[^"\\]|\\.)*)"\s*=\s*"((?:[^"\\]|\\.)*)"\s*;$')

    errors = []
    keys = {}
    in_multiline_comment = False

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for lineno, line in enumerate(lines, 1):
        stripped_line = line.strip()

        # 处理多行注释
        if in_multiline_comment:
            if '*/' in line:
                in_multiline_comment = False
            continue

        # 检查是否进入多行注释
        if '/*' in line:
            if '*/' not in line:
                in_multiline_comment = True
            continue

        # 检查单行注释
        if stripped_line.startswith(('//', '///')):
            continue

        # 跳过空行
        stripped = line.strip()
        if not stripped:
            continue

        # 检查分号结尾
        if not stripped.endswith(';'):
            errors.append(f"🚫 Line {lineno}: Missing semicolon")

        # 检查引号是否成对
        quotes = quote_pattern.findall(stripped)
        if len(quotes) % 2 != 0:
            errors.append(f"🚫 Line {lineno}: Unmatched quotes")

        # 检查键值对格式
        # match = re.match(r'^\s*"((?:[^"\\]|\\.)*)"\s*=\s*"((?:[^"\\]|\\.)*)"\s*;$', line)
        # 空格结尾的kv键值可能会导致匹配失败
        # match = kv_pattern.match(line)
        match = kv_pattern.match(line.rstrip())
        if not match:
            errors.append(f"❗️ Line {lineno}: Invalid format for key-value pair")
            continue

        key = match.group(1)
        value = match.group(2)

        # 检查键或值是否为空
        if not key:
            errors.append(f"⚠️ Line {lineno}: Empty key")

        if not value:
            errors.append(f"⚠️ Line {lineno}: Empty value")

        # 检查键重复
        if key in keys:
            errors.append(f"⚠️ Line {lineno}: Duplicate key '{key}' (also defined at line {keys[key]})")
        else:
            keys[key] = lineno

        # 检查值中的未转义双引号
        if unescaped_quote.search(value):
            errors.append(f"⚠️ Line {lineno}: Unescaped quote in value")

    # 检查是否有未闭合的多行注释
    if in_multiline_comment:
        errors.append("🚫 Error: Unclosed multiline comment in file")

    # 输出结果
    if errors:
        print(f"💬 Found {len(errors)} errors in {file_path}:")
        for error in errors:
            print(error)
    else:
        print("✅ No issues found in the strings file.")

def main():
    if len(sys.argv) != 2:
        print("Usage: csf <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not file_path.endswith('.strings'):
        print("Error: File must be a .strings file")
        sys.exit(1)

    check_strings_file(file_path)

# 入口检查必须写在定义main函数的同一个文件中
if __name__ == '__main__':
    main()  # 调用main函数