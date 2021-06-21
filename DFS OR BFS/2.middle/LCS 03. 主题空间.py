# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 21:13
# @File    : LCS 03. 主题空间.py
from leetcode import *


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        M, N = len(grid), len(grid[0])
        grid1 = [[int(grid[i][j]) for j in range(N)] for i in range(M)]
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(index):
            nonlocal tmp
            mark = True
            for step in range(4):
                m = index[0] + direct[step][0]
                n = index[1] + direct[step][1]
                if m < 0 or m >= M or n < 0 or n >= N:
                    mark = False
                    continue
                if grid1[m][n] == 0:
                    mark = False
                    continue
                if visit[m][n]:
                    continue
                if grid1[m][n] != grid1[index[0]][index[1]]:
                    continue
                visit[m][n] = True
                tmp += 1
                # mark = mark and dfs((m, n)) 错误写法，短路特性不会执行dfs!!!!!!!!!!!!!! debug了一小时
                mark = dfs((m, n)) and mark
            return mark

        ans = 0
        visit = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if grid1[i][j] == 0 or visit[i][j]:
                    continue
                tmp = 1
                visit[i][j] = True
                if dfs((i, j)): ans = max(tmp, ans)
        return ans


if __name__ == '__main__':
    grid = ["110", "231", "221"]
    grid = ["11111100000", "21243101111", "21224101221", "11111101111"]
    grid = ["113415514", "124112542", "313225220", "253354005", "352014331", "304514425", "553313413", "532352143",
            "220340311", "245210141"]
    print(Solution().largestArea(grid))
