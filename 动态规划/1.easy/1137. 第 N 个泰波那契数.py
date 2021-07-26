# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 18:17
# @File    : 1137. 第 N 个泰波那契数
from leetcode import *


# 动态规划
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp.append(dp[-1] + dp[-2] + dp[-3])
        return dp[n]


#  递归+记忆化搜索
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [None] * (n + 1)
        dp[:3] = [0, 1, 1]
        return self.search(dp, n)

    def search(self, dp, n):
        if dp[n] is None:
            dp[n] = self.search(dp, n - 1) + self.search(dp, n - 2) + self.search(dp, n - 3)
        return dp[n]
