# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 17:50
# @File    : 35. 搜索插入位置
from leetcode import *
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo