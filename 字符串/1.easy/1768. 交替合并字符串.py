# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 16:41
# @File    : 1768. 交替合并字符串.py
from leetcode import *


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]
            ans += word2[i]
        ans += word2[i + 1:] if len(word1) < len(word2) else word1[i + 1:]
        return ans
