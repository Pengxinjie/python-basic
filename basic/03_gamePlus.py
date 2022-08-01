# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 10:00
# @File:03_gamePlus.py
# @Software:PyCharm
import random

ans = random.randint(1, 100)  # 获取[0,100)的随机整数

counts = 10  # 有三次猜的机会
while counts > 0:
    print("请猜一个数字（剩余%d次机会）：" % counts, end='')
    temp = input()
    guess = int(temp)
    if ans == guess:
        print("猜对啦")
        break
    else:
        if guess > ans:
            print("大了")
        else:
            print("小了")
    counts -= 1

