#f[m,n] = f[m-1,n] + f[m, n-1]
#if m or n == 0, f[m,n] = 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n]*m
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    print(i,j)
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #print(dp)
        return dp[-1][-1]


############排列组合方法
# 思路与算法
#
# 从左上角到右下角的过程中，我们需要移动 m+n-2m+n−2 次，其中有 m-1m−1 次向下移动，n-1n−1 次向右移动。
# 因此路径的总数，就等于从 m+n-2m+n−2 次移动中选择 m-1m−1 次向下移动的方案数，即组合数：
# comb(m + n - 2, n - 1)
from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


if __name__ == '__main__':
    print(Solution().uniquePaths(3,4))