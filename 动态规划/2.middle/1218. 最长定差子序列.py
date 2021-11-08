# -*- coding: utf-8 -*-
# @Time    : 2021/11/5 09:27
# @File    : 1218. 最长定差子序列.py
from leetcode import *


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [[0] * 2 for _ in arr]
        dp[0][0] = 1
        dic = {arr[0]: 1}
        for i in range(1, len(arr)):
            prev = arr[i] - difference
            if prev in dic:
                dp[i][0] = dic[prev] + 1
            else:
                dp[i][0] = 1
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            dic[arr[i]] = dp[i][0]
        return max(dp[-1])


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = collections.defaultdict(int)
        ans = 0
        for each in arr:
            dic[each] = dic[each - difference] + 1
            ans = max(ans, dic[each])
        return ans
