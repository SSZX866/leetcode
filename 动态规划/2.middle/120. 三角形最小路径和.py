from typing import List

# 1
# 2 1
# 1 3 3
# 1 3 4 5
# 1 1 1 7 6
# dp[i] 到第i层最短路径之和
# dp[i] = dp[i-1] + min(triangle[i],triangle[i+1])
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         dp = [0]*n
#         dp[0] = triangle[0][0]
#         j = 0
#         for i in range(1,n):
#             if triangle[i][j] > triangle[i][j+1]:
#                 j += 1
#             dp[i] = dp[i - 1] + triangle[i][j]
#         print(dp)
#         return dp[-1]



# dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + triangle[i][j]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*x for x in range(1,n+1)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j-1], dp[i - 1][j]) + triangle[i][j]
        #print(dp)
        return min(dp[-1])

if __name__ == '__main__':
    triangle = [[1],[2,1],[1,3,3],[1,3,4,5],[1,1,1,7,6]]
    print(Solution().minimumTotal(triangle))