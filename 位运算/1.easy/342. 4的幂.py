# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 10:25
# @File    : 342. 4的幂.py
from leetcode import *


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ans = False
        if n <= 0: return ans
        flag = False
        while n:
            if flag:
                return False
            if n & 1:
                flag = not flag
            ans = not ans
            n >>= 1
        return ans
