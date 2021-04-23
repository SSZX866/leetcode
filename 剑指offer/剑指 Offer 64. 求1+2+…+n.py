# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 22:15
# @File    : 剑指 Offer 64. 求1+2+…+n.py
from leetcode import *


class Solution:
    def sumNums(self, n: int) -> int:
        return n and self.sumNums(n - 1) + n
