# 程序分支控制

# if语句
print("------if语句------")
num = int(input("请输入数字："))
if num % 2 == 0:
    print("数字是偶数")

print("------if...else语句------")
age = int(input("请输入年龄："))
if age >= 18:
    print("已成年")
else:
    print("未成年")

print("------if...elif...else语句------")
age = int(input("请输入年龄："))
if age <= 0:
    print("年龄输入错误——输入的数字不能小于0")
elif age < 18:
    print("未成年")
elif age <= 30:
    print("青少年")
elif age < 60:
    print("中年人")
elif age < 80:
    print("老年")
elif age < 120:
    print("长寿的人")
elif age <= 140:
    print("老寿星")
else:
    print("确定年龄没有输入错误吗？真是世所罕有的人。")

print("------if...elif 省略else语句------")
age = int(input("请输入年龄："))
if age <= 0:
    print("年龄输入错误——输入的数字不能小于0")
elif age < 18:
    print("未成年")
elif age <= 30:
    print("青少年")
elif age < 60:
    print("中年人")
elif age < 80:
    print("老年")
elif age < 120:
    print("长寿的人")
elif age <= 140:
    print("老寿星")
elif age > 140:
    print("确定年龄没有输入错误吗？真是世所罕有的人。")
