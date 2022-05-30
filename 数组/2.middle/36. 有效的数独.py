# -*- coding: utf-8 -*-
# @Time    : 2021/07/30 17:44
# @File    : 36. 有效的数独
from leetcode import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        block = [[set(), set(), set()] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in column[j]:
                    return False
                if board[i][j] in row[i]:
                    return False
                if board[i][j] in block[i // 3][j // 3]:
                    return False
                column[j].add(board[i][j])
                row[i].add(board[i][j])
                block[i // 3][j // 3].add(board[i][j])
        return True


# 优化空间
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [[False] * 9 for _ in range(9)]
        row = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                board[i][j] = int(board[i][j]) - 1
                if column[j][board[i][j]]:
                    return False
                if row[i][board[i][j]]:
                    return False
                if block[i // 3][j // 3][board[i][j]]:
                    return False
                column[j][board[i][j]] = True
                row[i][board[i][j]] = True
                block[i // 3][j // 3][board[i][j]] = True
        return True


# 位运算
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, column, block = [0] * 9, [0] * 9, [[0] * 3 for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if (row[j] << num) & 1 or (column[i] << num) & 1 or (
                        block[i // 3][j // 3] << num) & 1:
                    return False
                row[j] |= 1 << num
                column[i] |= 1 << num
                block[i // 3][j // 3] |= 1 << num
        return True