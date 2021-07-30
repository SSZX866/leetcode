# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 09:52
# @File    : 73. 矩阵置零.py

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            index = []
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        index.append((i, j))
            for each in index:
                matrix[each[0]] = [0] * n
            matrix[:] = list(map(list, zip(*matrix)))
            for each in index:
                matrix[each[1]] = [0] * m
            matrix[:] = list(map(list, zip(*matrix)))


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, column = [], []
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row.append(i)
                    column.append(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in column:
            for i in range(m):
                matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
