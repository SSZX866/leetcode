# -*- coding: utf-8 -*-
# @Time    : 2021/08/03 14:02
# @File    : 139. 单词拆分
from leetcode import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
