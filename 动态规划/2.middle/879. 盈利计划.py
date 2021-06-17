# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 21:51
# @File    : 879. 盈利计划.py
from leetcode import *


# dp[i][j][k] 使用j个人完成前i项任务获得恰好为k的收益的最大计划数
# dp[i][j][k] = dp[i-1][j-group[i]][k-profit[i]]
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0] * (sum(profit) + 1) for _ in range(n + 1)] for _ in range(len(group))]
        if group[0] <= n: dp[0][group[0]][profit[0]] = 1
        for i in range(1, len(group)):
            for j in range(n + 1):
                for k in range(sum(profit) + 1):
                    if j - group[i] >= 0 and k - profit[i] >= 0:
                        dp[i][j][k] = dp[i - 1][j - group[i]][k - profit[i]] + 1
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
        ans = 0
        # print(dp)
        # for j in range(n):
        #     for k in range(minProfit, sum(profit) + 1):
        #         ans += dp[-1][j][k]
        for k in range(minProfit, sum(profit) + 1):
            ans += dp[-1][-1][k]
        return ans


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0] * (sum(profit) + 1) for _ in range(max(n + 1, sum(group) + 1))] for _ in range(len(group))]
        if group[0] <= n: dp[0][group[0]][profit[0]] = 1
        for i in range(1, len(group)):
            for j in range(max(n + 1, sum(group) + 1)):
                for k in range(sum(profit) + 1):
                    if j - group[i] >= 0 and k - profit[i] >= 0:
                        dp[i][j][k] = dp[i - 1][j - group[i]][k - profit[i]]
                    dp[i][j][k] += dp[i - 1][j][k]
        ans = 0
        for j in range(n + 1):
            for k in range(minProfit, sum(profit) + 1):
                ans += dp[-1][j][k]
        return ans


if __name__ == '__main__':
    n = 5
    minProfit = 3
    group = [2, 2]
    profit = [2, 3]
    print(Solution().profitableSchemes(n, minProfit, group, profit))
