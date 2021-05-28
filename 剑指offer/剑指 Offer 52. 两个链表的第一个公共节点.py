# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 16:33
# @File    : 剑指 Offer 52. 两个链表的第一个公共节点.py
from leetcode import *


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur = headA
        if not cur: return
        while cur.next:
            cur = cur.next
        cur.next = headA
        tmp = cur
        fast = slow = headB
        while True:
            if not fast or not fast.next or not fast.next.next or not slow or not slow.next:
                tmp.next = None
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        slow = headB
        while slow != fast:
            slow = slow.next
            fast = fast.next
        tmp.next = None
        return fast
