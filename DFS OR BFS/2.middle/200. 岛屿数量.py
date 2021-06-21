# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 16:05
# @File    : 200. 岛屿数量.py
from leetcode import *


# BFS 76 ms
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        M, N = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '1':
                    continue
                que = deque([(i, j)])
                grid[i][j] = '-1'
                ans += 1
                while que:
                    tmp = que.popleft()
                    for step in range(4):
                        m = tmp[0] + direct[step][0]
                        n = tmp[1] + direct[step][1]
                        if m < 0 or n < 0 or m >= M or n >= N:
                            continue
                        if grid[m][n] != '1':
                            continue
                        que.append((m, n))
                        grid[m][n] = '-1'
        return ans


# DFS 100 ms
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0

        def dfs(index):
            if index[0] < 0 or index[0] >= M or index[1] < 0 or index[1] >= N:
                return
            if grid[index[0]][index[1]] != '1':
                return
            grid[index[0]][index[1]] = '-1'
            for step in range(4):
                m = index[0] + direct[step][0]
                n = index[1] + direct[step][1]
                dfs((m, n))

        for i in range(M):
            for j in range(N):
                if grid[i][j] != '1':
                    continue
                ans += 1
                dfs((i, j))
        return ans


# 优化DFS 80 ms
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0

        def dfs(index):
            grid[index[0]][index[1]] = '-1'
            for step in range(4):
                m = index[0] + direct[step][0]
                n = index[1] + direct[step][1]
                if m < 0 or m >= M or n < 0 or n >= N:
                    continue
                if grid[m][n] != '1':
                    continue
                dfs((m, n))

        for i in range(M):
            for j in range(N):
                if grid[i][j] != '1':
                    continue
                ans += 1
                dfs((i, j))
        return ans
