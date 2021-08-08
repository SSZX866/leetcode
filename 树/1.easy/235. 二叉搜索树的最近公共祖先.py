# -*- coding: utf-8 -*-
# @Time    : 2021/08/08 20:04
# @File    : 235. 二叉搜索树的最近公共祖先
from leetcode import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
