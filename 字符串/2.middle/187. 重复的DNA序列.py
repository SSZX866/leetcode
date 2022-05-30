# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 09:52
# @File    : 187. 重复的DNA序列.py
from leetcode import *


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = collections.defaultdict(int)
        ans = set()
        for i in range(0, len(s) - 9):
            tmp = s[i:i + 10]
            dic[tmp] += 1
            if dic[tmp] > 1:
                ans.add(tmp)
        return list(ans)


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, appeared = set(), set()
        for i in range(0, len(s) - 9):
            tmp = s[i:i + 10]
            if tmp in appeared: ans.add(tmp)
            appeared.add(tmp)
        return list(ans)
