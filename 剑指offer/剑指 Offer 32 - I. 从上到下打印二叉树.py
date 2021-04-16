# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 22:14
# @File    : 剑指 Offer 32 - I. 从上到下打印二叉树.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [root]
        ans = []
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return ans
