# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 10:16
# @File    : 852. 山脉数组的峰顶索引.py
from leetcode import *


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr)

        def check(index):
            return arr[index] - arr[index - 1] < 0

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
