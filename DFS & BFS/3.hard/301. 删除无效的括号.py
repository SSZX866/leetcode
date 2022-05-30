# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 08:53
# @File    : 301. 删除无效的括号.py
from leetcode import *


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(target):
            cnt = 0
            for each in target:
                if each == '(':
                    cnt += 1
                if each == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        ans = set()
        M = 0

        @lru_cache(None)
        def dfs(i, cur):
            if i == len(s):
                nonlocal M, ans
                if len(cur) < M:
                    return
                if check(cur):
                    if len(cur) > M:
                        ans = {cur}
                        M = len(cur)
                    else:
                        ans.add(cur)
                return
            if s[i] in '()':
                dfs(i + 1, cur)
            dfs(i + 1, cur + s[i])

        dfs(0, '')
        return list(ans)
