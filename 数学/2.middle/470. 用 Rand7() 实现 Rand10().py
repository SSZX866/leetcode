# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 20:34
# @File    : 470. 用 Rand7() 实现 Rand10().py
from leetcode import *


def rand7():
    return random.randint(1, 7)


# 生成一个1-5的数，制造1/2的概率使其+5或不变
class Solution:
    def rand10(self):
        a = rand7()
        # 生成一个1-6的数使用奇偶 生成1/2概率
        # 随机数为7时拒绝采样，重新生成随机数 舍弃一个 期望6/7
        while a == 7:
            a = rand7()
        b = rand7()
        # 生成1-5的数 大于5时重新采样 舍弃 两个 期望 5/7
        while b > 5:
            b = rand7()
        # 总期望 11/7
        return b if a % 2 else b + 5
