# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 22:39
# @File    : 5793. 迷宫中离入口最近的出口.py
from leetcode import *


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = {(entrance[0], entrance[1])}
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(entrance[0], entrance[1])])
        step = 0

        def getStatus(target):
            res = []
            for i in range(4):
                x = target[0] + direct[i][0]
                y = target[1] + direct[i][1]
                if x < 0 or y < 0 or x >= m or y >= n:
                    continue
                if maze[x][y] == '+':
                    continue
                res.append((x, y))
            return res

        while queue:
            step += 1
            cur_que = queue
            queue = deque()
            while cur_que:
                tmp = cur_que.popleft()
                for each in getStatus(tmp):
                    if each in visited:
                        continue
                    visited.add(each)
                    if each[0] == 0 or each[1] == 0 or each[0] == m - 1 or each[1] == n - 1:
                        return step
                    queue.append(each)
        return -1


if __name__ == '__main__':
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    print(Solution().nearestExit(maze, entrance))
