# -*- coding: utf-8 -*-
# @Time    : 2021/08/03 13:35
# @File    : 20. 有效的括号
from leetcode import *


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {key: value for key, value in [('{', '}'), ('[', ']'), ('(', ')')]}
        for each in s:
            if each in '({[':
                stack.append(each)
            else:
                if not stack or each != dic[stack.pop()]:
                    return False
        return not stack


#  巧妙地思路
class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('()', '')
            s = s.replace('[]', '')
        return not s
