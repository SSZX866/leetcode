# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 11:48
# @File    : 1860. 增长的内存泄露.py
from leetcode import *


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        cur = 1
        while memory1 >= cur or memory2 >= cur:
            if memory2 > memory1:
                memory2 -= cur
            else:
                memory1 -= cur
            cur += 1
        return [cur, memory1, memory2]