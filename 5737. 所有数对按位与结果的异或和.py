# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 10:58
# @File    : 5737. 所有数对按位与结果的异或和.py
from leetcode import *


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        arr1.sort()