# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 13:58
# @File    : 48. 旋转图像.py
from leetcode import *


# 情况一：顺时针转 90 度：先转置再左右镜像
# 情况二：顺时针转 180 度:先上下镜像，再左右镜像（先左右再上下也可）
# 情况三：顺时针转 270 度：先转置再上下镜像


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [each[::-1] for each in zip(*matrix)]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 左右镜像
        left, right = 0, n - 1
        while left < right:
            for i in range(n):
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)
