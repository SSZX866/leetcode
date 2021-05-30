# -*- coding: utf-8 -*-
# @Time    : 2021/5/30 10:35
# @File    : 5773. 插入后的最大值.py
from leetcode import *


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        ans = ''
        flag = False
        if n[0] != '-':
            for i in range(len(n)):
                if int(n[i]) < x:
                    ans += str(x)
                    flag = True
                    ans += n[i:]
                    break
                ans += n[i]
        else:
            ans += '-'
            for i in range(1,len(n)):
                if int(n[i]) > x:
                    ans += str(x)
                    flag = True
                    ans += n[i:]
                    break
                ans += n[i]
        if not flag:
            ans += str(x)
        return ans
