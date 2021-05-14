# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 10:33
# @File    : 1269. 停在原地的方案数.py
from leetcode import *


# dp[i][j]代表当前剩余操作数为i，所在位置为j的所有方案数。

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp, limit = [[0] * (steps + 1) for _ in range(steps + 1)], min(steps, arrLen)
        dp[steps][0] = 1
        for i in range(steps - 1, -1, -1):
            for j in range(limit):
                dp[i][j] = dp[i + 1][j] + dp[i + 1][j - 1] + dp[i + 1][j + 1]
        return dp[0][0] % 1000000007


if __name__ == '__main__':
    steps = 27
    arrLen = 7
    print(Solution().numWays(steps, arrLen))
