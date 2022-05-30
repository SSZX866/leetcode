# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 10:03
# @File    : 844. 比较含退格的字符串.py
from leetcode import *


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, t1 = '', ''
        for c in s:
            s1 = s1 + c if c != '#' else s1[:-1]
        for c in t:
            t1 = t1 + c if c != '#' else t1[:-1]
        return s1 == t1
