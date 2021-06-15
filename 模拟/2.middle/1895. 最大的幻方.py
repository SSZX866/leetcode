# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 22:48
# @File    : 5202. 最大的幻方.py
from leetcode import *


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        grid2 = list(zip(*grid))

        def check(level):
            i, j = 0, 0
            while i + level - 1 <= n and j + level - 1 <= m:
                # 检查每一行
                Sum = -1
                this = True
                for each in range(level):
                    sum_x = sum(grid[i + each][each:each + level])
                    sum_y = sum(grid2[j + each][each:each + level])
                    print(sum_x, sum_y, grid[i + each][each:each + level], grid2[j + each][each:each + level])
                    if sum_x != Sum and Sum != -1:
                        this = False
                        break
                    if Sum == -1: Sum = sum_x
                    if sum_y != Sum:
                        this = False
                        break
                if this: return True
                j += 1
                if j + level == m and i + level - 1 <= n:
                    j = 0
                    i += 1
                if i + level == n: return False

        for level in range(2, 51):
            if check(level): return level


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def check(tmp, level):
            sum_ = sum(tmp[0])
            for i in range(1, level):
                if sum(tmp[i]) != sum_:
                    return False
            for i in range(level):
                sum_y = 0
                for j in range(level):
                    sum_y += tmp[j][i]
                if sum_y != sum_:
                    return False
            sum_xy, sum_yx = 0, 0
            for i in range(level):
                sum_xy += tmp[i][i]
                sum_yx += tmp[i][level - 1 - i]
            if sum_yx != sum_ or sum_yx != sum_:
                return False
            return True

        ans = 1
        for level in range(1, 51):
            for x in range(len(grid) - level + 1):
                for i in range(len(grid[0]) - level + 1):
                    tmp = []
                    for x1 in range(level):
                        tmp.append(grid[x:x + level][x1][i:i + level])
                    # print(tmp)
                    if check(tmp, level):
                        print(level, tmp)
                        ans = level
        return ans


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 检验该矩阵是否为幻方
        def check(starti, startj, level):
            Sum = -1
            s = 0
            for i in range(starti, starti + level):
                for j in range(startj, startj + level):
                    s += grid[i][j]
                if s != Sum and Sum != -1: return False
                Sum = s
                s = 0
            for j in range(startj, startj + level):
                for i in range(starti, starti + level):
                    s += grid[i][j]
                if s != Sum: return False
                s = 0
            for i in range(level):
                s += grid[starti + i][startj + i]
            if s != Sum: return False
            s = 0
            for i in range(level):
                s += grid[starti + i][startj + level - i - 1]
            if s != Sum: return False
            return True

        # 从大到小枚举所有可能的幻方边长
        for level in range(min(m, n), 0, -1):
            # 枚举每一个可能的矩阵左上角坐标
            for i in range(m - level + 1):
                for j in range(n - level + 1):
                    if check(i, j, level): return level
        return 1


if __name__ == '__main__':
    grid = [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
    print(Solution().largestMagicSquare(grid))
