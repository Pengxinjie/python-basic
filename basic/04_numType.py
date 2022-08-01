# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/30 10:42
# @File:04_numType.py
# @Software:PyCharm
"""数字类型"""
import decimal

# 整数的长度是不受限制的，有无限大的精度
# 除法产生带小数的结果

print(12312 / 12412)
print(4 / 2)

print(0.1 + 0.2)  # 存在误差，谨慎比较浮点数
print(0.3 == 0.1 + 0.2)
print(0.3 == 0.3)
print('\n')

# 精确计算浮点数，导入decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
c = decimal.Decimal('0.3')
print(a + b == c)  # true

# 科学计数法
var1 = 0.00005
print(var1)
var1 = 5e-4
print(var1)
print('\n')

# 运算
print(5 // 2)  # 地板除  取比目标结果小的最大整数
print(-5 // 2)  # -3
print(5 % 2)  # 取余数
print(abs(-5))  # 绝对值
print(3 ** 4)  # 次方运算，3的四次方
print(pow(3, 4))  # 次方运算
