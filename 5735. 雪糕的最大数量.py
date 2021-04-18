# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 10:33
# @File    : 5735. 雪糕的最大数量.py
from leetcode import *


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans, coin = 0, 0
        for cost in costs:
            coin += cost
            if coin <= coins:
                ans += 1
        return ans
