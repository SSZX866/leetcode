# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 14:36
# @File    : 547. 省份数量.py
from leetcode import *


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m, n = len(isConnected), len(isConnected[0])
        queue = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] != 1:
                    continue
                ans += 1
                queue.append((i, j))
                isConnected[i][j] = -1
                while queue:
                    x, y = queue.popleft()
                    ny = y
                    for nx in range(m):
                        if not (0 <= nx < m and 0 <= ny < n) or isConnected[nx][ny] != 1:
                            continue
                        isConnected[nx][ny] = -1
                        queue.append((nx, ny))
                    nx = x
                    for ny in range(n):
                        if not (0 <= nx < m and 0 <= ny < n) or isConnected[nx][ny] != 1:
                            continue
                        isConnected[nx][ny] = -1
                        queue.append((nx, ny))
        return ans
