# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 14:12
# @File    : 130. 被围绕的区域.py
from leetcode import *

# BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        queue = deque()
        # 将边界处为'O'的标记为'Y'并加入队列
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = 'Y'
            if board[i][n - 1] == 'O':
                queue.append((i, n - 1))
                board[i][n - 1] = 'Y'
        for i in range(n):
            if board[0][i] == 'O':
                queue.append((0, i))
                board[0][i] = 'Y'
            if board[m - 1][i] == 'O':
                queue.append((m - 1, i))
                board[m - 1][i] = 'Y'
        # 将与边界处相邻的'O'标记为'Y'
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = dx + x
                ny = dy + y
                if not (0 <= nx < m and 0 <= ny < n) or board[nx][ny] != 'O':
                    continue
                board[nx][ny] = 'Y'
                queue.append((nx, ny))
        # 将剩下所有标记为'O'的标记为'X'，将剩下所有标记为'Y'的标记为'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
