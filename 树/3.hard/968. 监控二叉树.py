# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 11:48
# @File    : 968. 监控二叉树.py
from leetcode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 0 未配摄像头可被观察或为根结点 1 不可被观察 2 存在摄像头
        # 自底向上处理
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # 左右节点都为根结点
            if left == 0 and right == 0:
                # 该节点不可被观察
                root.val = 1
            # 左右节点存在未被观测的节点
            elif left == 1 or right == 1:
                # 装配摄像头
                root.val = 2
            # 左右节点存在摄像头
            else:
                # 该节点可被观察
                root.val = 0
            return root.val

        def vistor(root):
            if not root: return 0
            if root.val == 2: return vistor(root.left) + vistor(root.right) + 1
            return vistor(root.left) + vistor(root.right)

        dfs(root)
        # 根结点不被观察需要添加一个摄像头
        return vistor(root) + 1 if root.val == 1 else vistor(root)
