# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 12:01
# @File    : 451. 根据字符出现频率排序.py
from leetcode import *


class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        counter = Counter(s)
        for key in counter.keys():
            heapq.heappush(heap, (-counter[key], key))
        ans = ''
        while heap:
            k, v = heapq.heappop(heap)
            ans += -k * v
        return ans
