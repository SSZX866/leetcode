# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 10:30
# @File    : 5784. 重新分配字符使所有字符串都相等.py
from leetcode import *


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        dic = defaultdict(int)
        for word in words:
            for each in word:
                dic[each] += 1
        for key in dic:
            if dic[key] % n: return False
        return True
