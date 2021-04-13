# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 10:30
# @File    : 5726. 数组元素积的符号.py
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        cnt = 0
        for num in nums:
            if num < 0:
                cnt += 1
        return -1 if cnt % 2 else 1
