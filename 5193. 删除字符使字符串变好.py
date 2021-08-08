# -*- coding: utf-8 -*-
# @Time    : 2021/08/07 23:23
# @File    : 5193. 删除字符使字符串变好
from leetcode import *


class Solution:
    def makeFancyString(self, s: str) -> str:
        pre, cnt = s[0], 1
        ans = s[0]
        for i in range(1, len(s)):
            if s[i] == pre:
                cnt += 1
            else:
                pre = s[i]
                cnt = 1
            if cnt > 2:
                continue
            ans += s[i]
        return ans
