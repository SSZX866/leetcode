# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 13:44
# @File    : 1091. 二进制矩阵中的最短路径.py
from leetcode import *


#  dfs TLE
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        n = len(grid)
        inf = 1 << 32

        @lru_cache(None)
        def dfs(x, y, remain):
            if x == y == n - 1:
                return 1
            if not remain:
                return inf
            remain -= 1
            ans = inf
            for dx, dy in ((-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (-1, 1), (1, -1)):
                nx = dx + x
                ny = dy + y
                if not (0 <= nx < n and 0 <= ny < n) or grid[nx][ny]:
                    continue
                ans = min(ans, dfs(nx, ny, remain) + 1)
            return ans

        ans = dfs(0, 0, n * n - 1)
        return ans if ans != inf else -1


# bfs
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        n = len(grid)
        if n == 1: return n  # 去掉 [[0]]的情况
        ans = 1 << 32
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        while queue:
            cur = queue
            queue = deque()
            while cur:
                x, y, step = cur.popleft()
                for dx, dy in ((-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (-1, 1), (1, -1)):
                    nx = x + dx
                    ny = y + dy
                    if not (0 <= nx < n and 0 <= ny < n) or grid[nx][ny]:
                        continue
                    if nx == ny == n - 1:
                        ans = min(ans, step + 1)
                        continue
                    grid[nx][ny] = 1
                    queue.append((nx, ny, step + 1))
        return ans if ans != 1 << 32 else -1
