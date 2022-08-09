# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/5 17:10
# @File:25_file1.py
# @Software:PyCharm

"""文件"""

# f = open("lengxuan.txt", "w")
# f.write("pengxinjie\n")
# f.writelines(["neymar\n", "messi\n", "suarez\n"])
# print(f.writable())  # 可写
# f.close()
#
# r = open("lengxuan.txt", "r")
# print(r.readable())  # 可读
# print(r.read())
# r.close()
#
# # f = open("lengxuan.txt", "w")
# # f.write("xinjie")  # 把之前的覆盖了
#
# f = open("lengxuan.txt", "r+")  # 可读可写，续写
# print(f.readable())
# print(f.writable())
#
# f.write("newline\n")
# f.write("pengxinjie\n")
#
# print(f.tell())  # 查看文件指针的当前位置

# 修改文件指针的位置

f = open("lengxuan.txt", "r+")
print(f.read())
print(f.tell())
f.seek(0)  # 重置文件指针位置
print(f.readline())
print(f.tell())
print(f.read())

print(f.tell())

f.write("I love you!\n")
f.flush()