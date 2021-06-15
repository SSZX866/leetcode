# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 19:37
# @File    : 840. 矩阵中的幻方.py
from leetcode import *


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(starti, startj):
            Sum = 0
            dic = set()
            for i in range(starti, starti + 3):
                tmp = 0
                for j in range(startj, startj + 3):
                    if grid[i][j] in dic or not 1 <= grid[i][j] <= 9: return False
                    dic.add(grid[i][j])
                    tmp += grid[i][j]
                if Sum and Sum != tmp: return False
                Sum = tmp
            for j in range(startj, startj + 3):
                tmp = 0
                for i in range(starti, starti + 3):
                    tmp += grid[i][j]
                if Sum != tmp: return False
            tmp = 0
            for i in range(3):
                tmp += grid[starti + i][startj + i]
            if Sum != tmp: return False
            tmp = 0
            for i in range(3):
                tmp += grid[starti + i][startj + 2 - i]
            if Sum != tmp: return False
            return True

        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3: return 0
        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if check(i, j): ans += 1
        return ans
