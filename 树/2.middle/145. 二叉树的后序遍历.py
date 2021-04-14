# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 16:36
# @File    : 145. 二叉树的后序遍历.py
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# 迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], [[root, False]]
        while stack:
            node, needAdd = stack.pop()
            if needAdd:
                res.append(node.val)
            else:
                stack.append([node, True])
                if node.right: stack.append([node.right, False])
                if node.left: stack.append([node.left, False])
        return res


if __name__ == '__main__':
    null = None
    root = buildTreeWithValue([1, null, 2, 3])
    root = buildTreeWithValue([3, 9, 20, 4, 6, 15, 7])
    print(Solution().postorderTraversal(root))
