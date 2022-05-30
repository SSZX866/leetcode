# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 09:09
# @File    : 1034. 边界着色.py
from leetcode import *


# bfs
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        curColor = grid[row][col]
        visited = [[0] * n for _ in range(m)]
        res = []
        queue = collections.deque([(row, col)])

        while queue:
            x, y = queue.popleft()
            boundary = False
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] != curColor:
                    boundary = True
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = 1
                queue.append((nx, ny))
            if boundary: res.append((x, y))

        for x, y in res:
            grid[x][y] = color

        return grid


# dfs
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        curColor = grid[row][col]
        visited = [[0] * n for _ in range(m)]
        res = []

        def dfs(x, y):
            boundary = False
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] != curColor:
                    boundary = True
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = 1
                dfs(nx, ny)
            if boundary: res.append((x, y))

        dfs(row, col)
        for x, y in res:
            grid[x][y] = color

        return grid
