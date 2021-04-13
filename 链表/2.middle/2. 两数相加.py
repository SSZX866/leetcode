# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 15:40
# @File    : 2. 两数相加.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tmp = dummy
        t = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            tmp.next = ListNode((a + b + t) % 10)
            t = (a + b + t) // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            tmp = tmp.next
        tmp.next = ListNode(t) if t else None
        return dummy.next
