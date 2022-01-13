# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/12 15:53
# @File:stringTest.py
# @Software:PyCharm

# 三引号字符串
str1 = '''
    peng
    xin
    jie
'''
print(str1)

print("I'm Tom")
print('I\'m Tom')  # 转义字符

name = 'neymar'
print(name[1])

# 切片
print(name[1:5:2])
print(name[1:5])
print(name[:4])
print(name[:])
print(name[::2])
print(name[:-1])  # 表示到倒数第一个数，但不包含
print(name[::-1])  # 从后往前
print("--------------")


# 字符串常用方法
user = 'pengxinjie'
# find()寻找子串,找到则返回下标，否则返回-1
print(user.find('i'))
# 6,9表示起始位置和结束位置，左闭右开
print(user.find('i', 6, 9))
print(user.find('i', 9))  # 返回-1

# index()
print(user.index('i'))
# print(user.index('i', 9))  # 报错

print(user.count('i'))  # 统计子串出现次数

# 修改字符串
print(user.replace('i', '9'))
print(user)  # 并不改变原本的字符串

print(user.replace('i', '9', 1))  # 1表示只替换一次

# 分割
print(user.split('i'))
print(user.split('i', 1))  # 1同样表示次数

lists = ['1', '2', '3', '4']
t1 = ('1', '2', '3')
print('-'.join(lists))
print('_'.join(t1))

# 首字符转大写
print(user.capitalize())

uname = 'peng xin jie'
# 将所有单词的首字符转大写
print(uname.title())

# 将字符串中的大写转小写
print(uname.title().lower())

# 将字符串中的小写转大写
print(uname.upper())

uname = ' peng xin jie '
print(uname)
# 删除左右两侧的空格字符
print(uname.strip())

# 判断
# 检查字符串是否以指定子串开头
print('pengxinjie'.startswith('peng'))
print('pengxinjie'.startswith('peb'))

# 结尾
print('pengxinjie'.endswith('jie'))
print('pengxinjie'.endswith('jir'))

# 字符串至少有一个字符且全是字母
print('pengxinjie'.isalpha())
print('pengxinjie '.isalpha())

# 全是数字
print('123'.isdigit())
print('123 '.isdigit())
print(''.isdigit())

# 全是数字或者字母
print('lengxuan19'.isalnum())

# 只含空格
print('  '.isspace())