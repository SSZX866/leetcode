# -*- coding: utf-8 -*-
# @Time    : 2021/5/30 10:31
# @File    : 5772. 检查某单词是否等于两单词之和.py
from leetcode import *


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        tmp = 'abcdefghij'
        ans1, ans2 = '', ''
        target = ''
        for f in firstWord:
            ans1 += str(tmp.index(f))
        for s in secondWord:
            ans2 += str(tmp.index(s))
        for t in targetWord:
            target += str(tmp.index(t))
        return int(ans1) + int(ans2) == int(target)
