# 打印一行hello world，这是单行注释
print('hello world')

'''
这是
多行注释
'''

"""
这也是
多行注释
"""

# 变量
a = 21
b = 'neymar'
c = 99.99
e = True
print(a)

# 格式化输出
print("我%d岁了" % a)
print("我叫%s,今年%d岁了,有%f元" % (b, a, c))
print(f'我叫{b},今年{a + 8}岁了', end='')  # 去掉自带的\n
print(f'我叫{b},今年{a + 8}岁了')

print('-----------------')

# 输入
username = input('请输入用户名：')
print(f'你的输入是{username}')

# 查看变量类型  默认为str
print(type(username))