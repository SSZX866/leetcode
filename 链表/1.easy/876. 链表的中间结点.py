# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 22:26
# @File    : 876. 链表的中间结点.py
from leetcode import *


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    head = [1, 2]
    head = buildChainWithValue(head)
    printChainToValue(Solution().middleNode(head))
