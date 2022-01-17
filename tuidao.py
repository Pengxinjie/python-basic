# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/13 17:10
# @File:tuidao.py
# @Software:PyCharm

# 列表推导式
list1 = [i for i in range(10)]
print(list1)

# 加if
list2 = [i for i in range(10) if i != 5]
print(list2)

# 字典推导式
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)
