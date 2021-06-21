# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 21:00
# @File    : 1905. 统计子岛屿.py
from leetcode import *


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M, N = len(grid1), len(grid1[0])
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid2[i][j] != 1 or grid1[i][j] != 1:
                    continue
                stack = [(i, j)]
                grid2[i][j] = -1
                mark = True
                while stack:
                    tmp = stack.pop()
                    for step in range(4):
                        m = tmp[0] + direct[step][0]
                        n = tmp[1] + direct[step][1]
                        if m < 0 or n < 0 or m >= M or n >= N:
                            continue
                        if grid2[m][n] != 1:
                            continue
                        if grid1[m][n] != 1:
                            mark = False
                            # break 不能break 因为要将属于该岛屿的pixel标记
                        grid2[m][n] = -1
                        stack.append((m, n))
                if mark: ans += 1
        return ans
