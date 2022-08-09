# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/5 15:29
# @File:23_fun3_lambda.py
# @Software:PyCharm


square = lambda x: x * x

print(square(2))

"""生成器"""


def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1


for i in counter():
    print(i)


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c, "没啦"))


# 生成器实现斐波那契数列
def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1+back2


print()
f = fib()
i = 0
while i < 10:
    print(next(f))
    i += 1


# 生成器表达式
