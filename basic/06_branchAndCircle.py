# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 11:22
# @File:06_branchAndCircle.py
# @Software:PyCharm

# if
# score = input("请输入分数：")
# score = int(score)
#
# if 0 < score < 60:
#     print("不及格")
# elif 60 <= score < 80:
#     print("及格")
# elif 80 <= score <= 100:
#     print("良好")
# else:
#     print("错误的分数")

a = 14
b = 12

small = a if a < b else b

print(small)

# continue语句
num = 10
while num > 0:
    if num % 2 == 0:
        num -= 1
        continue
    else:
        print(num)
    num -= 1

print('\n')

# while+else语句
num = 1
while num < 5:
    print(num)
    if num == 2:
        break
    num += 1
else:  # 只在while循环条件不在满足时执行
    print(num)

# 打印九九乘法表
i = 1
j = 1
while i <= 9:
    while j <= 9:
        print("%d * %d = %d" % (i, j, i * j), end='\t')
        j += 1
    i += 1
    j = i
    print()

print()

# 迭代
for a in "pengxinjie":
    print(a, end=' ')

print()
i = 0
while i < len("pengxinjie"):
    print("pengxinjie"[i], end='-')
    i += 1

print()
print()

# range
for i in range(10):  # 从0到10的整数序列，但不包含10
    print(i)

for i in range(10, 20):  # 从10到20，左闭右开的区间
    print(i, end=' ')
print()

for i in range(10, 20, 2):  # 跨度为2
    print(i, end=' ')
print("\n\n")

# 找出10以内的素数
for i in range(2, 11):
    for j in range(2, i):
        if i % j == 0:
            # print("%d不是质数!" % i)
            print(i, "不是质数,", i, "=", j, "*", i // j)
            break
    else:
        print("%d是质数" % i)
