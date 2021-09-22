# -*- coding: utf-8 -*-
# @Time    : 2021/9/21 09:24
# @File    : 113. 路径总和 II.py
from leetcode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        ans = []

        def dfs(root, path, tSum):
            if not root.left and not root.right and not tSum:
                ans.append(path[:])
                return
            if root.left:
                path.append(root.left.val)
                dfs(root.left, path, tSum - root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                dfs(root.right, path, tSum - root.right.val)
                path.pop()

        dfs(root, [root.val], targetSum - root.val)
        return ans
