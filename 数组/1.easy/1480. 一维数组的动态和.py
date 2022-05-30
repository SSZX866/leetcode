# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 15:13
# @File    : 1480. 一维数组的动态和.py
from leetcode import *


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        for num in nums[1:]:
            pre.append(pre[-1] + num)
        return pre
