# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 16:22
# @File    : 剑指 Offer 40. 最小的k个数.py
from leetcode import *


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k: return []
        heap = []
        for num in arr:
            if k > 0:
                heapq.heappush(heap, (-num, num))
                k -= 1
            else:
                if num < heap[0][1]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-num, num))
        return [x[1] for x in heap]
