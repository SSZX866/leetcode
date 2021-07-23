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


#  模拟
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        tmp = [0] * 52
        for start, end in ranges:
            for idx in range(start, end + 1):
                tmp[idx] += 1
        for each in tmp[left:right + 1]:
            if not each:
                return False
        return True


# 差分数组
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for start, end in ranges:
            diff[start] += 1
            diff[end + 1] -= 1
        for i in range(1, 52):
            diff[i] += diff[i - 1]
            if left <= i <= right and not diff[i]:
                return False
            if i > right:
                return True
