# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 00:01
# @File    : 剑指 Offer 17. 打印从1到最大的n位数.py
from leetcode import *


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]
