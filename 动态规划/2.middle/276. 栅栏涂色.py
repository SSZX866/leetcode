# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:40
# @File    : 276. 栅栏涂色.py
from leetcode import *


# Error
class Solution:
    def numWays(self, n: int, k: int) -> int:
        p = q = 0  # p连续涂两个，q没有连续涂两个
        for i in range(1, n):
            tmpP, tmpQ = p, q
            p = tmpQ + 1
            q = tmpP + k - 1 + tmpQ + k - 1
        return p + q


class Solution:
    def numWays(self, n: int, k: int) -> int:
        p = 0
        q = k  # p连续涂两个，q没有连续涂两个，q初始应该有k种选择
        for i in range(1, n):
            tmpP, tmpQ = p, q
            p = tmpQ # 方案数相同
            q = tmpP * (k - 1) + tmpQ * (k - 1)  # 方案数应该相乘，乘法原理
        return p + q
