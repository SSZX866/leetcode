# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 21:31
# @File    : 1572. 矩阵对角线元素的和.py
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]: return 0
        res, length = 0, len(mat)
        for i in range(length):
            res += mat[i][i] + mat[i][length - i - 1]
        if length % 2: res -= mat[length // 2][length // 2]
        return res


if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print(Solution().diagonalSum(mat))
