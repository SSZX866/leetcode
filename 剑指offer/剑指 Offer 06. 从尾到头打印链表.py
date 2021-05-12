# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 13:32
# @File    : 剑指 Offer 06. 从尾到头打印链表.py
from leetcode import *


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head: return []
        if not head.next: return [head.val]
        return self.reversePrint(head.next) + [head.val]


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
