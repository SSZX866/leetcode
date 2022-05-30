# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 09:07
# @File    : 529. 扫雷游戏.py
from leetcode import *


class Solution:
    def __init__(self):
        self.visited = [[0] * 51 for _ in range(51)]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        self.visited[i][j] = 1
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        if board[i][j] in '12345678XB':
            return board
        if board[i][j] == 'E':
            cnt = 0
            directions = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1))
            m, n = len(board), len(board[0])
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if board[nx][ny] == 'M': cnt += 1
            if cnt:
                board[i][j] = str(cnt)
            else:
                board[i][j] = 'B'
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if not (0 <= nx < m and 0 <= ny < n) or self.visited[nx][ny]:
                        continue
                    self.visited[nx][ny] = 1
                    self.updateBoard(board, [nx, ny])
            return board
