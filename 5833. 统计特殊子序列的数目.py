# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 11:58
# @File    : 5833. 统计特殊子序列的数目.py
from leetcode import *
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in nums]
        dp[0][nums[0]] = 1
        ans = 0
        for i in range(1, len(nums)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
            dp[i][2] = dp[i - 1][2]
            dp[i][nums[i]] += 1
            if nums[i - 1] == 2 and nums[i] != 2:
                ans += dp[i - 1][0] * dp[i - 1][1] * dp[i - 1][2]
        if nums[-1] == 2:
            ans += dp[-1][0] * dp[-1][1] * dp[-1][2]
        print(dp)
        return ans % 1000000009