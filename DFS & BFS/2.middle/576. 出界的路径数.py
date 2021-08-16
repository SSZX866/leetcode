# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 16:25
# @File    : 576. 出界的路径数.py
from leetcode import *


# bfs 超时
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ans = 0
        visit = set()
        queue = deque([(startColumn, startRow, '')])

        def next_status(x, y, path):
            nonlocal ans
            res = []
            for x_, y_, p_ in [(0, 1, '0'), (0, -1, '2'), (1, 0, '1'), (-1, 0, '3')]:
                nx, ny, np = x + x_, y + y_, path + p_
                if 0 <= nx < n and 0 <= ny < m:
                    res.append((nx, ny, np))
                elif np not in visit:
                    visit.add(np)
                    ans += 1
            return res

        while queue and len(queue[0][2]) != maxMove:
            cur = queue
            queue = deque()
            while cur:
                x, y, path = cur.popleft()
                for status in next_status(x, y, path):
                    queue.append(status)
        for x, y, path in queue:
            if (not 0 <= x < n or not 0 <= y < m) and path not in visit:
                visit.add(path)
                ans += 1
        return ans % 1000000007


# 记忆化dfs
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(x, y, step):
            tmp = 0
            if not 0 <= x < m or not 0 <= y < n:
                return 1
            if not step:
                return 0
            for x_, y_ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + x_, y + y_
                tmp += dfs(nx, ny, step - 1)
            return tmp % 1000000007

        return dfs(startRow, startColumn, maxMove)

# 手动lru
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.dp = [[[None] * (maxMove + 1) for __ in range(n + 1)] for _ in range(m + 1)]

        def dfs(x, y, step):
            if self.dp[x][y][step] is not None: return self.dp[x][y][step]
            if not 0 <= x < m or not 0 <= y < n:
                self.dp[x][y][step] = 1
                return 1
            if not step:
                self.dp[x][y][step] = 0
                return 0
            tmp = 0
            for x_, y_ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + x_, y + y_
                tmp += dfs(nx, ny, step - 1)
            tmp %= 1000000007
            self.dp[x][y][step] = tmp
            return tmp

        ans = dfs(startRow, startColumn, maxMove)
        return ans
