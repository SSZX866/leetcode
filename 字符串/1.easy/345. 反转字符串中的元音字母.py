# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 12:15
# @File    : 345. 反转字符串中的元音字母.py
from leetcode import *


class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        ans = s
        while i < j:
            while i < j and s[i] not in 'aeiouAEIOU':
                i += 1
            while i < j and s[j] not in 'aeiouAEIOU':
                j -= 1
            if i == j: return ans
            ans = ans[:i] + ans[j] + ans[i + 1:j] + ans[i] + ans[j + 1:]
            i += 1
            j -= 1
        return ans
