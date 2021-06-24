# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 17:10
# @File    : 463. 岛屿的周长.py
from leetcode import *


# BFS
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        direct = [(1, 0), (0, -1), (-1, 0), (0, -1)]
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 1:
                    continue
                que = deque([(i, j)])
                grid[i][j] = -1
                while que:
                    tmp = que.popleft()
                    ans += 4
                    for step in range(4):
                        index = [tmp[0] + direct[step][0], tmp[1] + direct[step][1]]
                        if index[0] < 0 or index[0] >= M or index[1] < 0 or index[1] >= N:
                            continue
                        if grid[index[0]][index[1]] != 0:
                            ans -= 1
                        if grid[index[0]][index[1]] != 1:
                            continue
                        grid[index[0]][index[1]] = -1
                        que.append((index[0], index[1]))
        return ans


# DFS
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        direct = [(1, 0), (0, -1), (-1, 0), (0, -1)]
        ans = 0

        def dfs(index):
            nonlocal ans
            ans += 4
            for step in range(4):
                thisIndex = (index[0] + direct[step][0], index[1] + direct[step][1])
                if thisIndex[0] < 0 or thisIndex[0] >= M or thisIndex[1] < 0 or thisIndex[1] >= N:
                    continue
                if grid[thisIndex[0]][thisIndex[1]] != 0:
                    ans -= 1
                if grid[thisIndex[0]][thisIndex[1]] != 1:
                    continue
                grid[thisIndex[0]][thisIndex[1]] = -1
                dfs(thisIndex)

        for i in range(M):
            for j in range(N):
                if grid[i][j] != 1:
                    continue
                grid[i][j] = -1
                dfs((i, j))
        return ans
