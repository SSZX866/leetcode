# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 16:02
# @File    : 1915. 最美子字符串的数目.py
from leetcode import *


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        pre = [0]
        for c in word:
