# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/2 16:35
# @File:16_sequence2.py
# @Software:PyCharm

"""列表、元组、字符串相互转换"""
# list()  tuple()  str()
li = list("xinjie")
print(li)
print(list((1, 2, 3)))

print(tuple([1, 2, 3]))

print(type(str([1, 2, 3])))

s = [1, 1, 2, 3, 5]
print(min(s))
print(max(s))

st = "pengxinjie"
print(min(st))
print(max(st))

# sum
s = [1, 12, 2, 3, 4, 5]
print(sum(s))

print(sorted(s))
print(reversed(s))

s = ["a", "ab", "abcd", "abc", "ab"]

print(sorted(s, key=len))

print(list(reversed(s)))

print(list(reversed(range(0, 10))))