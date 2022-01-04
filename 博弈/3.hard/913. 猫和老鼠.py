# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 10:07
# @File    : 913. 猫和老鼠.py
from leetcode import *


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(m, c, i):
            """
            最大最小博弈
            老鼠最好的情况 胜利 -1 其次是平局 0
            猫最好的情况 胜利 1 其次是平局 0
            :param m: Mouse position
            :param c: Cat position
            :param i: Round
            :return:
            """
            if i > 2 * len(graph):
                return 0
            if m == 0:
                return -1
            if m == c:
                return 1
            if i % 2:
                # 猫回合
                res = -1
                for nxt in graph[c]:
                    if nxt == 0: continue
                    res = max(res, dfs(m, nxt, i + 1))
                    if res == 1:
                        break
            else:
                # 老鼠回合
                res = 1
                for nxt in graph[m]:
                    res = min(res, dfs(nxt, c, i + 1))
                    if res == -1:
                        break
            return res

        ans = dfs(1, 2, 0)
        return 0 if ans == 0 else 1 if ans == -1 else 2
