# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 13:34
# @File    : 217. 存在重复元素.py
from leetcode import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
