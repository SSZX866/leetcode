# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 22:35
# @File    : 5718. 统计一个圆中点的数目.py
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for querie in queries:
            ans.append(0)
            for point in points:
                if pow((point[0] - querie[0]), 2) + pow((point[1] - querie[1]), 2) <= querie[2] * querie[2]:
                    ans[-1] += 1
        return ans