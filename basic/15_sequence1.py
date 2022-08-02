# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/1 11:50
# @File:15_sequence1.py
# @Software:PyCharm

"""序列"""

# +,*的使用
print([1, 2, 3]+[4, 5, 6])
print((1, 2, 3)+(4, 5, 6))
print("hello "+"world")

print([1, 2]*3)

# 检测对象的id值是否相等
# is ; is not
x = "hello"
y = "hello"
print(x is y)

x = {1, 2}
y = {1, 2}
print(x is y)

# 判断包含
# in ; not in
print("hello" in "hello world")
print("peng" not in "peng xinjie ")


# del ：删除一个或多个指定对象
print(x)
print(y)

del x, y
# print(x)
# print(y)

# del删除指定元素
x = [1, 2, 3, 4, 5]
del x[1:4]
print(x)

y = [1, 2, 3, 4, 5]
y[1:4] = []
print(y)

# 清空列表
y = [1, 2, 3, 4, 5]
del y[:]
print(y)