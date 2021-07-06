# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 10:34
# @File    : 5798. 循环轮转矩阵.py
from leetcode import *


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[1])

        def generateList(matrix):
            res = []
            i = 0
            cnt = 0
            while cnt < m * n:
                cnt += (m + n - 2 - i * 2) * 2
                res.append([])
                while len(res[-1]) < (m + n - 2 - i * 2) * 2:
                    res[-1] += matrix.pop(0)
                    matrix = list(zip(*matrix))[::-1]
                i += 2

            return res

        def generateMatrix(target):
            matrix = [[0] * n for _ in range(m)]
            boundary = [[0, 0], [m - 1, n - 1]]
            face = 1  # 0,1,2,3 分别代表北东南西
            i, j = 0, 0
            for _ in range(m * n):
                if not target[-1]:
                    target.pop()
                k = target[-1].popleft()
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

        tmp = generateList(grid)
        Matrix = []
        for each in tmp:
            N = len(each)
            tmp2 = deque([0] * N)
            for i in range(N):
                tmp2[(i - k) % N] = each[i]
            Matrix.append(tmp2)
        return generateMatrix(Matrix[::-1])


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(min(m, n) // 2):
            x, y = i, i
            index = []
            for a in range(i, n - i - 1):
                index.append([x, y])
                y += 1
            for b in range(i, m - i - 1):
                index.append([x, y])
                x += 1
            for c in range(i, n - i - 1):
                index.append([x, y])
                y -= 1
            for d in range(i, m - i - 1):
                index.append([x, y])
                x -= 1
            for idx in range(len(index)):
                delta = (k + idx) % len(index)
                res[index[idx][0]][index[idx][1]] = grid[index[delta][0]][index[delta][1]]
        return res


if __name__ == '__main__':
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    k = 2
    grid = [[40, 10], [30, 20]]
    k = 1
    grid = [[10, 1, 4, 8], [6, 6, 3, 10], [7, 4, 7, 10], [1, 10, 6, 1], [2, 1, 1, 10], [3, 8, 9, 2], [7, 1, 10, 10],
            [7, 1, 4, 9], [2, 2, 4, 2], [10, 7, 5, 10]]
    k = 1
    print(Solution().rotateGrid(grid, k))
