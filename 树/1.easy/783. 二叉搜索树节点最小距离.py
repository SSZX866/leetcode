# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 09:56
# @File    : 783. 二叉搜索树节点最小距离.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # vals = []

        # def dfs(node, val):
        #     if not node: return
        #     if not node.left and not node.right: return
        #     dfs(node.left, val)
        #     if node.left: val.append(node.val - node.left.val)
        #     if node.right: val.append(node.right.val - node.val)
        #     dfs(node.right, val)

        # def dfs(node, val):
        #     if not node: return
        #     dfs(node.left, val)
        #     val.append(node.val)
        #     dfs(node.right, val)
        #
        # dfs(root, vals)
        # for i, val in enumerate(vals[1:][::-1]):
        #     vals[-i - 1] = val - vals[-i - 2]
        #     if vals[-i - 1] == 1: return 1

        def dfs(node):
            if not node: return
            dfs(node.left)
            self.ans = min(self.ans, node.val - self.pre)
            self.pre = node.val
            dfs(node.right)

        self.ans = float('inf')
        self.pre = float('-inf')
        dfs(root)
        return self.ans


if __name__ == '__main__':
    null = None
    root = [1, 0, 48, null, null, 12, 49]
    root = [27, null, 34, null, 58, 50, null, 44]
    root = [90, 69, null, 49, 89, null, 52]
    root = [5, 1, 7]
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
    queue = [tree]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    print(Solution().minDiffInBST(tree))
