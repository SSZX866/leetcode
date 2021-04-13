from typing import List
# dp[i][j] 表示从原点到i，j最小的和
# dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
# if i == 0 and j == 0: dp[i][j] = grid[i][j]
# elif i == 0: dp[i][j] = dp[i][j-1] + grid[i][j]
# elif j == 0: dp[i][j] = dp[i-1][1] + grid[i][j]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m * n == 0:
            return 0
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    print(dp[i][j],grid[i][j])
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    grid = [[1,2,3],[4,5,6]]
    print(Solution().minPathSum(grid))