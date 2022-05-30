# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 10:18
# @File    : 453. 最小操作次数使数组元素相等.py
from leetcode import *


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        M = min(nums)
        # return sum(nums[i] - M for i in range(len(nums)))
        return sum(nums) - len(nums) * min(nums)
