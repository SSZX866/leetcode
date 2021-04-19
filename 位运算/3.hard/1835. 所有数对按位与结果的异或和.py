# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 10:58
# @File    : 1835. 所有数对按位与结果的异或和.py
from leetcode import *


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        a, b = arr1[0], arr2[0]
        for i in range(1, len(arr1)):
            a ^= arr1[i]
        for i in range(1, len(arr2)):
            b ^= arr2[i]
        return a & b