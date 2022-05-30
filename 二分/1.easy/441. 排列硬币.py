# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 16:40
# @File    : 441. 排列硬币.py
from leetcode import *


class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ((1 + mid) * mid) // 2 > n:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
