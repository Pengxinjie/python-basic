# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/5 18:15
# @File:28_file4.py
# @Software:PyCharm

"""read pkl"""

import pickle
# with open("data.pkl", "rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)
#     s = pickle.load(f)
#     list1 = pickle.load(f)

with open("data.pkl", "rb") as f:
    x = pickle.load(f)
    y = pickle.load(f)
    s = pickle.load(f)
    list1 = pickle.load(f)

print(x)
print(y)
print(s)
print(list1)