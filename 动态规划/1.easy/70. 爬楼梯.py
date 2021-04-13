class Solution:
    def climbStairs(self, n: int) -> int:
        n = n+1
        dp = [0] * n
        dp[0] = 1
        for i in range(1,n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n-1]

print(Solution().climbStairs(10))