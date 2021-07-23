# -*- coding: utf-8 -*-
# @Time    : 2021/07/23 16:08
# @File    : 面试题 03.05. 栈排序
from leetcode import *


class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        heapq.heappush(self.stack, val)

    def pop(self) -> None:
        if not self.isEmpty():
            heapq.heappop(self.stack)

    def peek(self) -> int:
        return self.stack[0] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return not bool(self.stack)
