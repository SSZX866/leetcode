class Solution:
    def climbStairs(self, n: int) -> int:
        n = n + 1
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n - 1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        i, j = 1, 2
        for _ in range(2, n):
            i, j = j, i + j
        return j


print(Solution().climbStairs(10))
