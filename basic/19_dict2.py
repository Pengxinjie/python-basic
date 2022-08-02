# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/2 18:26
# @File:19_dict2.py
# @Software:PyCharm

d = dict.fromkeys("abcd", "")
print(d)

# update([other])  # 批量修改
d.update({"a": 1, "b": 2, "c": 3})
print(d)

d.update(a=10, b=2, c=3)
print(d)

# 查
print(d.get("a", "没有这个键"))
print(d.get("g", "没有这个键"))
print(d.get("g"))

# setdefault(key[,default])
d.setdefault("g", 12)
print(d)

d.setdefault("g", 1)  # 已存在g，赋值不起作用
print(d.setdefault("g", 1))
print(d)


# 视图对象  字典发生改变，视图对象也跟着变
keys = d.keys()
val = d.values()
items = d.items()
print(keys)
print(val)
print(items)

d['a'] = "safasd"

print(keys)
print(val)
print(items)

# len获取键值对数量
print(len(d))

print("a" in d)
print("a" not in d)

print(list(d))
print(list(d.values()))

# 字典嵌套
d = {"彭鑫杰": {"语文": 89, "数学": 89},
     "song": {"语文": 90, "数学": 89}}
print(d["彭鑫杰"]["数学"])

# 字典推导式
b = {x:ord(x) for x in "pengxinjie"}
print(b)