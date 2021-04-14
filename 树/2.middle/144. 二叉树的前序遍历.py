# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 15:35
# @File    : 144. 二叉树的前序遍历.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTreeWithValue(root):
    if not root: return root
    tree = TreeNode(root[0])
    queue = [tree]
    i = 1
    while i < len(root):
        node = queue.pop(0)
        if root[i] == None:
            i += 1
            if i < len(root) and root[i] != None:
                node.right = TreeNode(root[i])
                queue.append(node.right)
            i += 1
        else:
            node.left = TreeNode(root[i])
            queue.append(node.left)
            i += 1
            if i < len(root) and root[i] != None:
                node.right = TreeNode(root[i])
                queue.append(node.right)
            i += 1
    return tree


# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root):
            if not root: return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)

        ans = []
        preorder(root)
        return ans


# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return ans


if __name__ == '__main__':
    null = None
    root = [1, null, 2, 3]
    root = buildTreeWithValue(root)
    print(Solution().preorderTraversal(root))
