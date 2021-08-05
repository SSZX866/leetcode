# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 16:57
# @File    : 96. 不同的二叉搜索树
from leetcode import *
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]