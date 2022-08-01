# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/31 16:09
# @File:10_tuple.py
# @Software:PyCharm

"""元组"""
t1 = (1, 2, 3, 4, 5)
print(t1)
t2 = 1, 2, 3, 4, 5
print(t2)
print(t1[:2])

print(t1.count(3))  # 统计 元组中 元素3 的个数

print(t1.index(3))  # 求出3在元组t1中的位置

t3 = t1 + t2  # 元组拼接
print(t3)
print(t1*3)  # 乘法

# 元组嵌套
s = 1, 2, 3
t = 4, 5, 6
w = s, t
print(w)
print("---------------------")

for i in w:
    for j in i:
        print(j, end=' ')
print("\n-----------------")

# 列表推导式
tu = [j for i in w
      for j in i]
print(tu)

# 一直加上圆括号

# 生成只有一个元素的元组
x = (501)
print(type(x))  # 类型为int

y = (501, )
print(type(y))  # 类型为tuple


# 打包与解包
tup = (1, "hello", 3)  # 打包
li = [1, "hello", 3]  # 打包

x, y, z = tup
print("------------------------")
print(x, end=' ')
print(y, end=' ')
print(z, end=' ')

print()
x, y, z = li
print(x, end=' ')
print(y, end=' ')
print(z, end=' ')

print("-------------------")

# 多重赋值
x, y = 3, 4

print(x)
print(y)

# 元组中嵌套列表
li1 = [1, 2, 3]
li2 = [4, 5, 6]

tu1 = (li1, li2)
tu1[0][0] = 100  # 可修改
print(tu1)
