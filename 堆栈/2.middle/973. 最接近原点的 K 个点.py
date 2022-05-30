# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 12:36
# @File    : 973. 最接近原点的 K 个点.py
from leetcode import *


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(heap, (distance, x, y))

        ans = []
        while k:
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
            k -= 1

        return ans
