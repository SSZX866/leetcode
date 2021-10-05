# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 10:17
# @File    : 223. 矩形面积.py
from leetcode import *


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        ds = 0
        # 检测碰撞 在某一维度上固定一个矩形的左边界判断该边界是否在另一个矩形中的边界内
        # 836矩形重叠
        if (ax1 <= bx1 < ax2 or bx1 <= ax1 < bx2) and (ay1 <= by1 < ay2 or by1 <= ay1 < by2):
            dx = min(ax2, bx2) - max(ax1, bx1)
            dy = min(ay2, by2) - max(ay1, by1)
            ds = dx * dy
        return s - ds


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        dx = max(0, min(ax2, bx2) - max(ax1, bx1))
        dy = max(0, min(ay2, by2) - max(ay1, by1))
        return s - dx * dy
