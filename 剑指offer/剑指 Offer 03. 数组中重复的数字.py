# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 11:54
# @File    : 剑指 Offer 03. 数组中重复的数字.py
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                return num
