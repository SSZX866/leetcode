# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 10:08
# @File    : 997. 找到小镇的法官.py
from leetcode import *


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic = collections.defaultdict(set)
        s = set(range(1, n + 1))
        for start, end in trust:
            dic[end].add(start)
            if start in s: s.remove(start)
        for each in s:
            if len(dic[each]) == n - 1:
                return each
        return -1
