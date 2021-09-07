# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 10:37
# @File    : 56. 合并区间.py
from leetcode import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        pre = -1
        ans = []
        for start, end in intervals:
            if pre == -1:
                pre = end
                ans.append([start])
            elif pre >= start:
                pre = max(pre, end)
            else:
                ans[-1].append(pre)
                ans.append([start])
                pre = end
        if pre != -1: ans[-1].append(pre)
        return ans
