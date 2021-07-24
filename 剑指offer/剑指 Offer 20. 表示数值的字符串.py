# -*- coding: utf-8 -*-
# @Time    : 2021/07/24 18:38
# @File    : 剑指 Offer 20. 表示数值的字符串
from leetcode import *


class Solution:
    def isNumber(self, s: str) -> bool:
        def checkDecimal(string):
            if not string: return False
            if string[0] == '+' or string[0] == '-': string = string[1:]
            if not string or '+' in string or '-' in string: return False
            string_list = string.split('.')
            if len(string_list) != 2 or (not string_list[0] and not string_list[1]): return False
            try:
                int(string_list[0] + '1')
                int(string_list[1] + '1')
            except:
                return False
            return True

        def checkInterger(string):
            if not string: return False
            if string[0] == '+' or string[0] == '-': string = string[1:]
            if not string or '+' in string or '-' in string: return False
            try:
                int(string)
            except:
                return False
            return True

        s = s.strip()
        if ' ' in s: return False
        if 'e' in s:
            if 'E' in s or s.count('e') != 1: return False
            s_list = s.split('e')
            if not checkDecimal(s_list[0]) and not checkInterger(s_list[0]): return False
            return checkInterger(s_list[1])
        elif 'E' in s:
            if 'e' in s or s.count('E') != 1: return False
            s_list = s.split('E')
            if not checkDecimal(s_list[0]) and not checkInterger(s_list[0]): return False
            return checkInterger(s_list[1])
        else:
            return checkDecimal(s) or checkInterger(s)
