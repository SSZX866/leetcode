# -*- coding: utf-8 -*-
# @Time    : 2021/08/01 09:25
# @File    : 1337. 矩阵中战斗力最弱的 K 行
from leetcode import *
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        scores = [sum(each) for each in mat]
        heap = []
        for i in range(len(scores)):
            if not heap or len(heap) < k:
                heapq.heappush(heap, (-scores[i], -i))
            elif -heap[0][0] > scores[i]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-scores[i], -i))
        ans = []
        while heap:ans.append(-heapq.heappop(heap)[1])
        return ans[::-1]