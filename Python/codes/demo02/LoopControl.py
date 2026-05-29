# for循环
print("=======for循环======")
print("-----range()的使用-----")
print("range(5):", range(5), list(range(5)), tuple(range(5)))
print("range(0):", range(0), list(range(0)), tuple(range(0)))
print("range(1,10):", range(1, 10), list(range(1, 10)))
print("range(1,10,1):", range(1, 10, 1), list(range(1, 10, 1)))
print("range(1,10,3):", range(1, 10, 3), list(range(1, 10, 3)))
print("range(10,1,-1):", range(10, 1, -1), list(range(10, 1, -1)))
print("range(10,-10,-2):", range(10, -10, -2), list(range(10, -10, -2)))
print("range(5,0,1):", range(5, 0, 1), list(range(5, 0, 1)))
print("range(1,2,-1):", range(1, 2, -1), list(range(1, 2, -1)))

print("-----for+range 指定循环次数-----")
for i in range(10):
    print("循环次数：", i)

print("-----for+range 循环变量-----")

sum = 0
for i in range(0, 10, 1):
    print("循环次数：", i)
    sum += i

print("0-9求和：", sum)

# while循环
print("======while循环======")
content = input("请输入：")
while content != "exit" and content:
    print(type(content), content)
    content = input("请输入：")

num = int(input("请输入一个正整数，将计算1到这个数的正整数和："))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(sum)

while True:
    content = input("请输入：")
    if content == "continue":
        continue
    elif content == "break":
        break
    elif content == "pass":
        pass
    else:
        print(content)
