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


#  时间序列dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in nums]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][1] = dp[i - 1][0] + nums[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        return max(dp[-1][0], dp[-1][1])
