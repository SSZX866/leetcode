# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 9:58
# @File    : 59. 螺旋矩阵 II.py
from typing import List
import math


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        boundary = [[0, 0], [n - 1, n - 1]]
        face = 1  # 0,1,2,3 分别代表北东南西
        k = 0
        i, j = 0, 0
        for _ in range(n * n):
            k += 1
            # 更新face
            if i > boundary[1][0] or j > boundary[1][1] or i < boundary[0][0] or j < boundary[0][1]:
                # print(i,j,boundary)
                face = (face + 1) % 4
                # 更新boundary, 纠正i,j
                if face == 0:
                    boundary[1][0] -= 1
                    j += 1
                    i -= 1
                elif face == 1:
                    boundary[0][1] += 1
                    i += 1
                    j += 1
                elif face == 2:
                    boundary[0][0] += 1
                    j -= 1
                    i += 1
                else:
                    boundary[1][1] -= 1
                    i -= 1
                    j -= 1
            # print(i, j, face, result,boundary)
            matrix[i][j] = k
            # 更新i, j
            if face == 0:
                i -= 1
            elif face == 1:
                j += 1
            elif face == 2:
                i += 1
            else:
                j -= 1

        return matrix


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        cur = 1
        for i in range(math.ceil(n / 2)):
            x, y = i, i
            if i == n - i - 1:
                matrix[x][y] = cur
                break
                matrix[x][y] = cur
                y += 1
                cur += 1
            for _ in range(i, n - i - 1):
                matrix[x][y] = cur
                x += 1
                cur += 1
            for _ in range(i, n - i - 1):
                matrix[x][y] = cur
                y -= 1
                cur += 1
            for _ in range(i, n - i - 1):
                matrix[x][y] = cur
                x -= 1
                cur += 1
        return matrix


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
