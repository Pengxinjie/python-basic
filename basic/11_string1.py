# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/31 16:44
# @File:11_string1.py
# @Software:PyCharm

# 字符串回文数的判断
a = "12321"
b = "12345"
print("是回文数" if a == a[::-1] else "不是回文数")
print("是回文数" if b == b[::-1] else "不是回文数")

print(b[::-1])
c = "12321"
print(a == c)


# 字符串函数
# 一.大小写字母换来换去
str1 = "hello WOrld"
# ①capitalize() : 首字母变成大写,其他字母变成小写
print(str1.capitalize())
# ②casefold() : 所有字母变成小写
print(str1.casefold())
# ③title() : 所有单词的首字母大写，其他字母变成小写
print(str1.title())
# ④swapcase() ：大小写翻转
print(str1.swapcase())
# ⑤upper() : 所有字母变成大写
print(str1.upper())
# ⑥lower() ： 所有字母变成小写
print(str1.lower())

# 二、左中右对齐
x = "有内鬼，停止交易！"
# ①center(width,fillchar='')
print(x.center(5))  # 小于字符串长度，输出原字符串
print(x.center(15))  # 居中对齐，空格填充
print(x.center(15, "1"))  # 居中对齐，1填充
# ②ljust(width,fillchar='') ：左对齐
print(x.ljust(15))  # 右边空格填充
# ③rjust(width,fillchar='')
print(x.rjust(15))  # 右对齐，左边空格填充
# ④zfill(width)
print(x.zfill(15))  # 左边填充0

print("520".zfill(5))
print("-520".zfill(5))
# fillchar=''  指定字符填充