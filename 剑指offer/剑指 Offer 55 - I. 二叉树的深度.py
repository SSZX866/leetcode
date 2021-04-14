# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 21:18
# @File    : 剑指 Offer 55 - I. 二叉树的深度.py
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
    def maxDepth(self, root: TreeNode) -> int:
        ans = [0]

        def dfs(root, deep):
            if root:
                ans[:] = [max(ans[0], deep)]
                if root.left: dfs(root.left, deep + 1)
                if root.right: dfs(root.right, deep + 1)

        dfs(root, 1)
        return ans[0]


if __name__ == '__main__':
    null = None
    root = buildTreeWithValue([3, 9, 20, null, null, 15, 7])
    print(Solution().maxDepth(root))
