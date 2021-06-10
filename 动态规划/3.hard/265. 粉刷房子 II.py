# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 11:12
# @File    : 265. 粉刷房子 II.py
from leetcode import *


# 理解错题意，题目说是相邻房子不同，不是连续两次不同
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # 0 连续涂两次 1 没有连续涂两次
        dp = [[0] * 2 for _ in costs]
        p, q = 0, 0  # 记录涂的下标 p 连续两次下标 q 没有连续两次下标
        q = costs[0].index(min(costs[0]))
        dp[0][1] = costs[0][q]
        for i in range(1, len(costs)):
            dp[i][0] = dp[i - 1][1] + costs[i][p]
            if costs[i][:q] and costs[i][q + 1:]:
                tmp_q = costs[i].index(min(min(costs[i][:q]), min(costs[i][q + 1:])))
            elif not costs[i][:q]:
                tmp_q = costs[i].index(min(costs[i][q + 1:]))
            else:
                tmp_q = costs[i].index(min(costs[i][:q]))
            if costs[i][:p] and costs[i][p + 1:]:
                tmp_p = costs[i].index(min(min(costs[i][:p]), min(costs[i][p + 1:])))
            elif not costs[i][:p]:
                tmp_p = costs[i].index(min(costs[i][p + 1:]))
            else:
                tmp_p = costs[i].index(min(costs[i][:p]))
            if dp[i - 1][1] + costs[i][p] < dp[i - 1][0] + costs[i][q]:
                dp[i][1] = dp[i - 1][1] + costs[i][p]
                q = tmp_q
            else:
                dp[i][1] = dp[i - 1][1] + costs[i][p]
                p = tmp_p
        return min(dp[-1])


# dp[i][j] 表示第i个房间采取第j个涂料时的最小代价
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        def findMinIndex(nums, dismiss):  # 找到nums中下标不为dismiss的最小数的下标
            curIndex = 0 if dismiss != 0 else 1
            for i in range(len(nums)):
                if nums[i] < nums[curIndex] and i != dismiss:
                    curIndex = i
            return curIndex

        dp = [[0] * len(costs[0]) for _ in costs]
        for j in range(len(costs[0])):
            dp[0][j] = costs[0][j]
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                index = findMinIndex(dp[i - 1], j)
                dp[i][j] = dp[i - 1][index] + costs[i][j]
        return min(dp[-1])


# 优化 用min_id记录前一次选取的下标，如果这一次与前一次下标不同再查找
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])

        dp = [[0 for i in range(k)] for i in range(n)]

        for i in range(n):
            if i == 0:
                dp[i] = costs[i]
                # min_id = dp[0].index(min(dp[0]))
            else:
                for j in range(k):
                    if j != min_id:
                        dp[i][j] = costs[i][j] + dp[i - 1][min_id]
                    else:
                        dp[i][j] = costs[i][j] + min(dp[i - 1][0:j] + dp[i - 1][j + 1:])
            min_id = dp[i].index(min(dp[i]))

        return min(dp[n - 1])
