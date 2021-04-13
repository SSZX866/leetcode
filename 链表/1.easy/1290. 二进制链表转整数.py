# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 20:53
# @File    : 1290. 二进制链表转整数.py
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        while head:
            s += str(head.val)
            head = head.next
        return int(s,base=2)
