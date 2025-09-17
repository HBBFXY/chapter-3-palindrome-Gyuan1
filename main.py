s = input().strip()
if not (s.isdigit() and len(s) == 5):
    print("错误提示")
else:
    print("是回文数" if s == s[::-1] else "不是回文数")
