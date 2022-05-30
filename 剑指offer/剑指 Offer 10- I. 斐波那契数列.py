# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 19:00
# @File    : 剑指 Offer 10- I. 斐波那契数列.py
from leetcode import *


class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        return dp[n]
