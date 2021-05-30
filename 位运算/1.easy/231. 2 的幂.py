# -*- coding: utf-8 -*-
# @Time    : 2021/5/30 10:25
# @File    : 231. 2 的幂.py
from leetcode import *


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n: return False
        flag = False
        while n:
            if flag: return False
            if n & 1: flag = True
            n >>= 1
        return True
