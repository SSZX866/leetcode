# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 10:23
# @File    : 28. 实现 strStr().py
from leetcode import *


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n, i = len(haystack), len(needle), 0
        if n == 0: return 0
        while i <= m - n:
            if haystack[i] == needle[0]:
                s = haystack[i:i + n]
                if s == needle: return i
            i += 1
        return -1


if __name__ == '__main__':
    print(Solution().strStr('a', 'aa'))
