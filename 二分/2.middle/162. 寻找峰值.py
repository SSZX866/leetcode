# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 10:12
# @File    : 162. 寻找峰值.py
from leetcode import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-(1 << 32) - 1] + nums + [-(1 << 32) - 1]
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i - 1
        return -1


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # 峰值在右侧
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
