# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 20:09
# @File    : 149. 直线上最多的点数.py
from leetcode import *


# 确定一个基点base，扫描所有点，斜率相同的为同一直线的点
# 循环处理所有点为基点，最大值即所求
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i in range(len(points)):
            base_x, base_y = points[i][0], points[i][1]
            slopes = defaultdict(int)
            for point_x, points_y in points:
                if [point_x, points_y] == points[i]:
                    continue
                if point_x != base_x:
                    slope = (points_y - base_y) / (point_x - base_x)
                else:
                    slope = 'none'
                slopes[slope] += 1
            ans = max(max(slopes.values(), default=0) + 1, ans)
        return ans
