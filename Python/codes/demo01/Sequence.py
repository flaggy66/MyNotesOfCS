# 序列类型

# 字符串
print("------字符串------")

string1 = "Hello world!"
print(type(string1))
print(string1)

print("字符串长度：", len(string1))

print("字符串索引：", string1[0])

print("字符串切片：", string1[0:5])
print("字符串切片：", string1[2:6])

print("字符串查找：", string1.find("world"))

print("字符串迭代：")
for i in string1:
    print(i)

print("字符串转换：", string1.upper())

print("字符串转换：", string1.lower())

string2 = string1.replace("Hello", "Hi")
print("字符串替换：", string2)

string3 = "Tom."

print("字符串拼接：", string1 + string3)

print("字符串重复：", string3 * 3)

string4 = '单引号字符串'
string5 = """（首行）
三引号的
多行
字符串
（末行）"""

print(string4)
print(string5)

print("==========")

# 列表
print("------列表------")

cities = ["上海", "北京", "广州", "深圳"]
print(type(cities))
print(cities)

tom_infos = ["Tom", 18, 183.6, True, "slefslehf@lsfef.com"]
print(tom_infos)

print(cities[2])
print(tom_infos[-1])

# 列表切片
print("列表切片：")
print(cities[0:2])
print(tom_infos[1:4])

# 列表迭代
print("列表迭代：")
for i in cities:
    print(i)

# 列表查找
print("列表查找：")
print(cities.index("上海"))

# 列表计数
print("列表计数：")
print(cities.count("深圳"))

# 列表追加
print("列表追加：")
cities.append("杭州")
cities.append("合肥")
cities.append("武汉")
cities.append("长沙")
cities.append("南昌")
tom_infos.append("上海")
print(cities)
print(tom_infos)

# 列表插入
print("列表插入：")
cities.insert(1, "西安")
print( cities)

# 列表删除
print("列表删除：")
cities.remove("上海")
print(cities)
del cities[0]
print(cities)
tom_infos.pop()
print(tom_infos)
first_city = cities.pop(0)
print(first_city)
cities.remove("深圳")
print(cities)

# 修改列表元素
print("修改列表元素：")
cities[0] = "上海"
print(cities)

# 列表排序
print("临时排序：", sorted(cities))
print(cities)
print("列表排序：")
cities.sort()
print(cities)

# 列表反转
print("列表反转：")
cities.reverse()
print(cities)

# 判断值是否在列表中
chars = ['A','B','z','f','t','P']
print(chars)
print("z是否在chars中：", "z" in chars)
print("a是否不在chars中：", "a" not in chars)

print("==========")

# 元组
print("------元组------")
seasons = ("春", "夏", "秋", "冬")
months = ("1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月")
weeks = "周一", "周二", "周三", "周四", "周五", "周六", "周日"
one_content = (12,)
print(type(seasons))
print(type(one_content))
print(seasons)
print(months)
print(weeks)
print(one_content)

# 元组迭代
print("元组迭代：")
for i in seasons:
    print(i)


