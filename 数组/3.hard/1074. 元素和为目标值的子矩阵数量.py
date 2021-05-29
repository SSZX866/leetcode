# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 10:32
# @File    : 1074. 元素和为目标值的子矩阵数量.py
from leetcode import *


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + matrix[i][j]
        ans = 0
        for i in range(m + 1):
            for k in range(i + 1, m + 1):
                dic = defaultdict(int)
                for j in range(n):
                    tmp = pre[k][n] - pre[k][j] - pre[i][n] + pre[i][j]
                    ans += dic[tmp]
                    dic[tmp - target] += 1
                    if tmp == target: ans += 1
        return ans


if __name__ == '__main__':
    matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target = 0
    matrix = [[1, -1], [-1, 1]]
    target = 0
    print(Solution().numSubmatrixSumTarget(matrix, target))
