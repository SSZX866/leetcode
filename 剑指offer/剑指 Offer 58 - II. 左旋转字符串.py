# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 22:40
# @File    : 剑指 Offer 58 - II. 左旋转字符串.py
from leetcode import *
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]