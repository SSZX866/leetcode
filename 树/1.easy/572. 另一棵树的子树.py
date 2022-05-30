# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 14:15
# @File    : 572. 另一棵树的子树.py
from leetcode import *


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def preorder(node):
            if not node: return False
            if node.val == subRoot.val:
                if self.check(node, subRoot): return True
            return preorder(node.left) or preorder(node.right)

        return preorder(root)

    def check(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2 or root1.val != root2.val: return False
        return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val == subRoot.val and self.check(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2 or root1.val != root2.val: return False
        return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)
