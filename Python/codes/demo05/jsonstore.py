import json
from pathlib import Path

# 简单数据
names = ["Ton", "John", "Smith"]
json_str = json.dumps(names)
# 写入文件
json_file = Path("simple.json")
json_file.write_text(json_str, encoding="utf-8")
# 从文件读取
json_str = json_file.read_text(encoding="utf-8")
names = json.loads(json_str)
print(names)


# 对象类型
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = People("Ton", 20)
json_str = json.dumps(people.__dict__)
# 写入文件
json_file = Path("people.json")
json_file.write_text(json_str,encoding="utf-8")
# 从文件读取
json_str = json_file.read_text(encoding="utf-8")
people = json.loads(json_str)
print(people)