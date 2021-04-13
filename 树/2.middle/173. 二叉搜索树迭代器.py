# -*- coding: utf-8 -*-
# @Time    : 2021/3/28 10:18
# @File    : 173. 二叉搜索树迭代器.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nums = []
        self.inorder(root)

    def next(self) -> int:
        return self.nums.pop(0)

    def hasNext(self) -> bool:
        return self.nums != []

    def inorder(self, node: TreeNode):
        if not node: return None
        self.inorder(node.left)
        self.nums.append(node.val)
        self.inorder(node.right)
        return None
