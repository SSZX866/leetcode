# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 10:05
# @File    : 1790. 仅执行一次字符串交换能否使两个字符串相等.py
from leetcode import *


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if s1 == s2: return True
        tmp = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                tmp.append(i)
        if len(tmp) == 2:
            return True if s1[tmp[1]] == s2[tmp[0]] and s1[tmp[0]] == s2[tmp[1]] else False
        return False
