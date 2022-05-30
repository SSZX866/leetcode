# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 09:40
# @File    : 563. 二叉树的坡度.py
from leetcode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache(None)
    def sumTilt(self, root):
        if not root: return 0
        return self.sumTilt(root.left) + self.sumTilt(root.right) + root.val

    def findTilt(self, root: TreeNode) -> int:
        if not root: return 0
        absolute = abs(self.sumTilt(root.left) - self.sumTilt(root.right))
        a = self.findTilt(root.left) + self.findTilt(root.right) + absolute
        return a
