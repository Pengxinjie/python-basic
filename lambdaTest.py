# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/13 17:47
# @File:lambdaTest.py
# @Software:PyCharm

# lambda的应用场景
# 函数有一个返回值，并且只有一句代码

def my_sum(a, b):
    return a + b


fn1 = lambda a, b: a + b
print(fn1(1, 2))

# 带判断的lambda
fn2 = lambda a, b: a if a > b else b

print(fn2(100, 500))
print(fn2(1000, 500))

# 列表数据按字典key的值排序
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}]
# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(lambda x: x['name'])
print(students)


# # 按name值降序排列
# students.sort(key=lambda x: x['name'], reverse=True)
# print(students)
# # 按age值升序排列
# students.sort(key=lambda x: x['age'])
# print(students)


# 高阶函数
def sum_num(a, b, f):
    return f(a) + f(b)


# 先求绝对值，再求和
print(sum_num(-2, 5, abs))

# 内置高阶函数
# map()
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


result = map(func, list1)
print(list(result))


# reduce
import functools


def function(a, b):
    return a+b


result = functools.reduce(function, list1)
print(result)


def filter_function(x):
    return x % 2 == 0


result = filter(filter_function, list1)
print(list(result))