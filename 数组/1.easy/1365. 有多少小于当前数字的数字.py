# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 14:42
# @File    : 1365. 有多少小于当前数字的数字.py
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            cnt = 0
            for n in nums:
                if n < num: cnt += 1
            result.append(cnt)
        return result
