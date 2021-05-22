# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 10:35
# @File    : 1859. 将句子排序.py
from leetcode import *


class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split(' ')
        ans.sort(key=lambda x: x[-1])
        ans = [each[:-1] for each in ans]
        return ' '.join(ans)

class Solution:
    def sortSentence(self, s: str) -> str:
        ss = s.split()
        ss.sort(key = lambda a: a[-1])
        return " ".join(a[:-1] for a in ss)