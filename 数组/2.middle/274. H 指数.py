# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 16:34
# @File    : 274. H 指数.py
from leetcode import *


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i in range(len(citations)):
            if citations[i] > ans:
                ans += 1
            else:
                return ans
        return ans
