# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 19:49
# @File    : 1796. 字符串中第二大的数字.py
from leetcode import *


class Solution:
    def secondHighest(self, s: str) -> int:
        tmp = []
        for each in set(s):
            if each.isdigit():
                tmp.append(int(each))
        return sorted(tmp)[-2] if len(tmp) > 1 else -1
