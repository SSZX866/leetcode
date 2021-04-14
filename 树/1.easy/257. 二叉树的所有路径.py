# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 21:41
# @File    : 257. 二叉树的所有路径.py
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


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        def dfs(root, path):
            if not root.left and not root.right:
                ans.append(path + '->' + str(root.val))
            if root.left: dfs(root.left, path + '->' + str(root.val))
            if root.right: dfs(root.right, path + '->' + str(root.val))

        dfs(root, '')
        return [x[2:] for x in ans]


if __name__ == '__main__':
    null = None
    root = buildTreeWithValue([1, 2, 3, null, 5])
    root = buildTreeWithValue([3, 9, 20, null, null, 15, 7])
    print(Solution().binaryTreePaths(root))
