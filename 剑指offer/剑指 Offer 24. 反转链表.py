# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 13:46
# @File    : 剑指 Offer 24. 反转链表.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            last = cur.next
            cur.next = pre
            pre = cur
            cur = last
        return pre