# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:59
# @File    : 5782. 最大子序列交替和.py
from leetcode import *


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0]*2 for _ in range(N)]
        dp[0][0]=0
        dp[0][1]=nums[0]
        for i in range(1,N):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = max(dp[i-1][0]+nums[i],dp[i-1][1]-nums[i])