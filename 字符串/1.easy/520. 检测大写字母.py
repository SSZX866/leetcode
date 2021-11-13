# -*- coding: utf-8 -*-
# @Time:    2021/11/13 11:43
# @File:    520. 检测大写字母.py
from leetcode import *


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        mark = False if 'a' <= word[0] <= 'z' else True
        for i in range(1, len(word)):
            if mark and 'a' <= word[i] <= 'z':
                if i != 1:
                    return False
                mark = False
            elif not mark and 'A' <= word[i] <= 'Z':
                return False
        return True
