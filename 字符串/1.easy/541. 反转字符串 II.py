# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 09:37
# @File    : 541. 反转字符串 II.py
from leetcode import *


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        if k <= len(s) < 2 * k:
            return s[:k][::-1] + s[k:]
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k)


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k) if 2 * k <= len(s) else s[::-1] if len(s) < k else s[:k][::-1] + s[k:]
