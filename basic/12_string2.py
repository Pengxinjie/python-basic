# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/7/31 17:11
# @File:12_string2.py
# @Software:PyCharm

# 三、查找
s1 = "上海自来水来自海上"
# ①count(sub[,start[,end]]) ：查找子串出现次数
print(s1.count("上"))
print(s1.count("上", 0, 5))  # [0,5) 指定范围
print(s1.count("上海"))
# ②find(sub[,start[,end]]) : 查找子串的下标值
print(s1.find('自来水'))
print(s1.find('数'))  # 找不到返回-1
# ③rfind(sub[,start[,end]]) ：从右边开始找
print(s1.rfind("自"))
print(s1.rfind("数"))
# ④index(sub[,start[,end]])
print(s1.index("自来水"))
# print(s1.index("数"))  # 找不到，报错
# ⑤rindex(sub[,start[,end]])
print(s1.index("自来水"))


# expandtabs([tabsize=8]) : 将字符串中的tab转换成空格,参数指定一个tab等于多少个空格
# 不要混用tab和空格
code = """
    \tprint("hello")
    print("world")"""
print(code)
print(code.expandtabs(4))


# 替换
# replace(old, new, count=-1)  # 默认值-1，替换全部
s1 = "上海自来水来自海上"
print(s1.replace("海", "火"))
print(s1.replace("海", "火", 1))

# translate(table) ： 根据table参数转换后的字符串
# 获取表格
# str.maketrans(x[,y[,z]])
table = str.maketrans("abcd", "1234")
print("hello world ab".translate(table))

# 判断
s = "hello World"
# startwith(prefix[,start[,end]]) : [,start[,end]]->指定范围
print(s.startswith("he"))
print(s.startswith("e"))
if s.startswith(("saf", "fg", "he")):  # 只要匹配元组中的某一个元素就行
    print("匹配成功")

# endswith(suffix[,start[,end]])
print(s.endswith("ld"))
print(s.endswith("l"))
# isupper() : 所有的字母都是大写字母
print("AASFASD".isupper())
print("AASFASd".isupper())
print("safsFSAF".upper().isupper())  # 先转换后判断True
print("----------------")

# islower() : 所有字母都是小写
print("safasdfas".islower())
print("safasdfaD".islower())
# istitle() ：单词均以小写字母开头
print("I Love Python".istitle())
print("i love python".istitle())
# isalpha() ： 判断只有字母构成
print("sadfsafd".isalpha())
print("sadf safd".isalpha())  # 空格不是字母
print("sadfsafd234".isalpha())
# isascii()

# isspace()  ： 判断是否都是空格
print("  ".isspace())
print("  ss".isspace())
# isprintable() : 判断是否是可打印字符
print("hello world".isprintable())
print("hello world\n".isprintable())  # 转义字符\n不可打印
# isdecimal()
print("123".isdecimal())
print("0x12".isdecimal())
print("2²".isdecimal())
# isdigit()
print("2²".isdigit())  # True
# isnumeric()
print("2²".isnumeric())  # True
# isalnum()
# isidentifier()  # 判断是否是一个合法的python标志符
print("123saf".isidentifier())
print("hello world".isidentifier())  # 存在空格
print("hello_world".isidentifier())

# 判断是否是python的保留标志符
import keyword
print(keyword.iskeyword("if"))
print(keyword.iskeyword("ifs"))