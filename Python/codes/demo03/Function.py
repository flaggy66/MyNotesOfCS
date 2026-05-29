# 函数
def sum_one_to_num(num):
    """求1到num的整数和"""
    sum = (num / 2) * (1 + num)
    return int(sum)


print(sum_one_to_num(100))


def print_people(name, age, email, address, gender):
    """打印个人信息"""
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Address:", address)
    print("Gender:", gender)


print_people("Tom", 30, "<EMAIL>", "US", "male")
print_people(name="李明", email="good@a.com", gender="男", age=21, address="北京")


def draw(size, shape="circle", color="red"):
    """画图形"""
    print(f"The shape is {shape} , its size is {size}, and the color is {color}")


draw(size="large")
draw("100px", color="blue")


def print_names(*names):
    print(*names)
    print(names)


print_names("Jack", "Tom", "Aimy", "Bob", "Rose")


def print_students(school="Primary School", *students):
    print(school, students)


print_students("Jack", "Tom", "Aimy", "Bob", "Rose")
print_students("High School")
print_students("High School", "Jack", "Tom", "Aimy", "Bob", "Rose")


def print_university(**university):
    print(*university)
    print(university)


print_university(name="清华大学", location="北京", built_date="1911-3-30")
