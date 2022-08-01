# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 13:54
# @File:07_list1.py
# @Software:PyCharm

"""列表"""
li = [1, 2, 3, 4, "hello"]
print(li)

for l in li:
    print(l)  # 循环遍历列表

# 下标索引
print(li[2])

# 访问最后一个元素
print(li[len(li)-1])
print(li[-1])

# 切片
print(li[0:3])  # 左闭右开
print(li[3:6])  # 右边值超出不报错

print(li[2:])   # 从2开始的往后元素
print(li[:3])   # 下标3之前的所有元素
print(li[:])    # 列表中的所有元素

print(li[::2])  # 选取跨度为2
print(li[::-2])  # 选取跨度为2，但倒着来

print(li[::-1])  # 列表倒序输出

# 列表的增删改查
# 增
footballers = ["Neymar", "Messi", "Pengxinjie"]
footballers.append("suarez")  # 一个一个添加
print(footballers)

# extend添加可迭代对象
footballers.extend(["C罗", "Bale"])
print(footballers)

# 切片添加
footballers[len(footballers):] = [6, 7]  # 在最后位置追加
print(footballers)

# 指定位置添加元素
footballers.insert(0, "first")  # 在0号位置插入元素
print(footballers)
footballers.insert(len(footballers), "end")  # 在末尾位置插入元素
print(footballers)

# 删除指定元素(非指定位置)
footballers.remove("Pengxinjie")
print(footballers)
# 存在多个匹配的元素，只删除第一个
# 不存在该元素，则报错

# 删除指定位置元素
footballers.pop(0)
print(footballers)
footballers.pop(-1)
print(footballers)

# 清空列表
# footballers.clear()
# print(footballers)

# 改
footballers[0] = "Benzema"
print(footballers)
footballers[3:] = ["小罗", "大罗"]
print(footballers)

# 列表的排序
lists = [32, 4, 64, 6, 7, 856, 34, 231, 1, 2]
lists.sort()
print(lists)

# 翻转
lists.reverse()
print(lists)
print("\n---------------------------------------")

lists = [32, 4, 64, 6, 7, 856, 34, 231, 1, 2]
# 排序+翻转
lists.sort(reverse=True)
print(lists)

# 统计某元素出现的次数
print(lists.count(10))
print(lists.count(1))
print()
# 查找索引值
print(footballers.index("小罗"))
footballers[footballers.index("小罗")] = "小小罗"
print(footballers)

footballers_copy1 = footballers.copy()
print(footballers_copy1)

# 通过切片拷贝
footballers_copy2 = footballers[:]
print(footballers_copy2) # 都是浅拷贝