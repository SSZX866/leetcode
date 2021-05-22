# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 10:05
# @File    : 1738. 找出第 K 大的异或坐标值.py
from leetcode import *

# 堆 3500ms 应该是pop占用了大量时间
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n, heap = len(matrix), len(matrix[0]), []
        pre = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                heapq.heappush(heap, (-pre[i][j], pre[i][j]))
        return heapq.nsmallest(k, heap)[-1][1]


# 排序 1100ms
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
        ans = sorted([pre[i][j] for i in range(1, m + 1) for j in range(1, n + 1)])[-k]
        return ans


if __name__ == '__main__':
    matrix = [[5, 2], [1, 6]]
    k = 1
    matrix = [[5, 2], [1, 6]]
    k = 2
    print(Solution().kthLargestValue(matrix, k))
