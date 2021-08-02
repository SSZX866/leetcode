# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 12:49
# @File    : 116. 填充每个节点的下一个右侧节点指针
from leetcode import *


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = deque([root])
        while queue:
            cur_layer = queue
            queue = deque()
            while cur_layer:
                node = cur_layer.popleft()
                if not cur_layer:
                    node.next = None
                else:
                    node.next = cur_layer[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root
