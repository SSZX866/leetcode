# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 23:03
# @File    : 5757. 矩阵中最大的三个菱形和.py
import heapq

from leetcode import *


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m):
            for j in range(n):
                top, bottom, left, right = i, i, j, j
                while top >= 0 and bottom < m and left >= 0 and right < n:
                    tmp = 0
                    p = top
                    while p <= bottom:

                        if p == top:
                            tmp += grid[p][j]
                            q = j - 1
                            r = j + 1
                        elif p < i:
                            tmp += grid[p][q] + grid[p][r]
                            q -= 1
                            r += 1
                        elif p != bottom:
                            tmp += grid[p][q] + grid[p][r]
                            q += 1
                            r -= 1
                        else:
                            tmp += grid[p][j]
                        p += 1

                    if len(ans) < 3:
                        if tmp not in ans:
                            heapq.heappush(ans, tmp)
                    else:
                        if tmp not in ans and ans[0] < tmp:
                            heapq.heappop(ans)
                            heapq.heappush(ans, tmp)
                    top -= 1
                    bottom += 1
                    left -= 1
                    right += 1
        ans.sort()
        return ans[::-1]


if __name__ == '__main__':
    grid = [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    grid = [[7, 7, 7]]
    print(Solution().getBiggestThree(grid))
