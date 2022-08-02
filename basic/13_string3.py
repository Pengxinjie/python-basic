# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/1 9:23
# @File:13_string3.py
# @Software:PyCharm

"""字符串API"""

# 截取字符串
s = "  Hello World  "
print("原始字符串:", s)
# strip(chars=None)  # 去除左右侧空白
print(s.strip())
# lstrip(chars=None)
print(s.lstrip())  # 去除左侧空白
# rstrip(chars=None)
print(s.rstrip())  # 去除右侧空白
# 例子
s = "www.baiccdu.com"
print(s.lstrip("wcom."))  # 去除左侧开头的www和.
print(s.rstrip("wcom."))  # 去除右侧开头的com和.
print(s.strip("wcom."))  # 去除两侧

# python3.9
# removeprefix(prefix) ：删除指定前缀
# removesuffix(suffix) ：删除指定后缀


# 拆分和拼接
# partition(sep) ：从左往右切割
print("www.njier.top".partition("."))
# rpartition(sep) ：从右向左切割
print("www.njier.top".rpartition("."))

# split
print("www.njier.top".split("."))
print("www.njier.top".rsplit("."))
# 第二个参数指定分割的次数
print("www.njier.top".split(".", 1))  # 只分割一次
print("www.njier.top".rsplit(".", 1))  # 只分割一次，从右往左

print("www\nnjier\ntop".split("\n"))
print("www\nnjier\rtop".split("\n"))  # 但不同系统的换行符不一样

# 使用splitline方法
print("www\nnjier\ntop".splitlines())
print("www\nnjier\rtop".splitlines())
print("www\nnjier\rtop".splitlines())
print("www\nnjier\rtop".splitlines(True))  # 设置为True表示结果包含换行符


# 拼接：join
print(".".join(["www", "njier", "top"]))  # 将要拼接的字符串用列表包含起来
