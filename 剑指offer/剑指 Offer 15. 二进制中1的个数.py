# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 10:13
# @File    : 剑指 Offer 15. 二进制中1的个数.py
from leetcode import *


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
