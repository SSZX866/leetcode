# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 13:52
# @File    : 剑指 Offer 61. 扑克牌中的顺子.py
from leetcode import *


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
                continue
            if i > 0 and nums[i - 1] != 0 and nums[i] - nums[i - 1] != 1:
                cnt -= nums[i] - nums[i - 1] - 1
                if cnt < 0 or nums[i] == nums[i - 1]: return False
        return True
