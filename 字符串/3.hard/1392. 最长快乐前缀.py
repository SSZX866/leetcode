# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 09:37
# @File    : 1392. 最长快乐前缀.py
from leetcode import *


class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if s[:i] == s[len(s) - i:]:
                return s[:i]
        return ""
