# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 10:58
# @File    : 938. 二叉搜索树的范围和.py
from leetcode import *


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0

        def inorder(node):
            if not node: return
            inorder(node.left)
            if low <= node.val <= high:
                self.ans += node.val
            inorder(node.right)

        inorder(root)
        return self.ans
