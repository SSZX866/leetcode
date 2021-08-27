# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 14:03
# @File    : 79. 单词搜索.py
from leetcode import *


# dfs + 回溯
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        indexs = set()

        def dfs(x, y, cur, i):
            if i == len(word):
                if cur == word: return True
                return False
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = dx + x
                ny = dy + y
                if not (0 <= nx < m and 0 <= ny < n) or board[nx][ny] != word[i]:
                    continue
                if (nx, ny) in indexs:
                    continue
                indexs.add((nx, ny))
                if dfs(nx, ny, cur + board[nx][ny], i + 1): return True
                indexs.remove((nx, ny))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    indexs.add((i, j))
                    if dfs(i, j, word[0], 1):
                        return True
                    indexs.remove((i, j))
        return False


# 不使用set记录访问过的路径，直接在原board上记录
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(x, y, cur, i):
            if i == len(word):
                if cur == word: return True
                return False
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = dx + x
                ny = dy + y
                if not (0 <= nx < m and 0 <= ny < n) or board[nx][ny] != word[i]:
                    continue
                tmp, board[nx][ny] = board[nx][ny], '0'
                if dfs(nx, ny, cur + tmp, i + 1): return True
                board[nx][ny] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    tmp, board[i][j] = board[i][j], '0'
                    if dfs(i, j, word[0], 1):
                        return True
                    board[i][j] = tmp
        return False
