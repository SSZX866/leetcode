# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 10:18
# @File    : 304. 二维区域和检索 - 矩阵不可变.py

# dp[i][j]
# 表示从0，0
# 到i，j的数量和
# dp[0][0] = matrix[0][0]
# dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j], i > 0, j > 0
# dp[i][j] = dp[i][j - 1] + matrix[0][j], j > 0, i = 0
# dp[i][j] = dp[i - 1][0] + matrix[i][0], i > 0, j = 0

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * len(matrix[0]) for _ in matrix]
        if len(matrix) == 0 or len(matrix[0]) == 0:
            self.dp[0][0] = 0
        else:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i == 0 and j == 0:
                        self.dp[0][0] = matrix[0][0]
                    elif i == 0:
                        self.dp[i][j] = self.dp[i][j - 1] + matrix[0][j]
                    elif j == 0:
                        self.dp[i][j] = self.dp[i - 1][0] + matrix[i][0]
                    else:
                        self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + matrix[i][j]
        # print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1 - 1]
        elif col1 == 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 - 1] + self.dp[row1 - 1][col1 - 1]


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    num = NumMatrix(matrix)
    print(num.sumRegion(2, 1, 4, 3), num.sumRegion(1, 1, 2, 2), num.sumRegion(1, 2, 2, 4))
