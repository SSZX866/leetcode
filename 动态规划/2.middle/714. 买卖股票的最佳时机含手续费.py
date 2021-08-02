# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 16:31
# @File    : 714. 买卖股票的最佳时机含手续费
from leetcode import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in prices]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return dp[-1][1]
