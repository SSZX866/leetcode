# -*- coding: utf-8 -*-
# @Time    : 2021/08/07 22:43
# @File    : 5827. 检查操作是否合法
from leetcode import *


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        i, j = rMove - 1, cMove
        while i >= 0 and board[i][j] != color and board[i][j] != '.': i -= 1
        if i >= 0 and rMove - i >= 2 and board[i][j] != '.': return True
        i, j = rMove + 1, cMove
        while i < m and board[i][j] != color and board[i][j] != '.': i += 1
        if i < m and i - rMove >= 2 and board[i][j] != '.': return True
        i, j = rMove, cMove - 1
        while j >= 0 and board[i][j] != color and board[i][j] != '.': j -= 1
        if j >= 0 and cMove - j >= 2 and board[i][j] != '.': return True
        i, j = rMove, cMove + 1
        while j < n and board[i][j] != color and board[i][j] != '.': j += 1
        if j < n and j - cMove >= 2 and board[i][j] != '.': return True
        i, j = rMove - 1, cMove - 1
        while i >= 0 and j >= 0 and board[i][j] != color and board[i][j] != '.':
            i -= 1
            j -= 1
        if i >= 0 and j >= 0 and rMove - i >= 2 and board[i][j] != '.': return True
        i, j = rMove - 1, cMove + 1
        while i >= 0 and j < n and board[i][j] != color and board[i][j] != '.':
            i -= 1
            j += 1
        if i >= 0 and j < n and rMove - i >= 2 and board[i][j] != '.': return True
        i, j = rMove + 1, cMove - 1
        while i < m and j >= 0 and board[i][j] != color and board[i][j] != '.':
            i += 1
            j -= 1
        if i < m and j >= 0 and i - rMove >= 2 and board[i][j] != '.': return True
        i, j = rMove + 1, cMove + 1
        while i < m and j < n and board[i][j] != color and board[i][j] != '.':
            i += 1
            j += 1
        if i < m and j < n and i - rMove >= 2 and board[i][j] != '.':  return True
        return False
