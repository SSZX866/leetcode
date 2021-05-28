# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 21:04
# @File    : 1785. 构成特定和需要添加的最少元素.py
from leetcode import *


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return math.ceil(abs(goal - sum(nums)) / limit)
