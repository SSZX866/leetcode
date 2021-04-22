# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 12:09
# @File    : 363. 矩形区域不超过 K 的最大数值和.py
from leetcode import *
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + matrix[i][j]
        ans, num = -100000, k
        # 暴力超时
        # for i in range(m): # 上
        #     for j in range(n): # 左
        #         for k in range(i, m): # 下
        #             for l in range(j, n): # 右
        #                 tmp = dp[k + 1][l + 1] + dp[i][j] - dp[i][l + 1] - dp[k + 1][j]
        #                 # print(tmp, ans)
        #                 if ans < tmp <= num:
        #                     if tmp == num:
        #                         return num
        #                     ans = tmp
        for i in range(m):  # 上
            for j in range(i, m):  # 下
                sort_list = []
                bisect.insort(sort_list, 0)
                for r in range(n):
                    right = dp[j + 1][r + 1] - dp[i][r + 1]
                    left_idx = bisect.bisect_left(sort_list, right - k)
                    if left_idx < len(sort_list):
                        left = sort_list[left_idx]
                        curr = right - left
                        if curr == k:
                            return k
                        elif curr < k:
                            ans = max(ans, curr)
                    bisect.insort(sort_list, right)
        return ans


if __name__ == '__main__':
    print(Solution().maxSumSubmatrix(matrix=[[1, 0, 1], [0, -2, 3]], k=2))
    print(Solution().maxSumSubmatrix(matrix=[[2, 2, -1]], k=3))
