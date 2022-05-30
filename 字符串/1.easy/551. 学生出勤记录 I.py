# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 10:12
# @File    : 551. 学生出勤记录 I.py
from leetcode import *


class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and 'LLL' not in s


class Solution:
    def checkRecord(self, s: str) -> bool:
        L, A = 0, 0
        for c in s:
            if c == 'L':
                L += 1
            else:
                L = 0
            if c == 'A':
                A += 1
            if L == 3 or A == 2:
                return False
        return True
