# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 15:17
# @File:08_list2.py
# @Software:PyCharm
import copy
"""嵌套列表"""
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)

# 遍历嵌套列表
for i in matrix:
    for j in i:
        print(j, " ", end="")
    print()

# 通过下标访问嵌套列表
print(matrix[2][0])

print("---------------------------------------------------")
# 浅拷贝与深拷贝
a = [0] * 3
for i in range(3):
    a[i] = [0] * 3

print(a)

b = [[0] * 3] * 3
print(b)

print(a[0] is a[1])
print(b[0] is b[1])

# 深拷贝
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix_copy = copy.deepcopy(matrix)
matrix_copy[1][1] = 10;
print(matrix_copy)
print(matrix)