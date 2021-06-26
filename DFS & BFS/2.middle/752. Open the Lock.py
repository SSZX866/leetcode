# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 19:12
# @File    : 752. Open the Lock.py
from leetcode import *


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000': return 0
        deads = set(deadends)
        if '0000' in deads: return -1
        step = 0
        que = deque(['0000'])

        visited = {'0000'}

        def getStatus(target):
            statusList = []
            for i in range(4):
                for j in range(2):
                    if j % 2:
                        string = target[:i] + str((int(target[i]) + 10 + 1) % 10) + target[i + 1:]
                    else:
                        string = target[:i] + str((int(target[i]) + 10 - 1) % 10) + target[i + 1:]
                    statusList.append(string)
            return statusList

        while que:
            step += 1
            cur_que = que
            que = deque()
            while cur_que:
                tmp = cur_que.popleft()
                for status in getStatus(tmp):
                    if status in visited:
                        continue
                    visited.add(status)
                    if status in deads:
                        continue
                    if status == target:
                        return step
                    que.append(status)
        return -1


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    deadends = ["8888"]
    target = "0009"
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"

    print(Solution().openLock(deadends, target))
