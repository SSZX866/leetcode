# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 10:36
# @File    : 5736. 单线程 CPU.py
from leetcode import *
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        index = list(range(n))
        index.sort(key=lambda x: tasks[x][0])  # 按照tasks[i][0]排序
        j, i, timestamp, ans, q = 0, 0, 0, list(), list()
        while i < n:
            if not q:
                timestamp = max(tasks[index[i]][0], timestamp)
            while j < n and tasks[index[j]][0] <= timestamp:
                heapq.heappush(q, (tasks[index[j]][1], index[j]))
                j += 1
            needTime, res = heapq.heappop(q)
            timestamp += needTime
            ans.append(res)
            i += 1
        return ans


if __name__ == '__main__':
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    tasks = [[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4],
             [18, 18], [46, 39], [12, 24]]
    print(Solution().getOrder(tasks))
