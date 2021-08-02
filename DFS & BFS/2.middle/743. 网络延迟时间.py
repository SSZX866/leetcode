# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 11:00
# @File    : 743. 网络延迟时间
from leetcode import *


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connect = defaultdict(lambda:defaultdict(int))
        for u,v,w in times:
            connect[u][v] = w
        q = [(0, k)]
        explored = set()
        while q:
            t, node = heapq.heappop(q)
            if node in explored:
                continue
            explored.add(node)
            if len(explored) == n:
                return t
            for other, tm in connect[node].items():
                if other not in explored:
                    heapq.heappush(q, (t+tm, other))
        return -1



if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    times = [[1, 2, 1], [2, 1, 3]]
    n = 2
    k = 2
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
    n = 3
    k = 1
    times = [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]]
    n = 3
    k = 1
    print(Solution().networkDelayTime(times, n, k))
