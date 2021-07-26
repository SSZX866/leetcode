# -*- coding: utf-8 -*-
# @Time    : 2021/07/24 22:32
# @File    : 5805. 最小未被占据椅子的编号
from leetcode import *

# 排序+优先队列
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetTime = times[targetFriend][0]
        times.sort(key=lambda x: x[0])
        n = len(times)
        chairs = [i for i in range(n + 1)]
        heapq.heapify(chairs)
        q = list()
        for arrive, leave in times:
            while q and q[0][0] <= arrive:
                _, chair = heapq.heappop(q)
                heapq.heappush(chairs, chair)
            if arrive < targetTime:
                chair = heapq.heappop(chairs)
                heapq.heappush(q, (leave, chair))
            if arrive == targetTime: return chairs[0]


if __name__ == '__main__':
    times = [[33889, 98676], [80071, 89737], [44118, 52565], [52992, 84310], [78492, 88209], [21695, 67063],
             [84622, 95452], [98048, 98856], [98411, 99433], [55333, 56548], [65375, 88566], [55011, 62821],
             [48548, 48656], [87396, 94825], [55273, 81868], [75629, 91467]]
    targetFriend = 6
    print(Solution().smallestChair(times, targetFriend))
