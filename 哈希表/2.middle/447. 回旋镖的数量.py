# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 10:47
# @File    : 447. 回旋镖的数量.py
from leetcode import *


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            dic = defaultdict(int)
            for x2, y2 in points:
                if x1 == x2 and y1 == y2: continue
                distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
                ans += dic[distance]
                dic[distance] += 1
        return ans * 2
