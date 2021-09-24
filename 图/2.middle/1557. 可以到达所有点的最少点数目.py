# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 10:31
# @File    : 1557. 可以到达所有点的最少点数目.py
from leetcode import *


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for start, end in edges:
            indegree[end] += 1

        ans = []
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
        return ans
