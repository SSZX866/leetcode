# -*- coding: utf-8 -*-
# @Time    : 2021/12/9 09:56
# @File    : 794. 有效的井字游戏.py
from leetcode import *


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        cnt = Counter()
        for i in range(3):
            cnt += Counter(board[i])
        x, o = cnt['X'], cnt['O']
        if o > x: return False
        if x > o + 1: return False
        xxx, ooo = Counter(board)['XXX'], Counter(board)['OOO']
        xxx += Counter(zip(*board))[('X', 'X', 'X')]
        ooo += Counter(zip(*board))[('O', 'O', 'O')]
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            if board[0][0] == 'X':
                xxx += 1
            else:
                ooo += 1
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            if board[0][2] == 'X':
                xxx += 1
            else:
                ooo += 1
        if ooo and xxx: return False
        if ooo and x != o: return False
        if xxx and x != o + 1: return False
        return True
