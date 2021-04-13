# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 11:35
# @File    : 10. 正则表达式匹配.py

# dp[i][j]表示s中i到p中的j是否匹配

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] ]
