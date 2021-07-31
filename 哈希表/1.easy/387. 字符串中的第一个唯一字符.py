# -*- coding: utf-8 -*-
# @Time    : 2021/07/31 20:54
# @File    : 387. 字符串中的第一个唯一字符
from leetcode import *


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [1, i]
            else:
                dic[s[i]][0] += 1
        ans = len(s)
        for key in dic.keys():
            if dic[key][0] == 1:
                ans = min(ans, dic[key][1])
        return -1 if ans == len(s) else ans
