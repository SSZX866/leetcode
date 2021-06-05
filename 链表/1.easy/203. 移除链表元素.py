# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 16:38
# @File    : 203. 移除链表元素.py
from leetcode import *


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = dummy = ListNode()
        dummy.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
