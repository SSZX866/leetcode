# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 10:52
# @File    : 334. 递增的三元子序列.py
from leetcode import *


# trick 贪心
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = mid = 1 << 31
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False
