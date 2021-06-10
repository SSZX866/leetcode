# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 10:30
# @File    : 518. 零钱兑换 II.py
from leetcode import *


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                # 正序遍历，可以直接包含硬币多次使用的情况
                dp[i] += dp[i-coin]
        return dp[amount]
