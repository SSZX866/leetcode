from typing import List

# dp[i][j] 从原点到i,j的路径数
# dp[i][j] = dp[i][j-1]+dp[i-1][j]
# if obstacleGrid[i][j] == 1: dp[i][j] = 0
# elif i == 0: if not dp[i][j-1]: dp[i][j] = 0 else: dp[i][j] = 1
# elif j == 0: if not dp[i-1][j]: dp[i][j] = 0 else: dp[i][j] = 1

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    if not dp[i][j - 1]:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                elif j == 0:
                    if not dp[i - 1][j]:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
        # print(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))