# -*- coding: utf-8 -*-
# @Time    : 2021/08/07 23:16
# @File    : 5828. K 次调整数组大小浪费的最小总空间
from leetcode import *
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        dp = [[0]*(k+1) for _ in nums]
        dp[0][-1] = nums
        for i in range(1, len(nums)):
            for j in range(k):
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]+nums[i]