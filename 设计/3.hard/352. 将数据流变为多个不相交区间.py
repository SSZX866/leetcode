# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 09:41
# @File    : 352. 将数据流变为多个不相交区间.py
from leetcode import *


class SummaryRanges:

    def __init__(self):
        self.nums = []
        self.set = set()

    def addNum(self, val: int) -> None:
        if val in self.set: return
        self.set.add(val)
        index = bisect.bisect(self.nums, val)
        self.nums = self.nums[:index] + [val] + self.nums[index:]

    def getIntervals(self) -> List[List[int]]:
        res = []
        for num in self.nums:
            if not res or res[-1][-1] != num - 1:
                res.append([num, num])
            else:
                res[-1][-1] = num
        return res
