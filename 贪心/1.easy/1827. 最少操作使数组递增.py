# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 22:30
# @File    : 5717. 最少操作使数组递增.py
from leetcode import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans, i = 0, 0
        if len(nums) <= 1: return 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                tmp = nums[i]
                nums[i] = nums[i - 1] + 1
                ans += nums[i] - tmp
        return ans
