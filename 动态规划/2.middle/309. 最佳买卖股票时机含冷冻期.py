# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 22:11
# @File    : 309. 最佳买卖股票时机含冷冻期.py
from leetcode import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in prices]
        dp[0][0] = -prices[0]
        dp[0][1] = -9999999
        dp[0][2] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[-1])
