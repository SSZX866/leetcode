# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 12:54
# @File    : 909. 蛇梯棋.py
from leetcode import *


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def getStatus(curStatus):
            res = []
            for idx in range(1, 7):
                tmpStatus = curStatus + idx
                if tmpStatus > target: break
                if dic[tmpStatus]: tmpStatus = dic[tmpStatus]
                if tmpStatus not in res: res.append(tmpStatus)
            return res

        n = len(board)
        target = n * n
        dic = defaultdict(int)
        for i in range(n):
            base = ((n - i + 1) // 2) * n * 2 + 1
            for j in range(n):
                if (n - i) % 2:
                    if board[i][j] != -1:
                        dic[base - 2 * n + j] = board[i][j]
                else:
                    if board[i][j] != -1:
                        dic[base - 1 - j] = board[i][j]

        visited = {1}
        queue = deque([1])
        step = 0
        while queue:
            step += 1
            curQue = queue
            queue = deque()
            while curQue:
                tmp = curQue.popleft()
                for status in getStatus(tmp):
                    if status in visited:
                        continue
                    if status == target: return step
                    visited.add(status)
                    queue.append(status)
        return -1


if __name__ == '__main__':
    board = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 15, -1, -1, -1, -1]]
    board = [[-1, 4, -1], [6, 2, 6], [-1, 3, -1]]
    board = [[-1, 11, 6, -1], [-1, 15, 16, -1], [-1, 7, -1, 8], [-1, -1, -1, 8]]
    print(Solution().snakesAndLadders(board))
