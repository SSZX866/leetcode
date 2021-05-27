# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 20:32
# @File    : 1798. 你能构造出连续值的最大数目.py
from leetcode import *


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans = 0
        for x in coins:
            if x > ans + 1: break
            ans += x
        return ans
