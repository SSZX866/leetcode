# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 11:52
# @File    : 53. 最大子序和.py
from leetcode import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
