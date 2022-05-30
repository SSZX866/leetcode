# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 09:50
# @File    : 剑指 Offer 10- II. 青蛙跳台阶问题.py
from leetcode import *


class Solution:
    def numWays(self, n: int) -> int:
        a, b, res = 1, 1, 1
        for i in range(2, n + 1):
            res = (a + b) % 1000000007
            a = b
            b = res
        return res
