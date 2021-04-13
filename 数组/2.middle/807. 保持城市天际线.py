# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 13:40
# @File    : 807. 保持城市天际线.py
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        skyLine = [[0] * n for _ in range(2)]
        newGrid = [[0] * n for _ in range(n)]
        for i in range(n):
            skyLine[0][i] = max(list(zip(*grid))[i])
            skyLine[1][i] = max(grid[i])
        for i in range(n):
            for j in range(n):
                newGrid[i][j] = min(skyLine[0][j],skyLine[1][i])
        # print(skyLine,newGrid)
        return sum(sum(g) for g in newGrid) - sum(sum(g) for g in grid)

if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(Solution().maxIncreaseKeepingSkyline(grid))