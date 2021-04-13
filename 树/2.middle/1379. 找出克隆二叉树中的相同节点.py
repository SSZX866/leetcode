# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 14:34
# @File    : 1379. 找出克隆二叉树中的相同节点.py
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]
        while queue:
            node = queue.pop()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if node.val == target.val: return node
