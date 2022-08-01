# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 8:56
# @File:01_game.py
# @Software:PyCharm

'''用python设计一个游戏'''
temp = input("不妨猜一下彭鑫杰现在心里想的是哪个数字：")
guess = int(temp)

if guess == 8:
    print("猜对了！")
else:
    print("猜错了")

print("游戏结束！")