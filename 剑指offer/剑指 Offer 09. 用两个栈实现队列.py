# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 16:28
# @File    : 剑指 Offer 09. 用两个栈实现队列.py
class CQueue:

    def __init__(self):
        self.stack = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if not self.stack: return -1
        stack = []
        while self.stack:
            stack.append(self.stack.pop())
        ans = stack.pop()
        while stack:
            self.stack.append(stack.pop())
        return ans


class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        if not self.stack_in:
            return -1

        while (self.stack_in):
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()
