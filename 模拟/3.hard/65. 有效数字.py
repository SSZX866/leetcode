# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 10:48
# @File    : 65. 有效数字.py
from leetcode import *


class Solution:
    def isNumber(self, s: str) -> bool:
        check = set(list(map(str, range(10))) + ['e', 'E', '.', '+', '-'])
        for c in s:
            if c not in check: return False

        def isDecimal(target):
            if not target: return False
            if '.' not in target or target.count('.') > 1: return False
            if '+' == target[0] or '-' == target[0]:
                target = target[1:]
            if not target or '+' in target or '-' in target or '.' == target: return False
            return True

        def isInterger(target):
            if not target: return False
            if '.' in target: return False
            if '+' == target[0] or '-' == target[0]:
                target = target[1:]
            if not target or '+' in target or '-' in target: return False
            return True

        if 'e' in s:
            if 'E' in s or s.count('e') > 1: return False
            tmp = s.split('e')
            return (isDecimal(tmp[0]) or isInterger(tmp[0])) and isInterger(tmp[1])
        elif 'E' in s:
            if 'e' in s or s.count('E') > 1: return False
            tmp = s.split('E')
            return (isDecimal(tmp[0]) or isInterger(tmp[0])) and isInterger(tmp[1])
        else:
            return isDecimal(s) or isInterger(s)
