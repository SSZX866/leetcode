# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 12:38
# @File    : 面试题 17.14. 最小K个数.py
from leetcode import *


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for each in arr:
            if len(heap) < k:
                heapq.heappush(heap, -each)
                continue
            heapq.heappushpop(heap, -each)
        return list(map(lambda x: -x, heap))
