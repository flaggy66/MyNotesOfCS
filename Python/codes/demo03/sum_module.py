# 提供求和函数的模块
def sum_two(a, b):
    return a + b


def sum_three(a, b, c):
    return a + b + c


def sum_many(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum