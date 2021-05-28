# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 20:50
# @File    : 1784. 检查二进制字符串字段.py
from leetcode import *


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        tmp = False
        for each in s.split('0'):
            if each:
                if not tmp:
                    tmp = not tmp
                else:
                    return False
        return tmp
