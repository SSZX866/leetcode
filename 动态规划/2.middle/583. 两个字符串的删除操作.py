# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 12:44
# @File    : 583. 两个字符串的删除操作.py
from leetcode import *

# 找出最长公共子序列(1143. 最长公共子序列)用两个字符串长度之和减去两倍结果即所求
class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2): return self.minDistance(text2, text1)
        dp = [[0] * (len(text2)) for _ in text1]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i - 1 < 0 or j - 1 < 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    if i - 1 < 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j - 1 < 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(text1) + len(text2) - dp[-1][-1] * 2
