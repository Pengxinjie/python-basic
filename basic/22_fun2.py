# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/4 21:10
# @File:22_fun2.py
# @Software:PyCharm

"""闭包"""


def funa():
    x = 880

    def funb():
        print(x)

    return funb


fun = funa()
fun()


def power(exp):
    def exp_of(base):
        return base ** exp

    return exp_of


squ = power(2)
cube = power(3)
print(squ(5))
print(cube(5))


def outer():
    x = 0
    y = 0

    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"x = {x},y = {y}")

    return inner


ou = outer()
ou(4, 5)
ou(4, 5)
ou(10, 10)

import time


def time_master(func):
    print("开始运行程序......")
    start = time.time()
    func()
    end = time.time()
    return f"消耗：{end - start:.4f}"


def func():
    for i in range(1000):
        print("正在执行func...")
    return ""


# print(time_master(func))


def time_master(func):
    def call_func():
        print("开始运行程序......")
        start = time.time()
        func()
        end = time.time()
        print(f"消耗：{end - start:.4f}")
    return call_func


@time_master
def func():
    for i in range(1000):
        print("正在执行func...")
    return ""


func()