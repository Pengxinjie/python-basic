# Author:peng_xinjie
# -*- coding = utf-8 -*-
# @Time:2022/8/5 20:09
# @File:normal_distribution.py
# @Software:PyCharm

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

# 第一组 正态分布随机变量，均值为0，标准差为1
norm_0 = norm(loc=0, scale=1)
# 第二组 正态分布随机变量，均值为1，标准差为2
norm_1 = norm(loc=1, scale=2)

# -10到10等距1000个点，x就是有1000个值的向量（数组）
x = np.linspace(-10, 10, 1000)

# 画变量的p点图
ax.plot(x, norm_0.pdf(x), color='red', lw=3, alpha=0.6, label='loc=0,scale=1')
ax.plot(x, norm_1.pdf(x), color='black', lw=3, alpha=0.6, label='loc=0,scale=1')

ax.legend(loc='best')
plt.grid(ls='--')
plt.show()