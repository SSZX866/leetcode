# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 10:01
# @File    : 278. 第一个错误的版本.py
from leetcode import *


def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
