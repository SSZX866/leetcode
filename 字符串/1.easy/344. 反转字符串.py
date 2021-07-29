# -*- coding: utf-8 -*-
# @Time    : 2021/07/29 12:02
# @File    : 344. 反转字符串
from leetcode import *
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1