# 集合类型
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {"Java", "Python", "C++", "C#", "PHP", "JavaScript"}
print(type(set1))
print(set1)
print(set2)

set3 = {6, 9, 21, 4, 3, 2, 11, 13, 0}
print(set3)

print("集合长度：", len(set3))

print("集合查找，6：", 6 in set3)

print("集合迭代：")
for i in set3:
    print(i)

print("-----集合运算-----")
print("集合并集：", set1 | set3)
print("集交集：", set1 & set3)
print("集差集：", set1 - set3)
print("集补集：", set1 ^ set3)
print("集子集：", set1 <= set3)
print("集超集：", set1 >= set3)
print("集相等：", set1 == set3)
print("集不相等：", set1 != set3)
print("==========")
