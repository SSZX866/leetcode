# -*- coding: utf-8 -*-
# @Time    : 2021/08/07 15:46
# @File    : 700. 二叉搜索树中的搜索
from leetcode import *


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return None
        if root.val == val: return root
        if val > root.val: return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)
