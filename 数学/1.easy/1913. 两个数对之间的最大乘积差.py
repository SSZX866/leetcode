# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 15:13
# @File    : 1913. 两个数对之间的最大乘积差.py
from leetcode import *
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2]-nums[0]*nums[1]