# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 22:33
# @File    : 5767. 检查是否区域内所有整数都被覆盖.py
from leetcode import *


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            mark = False
            for each in ranges:
                if each[0] <= i <= each[1]:
                    mark = True
                    break
            if not mark: return False
        return True
