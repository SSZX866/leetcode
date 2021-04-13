# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 14:36
# @File    : 1313. 解压缩编码列表.py
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result += nums[i] * nums[i + 1]
        return result
