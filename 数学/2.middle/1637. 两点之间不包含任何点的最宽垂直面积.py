# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 20:44
# @File    : 1637. 两点之间不包含任何点的最宽垂直面积.py
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        if not points: return 0
        points = list(set(x[0] for x in points))
        if len(points) == 1: return points[0]
        points.sort()
        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i] - points[i - 1])
        return res


if __name__ == '__main__':
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print(Solution().maxWidthOfVerticalArea(points))
