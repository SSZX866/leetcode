# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 11:22
# @File    : 5869. 两个回文子序列长度的最大乘积.py
from leetcode import *


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        ans = 0

        def check(target):
            left, right = 0, len(target) - 1
            while left < right:
                if target[left] != target[right]:
                    return False
                left += 1
                right -= 1
            return True

        @lru_cache(None)
        def dfs(index, s1, s2):
            nonlocal ans
            if index == n:
                if not s1 or not s2 or not check(s1) or not check(s2):
                    return
                ans = max(ans, len(s1) * len(s2))
                return
            for i in range(index, n):
                dfs(i + 1, s1 + s[i], s2)
                dfs(i + 1, s1, s2)
                dfs(i + 1, s1, s2 + s[i])

        dfs(0, '', '')
        return ans
