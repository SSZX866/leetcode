# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 20:27
# @File    : LCP 06. 拿硬币.py
from leetcode import *


class Solution:
    def minCount(self, coins: List[int]) -> int:
        # return sum([(x >> 1) + 1 if x % 2 else x >> 1 for x in coins])
        return sum((x + 1) >> 1 for x in coins)
