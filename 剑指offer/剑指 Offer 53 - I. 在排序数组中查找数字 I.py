# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 09:02
# @File    : 剑指 Offer 53 - I. 在排序数组中查找数字 I.py
from leetcode import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        ans = 0
        while lo < len(nums) and nums[lo] == target:
            lo += 1
            ans += 1
        return ans


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(lo, hi, lower):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if lower and nums[mid] < target:
                    lo = mid + 1
                elif not lower and nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return hi

        left = search(0, len(nums), True)
        if left < len(nums) and nums[left] == target:
            return search(0, len(nums), False) - 1 - left
        return 0
