# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/13 16:53
# @File:publicOp.py
# @Software:PyCharm

# *的应用
print('1' * 10)

li = [1, 2]
print(li)
print(li * 10)

tu = (1, 2)
print(tu * 10)

# in 和 not in
print('a' in 'abc')
print('a' in 'bc')
print('a' not in 'bc')
# 列表元组同上

# len,计算长度
print(len('123'))
print(len(li))
print(len(tu))

# max,min
print(max(li))
print(min(li))


# range
for r in range(1, 10, 3):
    print(r, end=' ')
print('----------------')

for r in range(10):  # 不包含10
    print(r, end=' ')


