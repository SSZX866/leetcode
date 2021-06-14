# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 20:21
# @File    : 374. 猜数字大小.py
from leetcode import *


def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                hi = mid
            else:
                lo = mid + 1
