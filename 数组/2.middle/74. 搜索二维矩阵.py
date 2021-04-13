# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 9:18
# @File    : 74. 搜索二维矩阵.py
from typing import List
import math


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in sum([x for x in matrix],[])


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 7
    print(Solution().searchMatrix(matrix, target))
