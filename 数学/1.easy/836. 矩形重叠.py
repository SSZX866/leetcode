# -*- coding: utf-8 -*-
# @Time    : 2021/07/23 19:18
# @File    : 836. 矩形重叠
from leetcode import *


# [-7,-3,10,5]
# [-6,-5,5,10]
# WA
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec2[0] and rec1[1] == rec2[1]: return True  # 左下角重合
        if rec1[2] == rec2[2] and rec2[3] == rec2[3]: return True  # 右上角重合

        def checkInner(x, y, rec):
            if rec[0] < x < rec[2] and rec[1] < y < rec[3]:
                return True
            return False

        def checkBoundary(rec1, rec2):
            if rec1[0] == rec2[0] and rec1[1] < rec2[1] < rec1[3]:  # 左边重合
                return rec2[2] >= rec1[2]
            elif rec1[2] == rec2[2] and rec1[1] < rec2[3] < rec1[3]:  # 右边重合
                return rec2[0] >= rec1[0]
            elif rec1[1] == rec2[1] and rec1[0] < rec2[0] < rec1[2]:  # 上边重合
                return rec2[3] >= rec1[3]
            elif rec1[3] == rec2[3] and rec1[0] < rec2[2] < rec1[2]:  # 下边重合
                return rec2[1] >= rec1[1]
            return False

        index = [(0, 1), (0, 3), (2, 1), (2, 3)]
        for x, y in index:
            if checkInner(rec1[x], rec1[y], rec2):
                return True
            if checkInner(rec2[x], rec2[y], rec1):
                return True
        if not checkBoundary(rec1, rec2) and not checkBoundary(rec2, rec1):
            return False
        return True


# 两个矩阵左下角分别小于另一个矩阵的右上角
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec2[0] < rec1[2] and rec2[1] < rec1[3]


# 投影 若两矩形相交，则其在x方向和y方向的投影必同时相交
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 判断线段x1,x2是否与x3,x4相交
        def check(x1, x2, x3, x4):
            if x3 <= x1 < x4 or x1 <= x3 < x2:
                return True
            return False

        x1, x2, x3, x4 = rec1[0], rec1[2], rec2[0], rec2[2]
        y1, y2, y3, y4 = rec1[1], rec1[3], rec2[1], rec2[3]
        if check(x1, x2, x3, x4) and check(y1, y2, y3, y4):
            return True
        return False
