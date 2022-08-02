# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/2 16:53
# @File:17_sequence3.py
# @Software:PyCharm

# all() && any()
s = [1, 2, 3]
print(all(s))
s.append(0)
print(all(s))

print(any(s))
for i in range(0, len(s)):
    s[i] = 0

print(any(s))


# enumerate() : 返回一个枚举对象，将可迭代对象中的每个元素从0开始的序号
# 共同构成一个二元组的列表
s = ["peng", "xin", "jie"]
x = list(enumerate(s, start=1))  # start可选函数，选择起始的索引
print(x)

# zip()：创建一个聚合多个可迭代对象的迭代器，它会将作为参数传入的每个可迭代对象的
# 每个元素依次组成元组，即第i个元组包含来自每个参数的第i个参数
t = list(zip("peng", "xin", "jie"))
print(t)

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
z = [7, 8, 9]
zipped = zip(x, y, z)
print(list(zipped))


# map()
mapped = map(ord, "peng")  # ord，求出每个字母的编码
print(list(mapped))

print(list(map(pow, [1, 2, 3], [1, 2, 3])))

# fliter
print(list(filter(str.islower, "afsfaFASDFsf")))  # 将小写字母过滤出来
s = filter(str.islower, "afsfaFASDFsf")
# 可迭代对象可以重复使用
# 迭代器是一次性的
print("-------------------------------")
mapped = map(ord, "asfa")
print(list(mapped))  # 正常打印
print(list(mapped))  # 输出空

# iter() 迭代器
l = [1, 2, 3, 4]
y = [1, 2, 3, 4]
y = iter(y)
print(type(x))
print(type(y))

print(next(y, "迭代器到末尾啦~"))
print(next(y, "迭代器到末尾啦~"))
print(next(y, "迭代器到末尾啦~"))
print(next(y, "迭代器到末尾啦~"))
print(next(y, "迭代器到末尾啦~"))

