# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 17:37
# @File    : 136. 只出现一次的数字.py
from leetcode import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
