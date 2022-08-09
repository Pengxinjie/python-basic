# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/5 18:04
# @File:27_file3.py
# @Software:PyCharm

"""with 文件管理器"""
# with open("lengxuan.txt", "r+") as f:
#     f.write("hello world")
import pickle

"""pickle 二进制存储python"""

x, y = 1, 2
s = "hello world"
list1 = [1, 2, 3, "hello"]

with open("data.pkl", "wb") as f:
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(s, f)
    pickle.dump(list1, f)