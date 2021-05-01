# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 22:31
# @File    : 5730. 将所有数字用字符替换.py
from leetcode import *


class Solution:
    def replaceDigits(self, s: str) -> str:
        n, ans = len(s), ""
        for i in range(n):
            if i % 2 == 1:
                ans += chr(ord(ans[-1]) + int(s[i]))
            else:
                ans += s[i]
        return ans
