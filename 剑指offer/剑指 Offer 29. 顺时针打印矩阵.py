# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 13:11
# @File    : 剑指 Offer 29. 顺时针打印矩阵.py
from leetcode import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        if len(matrix) == 1: return matrix[0]
        if len(matrix[0]) == 1: return list(list(zip(*matrix))[0])
        m, n = len(matrix), len(matrix[0])
        ans = []
        a, b = m, n
        i = 0
        while a > 0 and b > 0:
            x, y = i, i
            for _ in range(b - 1):
                ans.append(matrix[x][y])
                y += 1
            for _ in range(a - 1):
                ans.append(matrix[x][y])
                x += 1
            for _ in range(b - 1):
                ans.append(matrix[x][y])
                y -= 1
            for _ in range(a - 1):
                ans.append(matrix[x][y])
                x -= 1
            i += 1
            a -= 2
            b -= 2
        if m % 2 and n % 2:
            ans.append(matrix[m // 2][n // 2])
        return ans


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])
        ans = []
        i = 0
        x, y = 0, -1

        def checkMN(m, n, x, y):
            if m == 0 or n == 0:
                if m == 0 and n == 0:
                    ans.append(matrix[x][y])
                elif m == 0:
                    while n != -1:
                        ans.append(matrix[x][y])
                        y += 1
                        n -= 1
                else:
                    while m != -1:
                        ans.append(matrix[x][y])
                        x += 1
                        m -= 1
                return True
            return False

        while len(ans) != M * N:
            m, n = M - 2 * i - 1, N - 2 * i - 1
            y += 1
            if checkMN(m, n, x, y): break
            for _ in range(n):
                ans.append(matrix[x][y])
                y += 1
            for _ in range(m):
                ans.append(matrix[x][y])
                x += 1
            for _ in range(n):
                ans.append(matrix[x][y])
                y -= 1
            for _ in range(m):
                ans.append(matrix[x][y])
                x -= 1
            x += 1
            i += 1
        return ans


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])
        ans = []
        left, right, top, bottom = 0, N - 1, 0, M - 1
        while left < right and top < bottom:
            for i in range(left, right): ans.append(matrix[top][i])
            for i in range(top, bottom): ans.append(matrix[i][right])
            for i in range(right, left, -1): ans.append(matrix[bottom][i])
            for i in range(bottom, top, -1): ans.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        if left == right:
            for i in range(top, bottom + 1): ans.append(matrix[i][left])
        elif bottom == top:
            for i in range(left, right + 1): ans.append(matrix[top][i])
        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
