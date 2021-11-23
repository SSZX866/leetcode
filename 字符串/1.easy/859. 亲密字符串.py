# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 09:23
# @File    : 859. 亲密字符串.py
from leetcode import *


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        j = -1
        for i in range(len(s)):
            if s[i] == goal[i]:
                continue
            if j == -1:
                j = i
            else:
                if j == -2: return False
                if goal[j] != s[i] or goal[i] != s[j]:
                    return False
                j = -2
        if j == -1:
            counter = collections.Counter(s)
            return any(counter[k] > 1 for k in counter)
        return j == -2
