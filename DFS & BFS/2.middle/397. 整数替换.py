# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 09:08
# @File    : 397. 整数替换.py
from leetcode import *


class Solution:
    def integerReplacement(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, step):
            if i == 1: return step
            if i % 2: return min(dfs(i + 1, step + 1), dfs(i - 1, step + 1))
            return dfs(i // 2, step + 1)

        return dfs(n, 0)
