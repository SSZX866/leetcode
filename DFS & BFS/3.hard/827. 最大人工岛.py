# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 19:27
# @File    : 827. 最大人工岛.py
from leetcode import *


# DFS超时
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        # 去掉不含0的情况
        if 0 not in [every for each in grid for every in each]: return M * N
        ans = 0

        def maxAreaOfIsland(tmpGrid: List[List[int]]) -> int:
            ans = 0
            direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for i in range(M):
                for j in range(N):
                    if tmpGrid[i][j] != 1:
                        continue
                    que = deque([(i, j)])
                    tmpGrid[i][j] = -1
                    tmp = 0
                    while que:
                        index = que.popleft()
                        tmp += 1
                        for step in range(4):
                            m = index[0] + direct[step][0]
                            n = index[1] + direct[step][1]
                            if m < 0 or m >= M or n < 0 or n >= N:
                                continue
                            if tmpGrid[m][n] != 1:
                                continue
                            tmpGrid[m][n] = -1
                            que.append((m, n))
                    ans = max(ans, tmp)
            return ans

        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0:
                    continue
                tmp = copy.deepcopy(grid)
                tmp[i][j] = 1
                ans = max(ans, maxAreaOfIsland(tmp))
        return ans


# 使用visit数组 超时
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        # 去掉不含0的情况
        if 0 not in [every for each in grid for every in each]: return M * N
        ans = 0

        def maxAreaOfIsland(visit) -> int:
            ans = 0
            direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for i in range(M):
                for j in range(N):
                    if grid[i][j] != 1 or visit[i][j]:
                        continue
                    que = deque([(i, j)])
                    visit[i][j] = True
                    tmp = 0
                    while que:
                        index = que.popleft()
                        tmp += 1
                        for step in range(4):
                            m = index[0] + direct[step][0]
                            n = index[1] + direct[step][1]
                            if m < 0 or m >= M or n < 0 or n >= N:
                                continue
                            if grid[m][n] != 1 or visit[m][n]:
                                continue
                            visit[m][n] = True
                            que.append((m, n))
                    ans = max(ans, tmp)
            return ans

        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0:
                    continue
                visit = [[False] * N for _ in range(M)]
                grid[i][j] = 1
                ans = max(ans, maxAreaOfIsland(visit))
                grid[i][j] = 0
        return ans


class Solution(object):
    def largestIsland(self, grid):
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        # 去掉不含0的情况
        if 0 not in [every for each in grid for every in each]: return M * N
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        ans = 1  # 去掉不含1的情况
        dic = dict()
        flag = 2

        # 将所有不同的岛标号，并将其面积存入字典中
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    que = deque([(i, j)])
                    tmp = 0
                    grid[i][j] = flag
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
                            grid[m][n] = flag
                            que.append((m, n))
                    dic[flag] = tmp
                    flag += 1

        # 搜索所有海周围的岛，计算最大值
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    tmp = set()
                    for step in range(4):
                        m = i + direct[step][0]
                        n = j + direct[step][1]
                        if m < 0 or m >= M or n < 0 or n >= N:
                            continue
                        if grid[m][n] < 2:
                            continue
                        tmp.add(grid[m][n])
                    ans = max(ans, 1 + sum(dic[each] for each in tmp))
        return ans


if __name__ == '__main__':
    grid = [[1, 0], [0, 1]]
    print(Solution().largestIsland(grid))
