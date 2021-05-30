# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 22:39
# @File    : 5755. 数组中最大数对和的最小值.py
from leetcode import *


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for i in range(len(nums) // 2):
            ans.append(nums[i] + nums[-i - 1])
        return max(ans)
