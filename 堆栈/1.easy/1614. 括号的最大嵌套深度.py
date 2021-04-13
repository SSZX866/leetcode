# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 19:08
# @File    : 1614. 括号的最大嵌套深度.py
class Solution:
    def maxDepth(self, s: str) -> int:
        stack, maxLength = [], 0
        for c in s:
            if c == "(":
                stack.append("(")
                maxLength = max(maxLength, len(stack))
            elif c == ")":
                if len(stack) > 0:
                    stack.pop()
        return maxLength
