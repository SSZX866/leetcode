# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 19:33
# @File    : 141. 环形链表.py
from leetcode import *


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
