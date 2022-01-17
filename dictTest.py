# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/13 16:30
# @File:dictTest.py
# @Software:PyCharm

# 键值对存储数据
dict1 = {'name': 'pengxinjie', 'age': 18}

dict1['name'] = 'neymar'
print(dict1)

dict1['num'] = 1001
print(dict1)

# 删除指定键值对
del dict1['age']
print(dict1)

# 清空
dict1.clear()
# 变为空字典
print(dict1)

dict1 = {'name': 'pengxinjie', 'age': 18}

# get()
print(dict1.get('name'))

# get不存在，则返回第二个参数的值
print(dict1.get('nana', 100))

# 没有第二个参数，则默认返回None
print(dict1.get('nana'))

# keys(),values,items
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# 遍历字典的key
for k in dict1.keys():
    print(k)

for key, val in dict1.items():
    print(f'{key} = {val}')
