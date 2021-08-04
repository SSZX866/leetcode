# -*- coding: utf-8 -*-
# @Time    : 2021/08/04 11:19
# @File    : 413. 等差数列划分
from leetcode import *


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        ans, cur = 0, 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cur = cur + 1
                ans += cur
            else:
                cur = 0
        return ans
