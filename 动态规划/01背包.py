# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 21:47
# @File    : 01背包.py
from leetcode import *


# 给一系列物品(价值为v，重量为w)，每个物品只能用一次。背包总容量上限是C。问最大能装多少价值的东西。
# 状态定义:dp[i][c] => 考虑仅在前i件物品的子集选择，且代价(所选物品的总重量)恰好是c时能得到的最大收益。
# 状态转移:当前的代价是c，那么前一轮的代价是 c 或者 c-Wi
# 边界条件:dp[0][0] = 0 dp[0][c] = NA
# 有点像第一类基本型: 考虑一件物品就是“一轮”; 只不过每轮的状态以代价为单位，有C种。

def bagValueProblem(value, wight, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(value) + 1)]
    dp[0][0] = 0
    for i in range(len(value)):
        for c in range(1, capacity + 1):
            if i == 0: dp[i][c] = -99999999
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wight[i]] + value[c])
    return max(dp[-1])


if __name__ == '__main__':
    value = [2, 4, 4, 5]
    wight = [1, 2, 3, 4]
    capacity = 5
    print(bagValueProblem(value, wight, capacity))
