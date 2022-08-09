# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/5 16:19
# @File:24_fun4.py
# @Software:PyCharm

"""递归"""


# 输出x句helloworld


def print_hello(x):
    if x > 0:
        print("hello world")
        print_hello(x - 1)


print_hello(2)


# 递归求一个数的阶乘


def jie_cheng(x):
    if x == 1:
        return 1
    else:
        return jie_cheng(x - 1) * x


print(jie_cheng(6))


# 递归实现斐波那契数列
def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)


print(fib(12))