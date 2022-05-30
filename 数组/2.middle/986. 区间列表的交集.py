# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 10:13
# @File    : 986. 区间列表的交集.py
from leetcode import *


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        n, m = len(A), len(B)
        i, j = 0, 0
        while i < n and j < m:
            left = max(A[i][0], B[j][0])
            right = min(A[i][1], B[j][1])
            # 判断是否有交集的条件
            if left <= right:
                res.append([left, right])
            # 哪个右区间元素较小，指针就向前移动一位
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res
