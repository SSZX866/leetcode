# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 15:40
# @File    : 476. 数字的补数.py
from leetcode import *


class Solution:
    def findComplement(self, num: int) -> int:
        res = ''
        while num:
            res += str(int(not (num & 1)))
            num >>= 1
        ans = 0
        for b in reversed(res):
            ans |= int(b)
            ans <<= 1
        return ans >> 1


# 异或
class Solution:
    def findComplement(self, num: int) -> int:
        tmp = 0
        target = num
        while num:
            num >>= 1
            tmp <<= 1
            tmp |= 1
        return target ^ tmp
