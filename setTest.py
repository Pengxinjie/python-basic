# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/13 16:43
# @File:setTest.py
# @Software:PyCharm

s = {1, 2, 3, 4}
print(s)

# 创建空集合，只能用set()
s2 = set()
print(s2)

# 集合内的元素不重复

# 增
s.add(5)
print(s)

# update：追加的是序列
s.update([6, 7])
print(s)

s.update('peng')
print(s)

# remove,删除数据,若不存在则报错
s.remove(5)
print(s)
# s.remove(10) 报错

# discard删除数据，不存在也不报错
s.discard(10)

# 查
print(10 in s)
print(1 in s)

