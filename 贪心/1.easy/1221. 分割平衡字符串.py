# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 10:11
# @File    : 1221. 分割平衡字符串.py
from leetcode import *


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L, R, ans = 0, 0, 0
        for c in s:
            if c == 'L':
                L += 1
            elif c == 'R':
                R += 1
            if L and L == R:
                ans += 1
                L, R = 0, 0
        return ans


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans, balance = 0, 0
        for c in s:
            balance += 1 if c == 'R' else -1
            if not balance: ans += 1
        return ans
