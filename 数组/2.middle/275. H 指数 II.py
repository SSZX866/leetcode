# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 12:42
# @File    : 275. H 指数 II.py
from leetcode import *


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo, hi = 0, len(citations)

        def check(target):
            if citations[len(citations) - 1 - target] > target:
                return True
            return False

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
