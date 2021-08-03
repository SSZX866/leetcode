# -*- coding: utf-8 -*-
# @Time    : 2021/08/03 10:46
# @File    : 581. 最短无序连续子数组
from leetcode import *


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        tmp = sorted(nums)
        while i < len(nums) and tmp[i] == nums[i]: i += 1
        while j >= 0 and tmp[j] == nums[j]: j -= 1
        return j - i + 1 if i <= j else 0
