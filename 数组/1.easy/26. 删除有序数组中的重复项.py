# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 18:49
# @File    : 26. 删除有序数组中的重复项.py
from leetcode import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans, i, j, n = 1, 0, 1, len(nums)
        if n < 2: return n
        while j < n:
            while j < n and nums[j] == nums[i]:
                j += 1
            if j >= n: return ans
            i += 1
            ans += 1
            nums[i] = nums[j]
        return ans
