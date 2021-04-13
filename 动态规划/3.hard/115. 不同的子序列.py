# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 20:41
# @File    : 115. 不同的子序列.py

# dp[i][j] 表示在 s[i:] 的子序列中 t[j:] 出现的个数。
# dp[i][j] = dp[i+1][j]+dp[i+1][j+1],s[i]=t[j]
# dp[i][j] = dp[i+1][j],s[i]!=t[j]
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i + 1][j]
        # print(dp)
        return dp[0][0]

if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    print(Solution().numDistinct(s, t))
