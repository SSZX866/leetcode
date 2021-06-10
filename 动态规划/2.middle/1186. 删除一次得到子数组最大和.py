# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 14:02
# @File    : 1186. 删除一次得到子数组最大和.py
from leetcode import *


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [[0] * 2 for _ in arr]
        # dp[i][0] 以arr[i]结尾的没有行使删除权力的最大和
        # dp[i][1] 以arr[i]结尾行使删除权力的最大和
        dp[0][0] = arr[0]
        # dp[0][1] = arr[0] if arr[0] > 0 else 0
        dp[0][1] = -9999999
        for i in range(1, len(arr)):
            dp[i][0] = max(arr[i] + dp[i - 1][0], arr[i])
            dp[i][1] = max(dp[i - 1][0], arr[i] + dp[i - 1][1])
        return max(max(list(zip(*dp))[1]), max(list(zip(*dp))[0]))
