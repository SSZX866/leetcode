# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 19:35
# @File    : 773. Sliding Puzzle.py
from leetcode import *


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def ToString(target):
            res = ''
            for i in range(2):
                for j in range(3):
                    res += str(target[i][j])
            return res

        def swapWithLeft(target, index):
            return target[:index - 1] + target[index] + target[index - 1] + target[index + 1:]

        def swapWithRight(target, index):
            return target[:index] + target[index + 1] + target[index] + target[index + 2:]

        def swapWithUp(target, index):
            return target[:index - 3] + target[index] + target[index - 2:index] + target[index - 3] + target[index + 1:]

        def swapWithDown(target, index):
            return target[:index] + target[index + 3] + target[index + 1:index + 3] + target[index] + target[index + 4:]

        def getStatus(target):
            statusList = []
            index = target.index('0')
            if index == 0:
                statusList.append(swapWithRight(target, index))
                statusList.append(swapWithDown(target, index))
            elif index == 1:
                statusList.append(swapWithLeft(target, index))
                statusList.append(swapWithRight(target, index))
                statusList.append(swapWithDown(target, index))
            elif index == 2:
                statusList.append(swapWithLeft(target, index))
                statusList.append(swapWithDown(target, index))
            elif index == 3:
                statusList.append(swapWithRight(target, index))
                statusList.append(swapWithUp(target, index))
            elif index == 4:
                statusList.append(swapWithUp(target, index))
                statusList.append(swapWithRight(target, index))
                statusList.append(swapWithLeft(target, index))
            elif index == 5:
                statusList.append(swapWithUp(target, index))
                statusList.append(swapWithLeft(target, index))
            return statusList

        tar = ToString([[1, 2, 3], [4, 5, 0]])
        start = ToString(board)
        visited = {start}
        if start == tar: return 0
        que = deque([start])
        step = 0
        while que:
            step += 1
            cur_que = que
            que = deque()
            while cur_que:
                tmp = cur_que.popleft()
                for status in getStatus(tmp):
                    if status in visited: continue
                    if status == tar: return step
                    visited.add(status)
                    que.append(status)
        return -1


if __name__ == '__main__':
    board = [[1, 2, 3], [4, 0, 5]]
    print(Solution().slidingPuzzle(board))
