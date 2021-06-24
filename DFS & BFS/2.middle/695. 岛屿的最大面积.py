# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 18:53
# @File    : 695. 岛屿的最大面积.py
from leetcode import *


# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        ans = 0
        tmp = 0
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(index):
            nonlocal tmp
            tmp += 1
            for step in range(4):
                m = index[0] + direct[step][0]
                n = index[1] + direct[step][1]
                if m < 0 or m >= M or n < 0 or n >= N:
                    continue
                if grid[m][n] != 1:
                    continue
                grid[m][n] = -1
                dfs((m, n))

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    grid[i][j] = -1
                    tmp = 0
                    dfs((i, j))
                    ans = max(tmp, ans)
        return ans


# 不使用全局变量
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        ans = 0
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(index):
            tmp = 1
            for step in range(4):
                m = index[0] + direct[step][0]
                n = index[1] + direct[step][1]
                if m < 0 or m >= M or n < 0 or n >= N:
                    continue
                if grid[m][n] != 1:
                    continue
                grid[m][n] = -1
                tmp += dfs((m, n))
            return tmp

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    grid[i][j] = -1
                    ans = max(dfs((i, j)), ans)
        return ans


# DFS栈实现
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        ans = 0
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 1:
                    continue
                stack = [(i, j)]
                grid[i][j] = -1
                tmp = 0
                while stack:
                    index = stack.pop()
                    tmp += 1
                    for step in range(4):
                        m = index[0] + direct[step][0]
                        n = index[1] + direct[step][1]
                        if m < 0 or m >= M or n < 0 or n >= N:
                            continue
                        if grid[m][n] != 1:
                            continue
                        grid[m][n] = -1
                        stack.append((m, n))
                ans = max(ans, tmp)
        return ans


# BFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        ans = 0
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 1:
                    continue
                que = deque([(i, j)])
                grid[i][j] = -1
                tmp = 0
                while que:
                    index = que.popleft()
                    tmp += 1
                    for step in range(4):
                        m = index[0] + direct[step][0]
                        n = index[1] + direct[step][1]
                        if m < 0 or m >= M or n < 0 or n >= N:
                            continue
                        if grid[m][n] != 1:
                            continue
                        grid[m][n] = -1
                        que.append((m, n))
                ans = max(ans, tmp)
        return ans
