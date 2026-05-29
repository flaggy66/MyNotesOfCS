# 简单值匹配
code = int(input("请输入错误代码："))
match code:
    case 400:
        print("错误代码：400，请求错误")
    case 404:
        print("错误代码：404，未找到")
    case 500:
        print("错误代码：500，服务器错误")
    case _:  # 这是一个通配符，表示匹配“其他所有情况”
        print("未知错误")

# 解构匹配
command = input("请输入指令（例如：goto 10 20）：").split()
match command:
    case ["quit"]:
        print("退出程序")
    case ["load", filename]:  # 匹配有两个元素，且第一个是 load 的列表
        print(f"正在加载文件：{filename}")
    case ["goto", x, y]:  # 自动把第二、三个元素赋值给变量 x 和 y
        print(f"移动到坐标：({x}, {y})")
    case ["say", *words]:  # *words 匹配剩余的所有内容
        print(f"你说：{' '.join(words)}")
    case _:
        print("无法识别的指令")

# 条件匹配
x = int(input("请输入x坐标："))
y = int(input("请输入y坐标："))
point = (x, y)
match point:
    case (x, y) if x == y:
        print(f"点在对角线上：{x}")
    case (x, y):
        print(f"普通坐标点：({x}, {y})")


# 对象匹配
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


user = User("Alice", "admin")

match user:
    case User(name=name, role="admin"):
        print(f"管理员 {name} 已登录")
    case User(name=name):
        print(f"普通用户 {name} 已登录")
