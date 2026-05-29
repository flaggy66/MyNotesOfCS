# 映射类型
print("------映射类型------")

#  字典
dict1 = {"name": "Tom", "age": 18, "height": 183.6, "is_married": True, "email": "tom@lsfef.com"}
dict2 = {0: "北京 ", 1: "上海", 2: "广州", 3: "深圳", 4: "杭州", 5: "合肥", 6: "武汉", 7: "长沙", 8: "南昌"}
dict3 = {}
print(type(dict1))
print(dict1)
print(dict2)
print(dict3)

#  嵌套
listIndic = {
    "name": "计算机科学与技术",
    "program_language": ["Python", "C++", "Java", "Rust"]
}
print(listIndic)

dictInlist = [
    {"city": "北京", "code": "0010", "name": "beijing"},
    "上海",
    "深圳",
    "广州"
]
print(dictInlist)

dictIndict = {
    "citis": ["北京", "上海", "广州", "深圳", "重庆", "成都"],
    "university": {
        "北京": "清华大学",
        "上海": "上海交通大学",
        "南京": "南京大学"
    },
    "counts": 158926
}
print(dictIndict)

print("==========")

# 获取字典中的值
print("获取字典中的值：")
print(dict1["name"])
print(dict2[2])

print(dict1.get("age"))
print(dict2.get(1))
print(dict2.get(100))
print(dict2.get(100, "键名不存在"))

# 添加键值对
print("添加键值对：")
dict1["gender"] = "male"
dict2[100] = "长春"
print(dict1)
print(dict2)

# 修改字典值
print("修改字典的值：")
dict1["name"] = "Jack"
dict2[1] = "香港"
print(dict1)
print(dict2)

# 删除键值对
print("删除键值对：")
del dict1["gender"]
del dict2[100]
print(dict1)
print(dict2)

# 字典遍历
print("字典遍历-获取键值对：")
for k, v in dict1.items():
    print(k, "::", v)

for num, city in dict2.items():
    print(num, "----", city)

print("字典遍历-获取键：")
for k in dict1.keys():
    print(k)

for num in dict2:
    print(num)

# 对键进行排序后遍历
print("字典遍历-键排序遍历：")
for k in sorted(dict1.keys()):
    print(k)

# 遍历字典中的所有值
print("字典遍历-获取所有值：")
for value in dict1.values():
    print(value)

for city in dict2.values():
    print(city)
