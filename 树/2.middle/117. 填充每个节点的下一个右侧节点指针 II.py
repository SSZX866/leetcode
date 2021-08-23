# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 14:00
# @File    : 117. 填充每个节点的下一个右侧节点指针 II.py
from leetcode import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = deque([root])
        while queue:
            cur = queue
            queue = deque()
            while cur:
                node = cur.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                node.next = cur[0] if cur else None
        return root
