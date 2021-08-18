# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 9:18
# @File    : 74. 搜索二维矩阵.py
from typing import List
import math


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in sum([x for x in matrix], [])


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][-1] < target:
                lo = mid + 1
            elif matrix[mid][-1] == target:
                return True
            else:
                hi = mid
        if lo == len(matrix): return False
        idx = lo
        lo, hi = 0, len(matrix[0])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[idx][mid] < target:
                lo = mid + 1
            elif matrix[idx][mid] == target:
                return True
            else:
                hi = mid
        return lo < len(matrix[0]) and matrix[idx][lo] == target


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 7
    print(Solution().searchMatrix(matrix, target))
