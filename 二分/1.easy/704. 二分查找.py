# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 23:13
# @File    : 704. 二分查找.py
from leetcode import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid
            else:
                return mid
        return lo if target == nums[lo] else - 1


if __name__ == '__main__':
    nums, target = [-1, 0, 3, 5, 9, 12], 9
    nums, target = [-1, 0, 3, 5, 9, 12], 2
    print(Solution().search(nums, target))
