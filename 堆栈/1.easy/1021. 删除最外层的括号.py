# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 23:44
# @File    : 1021. 删除最外层的括号.py
from leetcode import *


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans, stack = "", []
        for c in S:
            print(stack)
            if c == '(' and stack:
                stack.append(c)
            elif c == ')':
                stack.pop()
            else:
                stack.append(c)
                continue
            if stack:
                ans += c
        return ans


if __name__ == '__main__':
    S = "(()())(())"
    S = "(()())(())(()(()))"
    S = "()()"
    print(Solution().removeOuterParentheses(S))
