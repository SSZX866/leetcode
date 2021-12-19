# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 19:52
# @File    : 419. 甲板上的战舰.py
from leetcode import *


# bfs
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n, ans = len(board), len(board[0]), 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    ans += 1
                    board[i][j] = '.'
                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy
                            if not (0 <= nx < m and 0 <= ny < n) or board[nx][ny] != 'X':
                                continue
                            queue.append((nx, ny))
                            board[nx][ny] = '.'
        return ans


# 边角检测
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n, ans = len(board), len(board[0]), 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if not (0 <= i - 1 < m and 0 <= j < n) or board[i - 1][j] == '.':
                        if not (0 <= i < m and 0 <= j - 1 < n) or board[i][j - 1] == '.':
                            ans += 1
        return ans
