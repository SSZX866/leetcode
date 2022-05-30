# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 13:24
# @File    : 230. 二叉搜索树中第K小的元素.py
from leetcode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = None

        def dfs(node):
            nonlocal k
            if k == 0:
                return
            if node.left: dfs(node.left)
            k -= 1
            if k == 0:
                nonlocal ans
                ans = node.val
                return
            if node.right: dfs(node.right)

        dfs(root)
        return ans
