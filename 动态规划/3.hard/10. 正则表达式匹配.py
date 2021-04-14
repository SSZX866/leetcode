# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 11:35
# @File    : 10. 正则表达式匹配.py

# dp[i][j]表示s中i到p中的j是否匹配

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * len(p) for _ in s]
        dp[0][0] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if j == 0 or i ==
                if s[i] == p[j]:
                    dp[i][]