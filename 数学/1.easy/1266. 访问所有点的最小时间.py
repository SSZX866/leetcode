# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 20:27
# @File    : 1266. 访问所有点的最小时间.py
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        result = 0
        for i in range(1, len(points)):
            result += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
        return result