# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 23:55
# @File    : 面试题 02.02. 返回倒数第 k 个节点.py
from leetcode import *


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast = slow = head
        while fast:
            if k <= 0:
                slow = slow.next
            k -= 1
            fast = fast.next
        return slow.val
