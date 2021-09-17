# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 12:14
# @File    : 212. 单词搜索 II.py
from leetcode import *


# 未预处理 超时
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        m, n = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True
            res = False
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx = dx + x
                ny = dy + y
                if not (0 <= nx < m and 0 <= ny < n) or visited[nx][ny]:
                    continue
                if board[nx][ny] != word[index]:
                    continue
                visited[nx][ny] = 1
                if dfs(nx, ny, index + 1):
                    res = not res
                    visited[nx][ny] = 0
                    break
                visited[nx][ny] = 0
            return res

        visited = [[0] * n for _ in range(m)]
        for word in words:
            flag = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        visited[i][j] = 1
                        if dfs(i, j, 1):
                            ans.append(word)
                            flag = not flag
                            visited[i][j] = 0
                            break
                        visited[i][j] = 0
                if flag: break
        print(visited)
        return ans


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        m, n = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True
            res = False
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx = dx + x
                ny = dy + y
                if not (0 <= nx < m and 0 <= ny < n) or (nx, ny) in visited:
                    continue
                if board[nx][ny] != word[index]:
                    continue
                visited.add((nx, ny))
                if dfs(nx, ny, index + 1):
                    res = not res
                    visited.remove((nx, ny))
                    break
                visited.remove((nx, ny))
            return res

        visited = set()
        for word in words:
            flag = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        visited.add((i, j))
                        if dfs(i, j, 1):
                            ans.append(word)
                            flag = not flag
                            visited.remove((i, j))
                            break
                        visited.remove((i, j))
                if flag: break
        print(visited)
        return ans


# 预处理字母数量
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        m, n = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True
            res = False
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx = dx + x
                ny = dy + y
                if not (0 <= nx < m and 0 <= ny < n) or visited[nx][ny]:
                    continue
                if board[nx][ny] != word[index]:
                    continue
                visited[nx][ny] = 1
                if dfs(nx, ny, index + 1):
                    res = not res
                    visited[nx][ny] = 0
                    break
                visited[nx][ny] = 0
            return res

        # 预处理单词
        boardCnt = Counter()
        for i in range(m):
            for j in range(n):
                boardCnt[board[i][j]] += 1

        visited = [[0] * n for _ in range(m)]
        for word in words:
            curCnt = Counter(word)
            flag = False
            for key in curCnt:
                if curCnt[key] > boardCnt[key]:
                    flag = not flag
                    break
            if flag: continue
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        visited[i][j] = 1
                        if dfs(i, j, 1):
                            ans.append(word)
                            flag = not flag
                            visited[i][j] = 0
                            break
                        visited[i][j] = 0
                if flag: break
        return ans
