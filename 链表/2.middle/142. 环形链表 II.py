# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 21:55
# @File    : 142. 环形链表 II.py
from leetcode import *


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not (fast and fast.next and fast.next.next):
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
