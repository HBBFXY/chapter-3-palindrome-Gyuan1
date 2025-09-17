# 输入处理
num = input("请输入一个5位数字：")

# 验证输入是否为5位纯数字
if not (num.isdigit() and len(num) == 5):
    print("输入错误：请输入一个5位纯数字")
else:
    # 判断是否为回文数
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
