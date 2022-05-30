# -*- coding: utf-8 -*-
# @Time    : 2021/12/24 10:55
# @File    : 1705. 吃苹果的最大数目.py
from leetcode import *


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap, ans, n = [], 0, len(apples)
        for i in range(n):
            if apples[i]:
                heapq.heappush(heap, (days[i] + i, apples[i]))
            while heap and heap[0][0] < i + 1:
                heapq.heappop(heap)
            if heap:
                day, cnt = heapq.heappop(heap)
                if cnt != 1:
                    heapq.heappush(heap, (day, cnt - 1))
                ans += 1
        cur = n
        while heap:
            day, cnt = heapq.heappop(heap)
            ans += min(day - cur, cnt)
            cur += min(day - cur, cnt)
            while heap and heap[0][0] < cur:
                heapq.heappop(heap)
        return ans
