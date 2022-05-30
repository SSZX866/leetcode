# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 11:29
# @File    : 剑指 Offer 13. 机器人的运动范围.py
from leetcode import *


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def calcBitSum(target):
            res = 0
            while target:
                res += target % 10
                target //= 10
            return res

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * n for _ in range(m)]
        res = 0
        queue = collections.deque([(0, 0)])
        visited[0][0] = 1
        while queue:
            x, y = queue.popleft()
            res += 1
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or visited[nx][ny]:
                    continue
                visited[nx][ny] = 1
                if calcBitSum(nx) + calcBitSum(ny) > k:
                    continue
                queue.append((nx, ny))
        return res


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def calcBitSum(target):
            res = 0
            while target:
                res += target % 10
                target //= 10
            return res

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * n for _ in range(m)]
        visited[0][0] = 1

        def dfs(x, y):
            res = 1
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or visited[nx][ny]:
                    continue
                visited[nx][ny] = 1
                if calcBitSum(nx) + calcBitSum(ny) > k:
                    continue
                res += dfs(nx, ny)
            return res

        return dfs(0, 0)
