# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/2 18:53
# @File:20_set.py
# @Software:PyCharm

# 集合：唯一性
# 创建方法
se = {1, 3, 4, 5}
print(se)

s = {x for x in "pengxinjie"}
print(s)  # 集合的无序性

# 类型构造器
s = set("peng")
print(s)

# 集合无序，故无法使用下标索引访问

# in && not in  区分大小写
print("p" in s)
print("k" not in s)

for each in s:
    print(each)

# 利用集合去重
se = set([1, 2, 3, 4, 4])
print(se)

s = [1, 2, 3, 4, 4]
# 是否每个元素唯一？
print(len(s) == len(set(s)))

# 两个集合是否毫不相关
s = set("peng")
print(s.isdisjoint("fsf"))
print(s.isdisjoint("pfh"))

# 是否子集
print(set("peng").issubset("pengxinjie"))
print(set("peng").issubset("xinjie"))

# frozenset 不可变
t = frozenset("asf")

s = set("peng")
print(s)
s.update([1, 2], [1, 2, 3])
print(s)

# add方法，将整个字符串作为一个元素
s.add("neymar")
print(s)

# s.remove(34)  # 抛异常
s.discard(34)  # 不报错

# 可哈希
# 可哈希对象才能作为字典的键、集合的值
# 可变对象、容器不可哈希

y = {frozenset({1, 2, 3}), 2, 3}
print(y)