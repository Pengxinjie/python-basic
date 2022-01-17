# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/13 15:23
# @File:listTest.py
# @Software:PyCharm

lists = ['peng', 'xin', 'jie']

# 相关函数
# 长度
print(len(lists))

# 查找位置
print(lists.index('jie'))

# 统计该数据出现的次数
print(lists.count('peng'))

# 判断是否存在
print('peng' in lists)
print('peg' in lists)
print('oe' not in lists)

# 列表结尾追加数据
lists.append('neymar')
print(lists)
# 列表为可变类型

lis = ['1', '2']
lists.append(lis)  # 整个追加
print(lists)

lists.extend(lis)
print(lists)  # 逐个追加

# 指定位置添加
lists.insert(0, 'messi')
print(lists)

# 删除
# 指定下标删除
del lists[5]
print(lists)

lists.pop(5)
print(lists)

lists.append('1')
lists.append('1')
lists.append('2')
print(lists)
# 指定内容删除，只删除第一个匹配到的
lists.remove('2')

print(lists)

# clear清空&del删除
lis.clear()
print(lis)

del lis
# print(lis)  # NameError: name 'lis' is not defined

# 修改指定下标数据
lists[0] = 'ney'
print(lists)

lists[1] = "messi"
print(lists)

lists[5] = 'pengxinjie'
print(lists)

# 翻转
lists.reverse()
print(lists)

# 排序
lists.sort()
print(lists)

# 复制
list2 = lists.copy()
print(list2)

# 列表遍历
for list in lists:
    print(list)

