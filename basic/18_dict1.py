# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/2 17:59
# @File:18_dict1.py
# @Software:PyCharm

"""字典"""
dic = {"1": "neymar",
       "2": "messi",
       "3": "sureaz",
       3: "pengxinjie"}
# 键值对
print(type(dic))
print(dic)

for each in dic:
    print(each, ":", dic[each])

dic["100"] = "c ro"

for each in dic:
    print(each, ":", dic[each])

# 字典的创建方法
dic2 = dict(梅西="10", 内马尔="11")  # 此种方式即使键是字符串也不能加“”
print(dic2)

dic3 = dict([(10, "messi"), (11, "neymar"), (9, "suarez")])
print(dic3)

dic4 = dict(zip([9, 10, 11], ["suarez", "messi", "neymar"]))
print(dic4)


# 增
# fromkeys(iterable[, values])
# 快速创建字典，赋统一值
di = dict.fromkeys("pengxinjie", "0")
print(di)

di = dict.fromkeys(["messi", "neymar", "suarez"], 0)
print(di)

di["messi"] = 10
print(di)

di["bale"] = 18
print(di)

# 字典中的键不可重复，后添加的替换前添加的


# 删除
# pop()：返回键所对应的值
print(di.pop("bale"))

# di.pop("cluo")
print(di.pop("cluo", "字典中无此元素"))

# del 删除
del di["messi"]
print(di)

# del di    删除整个字典
# print(di)  报错

di.clear()  # 清空字典内容
print(di)  # 输出空字典
