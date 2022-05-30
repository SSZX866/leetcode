# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 13:38
# @File    : 2091. 从数组中移除最大值和最小值.py
from leetcode import *


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx, maxIdx = 0, 0
        n = len(nums)
        for i in range(n):
            minIdx = min(i, minIdx, key=lambda x: nums[x])
            maxIdx = max(i, maxIdx, key=lambda x: nums[x])
        left, right = min(minIdx, maxIdx), max(minIdx, maxIdx)
        once = min(right + 1, n - left)
        left_right = left + 1 + n - right
        return min(once, left_right)


# 使用index(max)比手动遍历快很多
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx, maxIdx = nums.index(min(nums)), nums.index(max(nums))
        n = len(nums)
        left, right = min(minIdx, maxIdx), max(minIdx, maxIdx)
        once = min(right + 1, n - left)
        left_right = left + 1 + n - right
        return min(once, left_right)


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        left, right = min(minIdx := nums.index(min(nums)), maxIdx := nums.index(max(nums))), max(minIdx, maxIdx)
        return min(left + 1 + len(nums) - right, min(right + 1, len(nums) - left))
