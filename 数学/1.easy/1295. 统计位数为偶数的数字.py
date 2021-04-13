# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 20:39
# @File    : 1295. 统计位数为偶数的数字.py
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1
        return res
