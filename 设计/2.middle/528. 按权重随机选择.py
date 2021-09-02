# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 13:28
# @File    : 528. 按权重随机选择.py
from leetcode import *


class Solution:

    def __init__(self, w: List[int]):
        self.pre = [0]
        for each in w:
            self.pre.append(self.pre[-1] + each)

    def pickIndex(self) -> int:
        lo, hi = 1, len(self.pre)
        target = random.randint(1, self.pre[-1])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.pre[mid] > target > self.pre[mid - 1]:
                return mid - 1
            elif target > self.pre[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
