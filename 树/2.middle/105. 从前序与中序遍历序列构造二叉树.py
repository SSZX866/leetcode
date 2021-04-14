# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 21:16
# @File    : 105. 从前序与中序遍历序列构造二叉树.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTreeToValue(root):
    print('[', end='')
    if root:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if queue:
                print(node.val, end=', ')
            else:
                print(node.val, end='')
    print(']', end='')


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        if not inorder: return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    printTreeToValue(Solution().buildTree(preorder, inorder))
