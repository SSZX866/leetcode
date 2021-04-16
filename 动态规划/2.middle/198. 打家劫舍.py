# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 11:31
# @File    : 198. 打家劫舍.py
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n == 1: return dp[0]
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        ans = dp[-1]
        return ans
