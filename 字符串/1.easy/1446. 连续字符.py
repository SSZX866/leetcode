# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 08:48
# @File    : 1446. 连续字符.py
from leetcode import *


class Solution:
    def maxPower(self, s: str) -> int:
        left = 0
        ans = 0
        for right in range(1, len(s)):
            if s[right] == s[left]:
                continue
            ans = max(ans, right - left)
            left = right
        ans = max(ans, len(s) - left)
        return ans
