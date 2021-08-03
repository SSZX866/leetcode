# -*- coding: utf-8 -*-
# @Time    : 2021/08/03 13:20
# @File    : 994. 腐烂的橘子
from leetcode import *


# 多源BFS

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(x, y, 0) for x in range(m) for y in range(n) if grid[x][y] == 2])
        ans = 0
        while queue:
            i, j, d = queue.popleft()
            ans = max(ans, d)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, d + 1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return ans
