# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 17:13
# @File    : 343. 整数拆分.py
from leetcode import *


#  dp[i] 表示 i 的组合最大乘积
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[-1]
