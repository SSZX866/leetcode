# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 12:32
# @File    : 125. 验证回文串.py
from leetcode import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tmp = ''
        for c in s:
            if c.isdigit() or 'a' <= c <= 'z': tmp += c
        return tmp[:len(tmp) // 2] == tmp[-1:-(len(tmp) // 2) - 1:-1]
