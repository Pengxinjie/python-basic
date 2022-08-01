# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 15:54
# @File:09_list3.py
# @Software:PyCharm

"""列表推导式"""
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [i for i in x]
print(y)

y = [i + 1 for i in x]
print(y)

y = [i * 2 for i in x]
print(y)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 提取出矩阵第二列的元素
col2 = [r[1] for r in matrix]
print(col2)

# 提取主对角线上的元素
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(diagonal)

# 创建二维空列表
S = [[0] * 3 for i in matrix]
print(S)

words = ["Great", "Fish", "brilliant", "Excellent", "Fantastic"]
# 筛选出F开头的单词
words_F = [s for s in words if s[0] == 'F']
print(words_F)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 嵌套列表推导式，降维
oneDimensional = [va for r in matrix
                  for va in r]
print(oneDimensional)



