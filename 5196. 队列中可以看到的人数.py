# -*- coding: utf-8 -*-
# @Time    : 2021/07/24 23:37
# @File    : 5196. 队列中可以看到的人数
from leetcode import *


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        dp = [1] * len(heights)
        dp[-1] = 0
        for i in range(len(heights) - 2, -1, -1):
            if heights[i + 1] > heights[i]:
                continue
            tmp = heights[i]
            j = i + 1
            while j < len(heights) and heights[j] < tmp:
                j += 1
            dp[i] = j - i + dp[j] if j < len(heights) else j - i
        return dp
