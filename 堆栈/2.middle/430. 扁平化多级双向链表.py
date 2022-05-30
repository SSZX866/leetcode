# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 09:55
# @File    : 430. 扁平化多级双向链表.py
from leetcode import *


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        stack = [head]
        dummy = Node(0, None, None, head)
        cur = dummy
        while stack:
            node = stack.pop()
            cur.next = node
            node.prev = cur
            while node:
                if node.child:
                    if node.next: stack.append(node.next)
                    node.next = node.child
                    node.next.prev = node
                    node.child = None
                cur = node
                node = node.next
        dummy.next.prev = None
        return dummy.next
