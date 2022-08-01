# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 9:39
# @File:02_varAndstring.py
# @Software:PyCharm

"""变量及字符串"""
import random
x = 3
y = 5

x, y = y, x  # 交换两个变量的值

print(x)
print(y)

print('I love you')  # 单引号和双引号都行

print("'watch movie?','let's go!'")  # 双引号中包含单引号
print('"watch movie?"\n"let\'s go!"')  # 单引号中包含双引号
# 使用\转义字符   \n：换行

# 原始字符串
print("hello \n world")
print(r"hello \n world")  # 输出\n


# 反斜杠作为跨行的方式
# print("hello
#       world") 报错
print("hello \
      world")

# 长字符串(三引号字符串)解决跨行问题
# triple quoted
print('''
hello
world
''')


# 字符串的加法和乘法
print(530+1414)
print('530'+'1314')  # 字符串拼接 加法
print('I love you. ' * 10)  # 乘法

# 随机数
aa = random.randint(1, 10)
print(aa)

# 随机数重现
xx = random.getstate()
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
# 4 7 7 5 5
random.setstate(xx)
bb = random.randint(1, 10)
cc = random.randint(1, 10)
dd = random.randint(1, 10)
ee = random.randint(1, 10)
ff = random.randint(1, 10)
# 4 7 7 5 5
print(bb)
print(cc)
print(dd)
print(ee)
print(ff)

