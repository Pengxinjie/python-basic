# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/4 13:34
# @File:21_fun1.py
# @Software:PyCharm

def myfun():
    for i in range(3):
        print("hello world")


myfun()


def myfunc(name, age):
    print(f"my name is {name}, age {age}")


myfunc("pengxinjie", 19)


def div(x, y):
    if y == 0:
        return "除数不能为0！"
    return x / y


print(div(7, 3))
print(div(7, 0))


def fun(x, y, z):
    return "".join((z, y, x))


print(fun("peng", "xin", "jie"))
print(fun(z="peng", y="xin", x="jie"))


# 默认参数--应放在参数列表的最后
def func(x, y, z="-messi-"):
    return "".join((z, y, x))


print(func("pengxinjie ", "neymar"))


def func(*args):
    print("有{}个参数".format(len(args)))
    for i in range(len(args)):
        print(args[i], end="")
    print()
    return 1, 2, 3  # 返回多个值


x, y, z = func("peng", "xin", "jie")

print(x)


# 结合关键字参数
def func(*args, x, y):
    print("有{}个参数".format(len(args)))
    for i in range(len(args)):
        print(args[i], end="")
    print("{}-{}".format(x, y))
    return 1, 2, 3  # 返回多个值


func(1, 2, 3, x="leng", y="xuan")  # 收集参数后面要用关键字参数


# 收集参数，以字典方式存储
def func(**kwargs):
    print(kwargs)
    return ""


func(name="pengxinjie", age=19, gender="male")


def func(x, *args, **kwargs):
    print(x)
    print(len(args), args)
    print(len(kwargs), kwargs)
    return ""


func(10, 1, 2, 3, a=100, b=101)

print(help(str.format))


args = (1, 2, 3, 4)


def myfunc(a, b, c, d):
    print(a, b, c, d)
    return ""


myfunc(*args)  # *args解包
print()
kwargs = {"a": 1,
          "b": 2,
          "c": 3,
          "d": 4}

myfunc(**kwargs)  # 解包


# global

val = 110


def fun():
    global val  # 使用global在函数中修改全局变量的值
    val = 230


print(val)
fun()
print(val)


# 嵌套函数
def fun():
    x = 503
    def funb():
        x = 880
        print(x, "in fun")
    funb()
    print(x, "in funb")


fun()

# nonlocal：内部函数修改外部变量

def fun():
    x = 503
    def funb():
        nonlocal x
        x = 880
        print(x, "in fun")
    funb()
    print(x, "in funb")


