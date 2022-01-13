# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/1/12 14:56
# @File:conditionAndCircle.py
# @Software:PyCharm

# 条件语句
# if 1 == 1:
#     print('1==1为真')

# 小例子
# 判断是否成年
# age = int(input('请输入您的年龄:'))
# if age >= 18:
#     print('已成年，可以上网')
# else:
#     print('未成年人，回去写作业吧')

# 多重判断
# age = int(input('请输入您的年龄：'))
# if age <18:
#     print('未成年')
# elif 8 <= age < 60:
#     print('中年人')
# else:
#     print('老人')

# while循环
# a = 0
# while a < 5:
#     a += 1
#     print(a)

# 计算1-100的累加
# a = 1
# sum = 0
# while a <= 100:
#     sum += a
#     a += 1
# print(sum)

# 计算1-100的偶数加和
# a = 0
# sum = 0
# while a <= 100:
#     sum += a
#     a += 2
# print(sum)

# while循环打印九九乘法表
# a = 1
# while a < 10:
#     b = 1
#     while b <= a:
#         print(f'{b}*{a}={b*a}', end='\t')
#         b += 1
#     a += 1
#     print()

# for循环
str1 = 'neymar'
for i in str1:
    if i == 'a':
        # 不打印a
        continue
    print(i)

