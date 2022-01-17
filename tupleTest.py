# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/13 16:25
# @File:tupleTest.py
# @Software:PyCharm

"""
元组tuple：不允许修改的列表
"""

t1 = (1, 2, 3)

for t in t1:
    print(t)

t2 = (10,)  # 只有一个元素也加上','，不然就不是tuple类型
t3 = (10)
print(type(t2))
print(type(t3))

# 不可修改元组内的数据，否则报错
t1[0] = 1
print(t1)  # TypeError: 'tuple' object does not support item assignment
