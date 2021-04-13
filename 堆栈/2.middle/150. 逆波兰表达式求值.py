# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 00:18
# @File    : 150. 逆波兰表达式求值.py
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == '-':
                stack.append(-(int(stack.pop()) - int(stack.pop())))
            elif c == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(c)
        return stack[0]

if __name__ == '__main__':
    tokens = ["4","13","5","/","+"]
    print(Solution().evalRPN(tokens))