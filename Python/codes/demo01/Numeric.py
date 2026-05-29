# 整数
intNum1 = 10
print(intNum1)
print(type(intNum1))

intNum2 = -10
intNum3 = 5
print("整数相加：-10+5", intNum2 + intNum3)

intNum4 = intNum1 - intNum2;
print("整数相减：10-（-10）", intNum4)

intNum5 = intNum1 * intNum2;
print("整数相乘：10*（-10）", intNum5)

intNum6 = intNum1 / intNum2;
print("整数除法：10/（-10）", intNum6)

print("整数取模或取余数：10%（-10）", intNum1 % intNum2)

print("整数取整：10//（-10）", intNum1 // intNum2)

print("整数取幂：10**（-10）", intNum1 ** intNum2)

print('2的10次方：', 2 ** 10)

# 浮点数
floatNum1 = 10.0
print(floatNum1)
print(type(floatNum1))

floatNum2 = -10.0
floatNum3 = 5.0
print("浮点数相加：-10.0+5.0", floatNum2 + floatNum3)

floatNum4 = floatNum1 - floatNum2;
print("浮点数相减：10.0-（-10.0）", floatNum4)

floatNum5 = floatNum1 * floatNum2;
print("浮点数相乘：10.0*（-10.0）", floatNum5)

floatNum6 = floatNum1 / floatNum2;
print("浮点数除法：10.0/（-10.0）", floatNum6)

print("浮点数取模或取余数：10.0%（-10.0）", floatNum1 % floatNum2)

print("浮点数取整：10.0//（-10.0）", floatNum1 // floatNum2)

print("浮点数取幂：10.0**（-10.0）", floatNum1 ** floatNum2)

print("浮点数四舍五入：10.01", round(10.01))

# 复数
complexNum1 = 10 + 5j
print(complexNum1)
print(type(complexNum1))

complexNum2 = -10 - 5j
complexNum3 = 5 + 5j
print("复数相加：-10-5j+5+5j", complexNum2 + complexNum3)

complexNum4 = complexNum1 - complexNum2;
print("复数相减：10+5j-（-10-5j）", complexNum4)

complexNum5 = complexNum1 * complexNum2;
print("复数相乘：10+5j*（-10-5j）", complexNum5)

complexNum6 = complexNum1 / complexNum2;
print("复数除法：10+5j/（-10-5j）", complexNum6)

# % 不能用于复数
# print("复数取模：10+5j%（-10-5j）", complexNum1 % complexNum2)
# // 不能用于复数
# print("复数取整：10+5j//（-10-5j）", complexNum1 // complexNum2)
print("复数取幂：10+5j**（-10-5j）", complexNum1 ** complexNum2)

print("==========")

print("不同数据类型相加：10+25.0", 10 + 25.0)
print("不同数据类型相加：10+5j+10", 10 + 5j + 10)
print("不同数据类型相加：10+5j+10.0", 10 + 5j + 10.0)
print("-----")
print("不同数据类型相减：10-25.0", 10 - 25.0)
print("不同数据类型相减：10+5j-10", 10 + 5j - 10)
print("不同数据类型相减：10+5j-10.0", 10 + 5j - 10.0)
print("-----")
print("不同数据类型相乘：10*25.0", 10 * 25.0)
print("不同数据类型相乘：（10+5j）*10", (10 + 5j) * 10)
print("不同数据类型相乘：（10+5j）*10.0", (10 + 5j) * 10.0)
print("-----")
print("不同数据类型相除：10/25.0", 10 / 25.0)
print("不同数据类型相除：（10+5j）/10", (10 + 5j) / 10)
print("不同数据类型相除：（10+5j）/10.0", (10 + 5j) / 10.0)
print("-----")
print("不同数据类型取模：10%25.0", 10 % 25.0)
# % 不能用于复数
# print("不同数据类型取模：（10+5j）%10", (10 + 5j) % 10)
# print("不同数据类型取模：（10+5j）%10.0", (10 + 5j) % 10.0)
print("-----")
print("不同数据类型取整：10//25.0", 10 // 25.0)
# // 不能用于复数
# print("不同数据类型取整：（10+5j）//10", (10 + 5j) // 10)
# print("不同数据类型取整：（10+5j）//10.0", (10 + 5j) // 10.0)
print("-----")
print("不同数据类型取幂：10**25.0", 10 ** 25.0)
print("不同数据类型取幂：（10+5j）**10", (10 + 5j) ** 10)
print("不同数据类型取幂：（10+5j）**10.0", (10 + 5j) ** 10.0)
print("-----")
print("不同数据类型四舍五入：10.01", round(10.01))
# round 不能用于复数
# print("不同数据类型四舍五入：（10+5j）", round(10 + 5j))

print("==========")
