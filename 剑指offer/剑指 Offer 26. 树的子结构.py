# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 11:15
# @File    : 剑指 Offer 26. 树的子结构.py
from leetcode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkTree(self, A, B):
        stackA, stackB = [A], [B]
        while stackB:
            nodeB = stackB.pop()
            if not stackA: return False
            nodeA = stackA.pop()
            if not nodeA or nodeA.val != nodeB.val: return False
            if nodeB.left:
                stackB.append(nodeB.left)
                if not nodeA.left: return False
                stackA.append(nodeA.left)
            if nodeB.right:
                stackB.append(nodeB.right)
                if not nodeA.right: return False
                stackA.append(nodeA.right)
        return True

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False
        return self.checkTree(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
