# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 11:45
# @File    : 290. 单词规律.py
from leetcode import *


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = dict()
        helpSet = set()
        for i, each in enumerate(s.split()):
            if i >= len(pattern): return False
            if pattern[i] not in dic:
                if each in helpSet: return False
                dic[pattern[i]] = each
                helpSet.add(each)
            else:
                if dic[pattern[i]] != each:
                    return False
        return i == len(pattern) - 1
defaultdict