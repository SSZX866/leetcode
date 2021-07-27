from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        print(dp)
        return min(dp[-1], dp[-2])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]


if __name__ == '__main__':
    cost = [10, 15, 20]
    print(Solution().minCostClimbingStairs(cost=cost))
