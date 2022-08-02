# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/1 10:47
# @File:14_string4_format.py
# @Software:PyCharm

"""格式化字符串"""

year = 2021
month = 1
print("现在是 year 年 month 月")
# 格式化
print("现在是 {} 年 {} 月".format(year, month))

print("{} 爱 {}".format("我", "你"))
print("{1} 爱 {0}".format("我", "你"))  # 指定索引值，参数中的字符串被当成元组来对待
print("{1} 爱 {0}，{0} 爱 {1}".format("我", "你"))  # 多次引用

print("我是{name}，今年{age}岁。".format(name="彭鑫杰", age=19))

# 显示花括号
print("{},{{}},{}".format(1, 2))  # 嵌套花括号
print("{},{},{}".format(1, {}, 2))  # 花括号注释花括号


print("{:^10}".format(20))  # 总共10个位置，20这个数字居中对齐
print("{:<10}".format(20))  # 左对齐
print("{:>10}".format(20))  # 右对齐
print("{1:>10}{0:<10}".format("aa", "bb"))

print("{:010}".format(520))  # 填充0
print("{:010}".format(-520))  # 填充0，感知正负号

# 显示正负号
print("{:+},{:-}".format(1, -1))

# 分隔数字
print("{:,}".format(1234567))  # ，分隔


# 小数取几位
print("{:.3f}".format(23.34345))  # f：小数点后几位
print("{:.3g}".format(23.34345))  # g：小数点前后几位（总位数）

print("{:.5}".format("helloworld"))  # .n：截取字符串

# 进制
print("{:b}".format(10))  # 10以二进制1010输出
print("{:#b}".format(10))  # 10以二进制0b1010输出，加了ob前缀
print("{:x}".format(10))  # 10以十六进制a输出
print("{:o}".format(10))  # 10以八进制进制12输出
print("{:#x}".format(10))  # 10以十六进制0xa输出，加了0x前缀

# 以unicode字符输出
print("{:c}".format(80))

# 以科学计数法输出
print("{:e}".format(123.456789))  # 默认精度6

print("{:f}".format(123.456789))  # 默认精度6

# 百分比输出
print("{:.2%}".format(0.923))
print("{:.{prec}%}".format(0.923, prec=1))  # 通过参数设置


# f-string
age = 19
print(f"我今年{age}岁了。")
print(f"{-50:010}")
print(f"{1234567:,}")
print(f"{31.415:.2f}")