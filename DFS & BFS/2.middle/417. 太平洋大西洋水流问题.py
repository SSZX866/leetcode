# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 20:37
# @File    : 417. 太平洋大西洋水流问题.py
from leetcode import *


# 环路无解，思路错误
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        visited = [[-1] * n for i in range(m)]  # -1 未处理 1 太平洋 2 大西洋 3 either 0 neither
        visited[0][n - 1] = 3
        visited[m - 1][0] = 3

        def dfs(x, y):
            print(x, y)
            if x < 0 or y < 0:
                return 1
            if x >= m or y >= n:
                return 2
            if visited[x][y] != -1: return visited[x][y]
            Pacific, Altantic = 0, 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or heights[nx][ny] <= heights[x][y]:
                    if (0 <= nx < m and 0 <= ny < n and visited[nx][ny] != -1):
                        tmp = visited[nx][ny]
                    else:
                        tmp = dfs(nx, ny)
                    if tmp == 1:
                        Pacific = 1
                    elif tmp == 2:
                        Altantic = 2
            visited[x][y] = Pacific + Altantic
            return visited[x][y]

        for i in range(m):
            for j in range(n):
                if visited[i][j] == -1:
                    visited[i][j] = dfs(i, j)
        ans = []
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 3:
                    ans.append([i, j])
        print(visited)
        return ans


# 思路： 分别从太平洋和大西洋逆流而上，寻找可以重叠的部分
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        visited = [[0] * n for i in range(m)]  # 0 未处理 1 太平洋 2 大西洋 3 either
        res = []

        queue = collections.deque([])
        for i in range(m):
            visited[i][0] = 1
            queue.append((i, 0))
        for j in range(1, n):
            visited[0][j] = 1
            queue.append((0, j))
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or visited[nx][ny] != 0:
                    continue
                if heights[nx][ny] < heights[x][y]:
                    continue
                visited[nx][ny] = 1
                queue.append((nx, ny))
        queue = collections.deque([])
        for i in range(m):
            if visited[i][n - 1] == 1:
                res.append([i, n - 1])
                visited[i][n - 1] = 3
            else:
                visited[i][n - 1] = 2
            queue.append((i, n - 1))
        for j in range(n - 1):
            if visited[m - 1][j] == 1:
                res.append([m - 1, j])
                visited[m - 1][j] = 3
            else:
                visited[m - 1][j] = 2
            queue.append((m - 1, j))
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or visited[nx][ny] >= 2:
                    continue
                if heights[nx][ny] < heights[x][y]:
                    continue
                if visited[nx][ny] == 1:  # 1
                    res.append([nx, ny])
                visited[nx][ny] += 2
                queue.append((nx, ny))

        return res


if __name__ == '__main__':
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]

    print(Solution().pacificAtlantic(heights))
