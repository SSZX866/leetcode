# -*- coding: utf-8 -*-
# @Time    : 2021/11/17 21:10
# @File    : 面试题 16.19. 水域大小.py
from leetcode import *


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1))
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    land[i][j] = -1
                    tmp = 0
                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        tmp += 1
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if not (0 <= nx < m and 0 <= ny < n) or land[nx][ny] != 0:
                                continue
                            land[nx][ny] = -1
                            queue.append((nx, ny))
                    res.append(tmp)
        res.sort()

        return res
