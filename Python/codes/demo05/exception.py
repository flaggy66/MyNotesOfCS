# 异常处理

a = int(input("请输入被除数："))
b = int(input("请输入除数："))
try:
    c = a / b
except ZeroDivisionError:
    print("除数不能为0！")
else:
    print("运行无异常。")
    print(f"{a} / {b} = {c}")