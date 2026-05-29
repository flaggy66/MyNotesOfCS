from random import randint, choice

name = "张三"  # 字符串
age = 18  # 数字
address = ['中国', '上海', '徐家汇']  # 列表

print(name, age, address)

# 同时给多个变量赋值
x, y, z = 0, 1, 2

prompt = """欢迎使用Python进行编程！
请输入你的名字："""

name = input(prompt)
print(name)

prompt = f"你好，{name} ! \n请输入你的年龄："
age = int(input(prompt))
print(age)

print(randint(1, 100))

tuple1 = ("花", "草", 1, 3, "ABC", "good")
print(choice(tuple1))
list1 = [1, 2, 25, 64, 0, 3, "Night", "world"]
print(choice(list1))
