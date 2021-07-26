# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 17:58
# @File    : 509. 斐波那契数
from leetcode import *


# dp
class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


# 记忆化搜索
class Solution:
    def fib(self, n: int) -> int:
        dp = [None] * (n + 1)
        dp[0:2] = [0, 1]
        return self.search(n, dp)

    def search(self, n, dp):
        if dp[n] is None:
            dp[n] = self.search(n - 1, dp) + self.search(n - 2, dp)
        return dp[n]

