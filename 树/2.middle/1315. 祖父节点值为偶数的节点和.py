# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 21:06
# @File    : 1315. 祖父节点值为偶数的节点和.py
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node, depth, resDepth, res):
            if not node: return
            if depth in resDepth:
                res[0] += node.val
            if not node.val % 2:
                resDepth.append(depth + 2)
                dfs(node.left, depth + 1, resDepth, res)
                dfs(node.right, depth + 1, resDepth, res)
                resDepth.pop()
            else:
                dfs(node.left, depth + 1, resDepth, res)
                dfs(node.right, depth + 1, resDepth, res)
        dfs(root, 0, [], res)
        return res[0]
