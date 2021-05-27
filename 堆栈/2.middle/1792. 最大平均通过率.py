# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 10:26
# @File    : 1792. 最大平均通过率.py
from leetcode import *


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        diff = lambda x, y: (x + 1) / (y + 1) - x / y

        q = list()
        ans = 0.
        for x, y in classes:
            ans += x / y
            q.append((-diff(x, y), x, y))

        heapq.heapify(q)

        for _ in range(extraStudents):
            d, x, y = heapq.heappop(q)
            ans += -d
            heapq.heappush(q, (-diff(x + 1, y + 1), x + 1, y + 1))

        return ans / len(classes)


if __name__ == '__main__':
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4
