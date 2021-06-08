# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 21:19
# @File    : 123. 买卖股票的最佳时机 III.py
from leetcode import *


# 0持有一次 1售出一次 2持有两次 3售出两次
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 4 for _ in prices]
        # 初始化 持有1收益为-prices[0] 卖出1收益为 0
        # 持有2和卖出2不可操作，因此设为-9999999
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = dp[0][3] = -9999999
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])
        return max(dp[-1])
