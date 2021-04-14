# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 21:59
# @File    : 124. 二叉树中的最大路径和.py
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
    def maxPathSum(self, root: TreeNode) -> int:
        val = []

        def help(root):
            if not root: return -99999
            if not root.left and not root.right: return root.val
            a = help(root.left)
            b = help(root.right)
            val.append(a)
            val.append(b)
            val.append(a + b + root.val, )
            print(a, b, root.val)
            return max(a + root.val, b + root.val, root.val)

        val.append(help(root))
        return max(val)


if __name__ == '__main__':
    null = None
    root = [1, 2, 3]
    root = [-10, 9, 20, null, null, 15, 7]
    root = [-3]
    root = [1, 2]
    root = [-2, -1]
    root = [2, -1]
    root = [1, -2, -3, 1, 3, -2, null, -1]
    root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]

    print(Solution().maxPathSum(buildTreeWithValue(root)))
