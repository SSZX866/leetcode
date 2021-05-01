# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 12:09
# @File    : 1704. 判断字符串的两半是否相似.py
from leetcode import *


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        dic, index, n, cnt = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}, 0, len(s), [0, 0]
        for c in s:
            if c in dic: cnt[0 if index < n // 2 else 1] += 1
            index += 1
        return cnt[0] == cnt[1]


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        half_len = len(s) // 2
        return sum(i in vowel for i in s[:half_len]) == sum(i in vowel for i in s[half_len:])
        # sum([True,False])=1
