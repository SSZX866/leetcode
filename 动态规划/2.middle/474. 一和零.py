# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 12:12
# @File    : 474. 一和零.py
from leetcode import *


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = s.count('1')
            for i in range(m, cnt0 - 1, -1):  # 0-1背包问题，内循环逆序
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        return dp[m][n]


# dp[i][c1][c2] 第i轮中代价为c1,c2的个数
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs))]
        zeros = strs[0].count('0')
        ones = strs[0].count('1')
        if zeros <= m and ones <= n: dp[0][zeros][ones] = 1
        for i in range(1, len(strs)):
            for j in range(m + 1):
                for k in range(n + 1):
                    zeros = strs[i].count('0')
                    ones = strs[i].count('1')
                    # if j - zeros >= 0 and k - ones >= 0: dp[i][j][k] = dp[i - 1][j - zeros][k - ones]
                    if j - zeros >= 0 and k - ones >= 0: dp[i][j][k] = dp[i - 1][j - zeros][k - ones] + 1
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
        ans = 0
        for j in range(m + 1):
            for k in range(n + 1):
                ans = max(ans, dp[-1][j][k])
        return ans


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    strs = ["00", "000"]
    m = 1
    n = 10
    print(Solution().findMaxForm(strs, m, n))
