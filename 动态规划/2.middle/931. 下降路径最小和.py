# -*- coding: utf-8 -*-
# @Time    : 2021/08/07 16:02
# @File    : 931. 下降路径最小和
from leetcode import *


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp1 = matrix[0]
        for i in range(1, len(matrix)):
            dp2 = [0] * len(dp1)
            dp2[0] = matrix[i][0] + min(dp1[0], dp1[1])
            for j in range(1, len(matrix) - 1):
                dp2[j] = matrix[i][j] + min(dp1[j - 1], dp1[j], dp1[j + 1])
            dp2[-1] = matrix[i][-1] + min(dp1[-1], dp1[-2])
            dp1 = dp2
        return min(dp1)
