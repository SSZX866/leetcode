# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 11:28
# @File    : 1816. 截断句子.py
from leetcode import *
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(' ')[:k])