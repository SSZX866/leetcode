# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 09:48
# @File    : 897. 递增顺序搜索树.py
from leetcode import *


class Solution:
    def __init__(self):
        self.node = self.tree = TreeNode()

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        return self.tree.right

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.node.right = TreeNode(root.val)
        self.node = self.node.right
        self.inorder(root.right)


if __name__ == '__main__':
    root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
    root = buildTreeWithValue(root)
    printTreeToValue(Solution().increasingBST(root))
