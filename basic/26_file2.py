# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/5 17:46
# @File:26_file2.py
# @Software:PyCharm

"""pathlib"""

from pathlib import Path

# cwd获取当前工作目录
print(Path.cwd())

p = Path('E:/programming/python/code/python基础语法/basic')
print(p)

q = p / "filetest1.txt"

print(q)

print(p.is_dir())
print(q.is_dir())

print(p.exists())
print(q.exists())

# 使用name属性获取最后路径的最后一部分

print(q.name)

# 获取文件名 stem
print(p.stem)

print(p.suffix)  # 获取文件的后缀
print(q.suffix)

# 获取父亲目录
print(q.parent)

