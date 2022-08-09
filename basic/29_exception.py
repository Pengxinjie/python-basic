# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/8 21:55
# @File:29_exception.py
# @Software:PyCharm

try:
    print(1/0)
except:
    print("除数不能为0")

try:
    print(1/0)
except ZeroDivisionError:
    print("除数不能为0")

print("============================")

try:
    print(1/0)
except ZeroDivisionError as e:
    print("除数不能为0")
    print(e)

print("-------------------------------")
try:
    print(12 + "pengxinjie")
    print(1/0)
except (ZeroDivisionError, TypeError, ValueError):
    pass


# 独立处理多个异常  只处理遇到的第一个异常
print("-------------------------------")
try:
    print(12 + "pengxinjie")
    print(1/0)
except ZeroDivisionError as ze:
    print(ze)
except TypeError as Te:
    print(Te)


print("-------------------------------")
try:
    print(12)
    print(1/1)
except ZeroDivisionError as ze:
    print(ze)
except TypeError as Te:
    print(Te)
else:
    print("没有发生异常")


# finally
print("-------------------------------")
try:
    print(12)
    print(1/1)
except ZeroDivisionError as ze:
    print(ze)
except TypeError as Te:
    print(Te)
else:
    print("没有发生异常")
finally:
    print("资源关闭")

# raise ValueError("值错误")  主动触发异常

# assert语句
a = 1
assert a == 1, "不合法的值"