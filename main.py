num = input("请输入一个 5 位数字: ")
if len(num) != 5 or not num.isdigit():
    print("错误提示：输入不是 5 位纯数字。")
else:
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
