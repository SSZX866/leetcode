# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 11:23
# @File    : 416. 分割等和子集.py
from leetcode import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dfs(l, r, i, remain):
            if i == n:
                return l == r
            # 剪枝
            if l > r and r + remain < l: return False
            if l < r and l + remain < r: return False
            return dfs(l + nums[i], r, i + 1, remain - nums[i]) or dfs(l, r + nums[i], i + 1, remain - nums[i])

        return dfs(0, 0, 0, sum(nums))
